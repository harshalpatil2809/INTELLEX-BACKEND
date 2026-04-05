from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Conversation, Message



# Create New Chat
@api_view(['POS'])
@permission_classes([IsAuthenticated])
def create_chat(request):
    convo = Conversation.objects.create(user=request.user)
    return Response({"id":convo.id})


# Send Message 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    convo_id = request.data.get("conversation_id")
    text = request.data.get("message")

    convo = Conversation.objects.get(id=convo_id)

    Message.objects.create(
        conversation=convo,
        role = "user",
        content=text
    )

    ai_reply = request.data.get("ai-reply")

    Message.objects.create(
        conversation= convo,
        role="ai",
        content = ai_reply
    )

    if not convo.title:
        convo.title = text[:30]
        convo.save()

    return Response({"reply":ai_reply})

# Get all Chats 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chats(request):
    chats = Conversation.objects.filter(user=request.user).order_by('-created_at')

    data = [
        {"id": c.id, "title": c.title}
        for c in chats
    ]

    return Response(data)


# Get All Message 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request, id):
    msgs = Message.objects.filter(conversation_id=id)

    data = [
        {"role": m.role, "content": m.content}
        for m in msgs
    ]

    return Response(data)
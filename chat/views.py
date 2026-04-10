from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Conversation, Message

import os
from groq import Groq


# 1. Create New Chat
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_chat(request):
    convo = Conversation.objects.create(user=request.user)
    return Response({"id": convo.id})



client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# 2. Send Message
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    convo_id = request.data.get("conversation_id")
    text = request.data.get("message")

    if not convo_id or not text:
        return Response({"error": "Missing data"}, status=400)

    try:
        convo = Conversation.objects.get(id=convo_id, user=request.user)

        Message.objects.create(
            conversation=convo,
            role="user",
            content=text
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": text,
                }
            ],
            model="llama3-8b-8192",
        )
        
        ai_reply = chat_completion.choices[0].message.content

        Message.objects.create(
            conversation=convo,
            role="ai",
            content=ai_reply
        )

        if not convo.title or convo.title == "New Chat":
            convo.title = text[:30] + "..." if len(text) > 30 else text
            convo.save()

        return Response({"reply": ai_reply})

    except Conversation.DoesNotExist:
        return Response({"error": "Conversation not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


# 3. Get All Chats (Sidebar)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chats(request):
    chats = Conversation.objects.filter(user=request.user).order_by('-created_at')

    data = [
        {"id": c.id, "title": c.title}
        for c in chats
    ]

    return Response(data)


# 4. Get Messages
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request, id):
    msgs = Message.objects.filter(conversation_id=id)

    data = [
        {"role": m.role, "content": m.content}
        for m in msgs
    ]

    return Response(data)
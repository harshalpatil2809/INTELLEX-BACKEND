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




GROQ_KEY = os.getenv("GROQ_API_KEY") # Replace with real key
client = Groq(api_key=GROQ_KEY)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    try:
        convo_id = request.data.get("conversation_id")
        text = request.data.get("message")

        # 1. Conversation Dhundna
        try:
            convo = Conversation.objects.get(id=convo_id, user=request.user)
        except Conversation.DoesNotExist:
            print("❌ Chat not found for this ID")
            return Response({"error": "Chat not found"}, status=404)

        # 2. User Message Save
        Message.objects.create(conversation=convo, role="user", content=text)

        # 3. Groq API Call
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": text}],
                model="openai/gpt-oss-120b",
            )
            ai_reply = chat_completion.choices[0].message.content
        except Exception as groq_err:
            print(f"❌ Groq API Error: {str(groq_err)}")
            return Response({"error": f"AI Error: {str(groq_err)}"}, status=502)

        # 4. AI Message Save
        Message.objects.create(conversation=convo, role="ai", content=ai_reply)

        return Response({"reply": ai_reply})

    except Exception as e:
        print(f"❌ CRASH ERROR: {str(e)}") # Is line ko terminal mein check karein
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
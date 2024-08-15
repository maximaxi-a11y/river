from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ChatMessage, ChatSession
from django.contrib.auth.decorators import login_required
import openai

openai.api_key = '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'


@login_required
def gpt_chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')

        # Получение текущей сессии чата
        session, created = ChatSession.objects.get_or_create(user=request.user, id=request.session.get('chat_session_id'))

        # Получение предыдущих сообщений из этой сессии
        previous_messages = session.messages.all().order_by('timestamp')
        previous_conversation = "\n".join([f"User: {msg.user_message}\nGPT: {msg.gpt_response}" for msg in previous_messages])

        # Генерация нового ответа с учетом предыдущих сообщений
        response = openai.Completion.create(
            engine="gpt-4o-mini",
            prompt=f"{previous_conversation}\nUser: {user_message}\nGPT:",
            max_tokens=150,
            temperature=0.7
        )

        gpt_response = response.choices[0].text.strip()

        # Сохранение нового сообщения и ответа в базу данных
        ChatMessage.objects.create(session=session, user_message=user_message, gpt_response=gpt_response)

        return JsonResponse({'response': gpt_response})

    messages = ChatMessage.objects.filter(session__user=request.user).order_by('timestamp')
    return render(request, 'chat.html', {'messages': messages})

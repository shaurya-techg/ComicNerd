from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ai.services.assistant import ask_ai
from comic_collections.documents import ComicCollection


@login_required
def chat_view(request):

    # Clear chat
    if request.GET.get("clear"):

        request.session["chat_history"] = []
        request.session.modified = True

        return redirect("ai_chat")

    # Create history if it doesn't exist
    if "chat_history" not in request.session:
        request.session["chat_history"] = []

    history = request.session["chat_history"]

    collection = [
        comic.comic_title
        for comic in ComicCollection.objects(
            user_id=request.user.id
        )
    ]

    if request.method == "POST":

        question = request.POST.get("question")

        if question:

            answer = ask_ai(
                question,
                history,
                collection
            )

            history.append({
                "role": "user",
                "content": question,
            })

            history.append({
                "role": "assistant",
                "content": answer,
            })

            request.session["chat_history"] = history
            request.session.modified = True

    return render(
        request,
        "ai/chat.html",
        {
            "history": history,
        }
    )
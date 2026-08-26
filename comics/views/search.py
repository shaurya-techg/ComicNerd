from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from comics.services.comicvine import search_comics


@login_required
def search_view(request):

    query = request.GET.get("q")

    print("QUERY =", query)

    results = None

    if query:
        print("Calling ComicVine...")
        api_response = search_comics(query)
        results = api_response.get("results", [])
        print("RESULTS =", results)

    return render(
        request,
        "comics/search.html",
        {
            "results": results,
            "query": query,
        }
    )
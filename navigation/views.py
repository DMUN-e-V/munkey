from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from navigation.forms import MUNkeyLinkChooserForm


def choose_munkey_link(request):
    initial_data = {
        "name": request.GET.get("link_url", ""),
        "link_text": request.GET.get("link_text", ""),
    }

    response = {}

    if request.method == "POST":
        form = MUNkeyLinkChooserForm(
            request.POST, initial=initial_data, prefix="munkey-link-chooser"
        )

        if form.is_valid():
            result = {
                "name": form.cleaned_data["name"],
                "title": form.cleaned_data["link_text"].strip()
                or form.cleaned_data["url"],
            }

            return JsonResponse({"step": "munkey_link_chosen", "result": result})
    else:
        form = MUNkeyLinkChooserForm(initial=initial_data, prefix="munkey-link-chooser")

    return JsonResponse(
        {
            "html": render_to_string(
                "navigation/munkey-link-chooser.html",
                request=request,
                context={"form": form},
            ),
            "step": "munkey_link",
        }
    )

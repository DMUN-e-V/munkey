import navigation


def menu(request):
    return {"menu": navigation.links.get_links()}

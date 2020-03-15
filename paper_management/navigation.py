from django.urls import reverse

import navigation
from navigation.links import Link


def add_links():
    root_link = Link("Papers", "#")
    root_link.add_child(Link("View all papers", reverse("paper_management:paper_list")))
    root_link.add_child(Link("Add paper", reverse("paper_management:paper_add")))
    return [root_link]


navigation.links.register(add_links)

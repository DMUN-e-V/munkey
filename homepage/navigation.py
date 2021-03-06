from wagtail.core.models import Site, Page

import navigation
from navigation.links import Link


def add_links():
    link_list = []
    try:
        root = Site.objects.first().root_page
        for page in Page.objects.child_of(root):
            link = Link(page.title, page.get_url)
            if page.get_descendants():
                for child in page.get_descendants():
                    link.add_child(Link(child.title, child.get_url))
            link_list.append(link)
    except AttributeError:  # during setup, there is no root_page present in wagtail, raising an AttributeError
        pass
    return link_list


navigation.links.register(add_links)

class Link:
    def __init__(self, title, target="#"):
        self.title = title
        self.target = target
        self.children = []

    def add_child(self, link):
        self.children.append(link)


class LinkCollector:
    def __init__(self):
        self._registry = []

    def register(self, function):
        self._registry.append(function)

    def get_links(self):
        link_list = []
        for function in self._registry:
            link_list = link_list + function()
        return link_list

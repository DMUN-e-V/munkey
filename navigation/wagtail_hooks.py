from django.urls import reverse, NoReverseMatch
from draftjs_exporter.dom import DOM
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineEntityElementHandler
from wagtail.core import hooks
from wagtail.core.rich_text import LinkHandler
import wagtail.admin.rich_text.editors.draftail.features as draftail_features

import navigation.urls


class MunkeyLinkHandler(LinkHandler):
    identifier = "munkey"

    @staticmethod
    def expand_db_attributes(attrs: dict) -> str:
        name = attrs.get("name")
        try:
            url = reverse(name)
        except NoReverseMatch:
            url = "#"
        return f"<a href='{url}'>"


class MUNkeyLinkElementHandler(InlineEntityElementHandler):
    """
    Database HTML to Draft.js ContentState.
    Converts the <a> tag into a MUNkeyLINK entity, with the right data.
    """
    mutability = 'IMMUTABLE'

    def get_attribute_data(self, attrs):
        return {
            'name': attrs['linktype'],
            "linktype": "munkey"
        }


def munkey_link_decorator(props):
    """
    Draft.js ContentState to database HTML.
    Converts the MUNkeyLINK entities into a <a> tag.
    """
    return DOM.create_element('a', {
        'linktype': "munkey",
        "name": props['name']
    }, props['children'])


@hooks.register('register_rich_text_features')
def register_link_handler(features):
    features.register_link_type(MunkeyLinkHandler)


@hooks.register('register_rich_text_features')
def register_munkey_link(features):
    features.default_features.append('MUNkeyLINK')
    feature_name = 'MUNkeyLINK'
    type_ = 'MUNkeyLINK'

    control = {
        'type': type_,
        'icon': 'link',
        'description': "MUNkey link",
        # We want to enforce constraints on which links can be pasted into rich text.
        # Keep only the attributes Wagtail needs.
        'attributes': ['url', 'id', 'parentId'],
        'whitelist': {
            # Keep pasted links with http/https protocol, and not-pasted links (href = undefined).
            'href': "^(http:|https:|undefined$)",
        }
    }
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.EntityFeature(
            control,
            js=['navigation/js/MUNkeyLINK.js']
        )
    )
    features.register_converter_rule('contentstate', 'MUNkeyLINK', {
        'from_database_format': {
            'a[linktype="munkey"]': MUNkeyLinkElementHandler("MUNkeyLINK"),
        },
        'to_database_format': {
            'entity_decorators': {'MUNkeyLINK': munkey_link_decorator}
        }
    })

@hooks.register('register_admin_urls')
def register_munkey_link_chooser_admin_urls():
    return navigation.urls.urlpatterns

from django.forms import forms, CharField


class MUNkeyLinkChooserForm(forms.Form):
    name = CharField()
    link_text = CharField(required=False)

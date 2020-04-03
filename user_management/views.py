from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.base import View

from user_management.admin import UserCreationForm


class RegisterView(View):
    form_class = UserCreationForm
    initial = {}
    template_name = "registration/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            url = request.build_absolute_uri(
                reverse(
                    "user_management:validate", kwargs={"token": token, "uidb64": uid}
                )
            )
            send_mail(
                "Activate your MUNkey account",
                url,
                "munkey@spitaler.uber.space",
                [user.email],
            )
            messages.success(
                request,
                "Profile created successfully. Please check your mails and click the verification"
                " link to activate your account.",
            )
            return HttpResponseRedirect(reverse("login"))

        return render(request, self.template_name, {"form": form})


class ValidateView(View):
    def get(self, request, uidb64, token):
        uid = urlsafe_base64_decode(uidb64)
        user = get_object_or_404(get_user_model(), pk=uid)
        if default_token_generator.check_token(user, token) and not user.is_active:
            user.is_active = True
            user.save()
            messages.success(request, "Account successfully activated.")
            return HttpResponseRedirect(reverse("login"))
        else:
            raise Http404

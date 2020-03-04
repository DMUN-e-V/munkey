from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from paper_management.models import Paper


class ListView(PermissionRequiredMixin, generic.ListView):
    model = Paper
    permission_required = "paper_management.view_paper"


class DetailView(PermissionRequiredMixin, generic.DetailView):
    model = Paper
    permission_required = "paper_management.view_paper"


class CreateView(PermissionRequiredMixin, generic.CreateView):
    model = Paper
    permission_required = "paper_management.add_paper"
    fields = ["committee", "type", "content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Paper
    permission_required = "paper_management.change_paper"
    fields = ["type", "content"]


class DeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Paper
    permission_required = "paper_management.delete_paper"
    success_url = reverse_lazy("paper_management:paper_list")

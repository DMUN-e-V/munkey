from datetime import datetime

from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from paper_management.models import Paper, Conference, Committee


class PaperListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="1234")
        self.user.user_permissions.add(Permission.objects.get(codename="view_paper"))
        self.conference = Conference.objects.create(
            name="Testkonferenz", start_date=datetime.now(), end_date=datetime.now()
        )
        self.committee = Committee.objects.create(
            name="Testkommitee", conference=self.conference
        )

    def test_no_papers(self):
        """
        Display message if there are no papers
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse("paper_management:paper_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No papers are available.")

    def test_display_paper(self):
        """
        Display a paper in the paper list
        """
        Paper.objects.create(
            user=self.user, committee=self.committee, type=1, content="Paper 1"
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse("paper_management:paper_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.committee.name)

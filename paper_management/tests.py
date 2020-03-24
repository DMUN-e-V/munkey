from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from paper_management.models import Paper, Conference, Committee


class PaperListViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            email="test@test.de",
            password="password",
            gender=0,
            food_preference=0,
            first_name="first_name",
            last_name="last_name",
            birth_date="1970-01-01",
            phone="12345",
            address_line_1="address_line_1",
            address_line_2="address_line_2",
            zip=12345,
            city="city",
            state="state",
        )
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

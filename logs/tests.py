from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Log


class LogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.log = Log.objects.create(
            customer_name="company name",
            assembly_number="A123",
            part_number="12345",
            lot_number="1234567",
            date="2024-01-25",
            shift=1,
            down_time="01:00:01",
            restart_time="01:00:02",
            problem="test problem",
            root_cause="test root cause",
            corrective_action="test correction",
            impact="test impact",
            initiator=cls.user,
        )

    def test_log_creation(self):
        self.assertEqual(self.log.customer_name, "company name")
        self.assertEqual(self.log.assembly_number, "A123")
        self.assertEqual(self.log.part_number, "12345")
        self.assertEqual(self.log.lot_number, "1234567")
        self.assertEqual(self.log.date, "2024-01-25")
        self.assertEqual(self.log.down_time, "01:00:01")
        self.assertEqual(self.log.restart_time, "01:00:02")
        self.assertEqual(self.log.problem, "test problem")
        self.assertEqual(self.log.root_cause, "test root cause")
        self.assertEqual(self.log.impact, "test impact")
        self.assertEqual(self.log.corrective_action, "test correction")
        self.assertEqual(self.log.impact, "test impact")
        self.assertEqual(str(self.log), "A123-1234567-Entry1")

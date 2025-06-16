from django.test import TestCase

# Create your tests here.
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'formedium.settings')
django.setup()

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Logs, Cabinets, Message


class LogsModelTests(TestCase):
    def setUp(self):
        self.log = Logs.objects.create(name='alice', number='101', action='received')

    def test_str_representation(self):
        s = str(self.log)
        self.assertIn('alice', s)
        self.assertIn('received', s)
        self.assertIn('101', s)

    def test_fields(self):
        self.assertEqual(self.log.name, 'alice')
        self.assertEqual(self.log.number, '101')
        self.assertEqual(self.log.action, 'received')
        self.assertIsNotNone(self.log.when)  # перевіряємо, що дата не None


class CabinetsModelTests(TestCase):
    def test_str_cabinet(self):
        cab = Cabinets.objects.create(number='202', name_teacher='Dr. Smith')
        self.assertEqual(str(cab), 'Cabinet 202 - Dr. Smith')
        self.assertEqual(cab.number, '202')
        self.assertEqual(cab.name_teacher, 'Dr. Smith')


class MessageModelTests(TestCase):
    def setUp(self):
        self.message = Message.objects.create(email='test@example.com', text='Hello!')

    def test_str_representation(self):
        s = str(self.message)
        self.assertIn('test@example.com', s)
        self.assertIn('Hello!', s)

    def test_fields(self):
        self.assertEqual(self.message.email, 'test@example.com')
        self.assertEqual(self.message.text, 'Hello!')
        self.assertIsNotNone(self.message.created_at)

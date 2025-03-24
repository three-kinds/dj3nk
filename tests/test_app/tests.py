from django.test import TestCase
from test_app.models import User
from dj3nk.nk_model import nature_key_generator


class T(TestCase):
    def test_success(self):
        s = nature_key_generator.get_core_increment_string()
        first = int(s.get() or 0)

        count = 10
        for i in range(count):
            user = User.objects.create(username=str(i))
            self.assertEqual(user.id >> 16, int(s.get() or 0))

        last = int(s.get() or 0)
        self.assertEqual(last - first, count)

        nature_key_generator.puzzle()
        value_after_puzzle = int(s.get() or 0)
        self.assertTrue(value_after_puzzle > last)

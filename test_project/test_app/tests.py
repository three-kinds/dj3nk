from django.test import TestCase
from test_app.models import User
from dj3nk.nk_model import nkg


class T(TestCase):

    def test_success(self):
        s = nkg.get_core_increment_string()
        first = int(s.get() or 0)

        count = 10
        for i in range(10):
            user = User.objects.create(
                username=str(i)
            )
            self.assertEqual(user.id >> 16, int(s.get() or 0))

        last = int(s.get() or 0)
        self.assertEqual(last - first, count)

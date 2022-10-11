from django.test import SimpleTestCase
from calc import add_num
from app_two import views

class  ViewsTests(SimpleTestCase):
    def test_make_list_unique(self):
        sample_items = [1,1,2,2,3,4,5,5]

        res = views.remove_duplicates(sample_items)
        res1 = list(res)
        self.assertEqual(res1, [1,2,3,4,5])

    def test_add(self):       
        res = add_num(2,3)
        self.assertEqual(res,5)
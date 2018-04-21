from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from tiger_distribution.views import home
from tiger_distribution.models import Item


class HomePageTest(TestCase):

    def test_get_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
        
    def test_home_page_return_corret_page(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'TigerTest1'

        response = home(request)
        expected_html = render_to_string('home.html', {'new_item_text': 'TigerTest1'})
        self.assertEqual(response.content.decode(), expected_html)

class ItemModeTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'the first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'the second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'the first (ever) list item')
        self.assertEqual(second_saved_item.text, 'the second item')
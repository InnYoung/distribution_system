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

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'TigerTest1')
        

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'TigerTest1'

        response = home(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/id/')

    def test_home_page_only_saves_item_when_neccessary(self):
        request = HttpRequest()
        home(request)
        self.assertEqual(Item.objects.count(), 0)

    # def test_home_page_display_all_list_items(self):
    #     Item.objects.create(text='Tiger1')
    #     Item.objects.create(text='Tiger2')

    #     request = HttpRequest()
    #     response = home(request)

    #     self.assertIn('Tiger1', response.content.decode())
    #     self.assertIn('Tiger2', response.content.decode())

class ListViewTest(TestCase):

    def test_displays_all_items(self):
        Item.objects.create(text='Tiger3')
        Item.objects.create(text='Tiger4')

        response = self.client.get('/lists/id/')

        self.assertContains(response, 'Tiger3')
        self.assertContains(response, 'Tiger4')

    def test_uses_list_template(self):
        response = self.client.get('/lists/id/')
        self.assertTemplateUsed(response, 'list.html')

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
from django.test import TestCasfrom django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from products.models import Product

class BagViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a test product
        self.product = Product.objects.create(name='Test Product', price=10.0)

    def test_add_to_bag_view(self):
        url = reverse('add_to_bag', args=[self.product.id])
        data = {'quantity': 2, 'redirect_url': '/'}

        # Log in the user
        self.client.login(username='testuser', password='testpass')

        # Make a POST request to add items to the bag
        response = self.client.post(url, data)

        # Check that the response is a redirect
        self.assertRedirects(response, '/')

        # Check that the bag session has been updated
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 2)

        # Check that success message is set
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'Added {self.product.name}

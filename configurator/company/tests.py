from django.test import TestCase
from django.urls import reverse

class DropdownMenuTestsCompanyIndex(TestCase):
    def setUp(self):
        """Setzt die Startseite für Tests"""
        self.response = self.client.get(reverse('company:index'))  # Lade die Startseite

    def test_dropdown_links_exist(self):
        """Testet, ob alle Links im Dropdown-Menü korrekt sind"""
        # Überprüfen, ob die Links auf die richtigen URLs verweisen
        self.assertContains(self.response, reverse('company:index'))
        self.assertContains(self.response, reverse('product:index'))
        self.assertContains(self.response, reverse('company:about'))

    #def test_dropdown_menu_not_empty(self):
        """Testet, ob das Dropdown-Menü mindestens einen Eintrag enthält"""
        #self.assertContains(self.response, '<li><a class="dropdown-item"', html=True)

    def test_home_link_functionality(self):
        """Testet, ob der Home-Link im Dropdown-Menü korrekt funktioniert"""
        response = self.client.get(reverse('company:index'))
        self.assertEqual(response.status_code, 200)

    def test_product_link_functionality(self):
        """Testet, ob der Products-Link im Dropdown-Menü korrekt funktioniert"""
        response = self.client.get(reverse('product:index'))
        self.assertEqual(response.status_code, 200)

    def test_about_us_link_functionality(self):
        """Testet, ob der About Us-Link im Dropdown-Menü korrekt funktioniert"""
        response = self.client.get(reverse('company:about'))
        self.assertEqual(response.status_code, 200)

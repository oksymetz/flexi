from django.test import TestCase
from django.test import TestCase
from product.models import Box, Material, Product, User


class BoxModelTests(TestCase):
    def setUp(self):
        self.material = Material.objects.create(name="Test Material")  # Beispiel: name ist ein Attribut von Material
        self.product = Product.objects.create(name="Test Product")  # Beispiel: name ist ein Attribut von Product
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_create_valid_box(self):
        """Testet die Erstellung einer Box mit gültigen Werten"""
        box = Box.objects.create(
            box_height=10.0,
            box_length=20.0,
            box_depth=15.0,
            material=self.material,
            product=self.product,
            user=self.user,
            quantity=5,
        )

        self.assertEqual(box.box_height, 10.0)
        self.assertEqual(box.box_length, 20.0)
        self.assertEqual(box.box_depth, 15.0)
        self.assertEqual(box.material, self.material)
        self.assertEqual(box.product, self.product)
        self.assertEqual(box.user, self.user)
        self.assertEqual(box.quantity, 5)


"""from django.test import TestCase, Client
from django.urls import reverse


class CalculatorTests(TestCase):
    def setUp(self):
        # Setup-Client für HTTP-Requests
        self.client = Client()

        # Erstelle einen Benutzer
        self.user = User.objects.create_user(username='viki2301', password='Zwilling2301')


        # URL des Tests
        self.url = reverse('product:configurator')  # Passe den Namen der URL an

        # Login für den Test (falls erforderlich)
        self.client.login(username='viki2301', password='Zwilling2301')

    def test_valid_body_height(self):
        body_height = 180
    

        # Beispielwerte für die fehlenden Felder depth, length und quantity
        depth = 70  # Beispielwert für Tiefe
        length = 120  # Beispielwert für Länge
        quantity = 1  # Beispielwert für die Menge

        data = {
            'inputBodyHeight': body_height,
            'depth': depth,  # Tiefe hinzufügen (das wird als width verwendet)
            'length': length,  # Länge hinzufügen
            'quantity': quantity, # Menge hinzufügen
            'user': self.user
        }

        self.product = Product.objects.create(name="Test Product")

        # HTTP-POST an die URL mit den Daten
        response = self.client.post(self.url, data)

        # Überprüfen, ob die Antwort den Statuscode 200 zurückgibt (OK)
        self.assertEqual(response.status_code, 200)

        # Parsen der JSON-Antwort
        response_data = response.json()

        # Überprüfen, ob die berechneten Höhen vorhanden sind
        self.assertIn('sitting_height', response_data)
        self.assertIn('standing_height', response_data)

        # Erwartete Ergebnisse für die Höhenberechnungen
        expected_sitting_height = 0.125 * 5 * body_height
        expected_standing_height = 0.125 * 3.5 * body_height

        # Überprüfen, ob die berechneten Höhen den erwarteten Werten entsprechen
        self.assertAlmostEqual(response_data['sitting_height'], expected_sitting_height, places=2)
        self.assertAlmostEqual(response_data['standing_height'], expected_standing_height, places=2)"""

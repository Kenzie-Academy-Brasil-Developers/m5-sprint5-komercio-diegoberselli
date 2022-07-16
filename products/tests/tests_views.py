from accounts.models import Account
from products.models import Product
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class ProductsViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        
        cls.product = {
            "description": "Monza 96",
            "price": 5.000,
            "quantity": 1
        }
        
        cls.update_product = {
            "description": "Xbox",
            "quantity": 1,
            "price": 1000
        }
        
        cls.accountSeller = Account.objects.create(
            first_name="nome",
            last_name="fake.last_name",
            email="teste2@tese.com",
            password="1234",
            is_seller=True,
        )
 
        cls.accountUser = {
            "email": "teste@teste.com",
            "password": "123",
            "first_name": "nome",
            "last_name": "sobrenome",
            "is_seller": False
        }
        
    def setUp(self):
        token = Token.objects.create(user=self.accountSeller)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")    

    def test_creating_product_with_token(self):
        response = self.client.post("/api/products/", data=self.product)
        
        self.assertEqual(response.status_code, 201)


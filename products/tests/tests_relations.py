from accounts.models import Account
from django.db import IntegrityError
from django.test import TestCase
from products.models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.products =[Product.objects.create(
                description="elétricos",
                price=10.0,
                quantity=1,
                is_active=True,
                seller_id=1,) 
                for _ in range(5)]
        
        cls.users = Account.objects.create(
            email = "teste@teste.com",
            password="123",
            first_name = "nome",
            last_name = "sobrenome",
            is_seller = True
        )

    def test_seller_may_contain_multiple_products(self):
            
        self.assertEquals(
            len(self.products), self.users.products.count()
        )
        
    def test_product_cannot_belong_to_more_than_one_seller(self):
        
        user_two = Account.objects.create(
            email = "teste2@teste.com",
            first_name = "nome",
            password="123",
            last_name = "sobrenome",
            is_seller = True
        )
        
        for product in self.products:
            product.seller = user_two
            product.save()
            
        for product in self.products:
            self.assertNotIn(product, self.users.products.all())
            self.assertIn(product, user_two.products.all())
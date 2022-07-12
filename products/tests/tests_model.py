from accounts.models import Account
from django.db import IntegrityError
from django.test import TestCase
from products.models import Product


class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.email = "teste@hotmail.com"
        cls.first_name = "Jane"
        cls.last_name = "Doe"
        cls.password = "1234"
        cls.is_seller = True
        
        cls.description = "description two"
        cls.price = 99.90
        cls.quantity = 20
        
        
        cls.seller = Account.objects.create(
            first_name=cls.first_name,
            last_name=cls.last_name,
            email=cls.email,
            is_seller=cls.is_seller,    
        )
        
        cls.product = Product.objects.create(
            description = cls.description,
            price = cls.price,
            quantity = cls.quantity,
            seller = cls.seller
        )
        
    def test_should_has_seller(self):
        product = Product.objects.get(id=1)
        self.assertTrue(product.seller)
        
    
    def test_shoul_not_create_without_seller(self):
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                description = "Produto 1",
                price = 20,
                quantity = 1,
                is_active = True,
            )

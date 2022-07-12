from django.test import TestCase
from accounts.models import Account

class AccountsTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.email = "teste@hotmail.com"
        cls.first_name = "Jane"
        cls.last_name = "Doe"
        cls.password = "1234"
        cls.is_seller = True
        
        cls.account = Account.objects.create(
            first_name=cls.first_name,
            last_name=cls.last_name,
            email=cls.email,
            password=cls.password,
            is_seller=cls.is_seller,
        )


    def test_first_name_max_length(self):
        account = Account.objects.get(id=1)
        max_length = account._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 50)
        
    def test_last_name_max_length(self):
        account = Account.objects.get(id=1)
        max_length = account._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 50)
        
    def test_is_seller(self):
        account = Account.objects.get(id=1)
        response = account.is_seller
        self.assertTrue(response)
        
    def test_saved_object_fields(self):
        self.assertEqual(self.account.first_name, self.first_name)
        self.assertEqual(self.account.last_name, self.last_name)
        self.assertEqual(self.account.is_seller, self.is_seller)

import ipdb
from accounts.models import Account
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class AccountViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.accountSeller = {    
        "email": "teste@teste.com",
        "password": "123",
        "first_name": "nome",
        "last_name": "sobrenome",
        "is_seller": True
                        }
        
        cls.accountUser = {
        "email": "teste@teste.com",
        "password": "123",
        "first_name": "nome",
        "last_name": "sobrenome",
        "is_seller": False
            
        }
        
        cls.WrongData = {
        "email": "teste@teste.com",
        "password": "123",
        "first_name": "nome"    
        }
        

    def test_create_seller(self):
        response = self.client.post('/api/accounts/', data=self.accountSeller)
        
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data["is_seller"])
        
    def test_create_user(self):
        response = self.client.post('/api/accounts/', data=self.accountUser)
        
        self.assertEqual(response.status_code, 201)
        self.assertFalse(response.data["is_seller"])
         
        
    def test_wrong_data(self):
        response = self.client.post('/api/accounts/', data=self.WrongData)
        
        self.assertEqual(response.status_code, 400)
        
    def test_login_seller(self):
        new_seller = Account.objects.create_user(**self.accountSeller)
        response = self.client.post("/api/login/", data=self.accountSeller) 
        
        self.assertEqual(response.status_code, 200)        
        self.assertEqual(response.data["token"], new_seller.auth_token.key)
        
    def test_login_user(self):
        new_user = Account.objects.create_user(**self.accountUser)
        
        response = self.client.post("/api/login/", data=self.accountUser) 

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["token"], new_user.auth_token.key)
        
    def test_get_all_accounts(self):
        
        response = self.client.get("/api/accounts/") 
        
        self.assertEqual(response.status_code, 200)   
        

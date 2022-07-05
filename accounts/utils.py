from django.contrib.auth.models import BaseUserManager

class CustonAccountManager(BaseUserManager):
    
    def _create_user(self, email, first_name, last_name, password, is_seller, is_superuser, **extra_fields ):
        
        if not email:
            raise ValueError ('The given email must be set')
        
        email = self.normalize_email(email)
        
        account = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_seller=is_seller,
            is_staff=is_seller,
            is_superuser=is_superuser,
            **extra_fields
        )
        
        account.set_password(password)
        account.save(using=self._db)
        
        return account
    
    def create_user(self, email, first_name, last_name, password, is_seller, **extra_fields):
        return self._create_user(email, first_name, last_name,  password, is_seller, False, **extra_fields)
    
    def create_superuser(self, email, first_name, last_name, password, is_seller=False, **extra_fields):
        return self._create_user(email, first_name, last_name, password, is_seller, True,**extra_fields)
    
    
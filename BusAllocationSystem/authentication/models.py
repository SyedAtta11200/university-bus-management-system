from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from universitybus.models import Bus

class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)

        user.save()

        return user
    
    def create_superuser(self, username, email, password=None):

        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    class Locations(models.TextChoices):
        ISLAMABAD = 'isl', 'Islamabad'
        ABBOTTABAD = 'atd', 'Abbottabad'
        HAVELIYAN = 'hvl', 'Haveliyan'
        MANSEHRA = 'msa', 'Mansehra'

    username = models.CharField(max_length=20, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)

    is_staff = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    phone_no = models.CharField(max_length=15, null=True, blank=True)

    location = models.CharField(max_length=3, choices=Locations.choices, null=False, blank=False)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="students", null=True, blank=True)

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"


    def __str__(self):
        return self.username
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()



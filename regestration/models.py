from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)

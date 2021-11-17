from django.db import models
import random,string
# Create your models here.

def get_fake_UUID(dim):
    return ''.join(random.sample(string.ascii_letters[26:] + string.digits, dim))
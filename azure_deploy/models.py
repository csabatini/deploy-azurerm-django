from django.db import models
from django.contrib.auth.models import User

class JSONFile(models.Model):
    file = models.FileField(upload_to='media/', null=True)
    type = models.CharField(max_length=50)
    user = models.ForeignKey(User)

from django.utils import timezone

from django.db import models


class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    when = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    action = models.CharField(max_length=200)

    class Meta:
        db_table = "loggs"

    def __str__(self):
        return f"{self.name} - {self.action} - {self.number} at {self.when}"


class Logs1(models.Model):
    id = models.AutoField(primary_key=True)
    when = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    action = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'loggs'

    def __str__(self):
        return f"{self.name} - {self.action} - {self.number} at {self.when}"


class Cabinets(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=50)
    name_teacher = models.CharField(max_length=50)

    class Meta:
        db_table = "cabinets"

    def __str__(self):
        return f"Cabinet {self.number} - {self.name_teacher}"

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "messages"

    def __str__(self):
        return f"Message from {self.email} at {self.created_at}: {self.text[:20]}..."

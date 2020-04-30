from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=60)
    quota = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=90)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    resource = models.URLField(max_length=120)
    transferred = models.PositiveIntegerField()

    def __str__(self):
        return self.transferred

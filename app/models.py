from django.db import models


# Create your models here.

class Avatar(models.Model):
    image = models.ImageField()


class PersonalInformation(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()


class Contact(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=200)


class About(models.Model):
    description = models.TextField(max_length=2000)


class Skills(models.Model):
    title = models.CharField(max_length=200)
    percent = models.FloatField()


class Education(models.Model):
    educational_institution = models.CharField(max_length=300)
    specialization = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()


class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    img = models.ImageField()
    description = models.TextField(max_length=2000)

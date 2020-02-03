from django.db import models

# Create your models here.



class Post(models.Model):

    TAGS = [
        ('AC', 'Academica'),
        ('CU', 'Cultural'),
        ('DE', 'Deportiva')
    ]
    title = models.CharField(max_length = 100)
    body = models.TextField()
    image = models.ImageField()
    date = models.DateField(auto_now = True)
    tag = models.CharField(max_length = 4, choices = TAGS, null = True)

class Calendars(models.Model):

    calendar = models.ImageField()

class Organigrama(models.Model):

    organigrama = models.ImageField()

class PersonalDetails(models.Model):

    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length = 100)
    academic_title = models.CharField(max_length = 100, null=True)
    description = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    department = models.CharField(max_length=100)


class CurricularPlan(models.Model):

    curricular_plan = models.ImageField()

class Programs(models.Model):

    SEMESTERS = [
            ('I','Semestre I '),
            ('II', 'Semestre II'),
            ('III', 'Semestre III'),
            ('IV', 'Semestre IV'),
            ('V', 'Semestre V'),
            ('VI', 'Semestre VI'),
        ]

    semester = models.CharField(max_length = 4, choices = SEMESTERS)
    link  = models.TextField()
    name = models.CharField(max_length = 50)

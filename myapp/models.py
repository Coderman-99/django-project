from django.db import models

# Create your models here.


class Char_detail(models.Model):
    vision = models.CharField(max_length=100, default="default")
    name = models.CharField(max_length=50, default="default")
    f_name = models.CharField(max_length=50, default="default")
    hp = models.CharField(max_length=20, default="default")
    atk = models.CharField(max_length=20, default="default")
    df = models.CharField(max_length=20, default="default")
    asc_rock = models.CharField(max_length=50, default="default")
    asc_rock1 = models.CharField(max_length=50, default="default")
    asc_rock2 = models.CharField(max_length=50, default="default")
    asc_rock3 = models.CharField(max_length=50, default="default")
    asc_mat1 = models.CharField(max_length=50, default="default")
    asc_mat2 = models.CharField(max_length=50, default="default")
    asc_mat3 = models.CharField(max_length=50, default="default")
    asc_mat4 = models.CharField(max_length=50, default="default")
    boss_mat = models.CharField(max_length=50, default="default")
    c1 = models.CharField(max_length=1000, default="default")
    c2 = models.CharField(max_length=1000, default="default")
    c3 = models.CharField(max_length=1000, default="default")
    c4 = models.CharField(max_length=1000, default="default")
    c5 = models.CharField(max_length=1000, default="default")
    c6 = models.CharField(max_length=1000, default="default")

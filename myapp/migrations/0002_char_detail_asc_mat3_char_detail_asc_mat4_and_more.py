# Generated by Django 5.0.2 on 2024-02-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='char_detail',
            name='asc_mat3',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AddField(
            model_name='char_detail',
            name='asc_mat4',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AddField(
            model_name='char_detail',
            name='asc_rock1',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AddField(
            model_name='char_detail',
            name='asc_rock2',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AddField(
            model_name='char_detail',
            name='asc_rock3',
            field=models.CharField(default='default', max_length=50),
        ),
    ]

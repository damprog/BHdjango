# Generated by Django 4.0.4 on 2022-05-18 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BeHealthyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BeHealthyApp.packages'),
            preserve_default=False,
        ),
    ]
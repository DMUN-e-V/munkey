# Generated by Django 2.2.10 on 2020-02-10 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("paper_management", "0002_auto_20200206_1903"),
    ]

    operations = [
        migrations.AlterField(
            model_name="munkeyuser", name="address", field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="munkeyuser",
            name="birth_date",
            field=models.DateField(null=True),
        ),
    ]
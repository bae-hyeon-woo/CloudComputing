# Generated by Django 3.0 on 2019-12-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0002_sreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
            ],
        ),
    ]
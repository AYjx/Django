# Generated by Django 2.0 on 2018-07-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='blog title', max_length=32)),
                ('content', models.TextField(null=True)),
                ('publish_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
# Generated by Django 4.0.4 on 2022-07-26 16:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('alias_category', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('alias_article', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('type', models.CharField(choices=[('1', 'Post'), ('2', 'Page')], default=1, max_length=255)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.category')),
            ],
        ),
    ]

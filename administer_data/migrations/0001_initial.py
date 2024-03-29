# Generated by Django 2.2.5 on 2022-09-19 08:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('class_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('evaluation', models.IntegerField(blank=True, default=0)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('site_url', models.URLField(blank=True, default='')),
                ('city', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='administer_data.City')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lecture_content', models.CharField(max_length=20, unique=True)),
                ('is_target_old', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('review_text', models.TextField(max_length=200)),
                ('faves', models.IntegerField(blank=True, default=0)),
                ('author', models.CharField(blank=True, default='名無し', max_length=20)),
                ('class_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='administer_data.ClassInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='classinfo',
            name='lecture',
            field=models.ManyToManyField(related_name='class_info', to='administer_data.Lecture'),
        ),
        migrations.AddField(
            model_name='city',
            name='prefecture',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='administer_data.Prefecture'),
        ),
    ]

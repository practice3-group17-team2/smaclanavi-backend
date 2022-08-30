# Generated by Django 2.2.5 on 2022-08-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administer_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('class_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('evaluation', models.IntegerField(blank=True, default=0)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('site_url', models.URLField(blank=True, default='')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]

# Generated by Django 2.2.5 on 2022-09-10 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administer_data', '0003_auto_20220903_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='administer_data.City'),
        ),
        migrations.AlterField(
            model_name='review',
            name='class_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='administer_data.ClassInfo'),
        ),
    ]
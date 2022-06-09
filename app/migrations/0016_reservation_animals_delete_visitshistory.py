# Generated by Django 4.0.4 on 2022-05-25 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_visitshistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='animals',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='app.animal'),
        ),
        migrations.DeleteModel(
            name='VisitsHistory',
        ),
    ]
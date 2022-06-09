# Generated by Django 4.0.4 on 2022-05-25 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0014_animal_how_old_animal_weight_alter_animal_rodo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitsHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_title', models.CharField(default='Tytuł wizyty', max_length=200, verbose_name='Tytuł wizyty')),
                ('visit_text', models.TextField(default='Opis wizyty', verbose_name='Treść wizyty')),
                ('visit_date', models.DateField(default=django.utils.timezone.now, verbose_name='Data')),
                ('vet', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Weterynarz')),
            ],
        ),
    ]
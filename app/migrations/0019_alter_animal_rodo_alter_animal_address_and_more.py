# Generated by Django 4.0.4 on 2022-05-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_reservation_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='RODO',
            field=models.CharField(choices=[('tak', 'TAK'), ('nie', 'NIE')], max_length=50, verbose_name='Zgoda na przetwarzanie danych?'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Adres zamieszkania'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.CharField(max_length=300, verbose_name='Rasa zwierzęcia'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='contact',
            field=models.CharField(max_length=12, verbose_name='Kontakt'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='how_old',
            field=models.CharField(default='3lata', max_length=20, verbose_name='Wiek'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='mail',
            field=models.CharField(max_length=30, verbose_name='Adres mailowy'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='neutered',
            field=models.CharField(choices=[('tak', 'TAK'), ('nie', 'NIE')], max_length=50, verbose_name='Czy kastrowany/sterylizowany?'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='nr_chip',
            field=models.CharField(max_length=15, verbose_name='Numer chip'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='owner_name',
            field=models.CharField(max_length=50, verbose_name='Imię właściciela'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='owner_surname',
            field=models.CharField(max_length=50, verbose_name='Nazwisko właściciela'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('żeńska', 'ŻEŃSKA'), ('męska', 'MĘSKA')], max_length=50, verbose_name='Płeć zwierzęcia'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='type',
            field=models.CharField(choices=[('pies', 'PIES'), ('kot', 'KOT'), ('gryzon', 'GRYZOŃ'), ('krolik', 'KRÓLIK'), ('gad', 'GAD'), ('fretka', 'FRETKA'), ('ptak', 'PTAK'), ('inne', 'INNE')], max_length=50, verbose_name='Typ zwierzęcia'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='weight',
            field=models.CharField(default='15kg', max_length=20, verbose_name='Waga'),
        ),
    ]

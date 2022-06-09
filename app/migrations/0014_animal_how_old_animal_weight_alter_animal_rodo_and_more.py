# Generated by Django 4.0.4 on 2022-05-25 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_animal_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='how_old',
            field=models.CharField(default='3', max_length=60, verbose_name='Wiek'),
        ),
        migrations.AddField(
            model_name='animal',
            name='weight',
            field=models.CharField(default='15kg', max_length=100, verbose_name='Waga'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='RODO',
            field=models.CharField(choices=[('tak', 'TAK'), ('nie', 'NIE')], max_length=60, verbose_name='Zgoda na przetwarzanie danych?'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='additional_info',
            field=models.CharField(max_length=3000, verbose_name='Dodatkowe informacje'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='address',
            field=models.CharField(max_length=500, verbose_name='Adres zamieszkania'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.CharField(max_length=500, verbose_name='Rasa zwierzęcia'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='chip',
            field=models.CharField(choices=[('tak', 'TAK'), ('nie', 'NIE')], max_length=60, verbose_name='Czy posiada chip?'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='contact',
            field=models.CharField(max_length=90, verbose_name='Kontakt'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='mail',
            field=models.CharField(max_length=500, verbose_name='Adres mailowy'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Imię zwierzęcia'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='neutered',
            field=models.CharField(choices=[('tak', 'TAK'), ('nie', 'NIE')], max_length=60, verbose_name='Czy kastrowany/sterylizowany?'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='nr_chip',
            field=models.CharField(max_length=150, verbose_name='Numer chip'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='owner_name',
            field=models.CharField(max_length=500, verbose_name='Imię właściciela'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='owner_surname',
            field=models.CharField(max_length=500, verbose_name='Nazwisko właściciela'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('żeńska', 'ŻEŃSKA'), ('męska', 'MĘSKA')], max_length=60, verbose_name='Płeć zwierzęcia'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='type',
            field=models.CharField(choices=[('pies', 'PIES'), ('kot', 'KOT'), ('gryzon', 'GRYZOŃ'), ('krolik', 'KRÓLIK'), ('gad', 'GAD'), ('fretka', 'FRETKA'), ('ptak', 'PTAK'), ('inne', 'INNE')], max_length=60, verbose_name='Typ zwierzęcia'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='animal_type',
            field=models.CharField(choices=[('pies', 'PIES'), ('kot', 'KOT'), ('gryzon', 'GRYZOŃ'), ('krolik', 'KRÓLIK'), ('gad', 'GAD'), ('fretka', 'FRETKA'), ('ptak', 'PTAK'), ('inne', 'INNE')], max_length=60, verbose_name='Typ zwierzęcia'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='owner_name',
            field=models.CharField(max_length=500, verbose_name='Imię właściciela'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(blank=True, max_length=90, verbose_name='Numer komórkowy'),
        ),
    ]

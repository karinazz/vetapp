from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.dateformat import format


#CHOICES

SEX_CHOICES = (
    ('żeńska',
     'ŻEŃSKA'),
    ('męska', 'MĘSKA'),
)


YES_NO_CHOICES = (
    ('tak', 'TAK'),
    ('nie', 'NIE'),
)

ANIMAL_TYPES_CHOICES = (
    ('pies', 'PIES'),
    ('kot', 'KOT'),
    ('gryzon', 'GRYZOŃ'),
    ('krolik', 'KRÓLIK'),
    ('gad', 'GAD'),
    ('fretka', 'FRETKA'),
    ('ptak', 'PTAK'),
    ('inne', 'INNE'),
)

VISIT_TYPES_CHOICES = (
    ('Wizyta kontrolna', 'WIZYTA KONTROLNA'),
    ('Konsultacja chirurgiczna', 'KONSULTACJA CHIRURGICZNA'),
)

#Grafik


class Agenda(models.Model):
    title = models.TextField(verbose_name='Miesiąc')
    cover = models.ImageField(upload_to='images/', verbose_name='Dodaj zdjęcie')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Harmonogram pracy"
        verbose_name_plural = "Harmonogram pracy"


#Klasa POST do BLOGA


class Post(models.Model):
    author = models.ForeignKey('auth.User', verbose_name='Autor', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Tytuł posta', max_length=200)
    text = RichTextField(blank=True, null=True, verbose_name='Tekst')
    created_date = models.DateTimeField(verbose_name='Data utworzenia', default=timezone.now)
    publish_date = models.DateTimeField(verbose_name='Data opublikowania', blank=True, null=True)
    post_date = models.DateField(auto_now_add=True, verbose_name='Data publikacji')

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse('blog')

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posty"

#Weterynarze


class Vet(models.Model):
    name = models.CharField(max_length=100, verbose_name='Imię weterynarza')
    photo = models.ImageField(upload_to="vet-photos/", verbose_name='Zdjęcie')
    description = models.CharField(max_length=200, verbose_name='Dodatkowe informacje')
    specialization = models.CharField(max_length=100, verbose_name='Specjalizacja')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "weterynarz"
        verbose_name_plural = "weterynarze"

# Czas pracy weterynarzy


class WorkingTime(models.Model):
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, verbose_name='Weterynarz')
    start_datetime = models.DateTimeField(verbose_name='Rozpoczęcie pracy')
    is_booked = models.BooleanField(default=False, verbose_name='Zajęty termin')

    def __str__(self):
        return format(self.start_datetime, settings.DATETIME_FORMAT) + f" {self.vet} "

    class Meta:
        verbose_name = "czas pracy"
        verbose_name_plural = "Czas pracy weterynarzy"

#Zwierzę


class Animal(models.Model):
    name = models.CharField(verbose_name='Imię zwierzęcia', max_length=100)
    sex = models.CharField(verbose_name='Płeć zwierzęcia', choices=SEX_CHOICES, max_length=50)
    type = models.CharField(verbose_name='Gatunek zwierzęcia', choices=ANIMAL_TYPES_CHOICES, max_length=50)
    breed = models.CharField(verbose_name='Rasa zwierzęcia', max_length=300)
    weight = models.CharField(verbose_name='Waga', max_length=20, default='15kg')
    how_old = models.CharField(verbose_name='Wiek', max_length=20, default='3lata')
    neutered = models.CharField(verbose_name='Czy kastrowany/sterylizowany?', choices=YES_NO_CHOICES, max_length=50)
    chip = models.CharField(verbose_name='Czy posiada chip?', choices=YES_NO_CHOICES, max_length=60)
    nr_chip = models.CharField(verbose_name='Numer chip', max_length=15)
    additional_info = models.CharField(verbose_name='Dodatkowe informacje', max_length=3000)
    owner_name = models.CharField(verbose_name='Imię właściciela', max_length=50)
    owner_surname = models.CharField(verbose_name='Nazwisko właściciela', max_length=50)
    contact = models.CharField(verbose_name='Kontakt', max_length=9)
    mail = models.CharField(verbose_name='Adres mailowy', max_length=30)
    address = models.CharField(verbose_name='Adres zamieszkania', max_length=200)
    RODO = models.CharField(verbose_name='Zgoda na przetwarzanie danych?', choices=YES_NO_CHOICES, max_length=50)

    def __str__(self):
        return str(self.name) + ' wł. ' + str(self.owner_name) + ' ' + str(self.owner_surname)

    @staticmethod
    def get_absolute_url():
        return reverse('animals')

    class Meta:
        verbose_name = "zwierzę"
        verbose_name_plural = "zwierzęta"


# Rezerwacja


class Reservation(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="reservations", null=True, blank=True,
                               verbose_name='Zwierzę w bazie',)
    animal_name = models.CharField(verbose_name='Imię zwierzęcia', max_length=50)
    animal_type = models.CharField(verbose_name='Gatunek zwierzęcia', choices=ANIMAL_TYPES_CHOICES, max_length=60)
    owner_name = models.CharField(verbose_name='Imię właściciela', max_length=500)
    owner_surname = models.CharField(verbose_name='Nazwisko właściciela', max_length=50)
    phone = models.CharField(verbose_name='Numer komórkowy', max_length=9, blank=True)
    working_time = models.ForeignKey(WorkingTime, on_delete=models.CASCADE, verbose_name="Data rezerwacji", blank=True,
                                     null=True)
    visit_type = models.CharField(verbose_name='Typ wizyty', choices=VISIT_TYPES_CHOICES, max_length=50,
                                  default='Typ wizyty...')
    visit_info = RichTextField(blank=True, null=True, verbose_name='Cel wizyty/Dodatkowe informacje')

    def __str__(self):
        return str(self.animal_name) + ' wł. ' + str(self.owner_name) + ' ' + str(self.owner_surname)

    @staticmethod
    def get_absolute_url():
        return reverse('home')

    class Meta:
        verbose_name = "rezerwacja"
        verbose_name_plural = "rezerwacje"

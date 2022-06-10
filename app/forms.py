from django import forms
from django.db.models import Q

from .models import Animal, Post, Reservation, WorkingTime


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.start_datetime


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twój tytuł...'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Zacznij pisać...'}),

        }


class ReservationForm(forms.ModelForm):
    working_time = MyModelChoiceField(queryset=WorkingTime.objects.all(),
                                      label="Data rezerwacji", widget=forms.Select(attrs={"class": "form-control"}))
    vet_name = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
        label="Weterynarz"
    )

    class Meta:
        model = Reservation
        fields = ('vet_name', 'visit_type', "working_time", 'animal_name', 'animal_type',
                  'owner_name', 'owner_surname', 'phone', 'visit_info')

        widgets = {
            'visit_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twój tekst...'}),
            'visit_type': forms.Select(attrs={'class': 'form-control'}),
            'animal_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię zwierzęcia...'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię właściciela...'}),
            'owner_surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko właściciela...'}),
            'animal_type': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Telefon kontaktowy...'}),
            'working_time': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        vet = kwargs.pop("vet")
        super().__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if instance:
            self.fields["working_time"].queryset = WorkingTime.objects.filter(
                Q(is_booked=False) | Q(pk=instance.working_time.pk), vet=vet)
        else:
            self.fields["working_time"].queryset = WorkingTime.objects.filter(is_booked=False, vet=vet)
        self.fields["vet_name"].initial = vet.name


class AnimalForm(forms.ModelForm):
    reservation = forms.ModelChoiceField(queryset=Reservation.objects.all(), label="Rezerwacja",
                                         widget=forms.Select(attrs={"class": "form-control"}))

    def save(self, commit=True):
        animal = super().save(commit=False)
        reservation = self.cleaned_data.get("reservation")
        if commit:
            animal.save()
            reservation.animal = animal
            reservation.save()
        return animal

    class Meta:
        model = Animal
        fields = ('name', 'sex', 'type', 'breed', 'weight', 'how_old', 'neutered', 'chip', 'nr_chip', 'owner_name',
                  'owner_surname', 'contact', 'mail', 'address', 'RODO', 'additional_info')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię zwierzęcia...'}),
            'animal': forms.Select(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rasa....'}),
            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Waga....'}),
            'how_old': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wiek....'}),
            'neutered': forms.Select(attrs={'class': 'form-control'}),
            'chip': forms.Select(attrs={'class': 'form-control'}),
            'nr_chip': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numer chip...'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię właściciela...'}),
            'owner_surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko właściciela...'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon kontaktowy...'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adres mailowy...'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ulica i Nr domu, Kod pocztowy,'
                                                                                      ' Miasto...'}),
            'RODO': forms.Select(attrs={'class': 'form-control'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dodaj dodatkowe '
                                                                                             'informacje...'}),
        }

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import AnimalForm, PostForm, ReservationForm
from .models import Animal, Post, Reservation, Vet, Agenda


class IsReceptionistMixin:
    def is_receptionist(self):
        return self.request.user.groups.filter(name='Recepcjonista').exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_receptionist"] = self.is_receptionist
        return context


# Blog
class BlogView(IsReceptionistMixin, ListView):
    model = Post
    template_name = 'app/blog.html'
    ordering = ['publish_date']


class ArticleDetailView(IsReceptionistMixin, DetailView):
    model = Post
    template_name = 'app/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app/add_post.html'
    success_message = "Opublikowano post"


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'app/update_post.html'
    # fields = ['title', 'author', 'text']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'app/delete_post.html'
    success_url = reverse_lazy('blog')


# Rezerwacja wizyt


class ReservationChooseVetView(TemplateView):
    template_name = 'app/choose_vet.html'
    extra_context = {
        "vets": Vet.objects.all()
    }


class ReservationView(SuccessMessageMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'app/reservation.html'
    success_url = "/"
    success_message = "Zarezerwowano wizytę"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        vet_obj = get_object_or_404(Vet, id=self.request.GET.get("vet_id"))
        kwargs.update({"vet": vet_obj})
        return kwargs

    def form_valid(self, form):
        obj = form.save()
        obj.working_time.is_booked = True
        obj.working_time.save()
        return super().form_valid(form)


class VisitsView(ListView):
    model = Reservation
    template_name = 'app/visits_panel.html'
    ordering = ['-id']


class EditVisitView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'app/edit_visit.html'
    success_url = reverse_lazy('visits-panel')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        vet = self.object.working_time.vet
        kwargs.update({"vet": vet})
        return kwargs


class DeleteVisitView(DeleteView):
    model = Reservation
    template_name = 'app/delete_visit.html'
    success_url = reverse_lazy('visits-panel')


class VisitDetailView(DetailView):
    model = Reservation
    template_name = 'app/visit_details.html'
    success_url = reverse_lazy('visits-panel')


# Zwierzęta


class AnimalsView(ListView):
    model = Animal
    template_name = 'app/animals.html'
    ordering = ['-id']


class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'app/animal_details.html'


def view_items(request):
    animal = Reservation.animal.filter()
    context = {
        'reservation': animal,
    }
    return render(request, 'app/animal_details.html', context)


class AddAnimalView(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'app/add_animal.html'
    success_url = reverse_lazy('animals')


class EditAnimalView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'app/edit_animal.html'
    success_url = reverse_lazy('animals')


class DeleteAnimalView(DeleteView):
    model = Animal
    template_name = 'app/delete_animal.html'
    success_url = reverse_lazy('animals')


class AgendaView(ListView):
    model = Agenda
    template_name = "app/agenda.html"


# Inne


def home(request):
    return render(request, 'app/home.html', {})


def about(request):
    return render(request, 'app/about.html', {})


def services(request):
    return render(request, 'app/services.html', {})


@login_required
def staff_panel(request):
    return render(request, 'app/staff_panel.html', {})

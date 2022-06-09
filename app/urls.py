from django.urls import path


from . import views
from .views import (AddAnimalView, AddPostView, AnimalDetailView,
                    AnimalsView, ArticleDetailView, BlogView, DeleteAnimalView,
                    DeletePostView, DeleteVisitView, EditAnimalView,
                    EditVisitView, ReservationChooseVetView, ReservationView,
                    UpdatePostView, VisitDetailView, VisitsView, AgendaView)

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('agenda.html', AgendaView.as_view(), name='agenda'),
    path('blog.html', BlogView.as_view(), name='blog'),
    path('services.html', views.services, name='services'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('staff_panel.html', views.staff_panel, name='staff-panel'),
    path('visits_panel.html', VisitsView.as_view(), name='visits-panel'),
    path('visits/edit/<int:pk>', EditVisitView.as_view(), name='edit-visit'),
    path('visits/delete/<int:pk>', DeleteVisitView.as_view(), name='delete-visit'),
    path('visits/<int:pk>', VisitDetailView.as_view(), name='visit-details'),
    path('choose-vet/', ReservationChooseVetView.as_view(), name='choose-vet'),
    path('reservation.html', ReservationView.as_view(), name='reservation'),
    path('animals.html', AnimalsView.as_view(), name='animals'),
    path('animals/<int:pk>', AnimalDetailView.as_view(), name='animal-details'),
    path('add_animal/', AddAnimalView.as_view(), name='add-animal'),
    path('animal/edit/<int:pk>', EditAnimalView.as_view(), name='edit-animal'),
    path('animal/delete/<int:pk>', DeleteAnimalView.as_view(), name='delete-animal'),
]

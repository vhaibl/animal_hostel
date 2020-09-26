from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import viewsets

from .forms import NewAnimalForm
from .models import Animal
from .serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

def animals_list_view(request, *args, **kwargs):
    context = Animal.objects.all()
    if request.user.is_authenticated and not request.user.is_superuser:
        print(f'Animals at shelter {request.user.first_name}')
    return render(request, 'animal_shelter/animals_list.html', {'animals_list': context})

def animal_detail_view(request, pk, *args, **kwargs):
    context = get_object_or_404(Animal, pk=pk)
    # print(request.user.is_authenticated, request.user.is_superuser, request.user.pk, context.shelter_id)
    return render(request, 'animal_shelter/animal_detail.html', {'animal_detail': context})

def new_animal_view(request):
    if request.method == "POST":
        form = NewAnimalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.arrival = timezone.now()
            post.save()
            return redirect('animals:animal_detail', pk=post.pk)
    else:
        form = NewAnimalForm()
    return render(request, 'animal_shelter/animal_edit.html', {'form': form})

def user_id_views(request):
    return request.user.pk


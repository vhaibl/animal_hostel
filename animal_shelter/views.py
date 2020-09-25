from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import NewAnimalForm
from .models import Animal
from .serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    # def list(self, request):
    #     queryset = Animal.objects.all()
    #     serializer = AnimalSerializer(queryset, many=True)
    #     return Response(serializer.data)
    # def retrieve(self, request, pk=None):
    #     queryset = Animal.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = AnimalSerializer(user)
    #     return Response(serializer.data)

# class AnimalView(APIView):
#     def get(self, request, *args, **kwargs):
#         animals = Animal.objects.all()
#         serializer = AnimalSerializer(animals, many=True)
#         return Response({"animals": serializer.data})
#
#     def post(self, request, *args, **kwargs):
#         animal = request.data.get('animals')
#
#         serializer = AnimalSerializer(data=animal)
#         if serializer.is_valid(raise_exception=True):
#             animal_saved = serializer.save()
#         return Response({"success": "Animal '{}' add successfully".format(animal_saved.name)})
#
#     def put(self, request, pk, *args, **kwargs):
#         saved_animal = get_object_or_404(Animal.objects.all(), pk=pk)
#         data = request.data.get('animals')
#         serializer = AnimalSerializer(instance=saved_animal, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             animal_saved = serializer.save()
#         return Response({
#             "success": "Animal '{}' updated successfully".format(animal_saved.name)
#         })
#
#     def delete(self, request, pk, *args, **kwargs):
#         # Get object with this pk
#         animal = get_object_or_404(Animal.objects.all(), pk=pk)
#         animal.delete()
#         return Response({
#             "message": "Animal with id `{}` has been deleted.".format(pk)
#         }, status=204)
#

def animals_list_view(request, *args, **kwargs):
    context = Animal.objects.all()
    if request.user.is_authenticated and not request.user.is_superuser:
        print(f'Animals at shelter {request.user.first_name}')
    return render(request, 'animal_shelter/animals_list.html', {'animals_list': context})

def animal_detail_view(request, pk, *args, **kwargs):
    context = get_object_or_404(Animal, pk=pk)
    print(request.user.is_authenticated, request.user.is_superuser, request.user.pk, context.shelter_id)
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
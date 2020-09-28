from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .forms import NewAnimalForm
from .models import Animal
from .serializers import AnimalSerializer, AnimalSerializerLimited


class AnimalViewSetReadOnly(ReadOnlyModelViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """
    serializer_class = AnimalSerializerLimited
    queryset = Animal.objects.all()


class IsSuperAdminUser(BasePermission):
    """
    Allows access only to superusers.
    """

    def has_permission(self, request, view):
        print('ama  superuser', bool(request.user and request.user.is_superuser))
        print('ama  staff', bool(request.user and request.user.is_staff))
        return bool(request.user and request.user.is_superuser)


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """

    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False


class MyModelViewSet(ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    permission_classes = (ActionBasedPermission,)

    action_permissions = {

        IsAdminUser: [  # 'destroy',
            # 'list',
            'retrieve',
            'update',
            'partial_update',
            'create',
            'metadata',
            'options', ],
        IsAuthenticated: [  # 'destroy',
            # 'list',
            'retrieve',
            'update',
            'partial_update',
            'create',
            'metadata',
            'options', ],
        IsSuperAdminUser: [
            'destroy',
            # 'list',
            'retrieve',
            'update',
            'partial_update',
            'create',
            'metadata',
            'options',
        ],
        AllowAny: []
    }
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)


def animals_list_view(request, *args, **kwargs):
    if request.user.is_authenticated and not request.user.is_superuser:
        context = Animal.objects.filter(shelter_id=request.user.id)
    else:
        context = Animal.objects.all()

    return render(request, 'animal_shelter/animals_list.html', {'animals_list': context})


def animal_detail_view(request, pk, *args, **kwargs):
    context = get_object_or_404(Animal, pk=pk)
    return render(request, 'animal_shelter/animal_detail.html', {'animal_detail': context})


def new_animal_view(request):
    if request.method == "POST":
        form = NewAnimalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.shelter = request.user
            post.arrival = timezone.now()
            post.save()
            return redirect('animals:animal_detail', pk=post.pk)
    else:
        form = NewAnimalForm()
    return render(request, 'animal_shelter/animal_edit.html', {'form': form})


def edit_animal_view(request, pk):
    post = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        form = NewAnimalForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.shelter = request.user
            post.arrival = timezone.now()
            post.save()
            return redirect('animals:animal_detail', pk=post.pk)
    else:
        form = NewAnimalForm(instance=post)
    return render(request, 'animal_shelter/animal_edit.html', {'form': form})


def delete_animal_view(request, pk):
    post = get_object_or_404(Animal, pk=pk)
    post.delete()
    return redirect('animals:animals_list')

def undelete_animal_view(request, pk):
    if request.user.is_superuser:
        post = Animal.deleted_objects.get(pk=pk)
        post.undelete()
    return redirect('animals:animals_list')
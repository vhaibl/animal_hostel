from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Animal


@admin.register(Animal)
class RestrictedFormAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        if not request.user.is_superuser: # Только суперпользователь может менять
            User = get_user_model()
            context['adminform'].form.fields['shelter'].queryset = User.objects.filter(username=request.user)
        return super(RestrictedFormAdmin, self).render_change_form(request, context, args, kwargs)
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field =  super(RestrictedFormAdmin, self).formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == 'shelter':
            field.initial = request.user.id
        return field

# admin.site.register(Animal)
# admin.site.register(Shelter)
# @admin.register(Shelter)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Client,Project,Product
from django.contrib.auth.forms import UserChangeForm

class RestrictedFormAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['userid'].queryset = User.objects.filter(is_staff=True)
        return super(RestrictedFormAdmin, self).render_change_form(request, context, args, kwargs)
    
class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class UserAdmin(UserAdmin):
    form = UserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('clientid','location')}),
    )


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Client,RestrictedFormAdmin)
admin.site.register(Project)
admin.site.register(Product)

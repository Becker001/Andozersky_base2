from django.contrib import admin

from myapp1.models import Contact, Application


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'surname', 'number', 'message')  #  поля должны отображаться в списке объектов


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'surname', 'number', 'data','data2','place', 'message')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Application, ApplicationAdmin)

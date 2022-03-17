from django.contrib import admin
from django.contrib.auth.models import Group, User
from . models import * 

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth']
    fields = [('user',),('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'due_back', 'status']
    # list_filter = ('due_back','status')

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','isbn','genres']

    inlines = [BookInstanceInline]



admin.site.register(Author, AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance,BookInstanceAdmin)
# admin.site.unregister(Group)
# admin.site.unregister(User)
# Register your models here.

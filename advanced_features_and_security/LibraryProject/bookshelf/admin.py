from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser # Customizing the Admin Interface

class BookAdmin(admin.ModelAdmin):
    # Display the book's field in list form
    list_display = ('title', 'author', 'publication_year')
    #Adding filters for the list view
    list_filter = ('author', 'publication_year')
    #Enables search capabilities for the title and author field
    search_fields = ('title', 'author')
    

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('permissions', {'fields', ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' :('email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_acive'),
        }),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    


admin.site.register(Book, CustomUser, CustomUserAdmin)




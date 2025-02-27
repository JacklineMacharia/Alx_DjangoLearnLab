from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
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
    


admin.site.register(CustomUser, CustomUserAdmin)

def create_groups_and_permissions():
    content_type = ContentType.objects.get_for_model(Book)
    
    permissions = [
        ("can_view", "Can view books"),
        ("can_create", "Can create books"),
        ("can_edit", "Can edit books"),
        ("can_delete", "Can delete books"),
    ]
    
    # Ensure each permission exists
    for codename, name in permissions:
        permission, created = Permission.objects.get_or_create(
            codename=codename,
            content_type=content_type,
            defaults={"name": name},
        )
    # Create groups
    groups = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    
    }
    
    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm in perms:
            permission = Permission.objects.get(codename=perm)
            group.permissions.add(permission)
            
create_groups_and_permissions()



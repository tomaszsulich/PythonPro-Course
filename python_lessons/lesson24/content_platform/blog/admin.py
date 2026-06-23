from django.contrib import admin
from .models import Author, Post

# Register your models here.
class PostInline(admin.TabularInline):
    model = Post
    extra = 1 # na ile rekordów mamy formularze

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...

# PREFEROWANY SPOSÓB
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ...
    
    list_display = ("name", "email")
    list_filter = ("email",)
    inlines = [PostInline]
    
    def full_name(self, obj):
        idx = obj.email.index("@")
        return f"{obj.name} {obj.email[:idx]}"
    full_name.short_description = "my custom field"
    


# admin.site.register(Author)
# powyższe dwie linijki są równoznaczne z poniższymi   
# class PostAdmin(admin.ModelAdmin):
#     ...

# admin.site.register(Post, PostAdmin)
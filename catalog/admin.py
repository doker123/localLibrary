from django.contrib import admin
from .models import Book, BookInstance, Language, Author, Genre

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Language)
# admin.site.register(Author)
# admin.site.register(Genre)



class BookInline(admin.TabularInline):
    model = Book
class BookInstanceInline(admin.TabularInline):
    model = BookInstance



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ('last_name', 'first_name', ('date_of_birth', 'date_of_death'))
    inlines = [BookInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    list_display = ('book', 'due_back', 'id')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
import uuid

from django.db import models
from django.urls import reverse

class Genre(models.Model):

    name = models.CharField(max_length=200, help_text='Жанр книги(например: Фантастика, Ужасы, Детектив.')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Описание книги')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Символов')
    genre = models.ManyToManyField(Genre, help_text='Выбирите жанры книги')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description = 'Genre'




class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный id для именно этой книги во всей библиотеке")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=10, choices=LOAN_STATUS, blank=True, default='m', help_text='Состояние книги')

    class Meta:
        ordering = ['due_back']


    def __str__(self):
        return '%s - %s' % (self.id, self.due_back)

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)
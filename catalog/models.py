from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True,blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died',null=True, blank=True)
    # date_joined = models.DateTimeField(auto_now_add=True)
    # active = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Authoresssseeeee'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Genre(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True ,help_text = 'Enter a book genre (e.g. Science Fiction)')
    class Meta:
        ordering = ['name']
    def __str__(self):
        # return f"{self.name} {self.last_name}"
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text = '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre,help_text='Select a genre for this book')


    def __str__(self):
        return f'{self.title} {self.author} {self.isbn}'

    def genres(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    genres.short_description = 'Genre'

class BookInstance(models.Model):
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200, null=True, blank=True)
    due_back = models.DateField(null=True, blank=True)


    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'

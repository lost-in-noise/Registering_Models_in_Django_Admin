from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
    bio = models.TextField(blank=True, verbose_name='Biography')

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Book Title')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN')
    published_date = models.DateField(verbose_name='Published Date')
    summary = models.TextField(blank=True, verbose_name='Summary')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


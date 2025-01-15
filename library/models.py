from django.db import models

class Books(models.Model):
    GENRE_CHOICES = (
        ('Ужасы', 'Ужасы'),
        ('Романтика', 'Романтика'),
        ('Фэнтэзи', 'Фэнтэзи')
    )
    image = models.ImageField(upload_to = 'books/', verbose_name= 'Add photo')
    title = models.CharField(max_length= 100, verbose_name= 'Add title for book')
    description = models.TextField(verbose_name='Add description', blank= True)
    price = models.PositiveIntegerField(verbose_name= 'Add price', default= 500)
    release_date = models.DateTimeField(auto_now_add= True)
    genre = models.CharField(max_length= 100, choices=GENRE_CHOICES, verbose_name='Add genre')
    mail_autor = models.EmailField(verbose_name='Add mail autor')
    autor = models.CharField(max_length=100, verbose_name='Add autor', default='Джоан Роулинг')
    trailer = models.URLField(verbose_name='Add link from Youtube')
    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'список книг'

    def __str__(self):
        return f'{self.title} : {self.price} сом'

class Comment(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    )
    comment = models.TextField(verbose_name='Комментарий')
    stars = models.CharField(choices=STARS, max_length= 10, verbose_name='Оценка')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name= 'reviews')

    def __str__(self):
        return f'{self.book.title}'
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'





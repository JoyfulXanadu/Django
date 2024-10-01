from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name="slug", **NULLABLE)
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    image = models.ImageField(**NULLABLE, upload_to='blog/', verbose_name='Превью')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
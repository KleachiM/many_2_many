from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField('Scope', related_name='scopes', through='ArticleScopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):

    topic = models.TextField()

    def __str__(self):
        return self.topic


class ArticleScopes(models.Model):

    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    scope = models.ForeignKey(Scope, on_delete=models.DO_NOTHING)
    is_main = models.BooleanField()

    def __str__(self):
        return f'Заголовок: {self.scope}. {self.is_main}'
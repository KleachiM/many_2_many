from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleScopes, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_main = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get('is_main') == True:
                count_main += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        if count_main != 1:
            raise ValidationError('Должен быть один главный заголовок!')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopesInline(admin.TabularInline):
    model = ArticleScopes
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopesInline]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass

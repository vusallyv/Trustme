from modeltranslation.translator import translator, TranslationOptions
from .models import Blog


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'author')


translator.register(Blog, BlogTranslationOptions)

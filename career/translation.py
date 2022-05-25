from modeltranslation.translator import translator, TranslationOptions
from .models import Vacancy


class VacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'full_description')


translator.register(Vacancy, VacancyTranslationOptions)

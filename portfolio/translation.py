from modeltranslation.translator import translator, TranslationOptions
from .models import ProjectProcess, ProjectResult, ProjectStatistic, ServiceProject


class ServiceProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class ProjectProcessTranslationOptions(TranslationOptions):
    fields = ('title', 'period',)


class ProjectResultTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ProjectStatisticTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


translator.register(ServiceProject, ServiceProjectTranslationOptions)
translator.register(ProjectProcess, ProjectProcessTranslationOptions)
translator.register(ProjectResult, ProjectResultTranslationOptions)
translator.register(ProjectStatistic, ProjectStatisticTranslationOptions)

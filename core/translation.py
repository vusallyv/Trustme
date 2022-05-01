from modeltranslation.translator import translator, TranslationOptions
from .models import AboutUs, AboutUsInfo, AboutUsStatistic, AboutUsTeam


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'slogan', 'slogan_author')


class AboutUsStatisticTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class AboutUsInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class AboutUsTeamTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'description')


translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(AboutUsStatistic, AboutUsStatisticTranslationOptions)
translator.register(AboutUsInfo, AboutUsInfoTranslationOptions)
translator.register(AboutUsTeam, AboutUsTeamTranslationOptions)

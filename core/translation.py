from modeltranslation.translator import translator, TranslationOptions
from .models import AboutUs, AboutUsInfo, AboutUsSlogan, AboutUsStatistic, AboutUsTeam


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class AboutUsStatisticTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class AboutUsInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class AboutUsTeamTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'description')


class AboutUsSloganTranslationOptions(TranslationOptions):
    fields = ('slogan', 'slogan_author')


translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(AboutUsStatistic, AboutUsStatisticTranslationOptions)
translator.register(AboutUsInfo, AboutUsInfoTranslationOptions)
translator.register(AboutUsTeam, AboutUsTeamTranslationOptions)
translator.register(AboutUsSlogan, AboutUsSloganTranslationOptions)

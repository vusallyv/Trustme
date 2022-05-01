from modeltranslation.translator import translator, TranslationOptions
from .models import Service, ServiceAdvantage, ServiceSpecialist, ServicePacket, ServiceCategory


class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


class ServiceAdvantageTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class ServiceSpecialistTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class ServicePacketTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'price_per')


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'full_description')


translator.register(ServiceCategory, ServiceCategoryTranslationOptions)
translator.register(ServiceAdvantage, ServiceAdvantageTranslationOptions)
translator.register(ServiceSpecialist, ServiceSpecialistTranslationOptions)
translator.register(ServicePacket, ServicePacketTranslationOptions)
translator.register(Service, ServiceTranslationOptions)

from django.contrib import admin

from example.models import Image
from .models import Choice, Question


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'get_attr')
    # fields = ('question_text', 'pub_date')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

    date_hierarchy = 'pub_date'

    list_display_links = ('question_text', 'pub_date')

    list_per_page = 10

    #


    def get_attr(self, obj):
        return 11

    # short_description = {'get_attr': 'custom_field'}


# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
admin.site.register(Image)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    raw_id_fields = ('question',)


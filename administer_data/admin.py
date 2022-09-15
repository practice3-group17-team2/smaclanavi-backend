from django.contrib import admin
from .models import Prefecture, City, Lecture, ClassInfo, Review
# Register your models here.

class PrefectureAdmin(admin.ModelAdmin):
    fields = ['pref_name']
class CityAdmin(admin.ModelAdmin):
    fields = ['city_name', 'prefecture']
class LectureAdmin(admin.ModelAdmin):
    fields = ['lecture_content', 'is_target_old']
class ClassInfoAdmin(admin.ModelAdmin):
    fields = ['class_name', 'phone_number', 'city', 'address', 'lecture', 'price', 'site_url']
class ReviewAdmin(admin.ModelAdmin):
    fields = ['class_info', 'review_text', 'faves', 'author']

admin.site.register(Prefecture, PrefectureAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(Review, ReviewAdmin)
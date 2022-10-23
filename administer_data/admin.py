from django.contrib import admin
# from .models import Prefecture, City, Lecture, ClassInfo, Review
import administer_data.models as md
# Register your models here.

class PrefectureAdmin(admin.ModelAdmin):
    fields = ['pref_name']

class CityAdmin(admin.ModelAdmin):
    fields = ['city_name', 'prefecture']

class LectureAdmin(admin.ModelAdmin):
    fields = ['lecture_content', 'is_target_old']

class ClassInfoAdmin(admin.ModelAdmin):
    fields = ['class_name', 'class_organizer', 'phone_number', 'city', 'address', 'lecture', 'price', 'site_url']

class ReviewAdmin(admin.ModelAdmin):
    fields = ['class_info', 'review_text', 'faves', 'author']

class ClassOrgAdmin(admin.ModelAdmin):
    fields = ['organizer_name']

class UpcomingLecInfosAdmin(admin.ModelAdmin):
    fields = ['lecture_content', 'which_class_held', 'is_personal_lec', 'is_iphone', 'can_select_date']

class LecScheduleAdmin(admin.ModelAdmin):
    fields = ['lec_info', 'date']



admin.site.register(md.Prefecture, PrefectureAdmin)
admin.site.register(md.City, CityAdmin)
admin.site.register(md.Lecture, LectureAdmin)
admin.site.register(md.ClassInfo, ClassInfoAdmin)
admin.site.register(md.Review, ReviewAdmin)
admin.site.register(md.ClassOrganizer, ClassOrgAdmin)
admin.site.register(md.UpcomingLecInfos, UpcomingLecInfosAdmin)
admin.site.register(md.LecSchedule, LecScheduleAdmin)

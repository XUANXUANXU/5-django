from django.contrib import admin
from booktest.models import BookInfo,HeroInfo
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','bname','bdate']
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname','isdelete']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)


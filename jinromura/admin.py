from django.contrib import admin
from .models import Village,Character
# Register your models here.
#DBのテーブル追加して、編集可能にする
admin.site.register(Village)
admin.site.register(Character)

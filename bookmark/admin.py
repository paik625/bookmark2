from django.contrib import admin

# Register your models here.
from .models import Bookmark

# Todo : 관리자 페이지 커스터마이징
admin.site.register(Bookmark)
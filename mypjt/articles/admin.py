from django.contrib import admin

# Article 에 대해 관리자 페이지에서 관리할 수 있도록...
from .models import Article

admin.site.register(Article)
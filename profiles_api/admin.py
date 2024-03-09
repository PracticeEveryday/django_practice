from django.contrib import admin
from profiles_api import models

# 해당 파일에 등록해야 피드 아이템을 모아 볼 수 있다.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
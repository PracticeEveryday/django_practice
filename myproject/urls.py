from django.contrib import admin
from django.urls import path
# http://127.0.0.1/
# http://127.0.0.1/app

# http://127.0.0.1/create/
# http://127.0.0.1/read/1/

urlpatterns = [
    # 쟝고가 가지고 있는 어드민 URL이 있음.
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # 쟝고가 가지고 있는 어드민 URL이 있음.
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))
]


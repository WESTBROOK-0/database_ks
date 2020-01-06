from django.urls import path, re_path
from .  import views
urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('index/',views.index,name='index'),
    re_path('(\d+)/',views.detail,name='detail')

]
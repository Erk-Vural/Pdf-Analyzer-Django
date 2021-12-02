from django.urls import path

from Main.views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('admin-panel', admin_panel_view, name='admin-panel'),
    path('user-panel', user_panel_view, name='user-panel')

]

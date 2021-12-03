from django.urls import path

from Main.views import *

urlpatterns = [
    # Login urls
    path('', login_view, name='login'),
    path('admin-panel', admin_panel_view, name='admin-panel'),
    path('user-panel', user_panel_view, name='user-panel'),

    # Admin panel urls
    path('user/create', user_create_view, name='user-create'),
    path('user/delete/<int:pk>/', user_delete_view, name='user-delete'),
    path('user/update<int:pk>/', user_update_view, name='user-update'),

    # User panel urls

]

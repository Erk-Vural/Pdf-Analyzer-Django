from django.urls import path

from Main.Views.admin import admin_panel_view
from Main.Views.document import document_create_view, document_delete_view
from Main.Views.login import login_view
from Main.Views.user import user_create_view, user_delete_view, user_update_view, user_panel_view

urlpatterns = [
    # Login urls
    path('', login_view, name='login'),

    # Admin panel urls
    path('admin-panel', admin_panel_view, name='admin-panel'),
    path('user/create', user_create_view, name='user-create'),
    path('user/delete/<int:pk>', user_delete_view, name='user-delete'),
    path('user/update/<int:pk>', user_update_view, name='user-update'),

    # User panel urls
    path('user-panel/<int:pk>', user_panel_view, name='user-panel'),
    path('document/create/<int:pk>', document_create_view, name='document-create'),
    path('document/delete/<int:tk>/<int:pk>', document_delete_view, name='document-delete'),

]

from django.urls import path

from Main.Views.admin import admin_panel_view
from Main.Views.document import document_create_view, document_delete_view, document_detail_view
from Main.Views.login import login_view
from Main.Views.query1 import query1_home_view, author_view, courseName_view, title_view, keyword_view, semester_view, \
    query1_list_view
from Main.Views.user import user_create_view, user_delete_view, user_update_view, user_home_view

urlpatterns = [
    # Login urls
    path('', login_view, name='login'),

    # Admin panel urls
    path('admin-panel', admin_panel_view, name='admin-panel'),
    path('user/create', user_create_view, name='user-create'),
    path('user/delete/<int:pk>', user_delete_view, name='user-delete'),
    path('user/update/<int:pk>', user_update_view, name='user-update'),

    # User panel urls
    path('user-home/<int:pk>', user_home_view, name='user-home'),
    path('document/create/<int:pk>', document_create_view, name='document-create'),
    path('document/delete/<int:tk>/<int:pk>', document_delete_view, name='document-delete'),
    path('document/detail/<int:tk>/<int:pk>', document_detail_view, name='document-detail'),

    # Query 1 urls
    path('query1-home/<int:pk>', query1_home_view, name='query1-home'),
    path('author-list/<int:pk>', author_view, name='author-list'),
    path('courseName-list/<int:pk>', courseName_view, name='courseName-list'),
    path('title-list/<int:pk>', title_view, name='title-list'),
    path('keyword-list/<int:pk>', keyword_view, name='keyword-list'),
    path('semester-list/<int:pk>', semester_view, name='semester-list'),
    path('query1-list/<int:tk>/<int:pk>', query1_list_view, name='query1-list'),



]

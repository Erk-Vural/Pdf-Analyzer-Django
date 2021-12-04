from django.contrib import admin

from .Models.Admin import Admin
from .Models.Document import Document
from .Models.User import User


# Register your models here.
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Document)

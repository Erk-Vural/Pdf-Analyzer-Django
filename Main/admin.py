from django.contrib import admin

from .Models.Admin import Admin
from .Models.Document import *
from .Models.User import User


# Register your models here.
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Document)

admin.site.register(Author)
admin.site.register(CourseName)
admin.site.register(Summary)
admin.site.register(Semester)
admin.site.register(Title)
admin.site.register(Keyword)
admin.site.register(MentorInfo)
admin.site.register(JuryInfo)

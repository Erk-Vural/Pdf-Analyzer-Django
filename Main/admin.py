from django.contrib import admin

from Main.Models.Admin import Admin
from Main.Models.Author import Author
from Main.Models.CourseName import CourseName
from Main.Models.Document import Document
from Main.Models.JuryInfo import JuryInfo
from Main.Models.Keyword import Keyword
from Main.Models.MentorInfo import MentorInfo
from Main.Models.Semester import Semester
from Main.Models.Summary import Summary
from Main.Models.Title import Title
from Main.Models.User import User

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

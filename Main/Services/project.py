from Main.Services.author import delete_author
from Main.Services.course_name import delete_course_name
from Main.Services.document import delete_document
from Main.Services.jury import delete_jury_info
from Main.Services.keyword import delete_keyword
from Main.Services.mentor import delete_mentor_info
from Main.Services.semester import delete_semester
from Main.Services.summary import delete_summary
from Main.Services.title import delete_title


def delete_project(pk):
    delete_document(pk)
    delete_author(pk)
    delete_course_name(pk)
    delete_jury_info(pk)
    delete_keyword(pk)
    delete_mentor_info(pk)
    delete_semester(pk)
    delete_summary(pk)
    delete_title(pk)



from Main.Services.author import delete_author
from Main.Services.course_name import delete_course_name
from Main.Services.document import delete_document
from Main.Services.jury import delete_jury_info
from Main.Services.keyword import delete_keyword
from Main.Services.mentor import delete_mentor_info
from Main.Services.semester import delete_semester
from Main.Services.summary import delete_summary
from Main.Services.title import delete_title


def delete_project(user_id, doc_id):
    delete_document(doc_id)
    delete_author(user_id, doc_id)
    delete_course_name(user_id, doc_id)
    delete_jury_info(user_id, doc_id)
    delete_keyword(user_id, doc_id)
    delete_mentor_info(user_id, doc_id)
    delete_semester(user_id, doc_id)
    delete_summary(user_id, doc_id)
    delete_title(user_id, doc_id)



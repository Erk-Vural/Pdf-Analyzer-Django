from django.shortcuts import render

from Main.Services.course_name import read_course_name_by_user
from Main.Services.semester import read_semester_by_user


def query2_home_view(request, pk):
    semesters = read_semester_by_user(pk)
    course_names = read_course_name_by_user(pk)

    datas = []
    for course_name in course_names:
        for semester in semesters:
            if course_name.doc_id == semester.doc_id:
                data = {
                    'content': course_name.content + " " + semester.content,
                    'doc_id': course_name.doc_id
                }
                datas.append(data)

    context = {
        'user_id': pk,
        'datas': datas
    }

    return render(request, "query2.html", context)

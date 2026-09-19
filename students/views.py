from django.shortcuts import render
from .models import Student


def student_list(request):

    students = Student.objects.all()

    context = {
        "students": students,
    }

    return render(
        request,
        "students/student_list.html",
        context
    )
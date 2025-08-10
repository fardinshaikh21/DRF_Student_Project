from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response    
from rest_framework import status 
from .models import Student  
from .serializers import StudentSerializer
#from django.views.decorators.csrf import csrf_exempt


#Create your views here.
# @api_view(["GET"])
# def StudentView(request):
#     students = Student.objects.all().values('name', 'age', 'email')
#     return Response(students, status=status.HTTP_200_OK)

#@csrf_exempt
@api_view(["GET","POST"])
def StudentView(request):

    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["GET","PUT","DELETE"])    
def StudentDetailView(request, pk):
    
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  


def index(request):
    if request.method == "POST":
        search = request.POST.get('search', '').strip()
        students = Student.objects.filter(name__icontains=search)  # case-insensitive search

        if not students.exists():
            return render(request, 'index.html', {
                'students': [],
                'error': "No student found"
            })

        return render(request, 'index.html', {
            'students': students
        })

    # GET request → show all students
    students = Student.objects.all()
    return render(request, 'index.html', { 'students': students })


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        if not name or not age or not email:
            return render(request, 'add.html', {
                'error': "All fields are required."
            })

        student = Student(name=name, age=age, email=email)
        student.save()
        return render(request, 'add.html', {
            'success': "Student added successfully."
        })

    return render(request, 'add.html')  # Render the form for adding a student


def update(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        if not name or not age or not email:
            return render(request, 'update.html', {
                'student': student,
                'error': "All fields are required."
            })

        student.name = name
        student.age = age
        student.email = email
        student.save()

        return render(request, 'update.html', {
            'student': student,
            'success': "Student details updated successfully!"
        })

    return render(request, 'update.html', { 'student': student })


def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return render(request, 'index.html', {
        'students': Student.objects.all(),
        'success': "Student deleted successfully."
    })
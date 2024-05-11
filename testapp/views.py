from django.shortcuts import render, redirect
from .models import Instructor, Course, Lecture

# Create your views here.

def admin(request):
        if request.method == 'GET':
            instructors = Instructor.objects.all()
            return render(request, 'admin.html', {'instructors': instructors})
        elif request.method == 'POST':
            name = request.POST['name']
            level = request.POST['level']
            description = request.POST['description']
            image = request.FILES['image']
            
            # instructor = Instructor.objects.get(id=instructor_id)
            course = Course.objects.create(name=name, level=level, description=description, image=image)
            
            return redirect('lecture/1', course_id=course.id)

def assign_lecture(request, course_id):
    course = Course.objects.get(id=course_id)
    
    if request.method == 'POST':
        date = request.POST['date']
        instructor_id = request.POST['instructor']
        
        instructor = Instructor.objects.get(id=instructor_id)
        lecture = Lecture.objects.create(date=date, course=course, instructor=instructor)
        
        return redirect('assign_lecture', course_id=course.id)
    
    instructors = Instructor.objects.all()
    return render(request, 'assign_lecture.html', {'course': course, 'instructors': instructors})

def panel(request):
    instructor = Instructor.objects.get(id=request.user.id)
    lectures = Lecture.objects.filter(instructor=instructor)
    return render(request, 'instructor_panel.html', {'lectures': lectures})
    # return render(request,"instructor_panel.html")
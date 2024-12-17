from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from schedule.forms import MajorForm, ScheduleForm, SubjectForm, TeacherForm
from schedule.models import Schedule, Subject, Major, Teacher

# Create your views here.
def dashboard(request):
    query = request.GET.get('query', '')
    flag = 0
    # check if user input something in the search bar and if yes, filter and return match schedule
    if query:
        schedules = Schedule.objects.filter(
            major__name__icontains=query
        ) | Schedule.objects.filter(
            subject__name__icontains=query
        ) | Schedule.objects.filter(
            teacher__name__icontains=query
        ) | Schedule.objects.filter(
            day__icontains=query
        )
        flag = 1
    else:
        majors = Major.objects.all()
        subjects = Subject.objects.all()
        schedules = Schedule.objects.all()
        teachers = Teacher.objects.all()

        major_dict = {}
        for major in majors:
            major_dict[major.id] = major

        subject_dict = {}
        for subject in subjects:
            subject_dict[subject.id] = subject

        teacher_dict = {}
        for teacher in teachers:
            teacher_dict[teacher.id] = teacher

        schedule_list = []
        for schedule in schedules:
            schedule_list.append(
                {
                    'id': schedule.id,
                    'major': major_dict[schedule.major_id],
                    'subject': subject_dict[schedule.subject_id],
                    'teacher': teacher_dict[schedule.teacher_id],
                    'time_begins': schedule.time_begins,
                    'time_ends': schedule.time_ends,
                    'room': schedule.room,
                    'day': schedule.day
                }
            )
        schedules = schedule_list
 
    context = {
        'schedules': schedules,
        'query': query,
        'flag': flag
    }
    return render(
        request=request, 
        template_name='dashboard.html',
        context=context
    )

def create_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    form = ScheduleForm()
    major_form = MajorForm()
    subject_form = SubjectForm()
    teacher_form = TeacherForm()
    majors = Major.objects.all().values()
    subjects = Subject.objects.all().values()
    teachers = Teacher.objects.all().values()
    return render(
        request=request,
        template_name='add-schedule.html',
        context={
            'form': form,
            'major_form': major_form,
            'subject_form': subject_form,
            'teacher_form': teacher_form,
            'majors': majors,
            'subjects': subjects,
            'teachers': teachers
        }
    )
    
def create_major(request):
    form = MajorForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/createSchedule')
    
def create_subject(request):
    form = SubjectForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/createSchedule')
    
def create_teacher(request):
    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/createSchedule')
    
def destroy(request, id):
    schedule = get_object_or_404(Schedule, pk=id)
    schedule.delete()
    return redirect('/')

def update(request, id):
    # Retrieve the specific schedule or return a 404 error if not found
    schedule = get_object_or_404(Schedule, pk=id)

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = ScheduleForm(instance=schedule)
    major_form = MajorForm()
    subject_form = SubjectForm()
    teacher_form = TeacherForm()
    return render(
        request=request,
        template_name='update-schedule.html',
        context={
            'schedule': schedule,
            'form': form,
            'major_form': major_form,
            'subject_form': subject_form,
            'teacher_form': teacher_form,
        }
    )

# for testing when fetch data
def get_schedules(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    schedules = Schedule.objects.all()

    major_dict = {}
    for major in majors:
        major_dict[major.id] = major.name
    
    subject_dict = {}
    for subject in subjects:
        subject_dict[subject.id] = subject.name
    
    schedule_list = []
    for schedule in schedules:
        schedule_list.append(
            {
                'id': schedule.id,
                'major': major_dict[schedule.major_id],
                'subject': subject_dict[schedule.subject_id],
                'teacher_name': schedule.teacher_name,
                'time_begins': schedule.time_begins,
                'time_ends': schedule.time_ends,
                'room': schedule.room,
                'day': schedule.day
            }
        )
    return JsonResponse(
        {
            'schedules': schedule_list
        }
    )

# for get majors
def get_majors(request):
    majors = Major.objects.all().values()
    return JsonResponse(
        {
            'majors': list(majors)
        }
    )

# for get subjects based on major id
def get_subjects(request):
    major_id = request.GET.get('major_id')
    subjects = list(Subject.objects.filter(major_id=major_id).values('id', 'name'))
    return JsonResponse({
        'subjects': subjects
    })

# for get subjects based on major id
def get_teachers(request):
    major_id = request.GET.get('major_id')
    teachers = list(Teacher.objects.filter(major_id=major_id).values('id', 'name'))
    return JsonResponse({
        'teachers': teachers
    })


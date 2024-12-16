from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from schedule.forms import MajorForm, ScheduleForm, SubjectForm
from schedule.models import Schedule, Subject, Major

# Create your views here.
def dashboard(request):
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
 
    context = {
        'schedules': schedule_list
    }
    return render(
        request=request, 
        template_name='dashboard.html',
        context=context
    )

def create_schedule(request):
    majors = Major.objects.all().values()
    subjects = Subject.objects.all().values()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ScheduleForm()
        major_form = MajorForm()
        subject_form = SubjectForm()
    
    return render(
        request=request,
        template_name='add-schedule.html',
        context={
            'form': form,
            'major_form': major_form,
            'subject_form': subject_form,
            'majors': majors,
            'subjects': subjects
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
    else:
        form = ScheduleForm(instance=schedule)
    return render(
        request=request,
        template_name='update-schedule.html',
        context={
            'form': form,
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

def get_majors(request):
    majors = Major.objects.all().values()
    return JsonResponse(
        {
            'majors': list(majors)
        }
    )

def get_subjects(request):
    subjects = Subject.objects.all().values()
    return JsonResponse(
        {
            'subjects': list(subjects)
        }
    )


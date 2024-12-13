from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
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

def create(request):
    template_name = 'add-schedule.html'
    return render(
        request=request,
        template_name=template_name
    )


def update(request, id):
    # Retrieve the specific schedule or return a 404 error if not found
    schedule = get_object_or_404(Schedule, pk=id)
    context = {
        'schedule': schedule
    }
    return render(
        request=request,
        template_name='update-schedule.html',
        context=context
    )


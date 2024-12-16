from django import forms
from schedule.models import Major, Schedule, Subject


class ScheduleForm(forms.ModelForm):
    major = forms.ModelChoiceField(queryset=Major.objects.all(), required=True, empty_label="Select Major")
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), required=True, empty_label="Select Subject")
    class Meta:
        model = Schedule
        fields = ['major', 'subject', 'teacher_name', 'time_begins', 'time_ends', 'room', 'day']

class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ['name']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

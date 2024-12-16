from django import forms
from schedule.models import Major, Schedule, Subject

class ScheduleForm(forms.ModelForm):
    major = forms.ModelChoiceField(
        queryset=Major.objects.all(),
        required=True,
        empty_label="Select Major",
        widget=forms.Select(attrs={'class': 'dropdown'})
    )
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        required=True,
        empty_label="Select Subject",
        widget=forms.Select(attrs={'class': 'dropdown'})
    )
    teacher_name = forms.CharField(
        required=True,
    )
    time_begins = forms.TimeField(
        required=True,
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'time-input'})
    )
    time_ends = forms.TimeField(
        required=True,
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'time-input'})
    )

    room = forms.ChoiceField(
        choices=[('', 'Select Room')] + Schedule.ROOM_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'dropdown'})
    )

    day = forms.ChoiceField(
        choices=[('', 'Select Day')] + Schedule.DAY_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'dropdown'})
    )

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

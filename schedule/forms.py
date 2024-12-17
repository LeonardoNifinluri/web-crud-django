from django import forms
from schedule.models import Major, Schedule, Subject, Teacher

class ScheduleForm(forms.ModelForm):
    major = forms.ModelChoiceField(
        queryset=Major.objects.all(),
        required=True,
        empty_label="Select Major",
        widget=forms.Select(attrs={'class': 'dropdown'})
    )
    # subject needs to be filtered
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        required=True,
        empty_label="Select Subject",
        widget=forms.Select(attrs={'class': 'dropdown'})
    )
    # teacher needs to be filtered
    teacher = forms.ModelChoiceField(
        queryset=Teacher.objects.all(),
        required=True,
        empty_label='Select Teacher',
        widget=forms.Select(attrs={'class': 'dropdown'})
    )
    time_begins = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter time begins'})
    )
    time_ends = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter time ends'})
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
        fields = ['major', 'subject', 'teacher', 'time_begins', 'time_ends', 'room', 'day']

class MajorForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter major name'})
    )
    class Meta:
        model = Major
        fields = ['name']

class SubjectForm(forms.ModelForm):
    major = forms.ModelChoiceField(
        queryset=Major.objects.all(),
        required=True,
        empty_label="Select Major",
        widget=forms.Select(attrs={'class': 'dropdown'})
    )
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter subject name'})
    )
    class Meta:
        model = Subject
        fields = ['major', 'name']

class TeacherForm(forms.ModelForm):
    major = forms.ModelChoiceField(
        queryset=Major.objects.all(),
        required=True,
        empty_label="Select Major",
        widget=forms.Select(attrs={'class': 'dropdown'})
    )
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter teacher name'})
    )
    class Meta:
        model = Teacher
        fields = ['major', 'name']

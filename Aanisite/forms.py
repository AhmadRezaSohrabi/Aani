from django import forms
from .models import TheraputicCategory, Form
LEVEL_CHOICES = [('TRAINEE', 'Trainee'), ('NOVICE', 'Novice'), ('PROFICIENT', 'Proficient'), ('EXPERT', 'Expert')]
class EducationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    from_date = forms.DateField(label='from')
    to_date = forms.DateField(label='to')
    educational_institution = forms.CharField(max_length=20)
    degree = forms.CharField(max_length=10)
    subject = forms.CharField(max_length=10)
    final_grade = forms.IntegerField()

class ForeignLanguageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    name = forms.CharField(max_length=10)
    listening = forms.ChoiceField(choices=LEVEL_CHOICES)
    reading = forms.ChoiceField(choices=LEVEL_CHOICES)
    writing = forms.ChoiceField(choices=LEVEL_CHOICES)
    speaking = forms.ChoiceField(choices=LEVEL_CHOICES)
    
class EmploymentHistoryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    from_date = forms.DateField(label='from')
    to_date = forms.DateField(label='to')
    company_name = forms.CharField(max_length=10)
    position = forms.CharField(max_length=20)

class EmploymentForm(forms.Form):
    surname = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    identification_number = forms.IntegerField()
    telephone = forms.IntegerField()
    home_address = forms.CharField(max_length=100,)
    post_code = forms.IntegerField()
    email = forms.EmailField(max_length=254,widget=forms.EmailInput(attrs={'style': 'border-color: green;'}))
    future_positions = forms.CharField(label='Please mention one or more positions that would interest you for future openings:', max_length=200, required=False, widget=forms.Textarea(attrs={"rows":4, "cols":60}))
    resume = forms.FileField(help_text="Upload your cv here if you have one!", required=False)
    condition = forms.BooleanField(label='I hereby confirm, that my answers to the foregoing questions are true and correct. Any misleading information will be considered as a reason of declining my application from Aani Darman Pharmaceutical Co.')


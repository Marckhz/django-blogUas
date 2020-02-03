from django import forms

from django.forms import ModelForm

from  blog.models import Organigrama,Calendars,CurricularPlan,Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['tag']
        widgets = {
            'body': forms.Textarea(attrs={'class':'materialize-textarea', 'id':'textarea1'})
        }

class PersonalForm(forms.Form):

    department = forms.CharField(label="Deparamento", max_length=100)
    name = forms.CharField(label ="Nombre",max_length=100)
    last_name = forms.CharField(label ="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Telefono", max_length=12)

class LoginForm(forms.Form):

    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="password", widget=forms.PasswordInput )

class ProgramsForm(forms.Form):

    SEMESTERS = (
            ('I','Semestre I '),
            ('II', 'Semestre II'),
            ('III', 'Semestre III'),
            ('IV', 'Semestre IV'),
            ('V', 'Semestre V'),
            ('VI', 'Semestre VI'),
        )

    semester = forms.ChoiceField(label="Semestre", widget= forms.Select(attrs={'class':'select'}), choices=SEMESTERS )
    subject = forms.CharField(label="Materia", max_length=50)
    link = forms.URLField(label="Url")


class OrganigramaForm(forms.ModelForm):
    class Meta:
        model = Organigrama
        fields = "__all__"


class CalendarioForm(forms.ModelForm):
    class Meta:
        model = Calendars
        fields = "__all__"


class CurricularPlanForm(forms.ModelForm):
    class Meta:
        model = CurricularPlan
        fields = "__all__"

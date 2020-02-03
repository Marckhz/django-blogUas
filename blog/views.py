from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from blog.forms import PersonalForm, LoginForm, ProgramsForm,OrganigramaForm,CalendarioForm, CurricularPlanForm,PostForm

from blog.models import PersonalDetails, Programs,Organigrama, Calendars,CurricularPlan, Post
# Create your views here.



class Index(View):
    template_name = 'website/index.html'

    def get(self, request):

        return render(request, self.template_name )

class LoginView(View):


    template_name = 'backoffice/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):

        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_view')
            else:
                messages.warning(request, "Error  de usuario/password")

                return render(request, self.template_name, {'form':form})


class PersonalView(LoginRequiredMixin, View):

    template_name = "backoffice/personal.html"
    form_class = PersonalForm

    def get(self, request):

        form = self.form_class

        return render(request, self.template_name, {'form':form } )

    def post(self, request):

        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            department = form.cleaned_data['department']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            personal = PersonalDetails(first_name = name, last_name=last_name, department=department, phone=phone, email=email)
            personal.save()
            messages.success(request, 'Usuario Agregado Exitosamente')
            form = self.form_class

        return render(request, self.template_name, {'form':form})


class ProgramsView(LoginRequiredMixin, View):

    template_name = "backoffice/programas.html"
    form_class = ProgramsForm
    title ='Agregar Programas'
    update_url = 'update_program_view'

    def get(self, request):

        form = self.form_class

        return render(request, self.template_name, {'form':form, 'title':self.title, 'url_link':self.update_url })

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            semester = form.cleaned_data['semester']
            subject = form.cleaned_data['subject']
            link = form.cleaned_data['link']
            new_program = Programs(semester = semester, link = link, name = subject)
            new_program.save()
            messages.success(request, 'Materia Agregada Exitosamente')
            form = self.form_class

        return render(request, self.template_name, {'form':form, 'title':self.title})

class ProgramsUpdateView(LoginRequiredMixin, View):

    template_name = 'backoffice/programs_update.html'
    form_class = ProgramsForm
    title ='Actualizar Programas'

    query = None

    def get(self, request):

        return render(request, self.template_name, {'title':self.title})
    """
    def post(self, request):
        semester = None
        form = self.form_class(request.POST)

        if form.is_valid():
            semester = cleaned_data['semester']


        return render(request, self.template_name, {'form':form, 'title':self.title})
    """

class ListSubjects(LoginRequiredMixin, View):

    template_name = 'backoffice/programs_list.html'
    title = 'Lista de Materias'
    #query  = None

    def get(self, request, semester):

        tmp_query =  Programs.objects.filter(semester=semester)

        return render(request, self.template_name, {'query':tmp_query} )

class SingleSubjectEdit(LoginRequiredMixin, View):

    template_name ='backoffice/single_subject.html'

    form = ProgramsForm

    main_query = None
    def get(self, request, pk):

        tmp_query = Programs.objects.filter(id=pk)
        self.main_query = tmp_query

        return render(request, self.template_name, {'query':self.main_query, 'form':self.form} )

    def post(self, request, pk):

        form = self.form(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            semester  = form.cleaned_data['semester']
            url = form.cleaned_data['link']

            tmp_query = Programs.objects.get(id=pk)

            if tmp_query is not None:
                tmp_query.name = subject
                tmp_query.semester = semester
                tmp_query.url = urlCalendarioForm
                tmp_query.save()
                self.get(request, pk)

        return render(request, self.template_name, {'query':self.main_query, 'form':form})

    """
    def delete(self, request, pk):
        tmp_query = Programs.objects.get(id=pk)

        if request.method =='POST':
            if tmp_query is not None:
                tmp_query.delete()
        print(tmp_query)

        return render(request, 'backoffice/single_subject.html', {'query':self.main_query, 'form':self.form})
"""
class SingleSubjectDelete(LoginRequiredMixin, View):

    def post(self, request, pk):

        tmp_query = get_object_or_404(Programs, id=pk)

        if tmp_query is not None:
            tmp_query.delete()
            return redirect('programs_view')

        print(tmp_query)

        return render(request, 'backoffice/single_subject.html', {'delete_query':tmp_query})
        #return render(requet, self.template_name)
class ProgramasWeb(View):

    template_name = 'website/programas.html'

    def get(self, request):
        query = Programs.objects.all()

        return render(request, self.template_name, {'query':query})

class MisionView(View):
    template_name ='website/mision.html'
    def get(self, request):
        return render(request, self.template_name)

class OrganigramaView(View):
    template_name ='website/organigrama.html'
    def get(self, request):
        return render(request, self.template_name)


class OrganigramaViewUpload(LoginRequiredMixin, View):

    template_name ='backoffice/upload_organigrama.html'
    form = OrganigramaForm

    def get(self, request):

        return render(request, self.template_name, {'form':self.form} )

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            self.form()

        return render(request, self.template_name, {'form':form})

class OrganigramaView(View):
    template_name = 'website/organigrama.html'
    def get(self, request):
        tmp_query = Organigrama.objects.all()
        return render(request, self.template_name, {'query':tmp_query})

class CalendarUploadView(LoginRequiredMixin, View):

    template_name = 'backoffice/upload_calendar.html'
    form = CalendarioForm

    def get(self, request):

        return render(request, self.template_name, {'form':self.form})

    def post(self, request):

        form  = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            self.form()

        return render(request, self.template_name, {'form':self.form})

class CalendarioView(View):

    template_name = 'website/calendario.html'
    def get(self, request):
        query = Calendars.objects.all().order_by('-id')
        this_calendar = query[0]

        return render(request, self.template_name, {'query':this_calendar})

class PlanCurricularView(LoginRequiredMixin, View):
    template_name ='backoffice/upload_curriculum.html'
    form = CurricularPlanForm
    def get(self, request):

        return render(request, self.template_name, {'form':self.form})

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            self.form()
        return render(request, self.template_name, {'form':self.form})


class CreatePostView(LoginRequiredMixin, View):

    template_name ='backoffice/upload_post.html'
    form = PostForm

    def get(self, request):

        return render(request, self.template_name, {'form':self.form})

    def post(self, request):

        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            self.form()

        return render(request, self.template_name, {'form':self.form})

class MainFeed(ListView):

    model = Post
    paginate_by = 6
    template_name = 'website/main_feed.html'

class SingleObjectView(DetailView):
    model = Post
    template_name = 'website/post_detail.html'

def logout_view(request):
    logout(request)
    return redirect('login_view')

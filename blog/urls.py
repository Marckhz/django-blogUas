from django.urls import path


from blog.views import Index,PersonalView,LoginView, logout_view,ProgramsView,ProgramsUpdateView,ListSubjects,SingleSubjectEdit,SingleSubjectDelete
from blog.views import ProgramasWeb
from blog.views import MisionView
from blog.views import OrganigramaView
from blog.views import OrganigramaViewUpload
from blog.views import CalendarUploadView
from blog.views import CalendarioView
from blog.views import PlanCurricularView
from blog.views import CreatePostView
from blog.views import MainFeed
from blog.views import SingleObjectView

urlpatterns = [
        #        path('', views.index, name= 'index'),
        path('home/', Index.as_view(), name="home_view" ),
        path('backoffice/personal/', PersonalView.as_view()  ),
        path('backoffice/login/', LoginView.as_view(), name="login_view" ),
        path('backoffice/logout/', logout_view, name="logout"),
        path('backoffice/programs/', ProgramsView.as_view(), name="programs_view"),
        path('backfoffice/programs/semestres/', ProgramsUpdateView.as_view(), name='semestres_view'),
        path('backoffice/programs/semestres/<str:semester>/', ListSubjects.as_view(), name='single_semester'),
        path('backoffice/programs/semestres/materia/<int:pk>/', SingleSubjectEdit.as_view(), name='single_subject'),
        path('backoffice/programs/semestres/materia/delete/<int:pk>/', SingleSubjectDelete.as_view(), name='delete_subject'),
        path('website/programas/', ProgramasWeb.as_view(), name='programas_web'),
        path('website/mision/', MisionView.as_view(), name='mision_vision'),
        path('backoffice/upload_organigrama/', OrganigramaViewUpload.as_view(), name='upload_organigrama'),
        path('home/organigrama/', OrganigramaView.as_view(), name='organigrama'),
        path('backoffice/upload_calendar/', CalendarUploadView.as_view(), name='upload_calendar'),
        path('website/calendario/', CalendarioView.as_view(), name='calendar'),
        path('backoffice/upload_curriculum/', PlanCurricularView.as_view(), name='upload_curriculum'),
        path('backoffice/new_post/', CreatePostView.as_view(), name='add_post'),
        path('', MainFeed.as_view(), name='main_feed'),
        path('website/post/<int:pk>/', SingleObjectView.as_view(), name='single_post' )

        ]

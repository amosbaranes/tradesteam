from django.urls import path
from .views import (home, fsa, fsaba, framework, fw_installation,
                    fw_django_allauth, fw_python_django,fw_database,fw_django_detail,
                    fw_apps, fw_team_work, fw_django_cms, fw_asynchronous, fw_internationalization,
                    fw_business_intelligence, fw_machine_learning,
                    business_intelligence, machine_learning, business_simulation, bs_overview, bs_registration)

app_name = "course"

urlpatterns = [
    path('', home, name='home'),

    path('fsa', fsa, name='fsa'),
    path('fsaba', fsaba, name='fsaba'),
    #
    path('framework', framework, name='framework'),
    path('fw_installation', fw_installation, name='fw_installation'),
    path('fw_django_allauth', fw_django_allauth, name='fw_django_allauth'),
    path('fw_python_django', fw_python_django, name='fw_python_django'),
    path('fw_database', fw_database, name='fw_database'),
    path('fw_django_detail', fw_django_detail, name='fw_django_detail'),
    path('fw_apps', fw_apps, name='fw_apps'),
    path('fw_team_work', fw_team_work, name='fw_team_work'),
    path('fw_django_cms', fw_django_cms, name='fw_django_cms'),
    path('fw_asynchronous', fw_asynchronous, name='fw_asynchronous'),
    path('fw_internationalization', fw_internationalization, name='fw_internationalization'),
    path('fw_business_intelligence', fw_business_intelligence, name='fw_business_intelligence'),
    path('fw_machine_learning', fw_machine_learning, name='fw_machine_learning'),
    #
    path('business_intelligence', business_intelligence, name='business_intelligence'),
    path('machine_learning', machine_learning, name='machine_learning'),
    path('business_simulation', business_simulation, name='business_simulation'),
    path('bs_overview', bs_overview, name='bs_overview'),
    path('bs_registration', bs_registration, name='bs_registration'),
]

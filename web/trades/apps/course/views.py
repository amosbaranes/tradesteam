from django.shortcuts import render


def home(request):
    title = 'Course'
    return render(request, 'course/home.html', {'title': title})


def fsa(request):
    args = {'title': 'Financial Statement Analysis (MBA)'}
    return render(request, 'course/classes/fsa.html', args)


def fsaba(request):
    args = {'title': 'Financial Statement Analysis (BA)'}
    return render(request, 'course/classes/fsaba.html', args)


# framework
# ---------
def framework(request):
    args = {'title': 'Framework for software Engineering'}
    return render(request, 'course/classes/framework.html', args)


def fw_installation(request):
    args = {'title': 'Installation for Framework'}
    return render(request, 'course/classes/framework/fw_installation.html', args)


def fw_django_allauth(request):
    args = {'title': 'Django AllAuth: for authentication'}
    return render(request, 'course/classes/framework/fw_django_allauth.html', args)


def fw_python_django(request):
    args = {'title': 'Introduction to Python / Django framework'}
    return render(request, 'course/classes/framework/fw_python_django.html', args)


def fw_database(request):
    args = {'title': 'Introduction to Databases'}
    return render(request, 'course/classes/framework/fw_database.html', args)


def fw_django_detail(request):
    args = {'title': 'Django Detail'}
    return render(request, 'course/classes/framework/fw_django_detail.html', args)


def fw_apps(request):
    args = {'title': 'Design applications with Django'}
    return render(request, 'course/classes/framework/fw_apps.html', args)


def fw_team_work(request):
    args = {'title': 'implement the application with your team'}
    return render(request, 'course/classes/framework/fw_team_work.html', args)


def fw_django_cms(request):
    args = {'title': 'Django CMS'}
    return render(request, 'course/classes/framework/fw_django_cms.html', args)


def fw_asynchronous(request):
    args = {'title': 'Asynchronous for Django'}
    return render(request, 'course/classes/framework/fw_asynchronous.html', args)


def fw_internationalization(request):
    args = {'title': 'Internationalization for Django'}
    return render(request, 'course/classes/framework/fw_internationalization.html', args)


def fw_machine_learning(request):
    args = {'title': 'Machine Learning with Django'}
    return render(request, 'course/classes/framework/fw_machine_learning.html', args)


def fw_business_intelligence(request):
    args = {'title': 'Business Intelligence with Django'}
    return render(request, 'course/classes/framework/fw_business_intelligence.html', args)


# Business Simulation
# -------------------
def business_intelligence(request):
    args = {'title': 'Business Intelligence'}
    return render(request, 'course/classes/business_intelligence/business_intelligence.html', args)


def machine_learning(request):
    args = {'title': 'Machine Learning'}
    return render(request, 'course/classes/machine_learning/machine_learning.html', args)


def business_simulation(request):
    args = {'title': 'Business Simulation'}
    return render(request, 'course/classes/business_simulation/business_simulation.html', args)


def bs_overview(request):
    args = {'title': 'Business Simulation - Overview'}
    return render(request, 'course/classes/business_simulation/bs_overview.html', args)


def bs_registration(request):
    args = {'title': 'Business Simulation - Registration'}
    return render(request, 'course/classes/business_simulation/bs_registration.html', args)



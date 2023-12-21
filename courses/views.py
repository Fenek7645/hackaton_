from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Главная
@login_required(login_url='')
def courses(requset):
    return render(requset, 'courses/courses.html')


# Курс про пароль
@login_required(login_url='')
def personal_data(requset):
    return render(requset, 'courses/personal_data.html')


# О том что делать если поался на удочку мошенников 
@login_required(login_url='')
def helpa(requset):
    return render(requset, 'courses/helpa.html')


#-----------------МОШЕННИКИ--------------------#

# Главная курсов про мошеннечество
@login_required(login_url='')
def mosheniki(requset):
    return render(requset, 'courses/mosheniki/main.html')


# Мошенники > вирусы
@login_required(login_url='')
def mosheniki_viruses(requset):
    return render(requset, 'courses/mosheniki/viruses.html')


# Мошенники > фишинг
@login_required(login_url='')
def mosheniki_fishing(requset):
    return render(requset, 'courses/mosheniki/phishing.html')


# Мошенники > финансовая пирамида
@login_required(login_url='')
def mosheniki_fin_piromida(requset):
    return render(requset, 'courses/mosheniki/fin_piromida.html')


# Мошенники > социальная инжинерия 
@login_required(login_url='')
def mosheniki_coshial_ingeering(requset):
    return render(requset, 'courses/mosheniki/coshial_ingeering.html')

#-----------------МОШЕННИКИ-КОНЕЦ--------------------#



#---------------Защита-личных-данных-----------------#
# Теория переходы
@login_required(login_url='')
def theory(requset):
    return render(requset, 'courses/theory.html')

# Правила хранения личных данных
@login_required(login_url='')
def rule_data(requset):
    return render(requset, 'courses/defe_data/rule_data.html')


# Правила поведения в веб приложениях, сервисах
@login_required(login_url='')
def rule_web(requset):
    return render(requset, 'courses/defe_data/rule_web.html')


@login_required(login_url='')
def rule_social_network(requset):
    return render(requset, 'courses/defe_data/rule_social_network.html')

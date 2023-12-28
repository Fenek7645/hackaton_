from django.shortcuts import render
from .models import UserPageVisit

# Создаём функции для вывода html страницы

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html') 


def check_visited_pages(request):
    user = request.user
    
    page1_visited = UserPageVisit.objects.filter(user=user, page_visited='/courses/personal_data/social_network').exists()
    page2_visited = UserPageVisit.objects.filter(user=user, page_visited='/courses/personal_data/web_rules').exists()
    page3_visited = UserPageVisit.objects.filter(user=user, page_visited='/courses/personal_data/data_rules').exists()
    page4_visited = UserPageVisit.objects.filter(user=user, page_visited='/courses/scammers/phishing').exists()
    page5_visited = UserPageVisit.objects.filter(user=user, page_visited='/courses/scammers/financial_pyramid').exists()
    page6_visited = UserPageVisit.objects.filter(user=user, page_visited='courses/scammers/viruses').exists()
    page7_visited = UserPageVisit.objects.filter(user=user, page_visited='/courses/scammers/coshial_ingeering').exists()
    
    if page1_visited and page2_visited and page3_visited and page4_visited and page5_visited and page6_visited and page7_visited == True:
        context = True
    
    
    return render(request, 'check_visited_pages.html', context)
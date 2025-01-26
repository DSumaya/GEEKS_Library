from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class ExperienceClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = int(request.POST.get('experience'))
            if experience < 1:
                return  HttpResponseBadRequest("Вы нам не подходите")
            elif experience >= 1 and experience < 3:
                request.club= 'Junior club 1000$ '
            elif experience >= 3 and experience < 7:
                request.club = 'Middle club 2000$'
            elif experience >= 5 and experience <= 10:
                request.club= 'Senior club 5000$'
            else:
                return HttpResponseBadRequest("Ваш опыт больше 10 лет")
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'Не удалось определить клуб ')
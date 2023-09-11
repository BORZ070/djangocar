from django.shortcuts import render
from mainpage_car.models import Car
from about.models import Bill
from django.core.mail import send_mail


def main_views(request):
    cars = Car.objects.order_by('?')[:6]
    return render(request, 'index_new.html', {'cars': cars})


def detail_views(request, pk):
    car = Car.objects.get(id=pk)
    success_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        bill = Bill(email=email, name=name, comment=comment)
        bill.save()

        email_subject = 'заявка'
        message = f'новая заявка от {name}, {email}' \
                  f'{comment}'

        from_email = 'xbox070@yandex.ru'
        email_manager = ['shdgit07@gmail.com']
        send_mail(email_subject, message, from_email, email_manager)
        success_message = 'Заявка отправлена!'

    return render(request, 'detail_new.html', {'car': car, 'success_message':success_message})


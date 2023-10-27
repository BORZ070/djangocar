import requests

from mainpage_car.models import RateUSD


def usd_rate():
    data = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()
    usd_rate = data['rates']['USD']
    rate = round(1 / usd_rate, 2)
    # save_rate_database
    kurs = RateUSD.objects.last()
    kurs.rate = rate
    kurs.save()

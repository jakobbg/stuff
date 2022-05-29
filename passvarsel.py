import requests
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

offices = {
 'Bergen Vest': 'd7b7dfe29e507f78dff90f35d540095f4d4eea1a78be9b1299b375e7ca30f227',
 'Bjørnafjorden': '7739c0f2a5d78841ea0c6e94053d75d64efbeb2a4a0ec0ba281fb33c851d5761',
 'Hardanger': '44bfcd71ead8cedb06cfac8966d899d89b1f13d6ed98cfc62e0b682dab870981',
 'Nordhordland': '407d47f595a2e79871a88e57359f789cd7b9bdc2dd8f747136d51c6e0ee2aa30',
 'Voss': '9d9f6c7a34c8fe900c987ffa4caf1b7302b4e86561373878c7e782c53f4dd60f',
 'Øygarden': '7e2786ecaf5ddd38194319b37b9c61528c7c8245c3ecba4c62828f14eff94e17'
}

for office, locationKey in offices.items():
    response = requests.get('https://pass-og-id.politiet.no/qmaticwebbooking/rest/schedule/branches/{locationKey}/dates;servicePublicId=8e859bd4c1752249665bf2363ea231e1678dbb7fc4decff862d9d41975a9a95a;customSlotLength=10'.format(locationKey=locationKey))
    if len(response.json()) > 0:
        firstAvailableDate = datetime.datetime.strptime(response.json()[0]['date'], '%Y-%m-%d').date()
        timeAheadToSearch = date.today() + relativedelta(months=2)
        if firstAvailableDate < timeAheadToSearch:
            print('%s har første ledige time %s'%(office, firstAvailableDate))

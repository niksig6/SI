from django.shortcuts import render
import requests

def page(request):
    data = requests.get('https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=schedule%2Cvehicle%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north').json()
    sortedData = []
    for i in data['data']:
        train = {}
        train['time'] = i['attributes']['departure_time']

        id = i['relationships']['trip']['data']['id']
        for y in data['included']:
            if y['id'] == id:
                train['destination'] = y['attributes']['headsign']

        if i['relationships']['vehicle']['data'] is None:
            train['train'] = 'None'
        else:
            for y in data['included']:
                if y['id'] == i['relationships']['vehicle']['data']['id']:
                    train['train'] = y['attributes']['label']

        train['track'] = 'TDB'

        train['status'] = i['attributes']['status']
        sortedData.append(train)


    return render(request, 'page.html',{'data': sortedData})
import requests
from datetime import datetime

from apps.models import FreeSpaces, Parking

BASE_URI: str = "https://openapi.emtmadrid.es/v1"


# def get_free_spaces_from():


def get_free_spaces():
    try:
        access_token = get_the_token()
        return get_the_availability(access_token)
    except requests.exceptions.ConnectionError as ce:
        raise ce


def get_the_token():
    url = BASE_URI + '/mobilitylabs/user/login'
    headers = {
        'email': '100465076@alumnos.uc3m.es',
        'password': 'baby9ROCK',
    }

    r = requests.get(url, headers=headers)
    access_token = r.json()['data'][0]['accessToken']

    print("access_token: " + access_token)
    return access_token


def get_the_availability(access_token):
    counter = 0
    free_spaces = []

    url = BASE_URI + '/citymad/places/parkings/availability/'
    headers = {
        'accessToken': access_token,
    }

    r = requests.get(url, headers=headers)
    data_body = r.json()['data']

    for parking in data_body:
        if parking['freeParking'] is not None:
            counter += 1
            free_spaces_unit = FreeSpaces()
            parking_object = Parking()
            print(str(counter) + ' parking_name: ' + parking['name'])
            print('free spaces: ' + str(parking['freeParking']))
            parking_object.parking_name = parking['name']
            free_spaces_unit.free_spaces_number = parking['freeParking']
            free_spaces_unit.parking = parking_object
            try:
                free_spaces_unit.updated_at = datetime.strptime(parking['lastUpd'], '%Y-%m-%dT%H:%M:%S.%f')
            except ValueError:
                free_spaces_unit.updated_at = datetime.strptime(parking['lastUpd'], '%Y-%m-%dT%H:%M:%S')
            # YYYY-MM-DD HH:MM

            # todo parse updated at
            free_spaces.append(free_spaces_unit)
    return free_spaces

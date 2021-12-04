import time

import requests
from django.http import HttpResponse

from apps.src import config
from apps.src.controllers import mad_free_spaces_controller, db_free_spaces_controller
from apps.src.utils.request_wrapper import check_body


def export_db(request):
    if request.method == 'GET':
        body = check_body(request.body, "export_db")
        db_free_spaces_controller.export()


def get_free_spaces(request):
    if request.method == 'GET':
        body = check_body(request.body, "free_spaces")
        time_lapsed = 0
        while time_lapsed < body["time"]:
            try:
                free_spaces = mad_free_spaces_controller.get_free_spaces()
            except requests.exceptions.ConnectionError:
                print("reintentar en " + str(config.ERROR_SLEEP_TIME) + " segundos")
                time.sleep(config.ERROR_SLEEP_TIME)
                time_lapsed += body["period"]
                continue
            db_free_spaces_controller.create_free_spaces(free_spaces)
            time.sleep(body["period"])
            time_lapsed += body["period"]
        return HttpResponse("{status: 200}", status=201, content_type="application/json")

# def get_free_spaces_from_parking(request, parking_name):

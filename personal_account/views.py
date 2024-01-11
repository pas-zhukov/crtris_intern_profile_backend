from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

from datetime import datetime


def current_user(request):
    temp_data = {
        "name": "Ким Юрий Михайлович",
        "is_curator": True,
        "group": 0,
        "avatar_url": "https://arsenalnn.com/wp-content/uploads/diler2-1.png"
    }
    return JsonResponse(temp_data)


def interns_list(request):
    temporary_response_data = {
        "all_interns": [
            {
                "id": 1,
                "name": "Ким Юрий Михайлович",
                "group": 112,
                "department": "ОВП",
                "medical": False,
                "vacation": True
            },
            {
                "id": 2,
                "name": "Жуков Павел Юрьевич",
                "group": 105,
                "department": "ДуТиБА",
                "medical": True,
                "vacation": False
            },
        ]}
    return JsonResponse(temporary_response_data)


def intern(request):
    temporary_response_data = {
        "isFiltered": False,
        "firstName": "Ким",
        "secondName": "Юрий",
        "group": 112,
        "rating": 8,
        "avatar_url": "https://arsenalnn.com/wp-content/uploads/diler2-1.png",

        "tasks": [
            {
              "id": 1,
              "name": "HEX-редактор",
              "type": "PRACTICAL_TASK",
              "status": "WIP",
              "beginDate": datetime.strptime("28.12.2023", "%d.%m.%Y").date(),
              "endDate": "",
              "expired": False
            },
            {
              "id": 2,
              "name": "Java - базовый курс",
              "type": "COURSE",
              "status": "DONE",
              "beginDate": datetime.strptime("25.12.2023", "%d.%m.%Y").date(),
              "endDate": datetime.strptime("27.12.2023", "%d.%m.%Y").date(),
              "expired": True
            },
        ],
    }
    return JsonResponse(temporary_response_data)

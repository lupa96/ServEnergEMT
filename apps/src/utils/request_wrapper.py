import json


def check_attribute(body, attribute):
    try:
        body[attribute]
    except (BaseException,):
        raise Exception(attribute + " attribute not set")


def check_body(body, type: str):
    if type == "free_spaces":
        print("body: " + body)
        body = json.loads(body)
        check_attribute(body, "time")
        check_attribute(body, "period")

    if type == "export_db":
        body = json.loads(body)
        check_attribute(body, "format")

    return body

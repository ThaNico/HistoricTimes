import json


def addMessageSuccess(array, message):
    array["message_success"] = message


def addMessageError(array, message):
    array["message_error"] = message


def moveSessionMessageToContext(key, request, array):
    if request.session.get(key):
        if key == "message_success":
            addMessageSuccess(array, request.session[key])
        else:
            addMessageError(array, request.session[key])
        del request.session[key]
        request.session.modified = True


def getRequestJsonData(request):
    return json.loads(request.body.decode("utf-8"))

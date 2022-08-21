KEY_REQUEST_MSG_SUCCESS = "message_success"
KEY_REQUEST_MSG_ERROR = "message_error"


def addMessageSuccess(array, message):
    array[KEY_REQUEST_MSG_SUCCESS] = message


def addMessageError(array, message):
    array[KEY_REQUEST_MSG_ERROR] = message


def moveSessionMessageToContext(key, request, array):
    if request.session.get(key):
        if key == KEY_REQUEST_MSG_SUCCESS:
            addMessageSuccess(array, request.session[key])
        else:
            addMessageError(array, request.session[key])
        del request.session[key]
        request.session.modified = True

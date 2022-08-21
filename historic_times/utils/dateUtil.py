from datetime import datetime


def timeStringToTime(hours, minutes):
    return datetime.strptime(str(hours) + ':' + str(minutes), '%H:%M').time()

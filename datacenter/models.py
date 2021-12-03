from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )


def get_duration(visit):
    """
    returns duarition of visit

    :param visit: queryset element
    return: duration of visit in seconds

    :example
    visit.entered_at = 10 июля 2020 г. 8:19
    visit.leaved_at = 10 июля 2020 г. 8:29

    returns: 600

    """

    duration = visit.leaved_at - visit.entered_at if visit.leaved_at\
        else localtime()-visit.entered_at
    return duration


def format_duration(duration):
    """
    :param duration: duration of visit in seconds
    return: formated duarition of visit
    
    :example: 

    duration = 120
    returns: 00:01:00
    """
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    formatted_duration = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
    return formatted_duration
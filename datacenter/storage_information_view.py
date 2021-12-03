from datacenter.models import Visit
from datacenter.models import get_duration, format_duration
from django.shortcuts import render

    
def storage_information_view(request):
    """
    Displays information on people currently in storage


    makes list with dicts
    [{
      'who_entered': person's name,
      'entered_at': date and time of entering,
      'duration': duration in hh:mm:ss
    }]
    """  

    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
      

    for visit in visits:
        who_entered = visit.passcard
        entered_at = visit.entered_at
        duration = get_duration(visit)

        non_closed_visits.append({
            'who_entered': who_entered,
            'entered_at': entered_at,
            'duration': format_duration(duration)
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

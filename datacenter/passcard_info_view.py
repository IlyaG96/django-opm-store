from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration




def passcard_info_view(request, passcode):
    """
    displays information about visits for a specific pass

    makes list with dicts
    [{
      'entered_at': visit date,
      'duration': time of visit,
      'is_strange': True if the visit is longer than 1 hour
    }]
    """

    passcard = Passcard.objects.all().get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []



    for visit in visits:
        entered_at = visit.entered_at
        duration = get_duration(visit)
        is_strange = int(duration.total_seconds()) > 3600

        this_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': format_duration(duration),
                'is_strange': is_strange
            })
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

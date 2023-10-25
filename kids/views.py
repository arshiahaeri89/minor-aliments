from django.contrib import messages
from django.shortcuts import render

from kids.forms import ColdForm


def cold(request):
    if request.method == 'POST':
        form = ColdForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['until_3_month'] or data['fever'] or data['ailment'] \
                    or data['breath'] or data['swallow']:
                messages.info(request,
                              'در صورت لزوم از داروی ضد تب استفاده کنید و هم اکنون به مرکز بهداشتی درمانی مراجعه کنید',
                              'info')
            elif data['fever_3_days'] or data['liquids'] or data['discharge'] or data['sputum']:
                messages.info(request, 'به مرکز بهداشتی درمانی مراجعه کنید', 'info')
            else:
                messages.info(request, '<a href="/kids/cold/advices">توصیه های خانگی</a> را مطالعه کنید.', 'info')
    else:
        form = ColdForm()
    return render(request, 'kids/cold.html', {'form': form})


def cold_advices(request):
    return render(request, 'kids/cold_advices.html')

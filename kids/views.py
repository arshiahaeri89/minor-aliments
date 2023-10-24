from django.shortcuts import render

from kids.forms import ColdForm


def cold(request):
    if request.method == 'POST':
        form = ColdForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
    else:
        form = ColdForm()
    return render(request, 'kids/cold.html', {'form': form})

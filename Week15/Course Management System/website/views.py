from django.shortcuts import render


def my_404_view(request):
    return render(request, 'website/404.html')

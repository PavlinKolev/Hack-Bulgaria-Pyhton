from django.shortcuts import render
from MyFirstSite.helpers import (factorial, fibonacci, first_N_primes,
                                encode_rle_string, decode_rle_string)


def index(request):
    return render(request, "index.html", locals())


def fact(request):
    if request.method == "POST":
        number = int(request.POST.get("number"))
        fact_number = factorial(number)
    return render(request, "index.html", locals())


def fib(request):
    if request.method == "POST":
        number = int(request.POST.get("number"))
        fib_number = fibonacci(number)
    return render(request, "index.html", locals())


def prime(request):
    if request.method == "POST":
        number = int(request.POST.get("number"))
        primes = first_N_primes(number)
    return render(request, "index.html", locals())


def enc_rle(request):
    if request.method == "POST":
        string = request.POST.get("string")
        encoded = encode_rle_string(string)
    return render(request, "index.html", locals())


def dec_rle(request):
    if request.method == "POST":
        string = request.POST.get("string")
        decoded = decode_rle_string(string)
    return render(request, "index.html", locals())

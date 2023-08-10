from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse


def test1(request):
    return HttpResponse('It works for test')

from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
    ss='''
    <center>
    <h1> hello </h1>
    <hr color="red"/>
    <h2> hi</h2>
    <hr color="blue"/>
    <h3>welcome to django</h3>
    <hr color="green"/>
    </center>
    '''
    return HttpResponse(ss);
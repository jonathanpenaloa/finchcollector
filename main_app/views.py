from django.shortcuts import render

from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Evening Grosbeak', 'Evning Grosbeak', 'yellow', 3),
  Finch('Pine', 'Grosbeak', 'orange demon', 3),
  Finch('Bobo', 'Brown-capper', 'brown little demon', 3),
]




def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})

# Create your views here.

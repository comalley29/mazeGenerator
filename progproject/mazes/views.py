from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from mazes.models import Style
from . forms import InputUserData, MazeInputs
from django.shortcuts import render
from .forms import MazeInputs
from django.views.generic.base import RedirectView
from django.shortcuts import redirect

# Create your views here.

def home(request):
    
    return render(request, 'mazes/home.html')

def styles(request):
    styles=Style.objects.all()
    name=Style.objects.name

    context = {'styles':styles, 'name':name}
    return render(request, 'mazes/styles.html', context)


def stylepage(request, style_id):
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body

    context = {'style':style, 'title':title, 'body':body}
    return render (request, 'mazes/stylepage.html', context)


def generate(request):
    style=Style.objects.all()

    #if request.POST:

    

    return render(request, 'mazes/generate.html')


def download(request):
    style=Style.objects.all()
    return render(request, 'mazes/download.html')


def kruskals(request,style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/kruskals.html', context)


def aldousbroder(request,style_id):
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    style=Style.objects.all()
    return render(request, 'mazes/aldousbroder.html', context)

def backtracking(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/backtracking.html', context)

def binarytree(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/binarytree.html', context)

def cellularautomation(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/cellularautomation.html', context)

def dungeonrooms(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/dungeonrooms.html', context)

def ellers(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/ellers.html', context)

def growingtree(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/growingtree.html', context)

def huntandkill(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/huntandkill.html', context)




def prims(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/prims.html', context)

def recursivedivision(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/recursivedivision.html', context)

def sidewinder(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/sidewinder.html', context)
    
def wilsons(request, style_id):
    style=Style.objects.all()
    style_detail = get_object_or_404(Style, pk=style_id)
    style = Style.objects.get(id=style_id)
    title = style.name
    body = style.body


    context = {'style':style, 'title':title, 'body':body}
    return render(request, 'mazes/wilsons.html', context)

def inputUserData(request):
    form = InputUserData()
    if request.method == 'POST':    
        form = InputUserData(request.POST, request.FILES)
        if form.is_valid():
                input = form.save(commit=False)



  
# Create your views here.
def generate_view(request):
    form = MazeInputs() 
    print(dir(form()))
    context = { "form": MazeInputs() }
    context['form'] = MazeInputs()
    return render( request, "generate.html", context)


def generate_maze(request):
    form = MazeInputs()
    if request.method == "POST": 
        form = MazeInputs(request.POST, request.FILES)
        if form.is_valid():
            Maze = form.save(commit=False)
            Maze.name = request.styles_field
            Maze.width = request.width_field
            Maze.height = request.height_field
            Maze.save()

            return redirect('home')
        else:
            form = MazeInputs()

    return render(request, 'mazes/generate.html', {'form':form})




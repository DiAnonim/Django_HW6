from django.shortcuts import render, redirect
from .models import *

def home(request):
    posts = Post.objects.all()
    workers = Worker.objects.all()
    context = {
        'posts': posts,
        'workers': workers
    }
    return render(request, 'home.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        bd = request.POST.get('bd')
        salary = request.POST.get('salary')
        status = request.POST.get('status')
        post = Post.objects.get(id=request.POST.get('post'))
        Worker.objects.create(
            name=name,
            bd=bd,
            salary=salary,
            status=status,
            post=post
        )
        return redirect('home')
    
    return render(request, 'create.html', {'posts': Post.objects.all(), 'statuses': Worker.Status.choices})

def worker(request, worker_id):
    return render(request, 'worker.html', {'worker': Worker.objects.get(id=worker_id)})

def update(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    if request.method == 'POST':
        name = request.POST.get('name', worker.name)
        bd = request.POST.get('bd', worker.bd)
        salary = request.POST.get('salary', worker.salary)
        status = request.POST.get('status', worker.status)
        post = Post.objects.get(id=request.POST.get('post', worker.post.id))
        Worker.objects.filter(id=worker_id).update(
            name=name,
            bd=bd,
            salary=salary,
            status=status,
            post=post
        )
        return redirect('home')
    return render(request, 'update.html', {'worker': worker, 'posts': Post.objects.all(), 'statuses': Worker.Status.choices})

def delete(request, worker_id):
    Worker.objects.filter(id=worker_id).delete()
    return redirect('home')
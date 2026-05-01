# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from .models import Task

# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'tasks/task_list.html', {'tasks': tasks})


from django.shortcuts import render, redirect
from .models import Task 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

# @login_required
# show tasks
# def task_list(request):
#     tasks = Task.objects.filter(user=request.user)
#     return render(request, 'tasks/task_list.html', {'tasks': tasks})

# from django.contrib.auth.decorators import login_required
# from .models import Task




@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    # SEARCH
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(title__icontains=query)

    # FILTER
    status = request.GET.get('status')
    if status == 'completed':
        tasks = tasks.filter(completed=True)
    elif status == 'pending':
        tasks = tasks.filter(completed=False)

    total_tasks = Task.objects.filter(user=request.user).count()
    completed_tasks = Task.objects.filter(user=request.user, completed=True).count()
    pending_tasks = Task.objects.filter(user=request.user, completed=False).count()

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks
    })

# add new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        deadline = request.POST['deadline']

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            priority=priority,
            deadline=deadline
        )

        return redirect('tasks')

    return render(request, 'tasks/add_task.html')

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('task_list')

#     return render(request, 'tasks/login.html')

def user_login(request):
    error = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/tasks/')
        else:
            error = "Invalid username or password"

    return render(request, 'tasks/login.html', {'error': error})




def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('tasks')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.priority = request.POST['priority']
        task.deadline = request.POST['deadline']
        task.completed = 'completed' in request.POST

        task.save()
        return redirect('tasks')

    return render(request, 'tasks/edit_task.html', {'task': task})



# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         User.objects.create_user(username=username, password=password)

#         return redirect('login')

#     return render(request, 'tasks/register.html')



# def register(request):
#     error = None

#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         if User.objects.filter(username=username).exists():
#             error = "Username already exists"
#         else:
#             User.objects.create_user(username=username, password=password)
#             return redirect('login')

#     return render(request, 'tasks/register.html', {'error': error})


def register(request):
    error = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       

        # Password validation
        if len(password) < 6:
            error = "Password must be at least 6 characters long"

        elif password.isnumeric():
            error = "Password cannot be only numbers"

        else:
            from django.contrib.auth.models import User
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, 'tasks/register.html', {'error': error})


def home(request):
    return render(request, 'tasks/home.html')

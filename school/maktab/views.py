from django.shortcuts import render
from .models import dars, tadbirlar, oqituvchilar, photolar, kitob
from django.core.mail import send_mail


# Create your views here.
def home(request):
    lesson = dars.objects.all()
    bayram = tadbirlar.objects.all()
    teacher = oqituvchilar.objects.all()
    if request.method == 'POST':
        ism = request.POST['user']
        fam = request.POST['familya']
        nomer = request.POST['raqam']
        xabar = request.POST['xabar']
        title=ism
        msg='Sizga '+fam+ ' '+ism+'dan Savol bor'+'\nSavoli: '+xabar+'\nNomeri :'+nomer

        print(ism, xabar, nomer)
        send_mail(
            ism,
            msg,
            nomer,
            ['alevcoder1@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'index.html', {'DARSLAR': lesson, 'BAYRAM': bayram, 'Ustozlar': teacher})

def about(request):
    return render(request, 'about.html')

def blog(request):
    bayram = tadbirlar.objects.all()
    return render(request, 'blog.html', {'BAYRAM': bayram})

def contact(request):
    if request.method == 'POST':
        ism = request.POST['user']
        xabar = request.POST['xabar']
        mavzu = request.POST['mavzu']
        email = request.POST['pochta']
        title=ism
        msg='Sizga '+ism+'dan xabar bor'+'\nMavzusi: '+mavzu+'\nEmail: '+email+'\nXABAR Mazmuni:\n'+xabar

        print(ism, xabar, email)
        send_mail(
            ism,
            msg,
            email,
            ['alevcoder1@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'contact.html')

def courses(request):
    lesson = dars.objects.all()
    return render(request, 'courses.html', {'DARSLAR': lesson})

def teacher(request):
    teacher = oqituvchilar.objects.all()
    return render(request, 'teacher.html', {'Ustozlar': teacher})

def book(request):
    kitobb = kitob.objects.all()
    return render(request, 'book.html', {'Kitoblar': kitobb})

def  elbook(request):
    return render(request, 'darslik_kitoblar.html')

def rasm(request):
    img = photolar.objects.all()
    return render(request, 'photolar.html', {'Images': img})
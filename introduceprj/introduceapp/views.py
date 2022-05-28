from django.shortcuts import render

# Create your views here.


def flex(request):
    return render(request,'flex.html')

def main(request):
    return render(request,'main.html')

def table(request):
    return render(request,'table.html')

def photoflex(request):
    return render(request,'photo_flex_layout.html')

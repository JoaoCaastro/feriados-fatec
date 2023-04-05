from django.shortcuts import render
import datetime

dataHoje = datetime.date.today()

def natal(request):
    
    if dataHoje.month != 12 and dataHoje != 25:
        contexto = {
            'natal': False
        }
        return render(request, 'natal.html', contexto)
    
    elif dataHoje.month == 12 and dataHoje.day == 25:
        contexto = {
            'natal': True
        }
        return render(request, 'natal.html', contexto)

def tiradentes(request):

    if dataHoje.month != 4 and dataHoje.day!= 21:
        contexto = {
            'tiradentes': False
        }
        return render(request, 'tiradentes.html', contexto)        
        
    elif dataHoje.month == 4 and dataHoje == 21:
        contexto = {
            'tiradentes': True
        }
        return render(request, 'tiradentes.html', contexto)
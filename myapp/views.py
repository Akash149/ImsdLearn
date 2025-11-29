from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json as JSON

from myapp.models import Analysis

def home(request):
    return render(request, 'index.html')

def default(request):
    return render(request, 'index.html')

def analysis(request):
    return render(request, 'index.html')

@csrf_exempt
def save_analysis(request):
    if request.method == 'POST':
        try:

            # ca = float(request.POST.get('ca', 0.0))
            # mg = float(request.POST.get('mg', 0.0))
            # na = float(request.POST.get('na', 0.0))
            # so4 = float(request.POST.get('so4', 0.0))
            # others = float(request.POST.get('others', 0.0))
            
            data = JSON.loads(request.body.decode("utf-8"))
            print(data)
            Analysis.objects.create().from_dict(data).save()
            return JsonResponse({'status': 'success', 'message': 'Analysis saved successfully'}, status=201)
        
        except (ValueError, TypeError) as e:
            print(str(e))
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

        # from myapp.models import Analysis
        # analysis = Analysis.objects.create(ca=ca, mg=mg, na=na, so4=so4, others=others)
        
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
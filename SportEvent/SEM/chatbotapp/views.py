from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
@csrf_exempt  # Use this only if you're testing and want to disable CSRF protection
def chatbot_view(request):
    if request.method == 'POST':
        # Handle the POST request
        data = request.POST.get('data')  # or request.body for JSON
        return JsonResponse({"response": "Data received", "data": data})
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)


def chatbot_index(request):
    return render(request, 'chatbotapp/index.html')
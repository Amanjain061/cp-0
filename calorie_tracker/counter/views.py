from django.shortcuts import render
import requests

#API Key: mfx6UcMy6tdHw1IJg0RM4w==vdRPhyyT7A72xL9A

# Create your views here.
def home(request):

    query = '1lb brisket and fries'
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'mfx6UcMy6tdHw1IJg0RM4w==vdRPhyyT7A72xL9A'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

    return render(request, 'home.html')
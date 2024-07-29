from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import Image

def fetch_data_from_api():
    try:
        response = requests.get('https://pixabay.com/api/?key=45168268-a25a242d4cec3221591e14a61&category=food')
        response.raise_for_status()  # Check if the request was successful
        return response.json().get('hits', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []

def home_view(request):
    api_data = fetch_data_from_api()

    # Insert API data into the database
    for img in api_data:
        if not Image.objects.filter(user=img['user'], tags=img['tags'], pageURL=img['pageURL'], views=img['views'], likes=img['likes'], comments=img.get('comments')).exists():
            Image.objects.create(
                user=img['user'],
                tags=img['tags'],
                pageURL=img['pageURL'],
                views=img['views'],
                likes=img['likes'],
                comments=img.get('comments')
            )

    images = Image.objects.all()
    return render(request, 'index.html', {"images": images})

def img_details_view(request, pk):
    img = Image.objects.filter(id=pk).values()
    img_list = list(img)
    return JsonResponse({"image_details": img_list})

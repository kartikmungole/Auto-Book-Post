from django.shortcuts import render
import requests
from faker import Faker
from django.http import JsonResponse

fake = Faker()

def create_and_submit_book(request):
    # Generate fake data
    fake_book = {
        "id": fake.random_int(min=1, max=100),
        "title": fake.sentence(nb_words=3),
        "author": fake.name(),
        "price": f"{fake.random_number(digits=3)}.00"
    }

    # Send POST request to the API
    api_url = "http://127.0.0.1:5000/api/books"
    response = requests.post(api_url, json=fake_book)

    if response.status_code == 201:  # Status code 201 indicates success
        return JsonResponse({"message": "Book submitted successfully", "book": fake_book})
    else:
        return JsonResponse({"message": "Failed to submit book", "status_code": response.status_code})


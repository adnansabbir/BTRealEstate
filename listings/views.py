from django.shortcuts import render
from listings.models import Listing


def index(request):
    return render(request, 'listings/listings.html')


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')

from django.shortcuts import render
from .models import *


def index(request):
    products_all = Products()
    full_data = products_all.get_full()
    products_agg = products_all.products_agg()
    categories_agg = products_all.categories_agg()

    context = {
        'full_data': full_data,
        'products': products_agg,
        'categories': categories_agg,
    }

    # Create files from DB for download
    for key, value in context.items():
        with open(f'products/static/products/files/{key}.txt', 'w') as the_file:
            the_file.write(str(value))

    return render(request, 'products/index.html', context=context)



from django.db.models import Q
from .models import Medicine, Manufacturer


def search_medicines(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    manufacturer = Manufacturer.objects.filter(name__icontains=search_query)

    medicines = Medicine.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(generic_name__icontains=search_query) |
        Q(manufacturer__in=manufacturer)
    )

    return medicines, search_query

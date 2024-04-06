from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Medicine, Manufacturer


def paginate_medicines(request, medicines, results):
    page = request.GET.get('page')
    results = results
    paginator = Paginator(medicines, results)

    try:
        medicines = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        medicines = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        medicines = paginator.page(page)

    left_index = (int(page) - 4)

    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 5)

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, medicines


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

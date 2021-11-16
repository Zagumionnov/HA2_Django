from django.http import HttpResponse
from square import parsers

from square.utils import generate_password, execute_query, format_name, format_list


def index(request):
    return HttpResponse('Hello World')


def get_password(request):
    try:
        length = parsers.parser_int(request, 'length', 10, min_a=2, max_a=100)
    except ValueError as ex:
        return HttpResponse(str(ex), status=400)

    result = generate_password(length)

    return HttpResponse(result)


def get_sales(request):
    query = 'SELECT COUNT (UnitPrice * Quantity) FROM invoice_items'
    result = execute_query(query)
    return HttpResponse(format_name(result))


def get_genres(request):
    query = """
            SELECT genres.Name, SUM(tracks.Milliseconds)
            FROM tracks
            JOIN genres
            ON tracks.GenreId = genres.GenreId
            GROUP BY genres.GenreId
            """
    result = execute_query(query)
    return HttpResponse(format_list(result))


def get_greatest_hits(request):
    count = parsers.parser_int(request, 'count', 10)
    query = f"""
            SELECT tracks.Name, invoice_items.UnitPrice
            FROM invoice_items
            JOIN tracks
            ON invoice_items.TrackId = tracks.TrackId
            ORDER BY invoice_items.UnitPrice DESC
            LIMIT {count}
            """
    result = execute_query(query)
    return HttpResponse(format_list(result))

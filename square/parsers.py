def parser_int(request, param_name, default, min_a=float('-inf'), max_a=float('inf')):
    value = request.GET.get(param_name, str(default))

    if not value.isdigit():
        raise ValueError("Error: int is expected for length param")

    value = int(value)

    if not (min_a < value < max_a):
        raise ValueError("Error: length is out of range")

    return value


def parser_str(request, param_name, default):

    value = request.GET.get(param_name, default)
    return value


def parse_response(response, get_rate):
    all_bit_rate = response.json()
    for dist_rate in all_bit_rate:
        if dist_rate['code'] == get_rate:
            return f"Current exchange rate in {dist_rate['code']}: {dist_rate['rate']}"
        else:
            return f"{get_rate} code doesn't exist"


def parser_str_two(request, param_name, default):
    value = request.GET.get(param_name, default)
    if value == default:
        return value
    else:
        return f"('{value}')"


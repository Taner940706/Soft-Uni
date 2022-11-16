# get the response from next middleware or view
from django.shortcuts import redirect


def measure_time_middleware(get_response):
    def middleware(request, *args, **kwargs):
        return get_response(request, *args, **kwargs)

    return middleware


def redirect_to_index_on_error_middleware(get_response):
    def middleware(*args, **kwargs):
        response = get_response(*args, **kwargs)

        if response.status_code == 500:
            return redirect('index')
        return response

    return middleware
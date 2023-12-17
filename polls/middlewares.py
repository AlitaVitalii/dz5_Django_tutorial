class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        print('start')
        print('get_response', self.get_response)
        print('request.path', request.path)
        print('request.GET', request.GET)
        print('request.POST', request.POST)
        print('request', request)
        response = self.get_response(request)
        print('response', response)
        print('the end')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('request', request)
        print('view_func', view_func)
        print('view_args', view_args)
        print('view_kwargs', view_kwargs)


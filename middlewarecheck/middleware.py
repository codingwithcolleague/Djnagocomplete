from django.http import  HttpResponse, response

def my_middleware(get_response):
    print("One Time Initialization")
    def my_function(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    return my_function



class MyMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Initialization")
    
    def __call__(self,request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response



class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Father Initialization")
    
    def __call__(self,request):
        print("This Father before view")
        response = self.get_response(request)
        print("This Father after view")
        return response



class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print(" Brother Initialization")
    
    def __call__(self,request):
        print("This  Brother before view")
        response = self.get_response(request)
        print("This  Brother after view")
        return response


class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print(" Mother Initialization")
    
    def __call__(self,request):
        print("This  Mother before view")
        response = self.get_response(request)
        print("This  Mother after view")
        return response

class  MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_responce = get_response

    def __call__(self,request):
        response = self.get_responce(request)
        return response

    def process_view(request,*args,**kwargs):
        print("This is process before view")
        # return HttpResponse("Hie")
        return None

class  MyProcessException:
    def __init__(self,get_response):
        self.get_responce = get_response

    def __call__(self,request):
        response = self.get_responce(request)
        return response

    def process_exception(self,request,exception):
        print("Exception Occured")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        return HttpResponse(msg)


class  MyTeamplateClassMiddleware:
    def __init__(self,get_response):
        self.get_responce = get_response

    def __call__(self,request):
        response = self.get_responce(request)
        return response

    def process_template_response(self,request,response):
        print("Process template response from middleware")
        response.context_data["name"] = "Sonam"
        return response
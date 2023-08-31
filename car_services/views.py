from django.views.generic import ListView
from car_services.models import Vehicles

class IndexView(ListView):
    model = Vehicles
    template_name = "car_services/home.html"
    context_object_name = 'vehicles'
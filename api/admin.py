from django.contrib import admin

from api.models import *

admin.site.register(User)
admin.site.register(Role)
admin.site.register(ChargingRequest)
admin.site.register(ParkingSpot)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Logs)

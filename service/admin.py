from django.contrib import admin
from service.models import Feedback,Featuredcars


# Register your models here.
class ServiceFeedBackAdmin(admin.ModelAdmin):
    list_display = ('user_image','feedback','name','place')

admin.site.register(Feedback,ServiceFeedBackAdmin)

class ServiceFeaturedCarsAdmin(admin.ModelAdmin):
    list_display = ('car_name','car_price','car_image_url','car_model','car_hp','car_type','car_odometer_reading','car_description')
admin.site.register(Featuredcars,ServiceFeaturedCarsAdmin)
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dietclinic.views import *

router = routers.DefaultRouter()

router.register(r'Dietitian info: ', DietitianViewsets)
router.register(r'Patient info: ', PatientViewsets)
router.register(r'Appointment info: ', AppointmentViewsets)
router.register(r'Invoice: ', InvoiceViewsets)
router.register(r'Assistant info: ', AssistantViewsets)
router.register(r'Program info: ', ProgramViewsets)
router.register(r'Health tips:', Health_TipsViewsets)
router.register(r'Food system: ', Food_SystemViewsets)
router.register(r'Meal type: ', Meal_TypeViewsets)
router.register(r'Program details: ', DetailsViewsets)
router.register(r'information about food system and the meal type: ', Foodsystem_MealtypeViewsets)
router.register(r'Item info: ', ItemViewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapi/', include(router.urls)),
]

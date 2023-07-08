from rest_framework import routers
from .api import VerduraViewset

router = routers.DefaultRouter()

router.register('api/verduras', VerduraViewset, 'verduras')

urlpatterns = router.urls

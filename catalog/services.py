from config.settings import CACHE_ENABLED
from django.core.cache import cache
def model_objects_all(model):

    if not CACHE_ENABLED:
        return model.objects.all()
    key = f"{model.__name__}_list"
    categories_in_cache = cache.get(key)
    if categories_in_cache:
        return categories_in_cache
    else:
        categories = model.objects.all()
        cache.set(key, categories)
        return categories
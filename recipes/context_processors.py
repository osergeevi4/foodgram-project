from .models import ShopingList


def get_shop_list(request):
    """ Количество рецептов в списке покупок. """
    if request.user.is_authenticated:
        shop_list_count = ShopingList.objects.filter(
            user=request.user
        ).count()
    else:
        shop_list_count = None

    return {'shop_list_count': shop_list_count}

from django import template

from recipes.models import FollowRecipe, FollowUser, Recipe, ShopingList

register = template.Library()


@register.filter(name='get_filter_values')
def get_filter_values(value):
    return value.getlist('filters')


@register.filter(name='get_filter_link')
def get_filter_link(request, tag):
    new_request = request.GET.copy()
    if tag.slug in request.GET.getlist('filters'):
        filters = new_request.getlist('filters')
        filters.remove(tag.slug)
        new_request.setlist('filters', filters)
    else:
        new_request.appendlist('filters', tag.slug)
    return new_request.urlencode()


@register.filter(name='is_shop')
def is_shop(recipe, user):
    return (ShopingList.objects.select_related('recipe')
            .filter(user=user, recipe=recipe))


@register.filter(name='is_favorite')
def is_favorite(recipe, user):
    return FollowRecipe.objects.filter(user=user, recipe=recipe).exists()


@register.filter(name='is_follow')
def is_follow(author, user):
    return FollowUser.objects.filter(user=user, author=author).exists()


@register.filter(name='get_recipes')
def get_recipes(author):
    return Recipe.objects.select_related('author').filter(author=author)[:3]


@register.filter(name='get_count_recipes')
def get_count_recipes(author):
    if author is not None:
        count = author.recipes.count()
        if count < 1:
            return False

        if count % 10 == 1 and count % 100 != 11:
            end = 'рецепт'
        elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
            end = 'рецепта'
        else:
            end = 'рецептов'

        return f'Посмотреть все {count} {end}.'


@register.filter(name='parse_tags')
def parse_tags(get):
    return get.getlist('tag')


@register.filter(name='set_tag_qs')
def set_tag_qs(request, tag):
    new_req = request.GET.copy()
    tags = new_req.getlist('tag')
    if tag.title in tags:
        tags.remove(tag.title)
    else:
        tags.append(tag.title)

    new_req.setlist('tag', tags)
    return new_req.urlencode()

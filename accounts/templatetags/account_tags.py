from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def get_user_profile_picture(user):
    """Safely get user's profile picture URL or return default"""
    try:
        if user.is_authenticated:
            profile = getattr(user, 'profile', None)
            if profile and profile.profile_picture:
                return profile.profile_picture.url
    except Exception:
        pass
    # Return default avatar path using STATIC_URL
    return f"{settings.STATIC_URL}img/default-avatar.png"


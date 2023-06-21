import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_username_tag(value):
    """Validate the username tag.

    The username tag should be in the format of <username> or <username#1234>.
    """
    pattern = r"^([a-zA-Z0-9]+(#[0-9]{4}))"
    if not re.match(pattern, value):
        raise ValidationError(
            _("%(value)s is not a valid username tag."),
            params={"value": value},
        )


def validate_range_level(value):
    """Validate the range level.

    The range level should be in the range of 1 to 100.
    """
    if value < 0 or value > 3:
        raise ValidationError(
            _("%(value)s is not a valid range level."),
            params={"value": value},
        )


# rest framework validator
def validate_user_tag(attrs):
    """Validate the username tag.

    The username tag should be in the format of <username> or <username#1234>.
    """
    pattern = r"^([a-zA-Z0-9]+(#[0-9]{4}))"
    if not re.match(pattern, attrs.get("username")):
        raise ValidationError(
            _("%(value)s is not a valid username tag."),
            params={"value": attrs},
        )

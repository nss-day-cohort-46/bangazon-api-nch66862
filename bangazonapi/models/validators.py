from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_price(value):
        if value > 17500 or value < 0:
            raise ValidationError(
                _('%(value)s is not below $17,500'),
                params={'value': value},
            )
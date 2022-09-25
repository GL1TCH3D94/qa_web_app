import re
from django.core.exceptions import ValidationError


class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                "The password must contain at least 1 digit, 0-9."
            )

    def get_help_text(self):
        return "Your password must contain at least 1 digit, 0-9."


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                "The password must contain at least 1 uppercase letter, A-Z."
            )

    def get_help_text(self):
        return "Your password must contain at least 1 uppercase letter, A-Z."


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                "The password must contain at least 1 special character: " +
                "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
            )

    def get_help_text(self):
        return "Your password must contain at least 1 special character: ()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"

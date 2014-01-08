"""@decorators
Useful decorator classes to extend the capabilities of other classes

Extends the capability of classes in easily implemented and consistent manner.
"""

# Decorators Included by python
# - @staticmethod
# - @classmethod

class ClassProperty(object):
    def __init__(self, func):
        self.func = func
    def __get__(self, inst, cls):
        return self.func(cls)
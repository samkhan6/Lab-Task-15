#Q3: Metaclass for Class Decoration
class MetaDecorator(type):
    def __new__(cls, name, bases, dct):
        # Inject additional logic or modify the class here
        dct['additional_property'] = 'This property is added by the metaclass'

        return super().__new__(cls, name, bases, dct)

# Example usage
class DecoratedClass(metaclass=MetaDecorator):
    def __init__(self, value):
        self.value = value

# Create an instance of DecoratedClass
obj = DecoratedClass(value=42)

# Access additional property injected by the metaclass
print(obj.additional_property)


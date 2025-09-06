"""Test module for inherited attributes issue."""


class BaseClass:
    """Base class with documented attributes."""
    
    #: This is a documented attribute in the base class
    base_attr = "base_value"
    
    #: Another documented base attribute
    base_data = 42


class DerivedClass(BaseClass):
    """Derived class that inherits attributes."""
    
    #: This is a documented attribute in the derived class  
    derived_attr = "derived_value"
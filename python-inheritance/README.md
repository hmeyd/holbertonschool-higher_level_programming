# Python Inheritance Project

This project focuses on understanding and implementing inheritance in Python. It covers concepts such as superclasses, subclasses, method overriding, and the use of built-in functions like `isinstance`, `issubclass`, `type`, and `super`.

## Resources

- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://realpython.com/inheritance-composition-python/)
- [Learn to Program 10: Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without relying on Google:

### General
- What is a superclass, baseclass, or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- When and how to use `isinstance`, `issubclass`, `type`, and `super` built-in functions

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files must end with a newline
- The first line of all files must be `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code must follow the `pycodestyle` (version 2.7.*)
- All files must be executable
- The length of files will be tested using `wc`

### Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All test files must end with a newline
- All test files must be inside a `tests` folder
- All test files must be text files (extension: `.txt`)
- Tests must be executed using the command: `python3 -m doctest ./tests/*`
- All modules, classes, and functions must have documentation
- Documentation must be meaningful and explain the purpose of the module, class, or function
- Do not use the words `import` or `from` in comments

## Tasks

### 0. Lookup
Write a function `lookup(obj)` that returns the list of available attributes and methods of an object.

**Prototype:**
```python
def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)
```

### 1. My List
Write a class `MyList` that inherits from `list`. It includes a public instance method `print_sorted(self)` that prints the list in ascending order.

**Example:**
```python
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.print_sorted()  # Output: [1, 2, 3, 4, 5]
```

### 2. Exact Same Object
Write a function `is_same_class(obj, a_class)` that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

**Prototype:**
```python
def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class; otherwise False."""
    return type(obj) is a_class
```

### 3. Same Class or Inherit From
Write a function `is_kind_of_class(obj, a_class)` that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

**Prototype:**
```python
def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or its subclass; otherwise False."""
    return isinstance(obj, a_class)
```

### 4. Only Subclass Of
Write a function `inherits_from(obj, a_class)` that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

**Prototype:**
```python
def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class; otherwise False."""
    return isinstance(obj, a_class) and type(obj) is not a_class
```

### 5. Geometry Module
Write an empty class `BaseGeometry`.

**Example:**
```python
class BaseGeometry:
    """An empty class representing base geometry."""
    pass
```

### 6. Improve Geometry
Enhance the `BaseGeometry` class by adding a public instance method `area(self)` that raises an `Exception` with the message `area() is not implemented`.

**Example:**
```python
class BaseGeometry:
    """A class representing base geometry with an area method."""
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
```

### 7. Integer Validator
Add a public instance method `integer_validator(self, name, value)` to the `BaseGeometry` class that validates the value:
- If `value` is not an integer, raise a `TypeError` with the message `<name> must be an integer`.
- If `value` is less than or equal to 0, raise a `ValueError` with the message `<name> must be greater than 0`.

**Example:**
```python
bg = BaseGeometry()
bg.integer_validator("my_int", 12)  # Valid
bg.integer_validator("age", 0)      # Raises ValueError
```

### 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry`. It initializes with `width` and `height`, which must be positive integers validated by `integer_validator`.

**Example:**
```python
r = Rectangle(3, 5)
print(r)  # Output: <Rectangle object>
```

### 9. Full Rectangle
Enhance the `Rectangle` class to include an `area()` method and a `__str__` method that returns the rectangle description in the format `[Rectangle] <width>/<height>`.

**Example:**
```python
r = Rectangle(3, 5)
print(r)        # Output: [Rectangle] 3/5
print(r.area()) # Output: 15
```

### 10. Square #1
Write a class `Square` that inherits from `Rectangle`. It initializes with `size`, which must be a positive integer validated by `integer_validator`.

**Example:**
```python
s = Square(13)
print(s)        # Output: [Rectangle] 13/13
print(s.area()) # Output: 169
```

### 11. Square #2
Enhance the `Square` class to override the `__str__` method and return the square description in the format `[Square] <width>/<height>`.

**Example:**
```python
s = Square(13)
print(s)        # Output: [Square] 13/13
print(s.area()) # Output: 169
```

---

## Repository

- GitHub Repository: [holbertonschool-higher_level_programming](https://github.com/holbertonschool/holbertonschool-higher_level_programming)
- Directory: `python-inheritance`

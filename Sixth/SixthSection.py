'''Why object-oriented programming?'''

#Object-oriented programming allows you to create large, modular programs that can easily expand over time.
#Object-oriented programs hide the implementation from the end user.

#Objects are defined by characteristics and actions

'''
Encapsulation: One of the fundamental ideas behind object-oriented programming is called encapsulation: you can combine functions and data all into a single entity. In object-oriented programming, this single entity is called a class. Encapsulation allows you to hide implementation details, much like how the scikit-learn package hides the implementation of machine learning algorithms.
A function and a method look very similar. They both use the def keyword. They also have inputs and return outputs. The difference is that a method is inside of a class whereas a function is outside of a class.

'''

'''
Set and get methods
    Following the Python convention, the underscore in front of price is to let a programmer know that price should only be accessed with get and set methods rather than accessing price directly with shirt_one._price



class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

Instance Methods
    Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.
    Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.

Class Methods
    Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.
    Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.
    Python only allows one __init__ method per class. Using class methods it’s possible to add as many alternative constructors as necessary. This can make the interface for your classes self-documenting (to a certain degree) and simplify their usage

Static Methods
    This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).
    Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.
'''

'''
Making a package
    In this next section, you'll convert the distribution code into a Python package. A package is a collection of Python modules. Although the previous code might already seem like it was a Python package because it contained multiple files, a Python package also needs an __init__.py file.

Python environments
    A virtual environment is a silo-ed Python installation apart from your main Python installation. That way you can install packages and delete the virtual environment without affecting your main Python installation.


python3 -m venv environmentname
source environmentname/bin/activate
pip install numpy





python -m unittest test
pip install --upgrade 
'''



'''
Decorators
    Decorators provide a simple syntax for calling higher-order functions.
    By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
    functions are first-class objects. This means that functions can be passed around and used as arguments
    Inner Functions
        It’s possible to define functions inside other functions. 
    Returning Functions From Functions
        Note that you are returning first_child without the parentheses. Recall that this means that you are returning a reference to the function first_child.
    Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax

    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_whee():
        print("Whee!")


    Decorating Functions With Arguments
        The solution is to use *args and **kwargs in the inner wrapper function. Then it will accept an arbitrary number of positional and keyword arguments.

            def do_twice(func):
                def wrapper_do_twice(*args, **kwargs):
                    func(*args, **kwargs)
                    func(*args, **kwargs)
                return wrapper_do_twice

    Returning Values From Decorated Functions
        make sure the wrapper function returns the return value of the decorated function
        
        def do_twice(func):s
            def wrapper_do_twice(*args, **kwargs):
                func(*args, **kwargs)
                return func(*args, **kwargs)
            return wrapper_do_twice

'''

'''
Mixins

    In Python, mixins are supported via multiple inheritance.
    The delineation between using true inheritance and using mixins is nuanced, but it comes down to the fact that a mixin is independent enough that it doesn’t feel the same as a parent class. Mixins aren’t generally used on their own, but aren’t abstract classes either.
    

'''



'''
Putting code on Pypi

cd binomial_package_files
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

pip install --index-url https://test.pypi.org/simple/ dsnd-probability

# command to upload to the pypi repository
twine upload dist/*
pip install dsnd-probability


'''
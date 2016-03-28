class CustomAttrArg(object):
    def __init__(self, value):
        self.value = value

    def __call__(self, obj):
        def wrap():
            print("wrapping starts")
            obj()
            print("wrapping ends")
        return wrap

@CustomAttrArg(1)
def func():
    print("function called")


def wrapthis(func):
    def wrapper(*args, **kwargs):
        print("wrapping starts")
        func(*args, **kwargs)
        print("wrapping ends")
    
    return wrapper
    
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
@tags("strong")
def get_text(name):
    return "Hello "+name

get_text_new = tags("h1")(get_text)


print (get_text("John"))
print(get_text_new("John2"))    
   
@wrapthis    
def hello():
    print("hello")

@wrapthis
def helloperson(name):
    print("hello " + name)
    

hello()
hello = wrapthis(hello)
hello()
helloperson("pop")

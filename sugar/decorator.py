def log_1(func):
    def wrapper(*args, **kw):
        print 'call %s()' % func.__name__
        return func(*args, **kw)
    return wrapper

def log_2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s()' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log_1
@log_2('execute')
def test_func():
    print 'funny'

test_func()
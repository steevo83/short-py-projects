from functools import wraps

def make_html(element):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{element}>{func(*args, **kwargs)}</{element}>'
        return wrapper
    return inner_dec
        
        
@make_html("a")
def get_text(text):
    return text

get_text("Picture")
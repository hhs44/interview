# 方法一： 使用装饰器实现单例模式

from functools import wraps
"""
带装饰功能的函数（上面代码中的`wrapper`函数）
通常都会用`functools`模块中的`wraps`再加以装饰，
这个装饰器最重要的作用是给被装饰的类或函数动态添加一个`__wrapped__`属性，
这个属性会将被装饰之前的类或函数保留下来，
这样在我们不需要装饰功能的时候，可以通过它来取消装饰器，
例如可以使用`President = President.__wrapped__`来取消对`President`类做的单例处理。
"""
def singleton(cls):
    """ 单例类装饰器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in  instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class President:
    pass


# 方法二： 使用元类实现单例模式
class SingletonMeta(type):
    """自定义单例元类"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    pass
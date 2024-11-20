def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        try:
            del annotations["return"]
        except KeyError as e:
            pass
        for key, value in kwargs.items():
            if isinstance(value, annotations[key]):
                del annotations[key]
            else:
                raise TypeError
        for item_arg, item_type in zip(args, annotations.values()):
            if not isinstance(item_arg, item_type):
                raise TypeError
        return func(*args, **kwargs)

    return wrapper

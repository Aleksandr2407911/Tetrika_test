class strict:
    def __init__(self, func):
        self.func = func
        self.annotations = func.__annotations__

    def __call__(self, *args, **kwargs):
        try:
            del self.annotations["return"]
        except KeyError:
            pass

        for key, value in kwargs.items():
            if key in self.annotations and not isinstance(value, self.annotations[key]):
                raise TypeError(
                    f"Argument '{key}' must be of type {self.annotations[key].__name__}"
                )

        for item_arg, item_type in zip(args, self.annotations.values()):
            if not isinstance(item_arg, item_type):
                raise TypeError(
                    f"Argument '{item_arg}' must be of type {item_type.__name__}"
                )

        return self.func(*args, **kwargs)

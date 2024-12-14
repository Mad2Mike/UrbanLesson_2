import inspect


def introspection_info(obj):

    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not attr.startswith('__')]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    obj_module = inspect.getmodule(obj)

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module':  obj_module.__name__ if obj_module else None,

            }


    return info


number_info = introspection_info(42)
print(number_info)


def get(obj, path: str, default=None):
    """
    Forgiving get dot prop.
    If some level doesn't exist, it returns the default.
    """
    value = obj
    for key in path.split('.'):
        if isinstance(value, list):
            index = int(key)
            if index < len(value):
                value = value[index]
            else:
                return default
        elif isinstance(value, dict):
            if key in value:
                value = value[key]
            else:
                return default
        else:
            if hasattr(value, key):
                value = getattr(value, key)
            else:
                return default
    return value
def strict_get(obj, path: str):
    """
    Strict get dot prop.
    If some level doesn't exist, it raises the appropriate exception.
    """
    value = obj
    for key in path.split('.'):
        if isinstance(value, list):
            value = value[int(key)]
        elif isinstance(value, dict):
            value = value[key]
        else:
            value = getattr(value, key)
    return value

data = {
    'code': 'S0001',
    'nested': {'x': 'y', 'int': 0, 'null': None},
    'nums': [[12, 14, 16, 18, 20]],
    'names': ['Hank Navas', 'Melinda Swatzell', 'Lucio Tardy', 'Hershel Luebke']
     }

print(get(data, 'code'))
print(get(data, 'nested.x'))
print(get(data, 'nested.null'))
print(get(data, 'nums.0.2'))
print(get(data, 'nums.0.-1'))
print(get(data, 'names.0'))
print(get(data, 'names.-1'))


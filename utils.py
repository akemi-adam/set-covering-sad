def print_dict(d, indent=0):
    for key, value in d.items():
        prefix = "  " * indent
        if isinstance(value, dict):
            print(f"{prefix}{key}:")
            print_dict(value, indent + 1)
        elif isinstance(value, list):
            print(f"{prefix}{key}:")
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    print(f"{prefix}  -")
                    print_dict(item, indent + 2)
                else:
                    print(f"{prefix}  - {item}")
        else:
            print(f"{prefix}{key}: {value}")
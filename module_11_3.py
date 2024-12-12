import inspect
def introspection_info(obj):
    type_1=type(obj).__name__
    dir_1=dir(obj)
    met=[]
    attr=[]
    for i in dir_1:
        if callable(getattr(obj,i)):
            met.append(i)
        if not callable(getattr(obj,i)):
            attr.append(i)
    mod=inspect.getmodule(obj)
    info={'type': type_1,'атрибут':attr,'метод':met,'module':mod}
    return info

number_info = introspection_info(42)
print(number_info)
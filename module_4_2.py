def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()        # ничего не происходит
inner_function()     #  выдает ошибку NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

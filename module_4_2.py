def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()        # ничего не происходит
inner_function()     #  выдает ошибку

# def get_doc(any_function):
#     def inner_function():
#         return any_function.__doc__
#
#     return inner_function()
#
#
# @get_doc
# def test():
#     """this is a doc"""
#     return "hello"
#
#
# print(test())
def zero_check(any_fun):
    def inn(x,y):
        if y==0:
            return ("y is zero")
        return any_fun(x,y)
    return inn


@zero_check
def sum(x,y):
    return x+y
print(sum(10,9))

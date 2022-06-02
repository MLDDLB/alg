class A:

    def __init__(self):
        self.__field = None

    field = property()

    @field.getter
    def field(self):
        return self.__field

    @field.setter
    def field(self, value):
        self.__field = value    



val = A()
val.field = 'str'
print(val.field)

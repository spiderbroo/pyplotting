class A:
    class_attr = 0

    def __init__(self, my_param):
        self.attr_equals = my_param
        self.attr_minus_two = my_param-2
        self.constant_attr = 5
    
    @classmethod
    def class_blabla(cls, msg):
        print(cls.class_attr, msg)

    def object_blabla(self, msg):
        print(self.class_attr, msg)
    
    @staticmethod
    def im_static_im_so_cool(msggg=''):
        print(msggg)

a1 = A(2)
a2 = A(4)

print("object a1", a1)
print("object a2", a2)
print("attributes A", A.__mro__)
print("class_attr of A:", A.class_attr)
print("A.im_static_im_so_cool", A.class_blabla("fdfdsf"))
print("a1 attrs")
print("class_attr of a1:", a1.class_attr)
print("a1.constant_attr:", a1.constant_attr)
print("a1.attr_equals:", a1.attr_equals)
print("a1.attr_minus_two:", a1.attr_minus_two)

a1.class_attr = 100
print("class_attr of a2:", a2.class_attr)
A.class_attr = 100
print("class_attr of a2:", a2.class_attr)
print("a2 attrs")
print("class_attr of a2:", a2.class_attr)
print("a2.constant_attr:", a2.constant_attr)
print("a2.attr_equals:", a2.attr_equals)
print("a2.attr_minus_two:", a2.attr_minus_two)

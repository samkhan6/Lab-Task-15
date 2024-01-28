#Q2: Overriding Methods in Multiple Inheritance

class A:
    def common_method(self):
        return "A's method"

class B(A):
    def overridden_method(self):
        return "B's method"

class C(A):
    def overridden_method(self):
        return "C's method"

class D(B, C):
    pass

# Example usage
obj_d = D()
print(obj_d.common_method())       # Output: A's method
print(obj_d.overridden_method())   # Output: B's method (inherits from B, not C)

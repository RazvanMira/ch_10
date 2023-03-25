def example_function(c: int) -> int:
    print("locals at the beginning", locals())
    d = 36
    print("locals at the end", locals())
    return a + b + c + d


print("globals at the beginning:", globals())

a = 10
b = 13

r = example_function(24)

# print(r)

# print(a)
# print(b)

print("global at the end:", globals())

# print(c)
# print(d)
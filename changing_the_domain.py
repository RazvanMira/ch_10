def bar():
    global foo
    foo = "spam"

foo = "global"
print(foo)
bar()
print(foo)
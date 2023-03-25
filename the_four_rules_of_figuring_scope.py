def one():
    global foo # used with the global keyword => global variable
    foo = "local one"
    print("in one:", foo)

def two():
    foo = "local two" # assigned without global keyword => local variable
    print("in two", foo)

def three():
    print("in three", foo) # used without global keyword and existing => global variable

def four():
    bar = foo # we can use the global variable value to assign it to a local variable
    print("in four", foo)
    print("in four", bar)

foo = "global"

print("in global", foo) # used in global scope => global variable

one()
print("in global", foo)

two()
print("in global", foo)

three()
print("in global", foo)



try:
    s="Hello"
    print(s[5])
except Exception as e:
    print("Index error got triggered for s[5]", e)

try:
    a="abc"
    s = 100/a
except NameError:
    print("NameError got triggered for s=100/a", )
except IndexError:
    print("Index error got triggered for s=100/a")
except Exception as e:
    print("last except block", e)
finally:
    print("inside finally block")
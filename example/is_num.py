def isnum(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False

print(isnum('foo'))
print(isnum('1.4'))
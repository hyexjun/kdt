print(type(-3))
print(type(3.4E-4))
print(type(0.00034))
print(type('대한민국'))
print(type(False))
print(type(None))

print(type(0b000111111))
print(type(0o77))
print(type(0x2f))
print(0b000111111)
print(0o77)
print(0x2f)

googol = 10**100
print(googol*googol)

data = 3-4j
print(type(data))
print(data.real)
print(data.imag)
print(data.conjugate())


if 3 > 0:
    print("True1")

if False:
    print("True2")

if 1:
    print("True3")

if -5:
    print("True4")

if 3 < 0:
    print("True5")

print(bool(-5))
print(bool(" "))
print(bool(""))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool({}))
print(bool([]))

print(10*7)
print(10//7)
print(10 % 7)
print(10**7)

a = 3
b = 7
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

data = 1
data = data+1
print(data)
data += 1
print(data)
data -= 1
print(data)


a = 3
b = 3
print(a == b)
print(a is b)

a = 500
b = 500
print(a == b)
print(a is b)


a = 3
b = 256
c = -256
print(a << 5)
print(b >> 5)
print(c >> 5)

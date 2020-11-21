#p = True
p = bool('true')
q = False
r = p and q
s = p or (q and r)

print(r)
print(s)

print(type(s))
print(type(bool('true')))

ttt = 'abc\t\tdef\nefg'
print (ttt)

ttt = 'abcd\tdef\nefg'
print (ttt)

ttt = 'abcde\tdef\nefg'
print (ttt)

def my_func(u):
    i=78
    print('running function=u=' + str(u))
    print('running function i=' + str(i))

def add (a, b):
    return a + b
i=60
my_func(20)
for j in range (2):
    for i in range (3):
        print('i=' + str(i))
        print('finished j loop for j=' + str(j))

print('after the loop')
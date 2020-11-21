print(1.79e+308)
print(1.8e+308)

for i in range(5):
    if i == 1:
        continue
    if i == 3:
        break
        print(i)

## NOT_DOESNT WORK
def add(a, b=20):
    return a + b
add()

## NOT_DOESNT WORK
%%file t.txt
abc def

f = 't.txt'
with open(f, 'r') as infile:
    line = infile.readline()
    while line:
        print(line)
        line = infile.readline

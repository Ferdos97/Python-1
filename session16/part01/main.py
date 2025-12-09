
## r ===> read
## w ===> write
## a ===> write (append)

## -----------------------------

## write to file (append):

f = open('test.txt', 'a')
f.write('hello')
f.close()

# --------------------

f = open('test.txt', 'w')

f.write('hello 1')
f.write('\n')
f.write('hello 2')
f.close()

# -------------------

## read file:

f = open('test.txt', 'r')
print(f.read())
f.close()

#--------------------

f = open('test.txt', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

#----------------------

f = open('test.txt', 'r')
print(f.readline())
f.seek(0)                      #------->   returns to first line
print(f.readline())
f.close()

#----------------------

## returns a list

f = open('test.txt', 'r')
print(f.readlines())
f.close()

#-----------------------

## open file with 'with':


f = open('test.txt', 'w')
f.write('hello')
f.close()



with open('test.txt', 'w') as f:
    f.write('hello')

# f.write('hello 2') ====> error


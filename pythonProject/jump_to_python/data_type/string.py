# ch1
food = "Python's favorite food is perl"
say = '"Python is very easy." he said.'
multiline1 = "Life is too short\nYou need Python"
multiline2 = '''
Life is too short
You need Python
'''
multiline3 = """
Life is too short
You need Python
"""

print(multiline1)
print(multiline2)
print(multiline3)

# ch2) add string
head = "Python"
tail = " is fun"
print(head + tail)

# ch3) multi string
a = "python"
print(a * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

# ch4) string len
a = "Life is too short"
print(len(a)) # 17

# ch5) string indexing
a = "Life is too short, You need Python"
print(a[3]) # e
print(a[0]) # L
print(a[12]) #s
print(a[-1]) #n
print(a[-2]) #o
print(a[-5]) #y

# ch6) string slicing
b = a[0] + a[1] + a[2] + a[3]
print(b) # Life
print(a[0:4]) # Life
print(a[0:3]) # Lif

print(a[5:7]) # is
print(a[12:17]) # short

print(a[19:]) # You need Python
print(a[:17]) # Life is too short

print(a[:]) # Life is too short, You need Python
print(a[19:-7]) # You need

a = "20230331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

year = a[:4]
day = a[4:8]
print(year)
print(day)

# ch7) replace
a = "Pithon"
# a[1] = 'y' : error
print(a[:1] + 'y' + a[2:])

# ch8) formatting
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples." % number)
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

# print("Error is %d%." % 98) : Error
print("Error is %d%%." % 98)

print("%10s" % "hi")
print("%-10sjane." % 'hi')

print("%0.4f" % 3.42134234) # 3.4213
print("%10.4f" % 3.42134234) # '    3.4213'

print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))

number = 3
print("I eat {0} apples".format(number))

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

print("{0:<10}".format('hi')) # 'hi        '
print("{0:>10}".format('hi')) # '        hi'
print("{0:^10}".format("hi")) # '    hi    '
print("{0:=^10}".format("hi")) # '====hi===='
print("{0:!<10}".format("hi")) # 'hi!!!!!!!!'

y = 3.42134234
print('{0:0.4f}'.format(y))
print('{0:10.4f}'.format(y))

print('{{ and }}'.format())

name = '홍길동'
age = 30
print(f'나의 이름은 {name} 입니다. 나이는 {age} 입니다.')
print(f'나는 내년이면 {age + 1} 살이 된다.')

d = {'name' : '홍길동', 'age' : '30'}
print(f'나의 이름은 {d['name']} 입니다. 나이는 {d['age']} 입니다.')

print(f'{'hi':<10}')
print(f'{'hi':>10}')
print(f'{'hi':^10}')

print(f'{'hi':=^10}')
print(f'{'hi':!^10}')

y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')

a = 'hobby'
print(a.count('b'))

a = 'Python is the best choice'
print(a.find('b'))
print(a.find('k'))

a = 'Life is too short'
print(a.index('t'))
# print(a.index('k'))

print(','.join('abcd'))
print(','.join(['a', 'b', 'c', 'd']))

a = 'hi'
print(a.upper())
a = 'HI'
print(a.lower())

a = ' hi '
print(a.rstrip())
print(a.lstrip())
print(a.strip())

a = 'Life is too short'
print(a.replace('Life', 'Your leg'))

a = 'Life is too short'
print(a.split())

b = 'a:b:c:d'
print(b.split(':'))
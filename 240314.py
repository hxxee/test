# print("hello")
# print("데이터사이언스")

# print(3+2)

# print('%d'%(3+2))
# print('%d'%100)

# print("나는 %d 살이고, 만 나이는 %d 살입니다."%(20,19))

# print("%d 나누기 %d는 %d 입니다."%(20,4,20/4))

# print("파이는 %f 이다".%3.14)

# print('우리과는 %s 전공입니다.'%'datascience')

# print(1,2,3)

x = 1
y = 2.1
z = 'hahee'

# print(x,y,z)
# print('%d %f %s'%(x,y,z))

# print('안녕\n')

# print('내 이름은\t안녕')

# print('안녕?')

# print('\"안녕\"')

# print(1,2,3,sep='')
# print('010','1234','5678',sep='-')

# var1 = 100
# var2 = 3.14
# var3 = "파이썬"
# var4 = True
# var5 = False

# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))
# print(type(var5))

# x = 10
# y = 2
# print('%.0f'%(x/y))
# print(type(x/y))


# x='동덕여대'
# print(x)
# print(type(x))

# y='동덕'+' '+'여대'
# print(y)

# a='메롱 '

# print(3*a)



# x=(100>10)
# print(x)
# y=(2<1)
# print(y)
# z=True
# print(z)


# x='동덕'
# y='동덕'
# print(x==y)


# a=3
# b=5
# print(b)
# b=7
# print(b)

# print('x X')



# a=input('당신은 몇살입니까?')
# num_age=int(a)
# print(num_age+5)


# num_age=int(input('당신은 몇살입니까? : '))
# print(num_age+8)


# x=int(input('숫자하나입력해봐 : '))
# y=int(input('숫자하나더입력해봐 : '))
# print(x+y)


# print("## 택배를 보내기 위한 정보를 입력하세요. ##")
# input('받는 사람 : ')

# 2 week example source code
# Name: 조혜인
# Student ID: 2024311266
# Date: 2024.3.17

'''
25 page
'''

# 출력문의 다양한 형태

# 쉼표와 + 연산자 사용
print("입력하신 이름은","조혜인")
print("입력하신 이름은"+"조혜인")


# %형식 지정자 사용
print("입력하신 이름은 %s"%("조혜인"))


# str.format() 사용
print("입력하신 이름은 {}".format("조혜인"))
                           

# f-string 사용
print(f"입력하신 이름은 {'조혜인'}")

                           

'''
27 page
'''


name = input("이름을 입력하시오: ")
print(name, "씨, 안녕하세요?")
print("파이썬에 오신 것을 환영합니다.")

                           

'''
30 page
'''

x = int(input("첫 번째 정수를 입력하시오:"))
y = int(input("두 번째 정수를 입력하시오:"))
sum_xy = x+y
print("합은 ", sum_xy)
                           


'''
31 page
'''

area = float(input("면접(제곱미터): "))
result = area / 3.3
print(result, "평")
                           


'''
32 page
'''

print("pine" + 'apple')
print('apple'*3)


'''
34 page
'''

print('나는' + str(10) + '개의 사과를 먹었다.')
print('나는', 10, '개의 사과를 먹었다.')

num = 10
print('나는'+ str(num) + '개의 사과를 먹었다.')
print('나는', num , '개의 사과를 먹었다.')

print(f'나는 {num} 개의 사과를 먹었다.')

                           

'''
35 page
'''
                           

'''
주석의 용도
'''

"""
모두주석
"""

comment = '''
이것은 주석의
다른
기능
입니다.
'''
print(comment)
                           
                           
                           

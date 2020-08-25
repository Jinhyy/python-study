print('hello python')

# 1. 변수 
x = 1
y = '안녕'
print(y) 
print(x == y) # 결과 False, 값이 틀리므로.

# 2. 타입
x = 1
y = 2
z = 3.0

print(z % y) # 결과 1
print(y ** z) # 제곱근, 결과 8

# 3. 문자열
y = "bye"
z="""안녕하세요 여러 줄의 문자열 따옴표 3개로 할수 있습니다.
하지만 주의해주세요~ ㅎㅎ 엔터도 들어갑니다.
ㅎㅎ
"""
print(y + z) 
# 결과 
#bye안녕하세요 여러 줄의 문자열 따옴표 3개로 할수 있습니다.
#하지만 주의해주세요~ ㅎㅎ 엔터도 들어갑니다.
#ㅎㅎ

print("숫자형과 문자열은 합칠 수 없습니다.1 " + str(4))
print(int("4") + 4) # 8

# 4. 불리언
x = True # int 1
y = False # int 0
print('%d %s %s' % (x, x, not y), end=' ~\n')

# 5. 조건문
if not (1 > 2) and not ( 1 > 2) :
  print('haha')
elif 1 == 1 :
  print('equal')
else :
  print(True)

# 6. 함수
# 오버로딩 지원 X
def hello(s):
  print(s)

def hello(s,y):
  return s+y

print(hello('hi','a')) # =>hia 리턴됨

# 7. 반복문
for i in range(4):
  print(i)

i=0
while i < 3:
  print(i)
  i = i + 1

# 8. 자료구조
# 8-1. 리스트
x = list(range(4))
y = [0,1]
print('%s %s' % (x,y)) # 결과 [] []
print(x[1] == y[1]) # true
sorted(y)

# 8-2. 튜플 - 튜플은 여러 타입을 가질 수 있지만 값을 바꿀 수 없다.
x = (1,2,3)
y = (1,'a','b')
z = (True, 1.0, 'a')

print(x+z)

# 8-3. 딕셔너리 - 키, 밸류형태 자료구조
# => 키는 반드시 불변형이어야함(가변형인 리스트는 불가능)
x = {
  (1,2,3) : 'hi',
  "age": 22
}

#enumerate() 내장 함수는 순서가 있는 자료형(tuple, list, string)을 첫번째 인자로 받아서 각각의 index 값과 value 값들을 enumerate 객체로 리턴한다.
for index, (key, value) in enumerate(x.items()):
  print(index, key, value, sep=',')

fruit = ['사과','사과','바나나','딸기']
dictionary = {}
for value in fruit:
  if(value in dictionary):
    dictionary[value] = dictionary[value]+1
  else:
    dictionary[value] = 1

print(dictionary)
# {'사과': 2, '바나나': 1, '딸기': 1}

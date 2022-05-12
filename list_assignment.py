from string import ascii_lowercase
aplphbet_list = list(ascii_lowercase) #소문자 리스트

#대문자
full_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#합친 리스트
alphabet = []
alphabet = full_list + aplphbet_list

#마지막에 공백
alphabet.append(' ')


#0부터 9까지의 숫자를 담은 리스트
number = []
for i in range(0,10):
    number.append(i)
    
number.append('-')

#we are skhu likelion, hack your life, my name is kimhyojung

likelion = ''  #we are like lion
hack = '' #hack your life
name = '' #my name is Kimhyojung
index1 = []  #index담을 리스트

str1 = 'we are skhu likelion'
for i in range (0,len(str1)): #돌면서 인덱스 찾아서 담기
    temp = alphabet.index(str1[i])
    index1.append(temp)
    
for i in range(0,len(index1)):
    likelion = likelion + alphabet[index1[i]]
    
index1.clear()

str2 = 'hack your life'
for i in range(0,len(str2)):
    temp = alphabet.index(str2[i])
    index1.append(temp)

for i in range(0,len(index1)):
    hack = hack + alphabet[index1[i]]

index1.clear()

str3 = 'my name is Kimhyojung'
for i in range(0,len(str3)):
    temp = alphabet.index(str3[i])
    index1.append(temp)

for i in range(0,len(index1)):
    name = name + alphabet[index1[i]]
    
index1.clear()

print(likelion)
print(hack)
print(name)

#number리스트에서 생일,전화번호,학번 만들고 변수에 저장하고 출력
birth = str(number[2])+str(number[0]) + str(number[0]) + str(number[0]) + str(number[0]) + str(number[4])+str(number[2])+str(number[6])

print("제 생일은 %s 입니다." %birth)

phone_num = str(number[0])+str(number[1])+str(number[0])+str(number[10])+str(number[7])+str(number[5])+str(number[3])+str(number[3])+str(number[10])+str(number[6])+str(number[1])+str(number[2])+str(number[5])
print(phone_num)
print("제 전화번호는 %s 입니다" %phone_num)

school_num = str(number[2])+str(number[0])+str(number[1])+str(number[9])+str(number[1])+str(number[4])+str(number[0])+str(number[2])+str(number[2])
print('제 학번은 %s 입니다' %school_num)
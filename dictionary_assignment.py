DICT_ = {"이름":"김효중","나이":23,"생일":"4월 26일","성별": "남자","전화번호": "010-7533-6125"}
DICT_second = {"이름":"김철수","나이":26,"생일":"5월 26일","성별": "남자","전화번호": "010-1234-5678"}
DICT_third = {"이름":"김수철","나이":27,"생일":"1월 26일","성별": "남자","전화번호": "010-9876-5432"}

birth = [] #생일
age = [] #나이
name = [] #이름
MW = [] #성별
phone = []#전화번호

for i in range(1,4): #1부터 3까지 리스트 append
    birth.append(i)
    age.append(i)
    name.append(i)
    MW.append(i)
    phone.append(i)
    
#key값으로 value찾기
birth[0] = DICT_["생일"] 
birth[1] = DICT_second["생일"]
birth[2] = DICT_third["생일"]

age[0] = DICT_["나이"]
age[1] = DICT_second["나이"]
age[2] = DICT_third["나이"]

name[0] = DICT_["이름"]
name[1] = DICT_second["이름"]
name[2] = DICT_third["이름"]

MW[0] = DICT_["성별"]
MW[1] = DICT_second["성별"]
MW[2] = DICT_third["성별"]

phone[0] = DICT_["전화번호"]
phone[1] = DICT_second["전화번호"]
phone[2] = DICT_third["전화번호"]

#출력
for i in range (0,1):
    
    print(name)
    print("\n")
    print(age)
    print("\n")
    print(birth)
    print("\n")
    print(MW)
    print("\n")
    print(phone)
    print("\n")
    
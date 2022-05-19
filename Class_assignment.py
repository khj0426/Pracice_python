class student:
    def __init__(self,name,grade,student_number,sex,address,phone_number,year):
       self.name = name
       self.phone_number = phone_number
       self.year = year
       self.grade = grade
       self.student_number = student_number
       self.sex = sex
       self.address  = address
       self.year = year

 
 
def introduce(self):
    print("이름은 %s 이다"%self.name)
    print("학년은 %d 이다"%self.grade)
    print("학번은 %d 이다"%self.student_number)
    print("성별은 %s 이다"%self.sex)
    print("주소는 %s 이다"%self.address)
    print("전화번호는 %s 이다"%self.phone_number)
    if self.year == 1:
        print("멋사 1년차")
        print("우와 아기사자다!")
    else:
        print("멋사 %d년차" % self.year)
        print("우와 운영진이다 !")


instance1 = student("김효중",2,201914022,"남자","파주","01075336125",0)
instance2 = student("김중효",3,202014022,"남자","고양","01075336125",2)
instance3 = student("김호중",1,201814022,"남자","서울","010752136125",1)

while True:

    class_NAME = input("객체 명을 입력하시오. (단, 영문으로):")
    if class_NAME == "종료":
        break
    name = input("이름을 입력하시오. (단,한글로):")
    instance1.name = name
    grade = int(input("학년을 입력하시오. (단,숫자로):"))
    instance1.grade = grade
    student_number = int(input("학번을 입력하시오. (단,숫자로):"))
    instance1.student_number = student_number
    sex = input("성별을 입력하시오. (모를 떄는 모른다 라고 입력.):")
    instance1.sex = sex
    address = input("주소를 입력하시오.(~시까지만)")
    instance1.address = address
    phone_number = input("전화번호를 입력하시오 (모를 떼는 모른다 라고 입력.):")
    instance1.phone_number = phone_number
    year = int(input("멋사 몇년차인가여?(단,숫자로):"))
    instance1.year = year
    introduce(instance1)










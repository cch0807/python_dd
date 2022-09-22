# self의 이해
# self는 인스턴스 객체!
# 클래스 안에 있는 self의 주소와 만들어진 인스턴스 주소는 같다! 즉, self는 인스턴스 그 자체이다!


class SelfTest:

    # 클래스 변수
    name = "amamov"

    def __init__(self, x):
        self.x = x  # 인스턴스 변수

    # 클래스 메서드
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")

    # 인스턴스 메서드
    def func2(self):
        print(f"self: {self}")
        print("class안의 self 주소 : ", id(self))
        print("func2")


test_obj = SelfTest(17)

test_obj.func2()
SelfTest.func1()

# SelfTest.func2()
# print(SelfTest.x)

# test_obj.__class__()

print("인스턴스의 주소: ", id(test_obj))

"""
self: <__main__.SelfTest object at 0x7f09eef26f70>
class안의 self 주소 :  139680640298864
func2
cls: <class '__main__.SelfTest'>
func1
인스턴스의 주소:  139680640298864
"""
test_obj.func1()
print(
    test_obj,
)

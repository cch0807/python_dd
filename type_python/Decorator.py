def copyright(func):
    def new_func():
        print("@ asvc")
        func()

    return new_func


@copyright
def smile():
    # print("@ asvc")
    print("ð")


@copyright
def angry():
    # print("@ asvc")
    print("ðĢ")


@copyright
def love():
    # print("@ asvc")
    print("ð")


# ėŽė ė í íėėėī @ ėŽėĐ
# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)

smile()
angry()
love()

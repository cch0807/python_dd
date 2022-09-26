"""
Python Advanced(2) - Context Manager(1)
Keyword - @Contextlib.contextmanager, __enter__, __exit__

"""

"""

가장 대표적인 with 구문 이해
Contextlib 데코레이터 사용
코드 직관적, 예외 처리 용이성
정확한 이해 후 사용이 프로그램이 개발에 중요(문제 발생 요소 감소를 위해)

"""

import contextlib
import time

# Ex1
# Use decorator


@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f  # __enter__
    f.close()  # __exit__


with my_file_writer("testfile4.txt", "w") as f:
    f.write("Context Manager Text4.\nContextlib Test4.")

# Ex2
# Use decorator


@contextlib.contextmanager
def ExcuteTimerDc(msg):
    start = time.monotonic()
    try:  # __enter__
        yield start
    except BaseException as e:
        print("Logging exception {}: {}".format(msg, e))
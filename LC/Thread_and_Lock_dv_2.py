import threading
import time
import random

# 동기화 사용 x
# def run(n):
#     global total_footprint
#     for i in range(10):
#         print(f'{n} {i}')
#         tmp = total_footprint
#         time.sleep(0.1)
#         total_footprint = tmp + i

#     print(f'* [{n} done]')

# if __name__ == '__main__':
#     lock = threading.Lock()
#     players= ['rabbit', 'turtle']
#     total_footprint = 0
#     t1 = threading.Thread(target=run, args=(players[0],))
#     t2 = threading.Thread(target=run, args=(players[1],))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

#     print(f'total_footprint: {total_footprint}')

# 동기화 사용
def run(n):
    global total_footprint
    for i in range(10):
        print(f"{n} {i}")
        lock.acquire()

        tmp = total_footprint
        # time.sleep(0.1)
        total_footprint = tmp + i
        lock.release()

    print(f"* [{n} done]")


if __name__ == "__main__":
    lock = threading.Lock()
    players = ["rabbit", "turtle"]
    total_footprint = 0
    t1 = threading.Thread(target=run, args=(players[0],))
    t2 = threading.Thread(target=run, args=(players[1],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"total_footprint: {total_footprint}")

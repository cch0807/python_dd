"""
Concurrency, CPU Bound vs I/O Bound - CPU Bound(2) - Multiprocessing
Keyword - CPU Bound

"""

# CPU-Bound Multiprocessing 예제

from multiprocessing import current_process, Array, Manager, Process, freeze_support
import time

# 실행 함수1(계산)
def cpu_bound(number):
    return sum(i * i for i in range(number))


def main():
    numbers = [3_000_000 + x for x in range(15)]

    # Check
    print(numbers)

    # 프로세스 리스트 선언
    processes = list()

    # 프로세스 공유 매니저
    manager = Manager()

    # 리스트 획득(프로세스 공유)
    total_list = manager.list()

    # 실행 시간 측정
    start_time = time.time()

    # 프로세스 생성 및 실행
    for i in numbers:  # 1 ~ 100 적절히 조절
        # 생성
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list))

        # 배열에 담기
        processes.append(t)

        # 시작
        t.start()

    # Join
    for process in processes:
        process.join()

    # 결과 출력
    print(f"Total list : {total_list}")
    print(f"Sum : {sum(total_list)}")

    # 실행 시간 종료
    duration = time.time() - start_time

    print()

    # 수행 시간
    print(f"Duration : {duration} seconds")


if __name__ == "__main__":
    main()

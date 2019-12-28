# -*- coding=utf-8 -*-

import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def task(id):
    """ 任务 """

    print(id)

    # 模拟程序运行
    time.sleep(1)

    if id > 0:
        return True
    else:
        return False

def main():

    # 线程池大小
    pool_count = 3

    # 任务列表
    task_list = [-9, -2, 0, 3, 4, 5]

    with ThreadPoolExecutor(max_workers=pool_count) as t:

        result_list = []
        begin = time.time()

        for id in task_list:
            # 提交任务
            result = t.submit(task, id)
            result_list.append(result)

        for future in as_completed(result_list):
            result = future.result()
            print(result)
            print("*" * 50)

        times = time.time() - begin
        print("耗时: {}".format(times))

if __name__ == "__main__":
    main()

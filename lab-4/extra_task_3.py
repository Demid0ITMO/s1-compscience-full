import time
import task as t1
import extra_task_1 as t2
import extra_task_2 as t3

def Time_check(name_of_file: str):
    start = time.time()
    for i in range(10):
        if name_of_file == 'task':
            t1.task()
        elif name_of_file == 'd1task':
            t2.task()
        else:
            t3.task()
    duration = time.time() - start
    return duration

with open("extra_task_3_output.txt", "w") as file:
    print('Без библиотек - ' + str(Time_check('task')), file=file)
    print('С библиотеками - ' + str(Time_check('d1task')), file=file)
    print('С регулярками - ' + str(Time_check('d2task')), file=file)

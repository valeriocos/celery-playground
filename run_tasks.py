from proj.tasks import add, mul, xsum
import time

if __name__ == '__main__':
    tasks = [add.delay(1, 2), mul.delay(1, 2), xsum.delay([1, 2, 3, 4, 5])]
    for t in tasks:
        while not t.ready():
            time.sleep(1)
        msg = "id: {}, name: {}, result: {}".format(t.id, t.name, t.result)
        print(msg)

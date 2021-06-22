import time
from threading import Thread, Event
import threading


# class CountdownTask():
#     def __init__(self):
#         self._running = True
#
#     def terminate(self):
#         self._running = False
#
#     def run(self, n):
#         while self._running and n > 0:
#             print('T-minus', n)
#             n -= 1
#             time.sleep(1)
#
#     @property
#     def running(self):
#         return self._running
#
#
# c = CountdownTask()
# t = Thread(target=c.run, args=(10,))
# t.start()
# print(t.name, '00')
# print(c.running, '111')
# print((t.is_alive()), '222')
# t.join()
# # t.join(timeout=5)
# c.terminate()
# print(threading.main_thread())


def countdowmn(n, started_evt):

    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)


started_evt = Event()

if __name__ == '__main__':

    print('Launching countdown')
    t = Thread(target=countdowmn, args=(10, started_evt))
    t.start()

    started_evt.wait()
    print('countdown is running')

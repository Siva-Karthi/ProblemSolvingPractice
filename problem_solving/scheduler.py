import heapq
from datetime import datetime, timedelta

"""
use asyncio and coroutine

async supported sleep -


--

min heap [ (1, "python"), (2, "world"), (3, "hello")]

min heap [ (2, "world"),(1,"hello again"), (3, "hello")]
(1,"hello again") - 12:00.02

(10, "hi") at 12  - 12:10
(9, "hello") at 12.2 - 12:11
(8, "python") at 12.5 - 12:13


"""


class Scheduler():
    def __init__(self, jobs):
        self.q = jobs
        if jobs:
            heapq.heapify(self.q)
            self.run()
        # else: # todo : handle dynamic inputs
        # self.q = heapq.heapify([])

    def run(self):
        while True:
            current_time = datetime.now()
            if self.q and self.q[0][0] == current_time:
                item = self.q.pop(0)
                print(item[1])


if __name__ == '__main__':
    """
    (3, "hello") at 12
    (2, "world") at 12
    (1, "python") at 12

    Output:
    python #12:00.01 
    world  #12:00.02
    hello  #12:00.03
    """
    jobs = [
        [3, "hello"],
        [2, "world"],
        [1, "python"]
    ]
    current_time = datetime.now()
    for i in range(len(jobs)):
        delay = timedelta(seconds=jobs[i][0])
        jobs[i][0] = current_time + delay
    scheduler = Scheduler(jobs)

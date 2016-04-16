from apscheduler import BlockingScheduler
import sys, os

def my_job():
    print 'hello world'
 
sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5)
sched.start()
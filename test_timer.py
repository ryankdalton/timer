import time
from timer import Timer


t1 = Timer('Hello')
time.sleep(1)
t1.pprint('start')
time.sleep(1)
t1.pprint('elapsed')
time.sleep(1)
t1.pprint('elapsed')
time.sleep(1)
t1.pprint('elapsed')
time.sleep(1)
t1.pprint('elapsed')
time.sleep(1)
t1.pprint('elapsed')
time.sleep(1)
t1.pprint('end')
t1.pprint('elapsed')


t2 = Timer('Goodbye')
time.sleep(1)
#t2.end_timer()



timer_dict = {}
timer_dict[t1.name] = str(t1.elapsed)
timer_dict[t2.name] = str(t2.elapsed)

print(timer_dict)
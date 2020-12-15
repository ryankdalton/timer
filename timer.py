import datetime, time

class Timer():
    """Create a timer object to track how long a process takes to complete"""
    
    def __init__(self, name='default'):
        """Begin a new timer and provide a unique name, if desired"""
        self.start = datetime.datetime.now()
        self.elapsed = None
        self.end = None
        self.name = name

    def elapsed_timer(self):
        """Calculate an intermediate elapsed time from the start of the timer"""
        self.elapsed = datetime.datetime.now() - self.start

    def end_timer(self):
        """End the timer and calculate total elapsed time"""
        self.end = datetime.datetime.now()
        self.elapsed = self.end - self.start

    def pprint(self, var):
        """Pretty print the requested property of the timer:  start, elapsed, end"""
        try:
            if var == 'start':
                print('Start time: {starttime}'.format(starttime=self.start))
            elif var == 'elapsed':
                if self.end == None:
                    self.elapsed_timer()
                print('Elapsed time: {elapsedtime}'.format(elapsedtime=self.elapsed))
            elif var == 'end':
                if self.end == None:
                    self.end_timer()
                print('End time: {endtime}'.format(endtime=self.end))
            else:
                print('Property "{var}" is not set'.format(var=var))
        except:
            print('Property "{var}" is not set'.format(var=var))



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
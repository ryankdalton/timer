import datetime

class Timer():
    """Create a timer object to track how long a process takes to complete"""
    
    def __init__(self, name='default'):
        """Begin a new timer and provide a unique name, if desired"""
        self.begin = datetime.datetime.now()
        self.elapsed = None
        self.end = None
        self.name = name

    def elapsed_timer(self):
        """Calculate an intermediate elapsed time from the begining of the timer"""
        self.elapsed = datetime.datetime.now() - self.begin

    def stop(self):
        """End the timer and calculate total elapsed time"""
        self.end = datetime.datetime.now()
        self.elapsed = self.end - self.begin

    def pprint(self, var):
        """Pretty print the requested property of the timer:  begin, elapsed, end"""
        try:
            if var == 'begin':
                print('Begin time: {begintime}'.format(begintime=self.begin))
            elif var == 'elapsed':
                if self.end == None:
                    self.elapsed_timer()
                print('Elapsed time: {elapsedtime}'.format(elapsedtime=self.elapsed))
            elif var == 'end':
                if self.end == None:
                    self.stop()
                print('End time: {endtime}'.format(endtime=self.end))
            else:
                print('Property "{var}" is not set'.format(var=var))
        except:
            print('Property "{var}" is not set'.format(var=var))


class Log():
    def __init__(self, name='default'):
        """Log timers to a dictionary that can be used for process reporting"""
        self.log = []
        self.name = name

    def append(self, key, value, index=None):
        if index == None:
            self.log.append({key:value})
        else:
            self.log.insert(index, {key:value})

    def pprint(self):
        print('\nProcessing time(s) per process:')
        for kv in self.log:
            for key,value in kv.items():
                print('... {key}: {value}'.format(key=key, value=value))

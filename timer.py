import time

class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None
        self._start_time = None

    def __enter__(self):
        self._start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self._start_time
        self.last_run = elapsed_time
        self.runs.append(elapsed_time)
        if self.min is None or elapsed_time < self.min:
            self.min = elapsed_time
        if self.max is None or elapsed_time > self.max:
            self.max = elapsed_time

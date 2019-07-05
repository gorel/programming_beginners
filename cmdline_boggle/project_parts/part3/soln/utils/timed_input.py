import datetime
import threading

class TimedInput(object):
    def __init__(self, prompt, timeout_seconds, timeout_msg):
        self.prompt = prompt
        self.timeout_seconds = timeout_seconds
        self.timeout_msg = timeout_msg
        self.answers = []

    def start(self):
        start = datetime.datetime.now()
        end_time = start + datetime.timedelta(seconds=self.timeout_seconds)
        timer = threading.Timer(self.timeout_seconds, print, [self.timeout_msg])
        timer.start()

        # Repeat until we get the timeout signal
        answer = None
        answered_at = None
        while datetime.datetime.now() < end_time:
            raw_answer = input(self.prompt)
            if raw_answer == "END ROUND":
                break
            answer = raw_answer.strip().lower()
            self.answers.append(answer)
            answered_at = datetime.datetime.now()

        # Remove the last answer if it was after the timer ended
        if answered_at is not None and answered_at > end_time:
            self.answers.pop()
        timer.cancel()

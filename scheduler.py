import os
import subprocess
import time
from daemon import runner

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/your-pid-name.pid'
        self.pidfile_timeout = 5
    def run(self):

        try:
            while True:

                print "hello"

                time.sleep(10)

        except Exception, e:
            raise

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()

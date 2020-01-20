import signal

class Detector:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self,signum, frame):
        self.kill_now = True

if __name__ == '__main__':
    killer = Detector()
    while not killer.kill_now:
        print('waiting...')


    print('Graceful Exit...')
    exit()
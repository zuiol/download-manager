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
        
    def on_created(self, event):
        self.process(event)

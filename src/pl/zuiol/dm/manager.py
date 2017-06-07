# Main class in this application
import sys

from PyQt5.QtWidgets import QApplication
from watchdog import observers
from pl.zuiol.dm.watcher.monitoring import MyHandler
from pl.zuiol.dm.gui import MainWindow


if __name__ == '__main__':    
    
    #Start window for application
    print("1")
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    print("2")
    
    observer = observers.Observer()
    observer.schedule(MyHandler(mw), "C:\\Users\\sg0212049\\Downloads\\", False)
    observer.start()
    
    """ try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
   
    observer.join()
    """
    
    sys.exit(app.exec_())
    
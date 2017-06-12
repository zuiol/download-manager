# Main class in this application
import sys

from PyQt5.QtWidgets import QApplication
from watchdog import observers
from pl.zuiol.dm.watcher.monitoring import MyHandler
from pl.zuiol.dm.gui import MainWindow
from configparser import SafeConfigParser



if __name__ == '__main__':    
    
    #Read properties
    config = SafeConfigParser()
    config.read("..\\..\\..\\..\\properties\\settings.ini")
    sourceDirectory = config['defaults']['source']
    print(sourceDirectory)
    
    #Start window for application
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    
    observer = observers.Observer()
    observer.schedule(MyHandler(mw), sourceDirectory, False)
    observer.start()
    
    """ try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
   
    observer.join()
    """
    
    sys.exit(app.exec_())
    
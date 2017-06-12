# Damian's application test
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout,\
    QLabel, QCheckBox, QSpacerItem, QSizePolicy, QSystemTrayIcon, QStyle,\
    QAction, qApp, QMenu, QPushButton, QLineEdit
from PyQt5.Qt import QSize
from pl.zuiol.dm.logic.mover import moveHandledFile

class MainWindow(QMainWindow):
    
    check_box = None
    try_icon = None
    
    
    handledFileLabel = None
    ok_button = None
    keyword_textbox = None
    
    def __init__(self):
        
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(480, 80)) 
        self.setMaximumSize(QSize(480, 80))
        self.setWindowTitle("Download Manager by zuiol")
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)
        grid_layout.addWidget(QLabel("Application, which can minimize to tray", self), 0, 0)
        
        #add check box
        self.check_box = QCheckBox('Minimize to tray')
        self.check_box.hide()
        grid_layout.addWidget(self.check_box, 1, 0)
        #grid_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding), 2, 0)
        
        #place for file name
        self.handledFileLabel = QLabel("NA POCZATKU NIC", self)
        grid_layout.addWidget(self.handledFileLabel, 2, 0)
        
        self.keyword_textbox = QLineEdit(self)
        grid_layout.addWidget(self.keyword_textbox, 3, 0)
        
        self.ok_button = QPushButton("OK", self)
        grid_layout.addWidget(self.ok_button, 3, 1)
        self.ok_button.setDefault(True)
        self.ok_button.clicked.connect(self.buttonClicked) 
        
        #init QSystemTryIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        
        '''
            Define and add steps to work with the system tray icon
            show - show window
            hide - hide window
            exit - exit from application
        '''
        self.show_action = QAction("Show", self)
        self.quit_action = QAction("Exit", self)
        self.hide_action = QAction("Hide", self)
        self.show_action.triggered.connect(self.show)
        self.hide_action.triggered.connect(self.hide)
        self.quit_action.triggered.connect(qApp.quit)
        self.tray_menu = QMenu()
        self.tray_menu.addAction(self.show_action)
        self.tray_menu.addAction(self.hide_action)
        self.tray_menu.addAction(self.quit_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()
        
    # Override closeEvent, to intercept the window closing event
    # The window will be closed only if there is no check mark in the check box
    def closeEvent(self, event):
        #if self.check_box.isChecked():
        event.ignore()
        #self.hide()
        self.hide_action.trigger()
        self.tray_icon.showMessage(
            "Download Manager",
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            2000
        ) 
            
    #my methods
    
    def buttonClicked(self):
        print("Button has been clicked")
        key_words = self.keyword_textbox.text()
        moveHandledFile(self.handledFileLabel.text(), key_words)
        self.keyword_textbox.setText("")
        self.hide_action.trigger()
    
    def showApp(self, fileName):
        self.handledFileLabel.setText(fileName)
        self.show_action.trigger() 


            


    
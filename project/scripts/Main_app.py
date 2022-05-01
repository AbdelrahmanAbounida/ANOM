import random
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PySide2 import *

########################################################################
# IMPORT GUI FILE
from ui_app_nosidebar import *


########################################################################


class MainApp(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setGeometry(650, 450, 900, 900)

        ################### Figures ##########################
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.canvas.figure.add_subplot(111)

        ########################### Plotting Variables
        self.datafile_location = ''
        self.data = []
        self.headers = []
        self.colors = ['#ff7404', '#e53838', '#8ee000', '#f5df2e', '#f784b6', '#2dbe60', '#f9b949', '#ff0033',
                       '#00ff00', '#00d8ff', '#ffffff', '#2091eb', '#ff8200']
        ################### Remove window tittle bar ######################
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setIcon()

        ################### Set main background to transparent ###################
        self.setAttribute(Qt.WA_TranslucentBackground)

        ################### Shadow effect style ###################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        ################### Appy shadow to central widget ###################
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #################### Set window Icon ###################
        # This icon and title will not appear on our app main window because we removed the title bar
        self.setWindowIcon(QIcon(u"icons/analysis.png"))

        ################### Set window tittle ###################
        self.setWindowTitle("ANOM")

        ################### Minimize window ###################
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())

        ################### Close window ###################
        self.ui.out.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())

        ################### Restore/Maximize window ###################
        self.ui.expand.clicked.connect(lambda: self.restore_or_maximize_window())

        # Function to Move window on mouse drag event on the tittle bar
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################
            if self.isMaximized() == False:  # Not maximized
                # Move window only when window is normal size
                # ###############################################
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPosition().toPoint() - self.clickPosition)
                    self.clickPosition = e.globalPosition().toPoint()
                    e.accept()

        # Add click event/Mouse move event/drag event to the top header to move the window
        self.ui.ToolBar.mouseMoveEvent = moveWindow

        # Left Menu toggle button
        self.ui.open_close_side_bar.clicked.connect(lambda: self.slideLeftMenu())

        # Left Choices buttons
        # Home Button
        self.ui.home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        # Time Button
        self.ui.time_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.time_page))
        # Fourier Button
        self.ui.fourier_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fourier_page))
        # Compare Button
        self.ui.compare_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.compare_page))
        # upload button
        self.ui.upload_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.upload_page))

        # pages buttons
        self.ui.pushButton_3.clicked.connect(lambda: self.browse_files())

        # time domain buttons
        self.ui.jan_3.clicked.connect(lambda: self.plot_domain(2))
        self.createWindow()

    def gather_data(self):
        with open(self.datafile_location, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:
                    a = line.split(' ')
                    for j in a:
                        if j.strip() != '':
                            self.headers.append(j.strip())

                    continue

                a = line.split('  ')
                k = []
                for j in a:
                    if j.strip() != '':
                        k.append(j.strip())

                k = [float(m) for m in k]
                self.data.append(k)

    ###############################################################
    # plot domains
    ###############################################################
    def plot_domain(self, month=1, domain='time'):
        self.gather_data()
        df = pd.DataFrame(self.data, columns=self.headers)

        x = np.linspace(1950, 2010, 68)
        if domain == 'time':
            y = df.loc[df['MON'] == month, ['ANOM']]
            title = "ANOM Time Domain"
        else:
            y = []
            title = "ANOM Fourier Domain"

        '''ax = plt.axes()
        plt.title(title, fontsize=17)
        plt.ylabel("ANOM DATA", fontsize=13)'''

        if month == 1:
            plt.xlabel("January", fontsize=13)
        elif month == 2:
            plt.xlabel("February", fontsize=13)
        elif month == 3:
            plt.xlabel("March", fontsize=13)
        elif month == 4:
            plt.xlabel("April", fontsize=13)
        elif month == 5:
            plt.xlabel("Mai", fontsize=13)
        elif month == 6:
            plt.xlabel("June", fontsize=13)
        elif month == 7:
            plt.xlabel("July", fontsize=13)
        elif month == 8:
            plt.xlabel("August", fontsize=13)
        elif month == 9:
            plt.xlabel("September", fontsize=13)
        elif month == 10:
            plt.xlabel("October", fontsize=13)
        elif month == 11:
            plt.xlabel("November", fontsize=13)
        elif month == 12:
            plt.xlabel("December", fontsize=13)


        index = random.randint(0,len(self.colors)-1)
        color = self.colors[index]
        self.ui.time_graph.addWidget(self.canvas)
        # self.figure.set_facecolor('#384d54')
        self.canvas.axes.clear()
        self.canvas.axes.plot(x, y)
        # self.canvas.axes.legend((),loc='upper right')
        self.canvas.axes.set_title(title, fontsize=18)
        plt.plot(x, y, color)
        self.canvas.draw()
        plt.show()



    def draw_canvase(self,x,y,title):
        self.ui.time_graph.addWidget(self.canvas)
        #self.figure.set_facecolor('#384d54')
        self.canvas.axes.clear()
        self.canvas.axes.plot(x,y)
        #self.canvas.axes.legend((),loc='upper right')
        self.canvas.axes.set_title(title, fontsize=18)
        self.canvas.draw()

    ###############################################################
    # upload file
    ###############################################################
    def browse_files(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',
                                            "Excel files (*.csv *.xls *.xls), Text files (* .txt)")
        self.datafile_location = fname[0]
        self.ui.file_name.setText(fname[0])

    ###############################################################
    # Update restore button icon on msximizing or minimizing window
    ###############################################################
    def restore_or_maximize_window(self):
        # If window is maxmized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.expand.setIcon(QIcon(u"icons/assets/expand-arrows-free-icon-font.svg"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.expand.setIcon(QIcon(u"icons/minimize.png"))

    ########################################################################
    # Slide left menu function
    ########################################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.left_body.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 210
            self.ui.open_close_side_bar.setIcon(QIcon(u"icons/left-arrow.png"))
            self.ui.sidebar_icon.setMaximumWidth(190)
            self.ui.open_close_side_bar.setMaximumWidth(100)
            self.ui.logo_name.setMaximumWidth(100)
            self.ui.Logo.setMaximumWidth(90)

        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.logo_name.setMaximumWidth(0)
            self.ui.Logo.setMaximumWidth(0)
            self.ui.open_close_side_bar.setIcon(QIcon(u"icons/align-justify-free-icon-font.png"))
            self.ui.sidebar_icon.setMaximumWidth(40)

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.left_body, b"maximumWidth")  # Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    ########################################################################
    # show window
    ########################################################################
    def createWindow(self):
        self.show()
        sys.exit(self.app.exec())

    ########################################################################
    # set the application icon
    ########################################################################
    def setIcon(self):
        icon = QIcon('increasing.png')
        icon.addFile('../assets/increasing.png')
        self.setWindowIcon(icon)

    #######################################################################
    # Add mouse events to the window
    #######################################################################
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPosition().toPoint()
        # We will use this value to move the window


if __name__ == '__main__':
    app = MainApp()

    # app.geometry().center()

import sys
import serial.tools.list_ports
import serial
from PyQt5 import QtWidgets
import GUI_design_ver1 as ui  # Import the generated UI file
from Dark import *
from Light import *
from GUI_design_ver1 import Ui_MainWindow


######################################################################################################
########################################## Global Variables ##########################################

RobotPorts = 0
RobotCom = 0
Robot = 0
RobotState = 0
Prev_Connection_State = 0
GUI = 0
Joints = {'J1':0,'J2':0,'J3':0,'J4':0,'J5':0,'J6':0}
JointsLimits = {'J1':[-165,165],'J2':[-130,74],'J3':[-165,37.5],'J4':[-155,155],'J5':[-115,115],'J6':[-360,360]}
Cart = {'X':300,'Y':0,'Z':500,'A':0,'B':180,'C':0}
PrevCart = {'X':0,'Y':0,'Z':0,'A':0,'B':180,'C':0}
Stop = 0
InAction = 0
Busy = 0
Pause = 0
File = []
Fname = ''
FileExist = 0
Size = 0
FileRunning = 0
Reset = 0
Ports = []
######################################################################################################
########################################## Global Variables ##########################################
def FindSerial():
    global RobotCom
    global RobotPorts
    global Robot
    global Ports
    global RobotState
    TempList = []
    ComsList = []

    RobotPorts = [
        p
        for p in serial.tools.list_ports.comports()
    ]
    if len(RobotPorts) > 0:
        Ports = [
            p.device
            for p in RobotPorts
        ]
    else:
        try:
            Robot.close()
            Robot = 0
            # RobotState = 0
        except:
            pass

    for port in RobotPorts:
        ComsList.append(port.description)

    if not RobotPorts:
        TempList = []
        GUI.ComsMenu.clear()

        return False

    if len(RobotPorts) >= 1:

        for port in RobotPorts:
            if -1 == GUI.ComsMenu.findText(port.description):
                GUI.ComsMenu.addItem(port.description)
            # print(port.device)

        for j in range(GUI.ComsMenu.count()):
            if GUI.ComsMenu.itemText(j) not in ComsList:
                GUI.ComsMenu.removeItem(j)
    try:
        if (Robot.port not in Ports) or (len(Ports) == 0):
            Robot.close()
            Robot = 0
    except:
        pass

    try:
        RobotCom = RobotPorts[ComsList.index(GUI.ComsMenu.currentText())]
    except:
        pass

    return True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    GUI = ui.Ui_MainWindow()
    GUI.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
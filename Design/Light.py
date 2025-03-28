def Light_Mode(self, MainWindow):
    
    MainWindow.setStyleSheet("QTabBar::tab {\n"
"    border: 3px solid #1d282b;\n"
"    border-radius: 10px;\n"
"    margin: 5;\n"
"    padding: 5;\n"
"    font: bold; \n"
"    font-family: arial;\n"
"    font-size: 20px;\n"
"    color: #1d282b;\n"
"    width: 100px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"    background: #f1f1ed;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: rgba(72, 72, 72, 0.4);\n"
"\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background: #1d282b;\n"
"    color: #e7e7e7\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 0px solid #1d282b;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 5px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right:0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 0px;\n"
"}\n"
"QWidget{\n"
"    border: 0px solid #1d282b;\n"
"    background: transparent;\n"
"    color: #1d282b;\n"
"}\n"
"QFrame#frame_1,#frame_2,#frame_3,#frame_4{\n"
"    border: 3px solid #1d282b;\n"
"    border-radius : 20px;\n"
"    font: bold; \n"
"    font-family: arial;\n"
"    font-size: 30px;\n"
"    color: #1d282b;\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    border: 5px solid #f69322;\n"
"    background-color: #1d282b;\n"
"    font-family: arial;\n"
"    font-size: 30px;\n"
"    font: bold;\n"
"    color: #e7e7e7;\n"
"    border-radius: 15%;\n"
"}\n"
"QPushButton#main_connect{\n"
"    border: 5px solid #f69322;\n"
"    background-color: #1d282b;\n"
"    font-family: arial;\n"
"    font-size: 30px;\n"
"    font: bold;\n"
"    color: #e7e7e7;\n"
"    border-radius: 15%;\n"
"    min-width: 120px;\n"
"    min-height: 30px;\n"
"    max-width: 150px;\n"
"    max-height: 35px;\n"
"}\n"
"QPushButton:hover#main_connect{\n"
"     background-color:#c67a00;\n"
"}\n"
"\n"
"QPushButton:pressed#main_connect{\n"
"     background-color: #ffba43;\n"
"}\n"
"\n"
"QPushButton#Set_velocity_button{\n"
"    border: 5px solid #f69322;\n"
"    background-color: #1d282b;\n"
"    font-family: arial;\n"
"    font-size: 30px;\n"
"    font: bold;\n"
"    color: #e7e7e7;\n"
"    border-radius: 15%;\n"
"    min-width: 150px;\n"
"    min-height: 30px;\n"
"    max-width: 150px;\n"
"    max-height: 35px;\n"
"}\n"
"QPushButton:hover#Set_velocity_button{\n"
"     background-color:#c67a00;\n"
"}\n"
"\n"
"QPushButton:pressed#Set_velocity_button{\n"
"     background-color: #ffba43;\n"
"}\n"
"QPushButton#Offline_indecator{\n"
"    border: 5px solid #de4041;\n"
"    background-color: #de4041;\n"
"    font-family: arial;\n"
"    font-size: 30px;\n"
"    font: bold;\n"
"    color: #e7e7e7;\n"
"    border-radius: 15%;\n"
"}\n"
"QPushButton:hover{\n"
"     background-color:#c67a00;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"     background-color: #ffba43;\n"
"}\n"
"QComboBox{\n"
"    border: 2px solid #1d282b;\n"
"    border-radius: 8px;\n"
"    color: #1d282b;\n"
"    font: bold;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"\n"
"QLabel#ComsLabel,#Speed_ratioLabel_2,#ComsLabel_3{\n"
"    margin: 5px;\n"
"    font: bold; \n"
"    font-family: arial;\n"
"    font-size: 22px;\n"
"    border: 3px solid #1d282b;\n"
"    background: #1d282b;\n"
"    color: #e7e7e7;\n"
"    border-radius: 10px;\n"
"    padding: 7px;\n"
"    padding-left: 17px;\n"
"    padding-right: 17px;\n"
"}\n"
"QLabel#ComsLabel{\n"
"    margin: 5px;\n"
"    font: bold; \n"
"    font-family: arial;\n"
"    font-size: 22px;\n"
"    border: 3px solid #1d282b;\n"
"    background: #1d282b;\n"
"    color: #e7e7e7;\n"
"    border-radius: 10px;\n"
"    padding: 7px;\n"
"    padding-left: 17px;\n"
"    padding-right: 17px;\n"
"    min-width: 120px;\n"
"    min-height: 30px;\n"
"    max-width: 120px;\n"
"    max-height: 30px;\n"
"\n"
"}\n"
"QLabel#label_Logo{\n"
"    font: bold; \n"
"    font-family: arial;\n"
"    font-size: 22px;\n"
"    border: 3px solid #1d282b;\n"
"   \n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"QLabel#speed_percentages{\n"
"\n"
"    font: bold; \n"
"    font-family: arial;\n"
"    font-size: 45px;\n"
"color = #1d282b\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 3px;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"    background-color: #1d282b;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color:#f69322;\n"
"    border: none;\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    margin: -20px 0;\n"
"    border-radius: 10px;\n"
"    padding: -20px 0px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #c67a00;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #ffba43;\n"
"}\n"
"QSlider\n"
"{\n"
"   min-width:550px;\n"
"    min-height: 60px;\n"
"    max-width: 120px;\n"
"    max-height: 70px;\n"
"\n"
"}\n"
"QSpinBox{\n"
"    border: 0px solid #1d282b;\n"
"    background: transparent;\n"
"    padding: 3px;\n"
"    border-radius : 5px;\n"
"     font-family: arial;\n"
"    font-size: 30px;\n"
"    font: bold;\n"
"    color: #1d282b;\n"
"}\n"
"QPushButton#Stop_button{\n"
"    border: 5px solid #de4041;\n"
"    background-color: #1d282b;\n"
"    font-family: arial;\n"
"    font-size: 30px;\n"
"    font: bold;\n"
"    color: #e7e7e7;\n"
"    border-radius: 15%;\n"
"}\n"
"QPushButton:hover#Stop_button{\n"
"     background-color:#b03030;\n"
"}\n"
"\n"
"QPushButton:pressed#Stop_button{\n"
"     background-color: #ff8e8a;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QRadioButton{\n"
"    border: 0px solid #1d282b;\n"
"    margin: 5px;\n"
"    width: 35px;\n"
"    border-radius: 18px;\n"
"    background-color: #1d282b;\n"
"}\n"
"\n"
"\n"
"QRadioButton:unchecked {\n"
"   background-color: rgba(246, 147, 34, 0.6);\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"    width: 36px;\n"
"   height: 36px;\n"
"   border-radius: 18px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"    background-color: #f69322;\n"
"    margin-left: 0px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  background-color: #c67a00;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed\n"
"{\n"
"     background-color: #ffba43;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked \n"
"{\n"
"  background-color: #f69322;\n"
"   margin-left: 50px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover \n"
"{\n"
"   background-color: #c67a00;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed \n"
"{\n"
"    background-color: #ffba43;\n"
"}\n"
"\n"
"QLabel#DarkModeLabel{\n"
"    border: 0px solid #1d282b;\n"
"    border-radius : 20px;\n"
"    font: bold; \n"
"    font-family: arial;\n"
"    font-size: 22px;\n"
"    background-color: transparent;\n"
"    color: #1d282b;\n"
"    margin: 0px 0px 0px 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

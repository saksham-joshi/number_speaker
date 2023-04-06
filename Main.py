from PyQt5.QtWidgets import QApplication , QWidget , QLineEdit , QTextEdit , QPushButton , QRadioButton
from PyQt5.QtGui import QIcon , QFont
from sys import exit,argv
from winsound import PlaySound,SND_FILENAME

class speak_number :

    def __str__(self) :
        return self.fin[1:].capitalize();
    
    def __input_checker(self,b : str) -> bool :
        a = b
        if a[0] == '-' :
            a = a[1:]
        point_count=0
        for i in a :
            if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0' :
                continue
            elif i=='.' :
                if point_count == 1 :
                    return True
                point_count+=1
            else :
                return True
        return False

    def __init__(self , a : str) :
        if self.__input_checker(a) :
            self.fin=" Wrong or Invalid Input (only integer or decimal are allowed)"
            return
        self.fin = ""
        self.before = 0
        self.after = 0
        try :
            if a[0] =='-' :
                self.fin = self.fin +' minus'
                a = a[1:]
        except :
            pass
        try :
            self.before = int(a)
            if a.__len__() > 6 :
                self.fin=" Unsupported for more than or equal to 1 million and less than -1 million."
            self.__before_decimal(a)
        except :
            if a[:a.find('.')].__len__() > 6 :
                self.fin= " Unsupported for more than or equal to 1 million and less than -1 million."
                return
            self.__before_decimal(a[:a.find('.')])
            after = str(float(a))
            self.__after_decimal(after[after.find('.'):])      
    
    
    def __before_decimal(self,a : str) :
        int_num = int(float(a))
        if int_num <=99:
            self.__double_words(str(int_num))
        elif int_num >=100 and int_num <=999 :
            self.fin = self.fin + self.__single_words(int(a[0])) + ' hundred'
            self.__before_decimal(str(int(a[1:])))
        elif int_num >=1000 and int_num <=9999 :
            self.fin = self.fin + self.__single_words(int(a[0])) + ' thousand'
            self.__before_decimal(str(int(a[1:])))
        elif int_num>=10000 and int_num<=99999 :
            self.__double_words(a[:2])
            self.fin = self.fin + ' thousand'
            self.__before_decimal(a[2:])
        elif int_num >=100000 and int_num <=999999 :
            self.__before_decimal(a[0:3])
            self.fin = self.fin + ' thousand'
            self.__before_decimal(str(int(a[3:])))
    
    def __after_decimal(self,a : str) :
        for i in a:
            if i == '.' :
                self.fin = self.fin + ' point'
                continue
            self.fin = self.fin + self.__single_words(int(i))
    
    
    def __double_words(self, a : str) :
        if int(a) == 0 :
            return
        st = self.__single_words(int(a))
        if st.__len__() == 0 :
            if int(a)>20 and a[1] != '0' :
                self.fin = self.fin + self.__single_words(int(str(a[0] + '0'))) + self.__single_words(int(a[1]))
        else :
            self.fin = self.fin + st

    def __single_words(self,a : int) -> str :
        match(a) :
            case 0 : return ' zero'

            case 1 : return ' one'

            case 2 : return ' two'

            case 3 : return ' three'

            case 4 : return ' four'

            case 5 : return ' five'

            case 6 : return ' six'

            case 7 : return ' seven'

            case 8 : return ' eight'

            case 9 : return ' nine'

            case 10 : return ' ten'

            case 11 : return ' eleven'

            case 12 : return ' twelve'

            case 13 : return ' thirteen'

            case 14 : return ' fourteen'

            case 15 : return ' fivteen'

            case 16 : return ' sixteen'

            case 17 : return ' seventeen'

            case 18 : return ' eighteen'

            case 19 : return ' nineteen'

            case 20 : return ' twenty'

            case 30 : return ' thirty'

            case 40 : return ' fourty'

            case 50 : return ' fifty'

            case 60 : return ' sixty'

            case 70 : return ' seventy'

            case 80 : return ' eighty'

            case 90 : return ' ninety'

            case 100 : return ' hundred'

            case 1000 : return ' thousand'

        return ""
    
    def speaker(self , gender : str) :
        lst = self.fin[1:].split(" ")
        if lst[0] == 'Wrong' :
            PlaySound('wrong_input_audio'+gender,SND_FILENAME)
            return
        elif lst[0] =='Unsupported' :
            PlaySound('unsupported_audio'+gender,SND_FILENAME)
            return
        for i in range(lst.__len__()) :
            st = lst[i]+gender
            PlaySound(st,SND_FILENAME)
        

class main () :
    font_ackn = QFont("Acknowledgement",10)
    def __init__(this) :
        this.app = QApplication(argv)
        this.widget = QWidget()
        this.widget.setWindowTitle("Number Speaker")
        this.widget.setWindowIcon(QIcon("icon.png"))
        this.widget.setFixedWidth(500)
        this.widget.setFixedHeight(250)
        this.widget.setStyleSheet("background-color:rgb(37, 150, 190)")

        this.inputbox = QLineEdit(this.widget)
        this.inputbox.setPlaceholderText("Enter the number . . . .")
        this.inputbox.setFont(this.font_ackn)
        this.inputbox.setGeometry(10,10,400,40)
        this.inputbox.setStyleSheet("background-color:rgb(231, 253, 255)")
        this.inputbox.returnPressed.connect(this.__return_pressed)

        this.enterbutton = QPushButton(this.widget)
        this.enterbutton.setText(">")
        this.enterbutton.setFont(this.font_ackn)
        this.enterbutton.setGeometry(420,10,70,40)
        this.enterbutton.setStyleSheet("background-color:rgb(214,234,238)")
        this.enterbutton.clicked.connect(this.__enter_button_clicked)
        this.enterbutton.setEnabled(True)

        this.outputbox = QTextEdit(this.widget)
        this.outputbox.setPlaceholderText("Output will be shown here . . . .")
        this.outputbox.setFont(this.font_ackn)
        this.outputbox.setGeometry(10,70,480,80)
        this.outputbox.setStyleSheet("background-color:rgb(231, 253, 255)")
        this.outputbox.setEnabled(False)

        this.play = QPushButton(this.widget)
        this.play.setIcon(QIcon("icon.png"))
        this.play.setFont(QFont('Impact',10))
        this.play.setText(" : Play")
        this.play.setGeometry(120,180,120,50)
        this.play.setStyleSheet("background-color:rgb(214,234,238)")
        this.play.clicked.connect(this.__play_button_clicked)        
        
        this.radiomale = QRadioButton(this.widget)
        this.radiomale.setText("Male")
        this.radiomale.setFont(QFont('sans-serif',pointSize= 10,weight=87))
        this.radiomale.setGeometry(270,170,120,50)
        this.radiomale.setStyleSheet("background-color:rgba(0,0,0,0)")
        this.radiomale.show()

        this.radiofemale = QRadioButton(this.widget)
        this.radiofemale.setText("Female")
        this.radiofemale.setFont(this.radiomale.font())
        this.radiofemale.setGeometry(270,195,120,50)
        this.radiofemale.setStyleSheet("background-color:rgba(0,0,0,0)")
        this.radiofemale.setChecked(True)
        this.radiofemale.show()

        this.widget.show()
        exit(this.app.exec_())
    
    def __return_pressed(this) :
        this.__enter_button_clicked()
        this.__play_button_clicked()

    def __enter_button_clicked(this) :
        st = this.inputbox.text()
        if len(st) != 0 :
            this.obj = speak_number(st)
            this.outputbox.setText(this.obj.__str__())
    
    def __play_button_clicked(this) :
        try :
            if this.radiofemale.isChecked() :
                this.obj.speaker("_female.wav")
            else :
                this.obj.speaker("_male.wav")
        except :
            pass       
main()
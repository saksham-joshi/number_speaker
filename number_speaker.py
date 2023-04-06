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
        if a[0] =='-' :
                self.fin = self.fin +' minus'
                a = a[1:]
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
    
    def speaker(self) :
        for i in self.fin[1:].split(" ") :
            if i == 'Wrong' :
                PlaySound('wrong_input_audio.wav',SND_FILENAME)
                break;
            elif i=='Unsupported' :
                PlaySound('unsupported_audio.wav',SND_FILENAME)
                break
            else :
                st = i+'.wav'
                PlaySound(st,SND_FILENAME)


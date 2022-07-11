class Terminal:
    balance = 0
    def __init__(self, number, pin):
        if len(str(number)) == 16 and len(str(pin)) == 4:
            self.__number = number
            self.__pin = pin
        else:
            raise Exception('Введите верные данные!')
    
    def put(self, __pin, sum):
        if self.__pin == __pin:
            self.balance += sum

    def get_money(self, __pin, sum_get):
        if self.__pin == __pin:
            if sum_get % 10 == 0 and self.balance>=sum_get:
                self.balance -= sum_get
            else:
                raise Exception('Введите округленную сумму!')
        else:
            raise Exception('Введите верный пин-код!')

card1 = Terminal(1234567812341678, 1224)
card1.put(1224, 1000)
card1.get_money(1224, 500)
print(card1.balance)
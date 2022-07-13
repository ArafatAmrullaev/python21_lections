
""" Task №1 """
# class Smarphone:
#     def call(self, number):
#         return f'Звоню на номер {number}'
#     def where_to_wear(self):
#         print('You can keep me anywhere')

# class Watch:
#     def see_time(self):
#         import time
#         n = time.localtime()
#         current_time = time.strftime('%H:%M:%S', n)
#         return f'Время сейчас: {current_time}'
#     def where_to_wear(self):
#         print('You should wear me on your hand')
# class Smartwatch(Watch, Smarphone):
#     ...

# obj = Smartwatch()
# print(obj.call('+996700700700'))
# print(obj.see_time())
# obj.where_to_wear()

#==========================================================================

""" Task №2 """
class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def post_post(self, username, password):
        self.username = username
        self.password = password
        Soc.valid(self)


class TikTok:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def post_post(self, username, password):
        print('Succesfully created')

class Soc(Instagram):
    def valid(self):
        if self.password == self.password and self.username == self.username:
            print('Succesfully created')

pers = Instagram('arafat',1234)
pers.post_post('arafat', 1234)

""" Task №1 """
class Smartphone:
    def call(self, number):
        return f'Звоню на номер {number}'
    def where_to_wear(self):
        print('You can keep me anywhere')

class Watch:
    def see_time(self):
        import time
        n = time.localtime()
        current_time = time.strftime('%H:%M:%S', n)
        return f'Время сейчас: {current_time}'
    def where_to_wear(self):
        print('You should wear me on your hand')
class Smartwatch(Watch, Smartphone):
    ...

obj = Smartwatch()
print(obj.call('+996700700700'))
print(obj.see_time())
obj.where_to_wear()

#==========================================================================

""" Task №2 """
class Instagram:
    posts = 0
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def post_post(self,title, username, password):
        self.nn = username
        self.pp = password
        Soc.valid(self)
        self.posts += 1


class TikTok:
    videos = 0
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def post_video(self, title, username, password):
        self.nn = username
        self.pp = password
        Soc.valid(self)
        self.videos += 1

class Soc(Instagram, TikTok):
    def valid(self):
        if self.password == self.pp and self.username == self.nn:
            print('Succesfully created')
        else:
            raise Exception('Неверный пароль или логин!')

pers = TikTok('arafat',1234)
pers2 = TikTok('arafat2', '4321')
pers2.post_video('title', 'arafat2', '4321')
pers3 = Instagram('qwerty', 'qwerty')
pers.post_video('title','arafat', 1234)
pers.post_video('title','arafat', 1234)
pers.post_video('title','arafat', 1234)
pers.post_video('title','arafat', 1234)
pers3.post_post('title', 'qwerty', 'qwerty')
pers3.post_post('title', 'qwerty', 'qwerty')
pers3.post_post('title', 'qwerty', 'qwerty')
pers3.post_post('title', 'qwerty', 'qwerty')

print(pers.videos)
print(pers3.posts)
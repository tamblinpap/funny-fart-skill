from mycroft import MycroftSkill, intent_file_handler


class FunnyFart(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fart.funny.intent')
    def handle_fart_funny(self, message):
        self.speak_dialog('fart.funny')


def create_skill():
    return FunnyFart()


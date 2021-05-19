from mycroft import MycroftSkill, intent_file_handler


class Alcoolemgel(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('alcoolemgel.intent')
    def handle_alcoolemgel(self, message):
        self.speak_dialog('alcoolemgel')


def create_skill():
    return Alcoolemgel()


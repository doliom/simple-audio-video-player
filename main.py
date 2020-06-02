import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.audio import SoundLoader
from kivy.uix.actionbar import ActionBar
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton

class ScreenThree(Screen):
    def test_on_enter(self, audname):
        self.sound = SoundLoader.load(audname)
        self.sound.play()

    def on_play(self):
        self.sound.play()

    def on_stop(self):
        self.sound.stop()

    def on_leave(self):
        pass

    def onBackBtn(self):
        self.sound.stop()
        self.manager.current = self.manager.list_of_prev_screens.pop()


class ScreenTwo(Screen):
    def test_on_enter(self, vidname):
        self.vid = VideoPlayer(source=vidname, state='play',
                               options={'allow_stretch':False,
                                        'eos': 'loop'})
        self.add_widget(self.vid)

    def on_leave(self):
        pass

    def onBackBtn(self):
        self.vid.state = 'stop'
        self.remove_widget(self.vid)
        self.manager.current = self.manager.list_of_prev_screens.pop()

class ScreenOne(Screen):
    def onNextScreen(self, btn, fileName):
        self.manager.list_of_prev_screens.append(btn.parent.name)
        self.manager.current = 'screen2'
        self.manager.screen_two.test_on_enter('Resources/Videos/' + fileName +'.mp4')

    def onNextScreenAudio(self, btn, fileName):
        self.manager.list_of_prev_screens.append(btn.parent.name)
        self.manager.current = 'screen3'
        self.manager.screen_three.test_on_enter('Resources/Audios/' + fileName +'.wav')

class Manager(ScreenManager):
    transition = NoTransition()
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)
    screen_four = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)
        self.list_of_prev_screens = []

class ScreensApp(App):
    def build(self):
        return Manager()

if __name__ == "__main__":
    ScreensApp().run()
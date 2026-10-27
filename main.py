from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class WorldWarGame(App):
    def build(self):
        self.money = 100000
        self.army = 1000

        layout = BoxLayout(orientation="vertical")

        self.info = Label(
            text="WORLD WAR IRAN\nMoney: 100000\nArmy: 1000"
        )
        layout.add_widget(self.info)

        attack = Button(text="ATTACK")
        attack.bind(on_press=self.attack)
        layout.add_widget(attack)

        recruit = Button(text="RECRUIT ARMY")
        recruit.bind(on_press=self.recruit)
        layout.add_widget(recruit)

        return layout

    def attack(self, instance):
        if self.army >= 100:
            self.army -= 100
            self.money += 5000
        self.update_info()

    def recruit(self, instance):
        if self.money >= 1000:
            self.money -= 1000
            self.army += 100
        self.update_info()

    def update_info(self):
        self.info.text = (
            f"WORLD WAR IRAN\n"
            f"Money: {self.money}\n"
            f"Army: {self.army}"
        )

WorldWarGame().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from face_recognizer import log_in
from face_taker import face_signup
from face_train import face_train

from kivy.uix.textinput import TextInput

class LoginSignUpApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_id = 1  # Initialize the current ID to 1

    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create the "Log In" button
        login_button = Button(text="Log In", size_hint=(None, None), size=(200, 50))
        login_button.bind(on_press=self.login_pressed)

        # Create the "Sign Up" button
        signup_button = Button(text="Sign Up", size_hint=(None, None), size=(200, 50))
        signup_button.bind(on_press=self.signup_pressed)

        # Create a TextInput for the user's name
        self.username_input = TextInput(
            hint_text="Enter your name",
            multiline=False,
            size_hint=(None, None),
            size=(200, 50)
        )

        layout.add_widget(self.username_input)
        layout.add_widget(signup_button)
        layout.add_widget(login_button)

        return layout

    def login_pressed(self, instance):
        log_in()

    def signup_pressed(self, instance):
        user_name = self.username_input.text
        id = self.current_id  # Get the current ID
        self.current_id += 1  # Increment the current ID

        face_signup(id, user_name)
        face_train()
        print(f"Sign Up Successful! Welcome: {user_name}")

if __name__ == '__main__':
    LoginSignUpApp().run()

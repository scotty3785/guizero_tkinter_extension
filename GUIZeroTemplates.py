"""
GUI Zero extension for Tkinter
"""
import re
from idlelib.configHandler import idleConf

class GUIZeroTemplates:

    menudefs = [
        ('format', [
            None,
            ('Insert GUIZero PushButton', '<<add_guizero_button>>'),
            ('Insert GUIZero Text', '<<add_guizero_text>>'),
         ])
    ]

    def __init__(self, editwin):
        self.editwin = editwin
        print("Enabled GUI Zero")

    def close(self):
        self.editwin = None

    def add_guizero_button_event(self, event, limit=None):
        """
        Add code template for a GUIZero pushbutton
        """
        text = self.editwin.text
        first, last = self.editwin.get_selection_indices()

        text.insert("insert","button = PushButton(app, text='myNewButton')")
        
        return "break"
    
    def add_guizero_text_event(self, event, limit=None):
        """
        Add code template for a GUIZero text (label)
        """
        text = self.editwin.text
        first, last = self.editwin.get_selection_indices()

        text.insert("insert","text = Text(app, text='Hello World')")
        
        return "break"


if __name__ == "__main__":
    ## TODO Add Unit test.
    pass

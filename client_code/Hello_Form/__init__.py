from ._anvil_designer import Hello_FormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Hello_Form(Hello_FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def hello_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name_box.text
    
    self.message_label.text = "Hello, " + name + '!'
    # make a call to the server procedure
    anvil.server.call('say_hello', name)

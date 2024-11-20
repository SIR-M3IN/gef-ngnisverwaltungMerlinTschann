from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    x = self.gefaengnisse_drop_down.selected_value
    gefängnisID = anvil.server.call('def_gefängnis', x)
    gefängnisID = int(gefängnisID[0])
    # anvil.server.call('get_direktor', gefängnisID)
    self.label_direktor.text = anvil.server.call('get_direktor', gefängnisID)[0]
    # self.label_direktor.text = anvil.server.call('get_direktor')
    self.label_freie_zellen.text = anvil.server.call('get_freieZellen', 1)[0]
    self.repeating_zellen.items = [{'zellennummer': anvil.server.call('get_zellennummer', 0), 'anzahl_häftlinge': 'TODO'}, 
                                   {'zellennummer': anvil.server.call('get_zellennummer', 1), 'anzahl_häftlinge': 'TODO'}]

  def gefaengnisse_drop_down_change(self, **event_args):
    x = self.gefaengnisse_drop_down.selected_value
    gefängnisID = anvil.server.call('def_gefängnis', x)
    gefängnisID = int(gefängnisID[0])
    # anvil.server.call('get_direktor', gefängnisID)
    self.label_direktor.text = anvil.server.call('get_direktor', gefängnisID)[0]


 



  
 

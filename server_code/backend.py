import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3


@anvil.server.callable
def get_gefaengnisse():
    conn = sqlite3.connect(data_files["prison_management.db"])
    cursor = conn.cursor()
    res = [(f"{row[0]}") for row in cursor.execute("SELECT CAST(Name AS TEXT) FROM Gefängnis")]
    print(res)
    
    return res

@anvil.server.callable
def get_direktor(gefängnisID):
    conn = sqlite3.connect(data_files["prison_management.db"])
    cursor = conn.cursor()
    res = [(f"{row[0]}") for row in cursor.execute(f"SELECT CAST(Direktor AS TEXT) FROM Verwaltung WHERE GID IS {gefängnisID}")]
    
    print(res)
    
    return res
@anvil.server.callable
def def_gefängnis(x):
    conn = sqlite3.connect(data_files["prison_management.db"])
    cursor = conn.cursor()
    print(f"x = {x}")
    res = [(f"{row[0]}") for row in cursor.execute(f"SELECT GID FROM Gefängnis WHERE Name IS '{x}'")]
    print(res)
    
    return res
@anvil.server.callable
def get_freieZellen(x):
    conn = sqlite3.connect(data_files["prison_management.db"])
    cursor = conn.cursor()
    res = [(f"{row[0]}") for row in cursor.execute(f"SELECT CAST(AnzahlFreierBetten AS TEXT) FROM Verwaltung WHERE VID IS {x}")]
    
    print(res)
    
    return res
  
@anvil.server.callable
def get_zellennummer(wzelle):
    conn = sqlite3.connect(data_files["prison_management.db"])
    cursor = conn.cursor()
    print(wzelle)
    res = [(f"{row[0]}") for row in cursor.execute("SELECT CAST(ZID AS TEXT) FROM Zelle")]
  
    print(f"{res}")
    
    return res
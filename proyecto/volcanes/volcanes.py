##########################################
# 
# Copyright 2013 José Lorenzo Herrero Rico
# 
# Volcanes, aplicación para saber los cinco Volcanes mas altos de la tierra en la actualidad.
# 
# Es software libre y se distribuye bajo una licencia Affero (AFFERO GENERAL PUBLIC LICENSE: http://www.affero.org/oagpl.html).
# 
# This program is free software and it's licensed under the AFFERO GENERAL PUBLIC LICENSE (http://www.affero.org/oagpl.html).
# 
##########################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys

"""Utilizamos el metodo para conectar el par señal (evento) con funcion asociada (callback)
con el diccionario de variables handlers, idetificador la señal y valor la función"""
class GUI:
    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("volcanes.glade")
        self.handlers = {"onDeleteWindow": Gtk.main_quit}
        
        self.builder.connect_signals(self.handlers)
    
        self.window = self.builder.get_object("window1")

        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()
       

    def destroy(self,window):
        Gtk.main_quit()
        
   



def main():
            
    app = GUI()
    Gtk.main()


if __name__ == "__main__":
    sys.exit(main())

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

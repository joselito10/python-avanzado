from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys

"""Utilizamos el metodo para conectar el par sennal (evento) con funcion asociada (callback)
con el diccionario de variables handlers, idetificador la sennal y valor la funcion"""
class GUI:
    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("crud.glade")
        self.handlers = {"onDeleteWindow": Gtk.main_quit,
                        "onButtonPressed": self.onButtonPressed,
                        "onAboutDialog": self.onAboutDialog,
                        "onCloseAbout": self.onCloseAbout,
                        "pintar": self.pintar,
                        }
        
        self.builder.connect_signals(self.handlers)
    
        self.window = self.builder.get_object("window1")

        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()
        self.label1 = self.builder.get_object("label1")
        self.label1.hide()
        self.entry1 = self.builder.get_object("entry1")
        self.entry1.hide()

    def onAboutDialog(self, *args):
        self.about = self.builder.get_object("aboutdialog1")
        self.about.show_all()

    def destroy(self,window):
        Gtk.main_quit()
        
    def pintar(self,button):
        self.label1.show()
        self.entry1.show()
        print "Pintar"

    def onButtonPressed(self,button):
        #windows = self.builder.get_object("aboutdialog1")
        #windows.show_all()
        print "hola mundo"

    def onCloseAbout(self, *args):
        self.about = self.builder.get_object("aboutdialog1")
        self.about.hide()

def main():
            
    app = GUI()
    Gtk.main()


if __name__ == "__main__":
    sys.exit(main())

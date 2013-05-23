from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys


class GUI:
  def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file("crud.glade")
		self.handlers = {"onDeleteWindow": Gtk.main_quit,
						#"onButtonPressed": self.onButtonPressed,
						"onAboutDialog": self.onAboutDialog,
						"onCloseAbout": self.onCloseAbout
						}
        
		self.builder.connect_signals(self.handlers)
		
		self.window = self.builder.get_object("window1")

		self.window.connect("delete-event", Gtk.main_quit)
		self.window.show_all()

	
	def onAboutDialog(self, *args):
		self.about = self.builder.get_object("aboutdialog1")
		self.about.show_all()
	
	def destroy(self,window):
		Gtk.main_quit()
	
	#def onButtonPressed(self,button):
		#windows = self.builder.get_object("aboutdialog1")
		#windows.show_all()
		
	def onCloseAbout(self, *args):
		self.about = self.builder.get_object("aboutdialog1")
		self.about.hide()

def main():
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
    sys.exit(main())

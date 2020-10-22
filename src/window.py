# window.py
#
# Copyright 2020 Muhammad Rivan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, GLib

from .content import MonocotsContent
import time

@Gtk.Template(resource_path='/org/example/App/window.ui')
class MonocotsWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MonocotsWindow'
    
    ovl_main = Gtk.Template.Child()
    frm_splash = Gtk.Template.Child()
    img_splash = Gtk.Template.Child()
    
    content = None
    
    subapp = ""
    subapp_icon = ""
    subapp_name = ""
    subapp_file_name = ""
    show_mb = False

    def __init__(self, subapp, show_mb, win_size, **kwargs):
        super().__init__(**kwargs)
        self.subapp = subapp
        self.show_mb = show_mb
        
        if subapp == "Writer":
            self.subapp_name = "LibreOffice Writer"
            self.subapp_file_name = "Document"
            self.subapp_icon = "libreoffice-writer"
        elif subapp == "Calc":
            self.subapp_name = "LibreOffice Calc"
            self.subapp_file_name = "Spreadsheet"
            self.subapp_icon = "libreoffice-calc"
        elif subapp == "Impress":
            self.subapp_name = "LibreOffice Impress"
            self.subapp_file_name = "Presentation"
            self.subapp_icon = "libreoffice-impress"
            
        if subapp:
            self.set_icon_name(self.subapp_icon)
            self.img_splash.set_from_icon_name(self.subapp_icon, 100)
        else:
            self.subapp_name = "LibreOffice"
        
        self.set_title("Starting {0} ...".format(self.subapp_name))
        
        if win_size:
            w, h = win_size.split("x", 1)
            self.set_default_size(int(w), int(h))
        
    def init_content(self):
        # initialize something
        # initialize something else
        # initialize something else
        # add a more fake loading :D
        time.sleep(5)
        if not self.content:
            self.content = MonocotsContent()
            self.ovl_main.add_overlay(self.content)
            
            # menubar
            self.content.chk_show_mb.set_active(self.show_mb)
            
            # final show
            self.frm_splash.hide()
            self.content.show()
            
            if self.subapp:
                self.set_title(
                    "New {0} 1 - {1}".format(self.subapp_file_name,
                                                         self.subapp_name))
            else:
                self.set_title("Create any office stuffs with LibreOffice!")
        
    def present(self):
        super().present()
        # Make sure the icon is drawn already
        GLib.timeout_add(350, self.init_content)

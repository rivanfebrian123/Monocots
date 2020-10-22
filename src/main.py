# main.py
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

import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, GLib

from .window import MonocotsWindow


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.example.App',
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE)
        self.win = None
        
        self.add_main_option("subapp", ord("a"), GLib.OptionFlags.NONE,
                             GLib.OptionArg.STRING,
                             "Sub application to launch",
                             "(Writer, Calc, etc.)")
        self.add_main_option("show-menubar", ord("m"), GLib.OptionFlags.NONE,
                             GLib.OptionArg.NONE,
                             "Show menubar",
                             None)
        self.add_main_option("window-size", ord("s"), GLib.OptionFlags.NONE,
                             GLib.OptionArg.STRING,
                             "Window size",
                             "WIDTHxHEIGHT, for example: 100x200") #TODO
        
        
        #TODO: consider to use CSS to change the background color to white

    def do_command_line(self, cmd):
        options = cmd.get_options_dict().end().unpack()
        subapp = ""
        show_mb = False
        win_size = ""
            
        if "subapp" in options:
            subapp = options["subapp"]
        if "show-menubar" in options:
            show_mb = True
        if "window-size" in options:
            win_size = options["window-size"]
            
        if not self.win:
            self.win = MonocotsWindow(subapp, show_mb, win_size,
                                      application=self)
            
        self.win.present()

def main(version):
    app = Application()
    return app.run(sys.argv)

# content.py
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

from gi.repository import Gtk


@Gtk.Template(resource_path='/org/example/App/content.ui')
class MonocotsContent(Gtk.Box):
    __gtype_name__ = 'MonocotsContent'

    mb_main = Gtk.Template.Child()
    chk_show_mb = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        
    @Gtk.Template.Callback()
    def on_chk_show_mb_toggled(self, widget):
        self.mb_main.set_visible(widget.get_active())

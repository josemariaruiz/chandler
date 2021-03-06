********************************************************************************

 			          XRCed README

********************************************************************************

System requirements
-------------------

XRCed requires wxWindows and wxPython greater or equal to 2.3.3, and 
Python 2.2 or newer (it may work with earlier version, but was not tested).

wxPython must be compiled with XRC support.


Short manual
------------

XRCed's idea is very straightforward: it is a visual tool for editing an XML
file conforming to XRC format. Every operation performed in XRCed has direct
correspondence to XML structure. So it is not really a usual point-and-click
GUI builder, but don't let that scare you.

To start xrced, change to the directory where you installed it and run
"python2.2 xrced.py".

On UNIX you can edit wrapper script "xrced.sh" to point to your installation
directory.

To create an object, first you should select some object in the tree (or the
root item if it's empty) then press the right mouse button and select an
appropriate command. The pulldown menu is context-dependent on the selected
object.

XRCed tries to guess if new object should be added as a next sibling or a
child of current object, depending on the possibility of the object to have
child objects and expanded state (if tree item is collapsed, new object will
be sibling). You can change this behavior to create siblings by pressing and
holding the Shift and Control keys before clicking the mouse.

Pressed Control key while pressing right button makes next item a sibling of
selected item regardless of its expanded state.

Pressed Shift key changes the place for inserting new child to be before
selected child, not after as by default.

Panel on the right contains object properties. Properties which are optional
should be "checked" first. This panel can be made separate by unchecking
"Embed Panel" in View menu.

All properties can be edited as text, and some are supplied with special
editing controls.

The names of the properties are exactly as in XRC file, and it's usually not
hard to guess what they do. XML ID is the name of the window, and must be
present for top-level windows (though this is not enforced by XRCed).

To display the preview window double-click a top-level object (you should
assign an XMLID to it first), press "Test" toolbar button or select command
from View menu, or press F5. After that, if you select a child object, it
becomes highlighted, and if you change it, preview is updated when you select
another item or press Ctrl-R (refresh). To turn off automatic update, toggle
"View->Auto-refresh" or toolbar auto-refresh button (to the right of the
refresh button).

--------------------------------------------------------------------------------

Copyright 2001-2003 Roman Rolinsky <rollrom@xrced.sourceforge.net>

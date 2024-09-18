
from typing import Dict, Sequence, Union

from gi.repository import Gtk

VIEW_ACCELERATORS: Dict[str, Union[str, Sequence[str]]] = {
    # DUNNO: Changing app.quit doesn't work: You'll see the new
    # binding reflected in the menubar, but neither <Ctrl-Q> nor
    # <Cmd-Q> work, and you gotta click the close button (×) to
    # quit. (Perhaps because this is the only accelerator that
    # appears in the menubar; all other accelerators are "silent"
    # (the menubar shows a single "python3" dropdown and nothing
    # else).
    # - REFER: If you want <Ctrl-Q> to work, you can use Hammerspoon.
    #   - This Spoon wires <Ctrl-Q> to send <Cmd-Q> (so then either
    #     binding will quit Meld):
    #       https://github.com/DepoXy/macOS-Hammyspoony#🥄
    #       https://github.com/DepoXy/macOS-Hammyspoony/blob/release/Source/AppTapMeld.spoon/init.lua
    #
    #  'app.quit': '<Control>Q',  # Doesn't work
    'app.quit': '<Primary>Q',
    'app.help': 'F1',
    'app.preferences': '<Control>comma',
    'view.find': '<Control>F',
    'view.find-next': ('<Control>G', 'F3'),
    'view.find-previous': ('<Control><Shift>G', '<Shift>F3'),
    'view.find-replace': '<Control>H',
    'view.go-to-line': '<Control>I',
    # Overridden in CSS
    'view.next-change': ('<Alt>Down', '<Alt>KP_Down', '<Control>D'),
    'view.next-pane': '<Alt>Page_Down',
    'view.open-external': '<Control><Shift>O',
    # Overridden in CSS
    'view.previous-change': ('<Alt>Up', '<Alt>KP_Up', '<Control>E'),
    'view.previous-pane': '<Alt>Page_Up',
    'view.redo': '<Control><Shift>Z',
    'view.refresh': ('<control>R', 'F5'),
    'view.save': '<Control>S',
    'view.save-all': '<Control><Shift>L',
    'view.save-as': '<Control><Shift>S',
    'view.undo': '<Control>Z',
    'win.close': '<Control>W',
    'win.gear-menu': 'F10',
    'win.fullscreen': 'F11',
    'win.new-tab': '<Control>N',
    'win.stop': 'Escape',
    # Shared bindings for per-view filter menu buttons
    'view.vc-filter': 'F8',
    'view.folder-filter': 'F8',
    'view.text-filter': 'F8',
    # File comparison actions
    'view.file-previous-conflict': '<Control>J',
    'view.file-next-conflict': '<Control>K',
    'view.file-push-left': '<Alt>Left',
    'view.file-push-right': '<Alt>Right',
    'view.file-pull-left': '<Alt><shift>Right',
    'view.file-pull-right': '<Alt><shift>Left',
    'view.file-copy-left-up': '<Alt>bracketleft',
    'view.file-copy-right-up': '<Alt>bracketright',
    'view.file-copy-left-down': '<Alt>semicolon',
    'view.file-copy-right-down': '<Alt>quoteright',
    'view.file-delete': ('<Alt>Delete', '<Alt>KP_Delete'),
    'view.show-overview-map': 'F9',
    # Folder comparison actions
    'view.folder-compare': 'Return',
    'view.folder-copy-left': '<Alt>Left',
    'view.folder-copy-right': '<Alt>Right',
    'view.folder-delete': 'Delete',
    # Version control actions
    'view.vc-commit': '<Control>M',
    'view.vc-console-visible': 'F9',
    # Swap the two panes
    'view.swap-2-panes': '<Alt>backslash',
}


def register_accels(app: Gtk.Application):
    for name, accel in VIEW_ACCELERATORS.items():
        accel = accel if isinstance(accel, tuple) else (accel,)
        app.set_accels_for_action(name, accel)

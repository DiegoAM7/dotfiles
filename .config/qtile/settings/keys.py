from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "k", lazy.layout.down()),
    ([mod], "i", lazy.layout.up()),
    ([mod], "j", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "j", lazy.layout.grow()),
    ([mod, "shift"], "l", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "k", lazy.layout.shuffle_down()),
    ([mod, "shift"], "i", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Restart Qtile
    ([mod, "control"], "o", lazy.restart()),
    ([mod, "control", "shift"], "p", lazy.shutdown()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume",
        lazy.spawn("amixer sset Master 5%-"),
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")
    ),
    ([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer sset Master 5%+"),
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")
    ),
    ([], "XF86AudioMute",
        lazy.spawn("amixer sset Master toggle"),
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")
    ),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]

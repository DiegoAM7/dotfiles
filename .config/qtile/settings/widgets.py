from libqtile import widget
from settings.theme import colors
import requests


def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )

def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]

primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color3', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),

    widget.CurrentLayout(**base(bg='color3'), padding=5),

    powerline('color4', 'color3'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        distro= 'Arch',
        update_interval=900,
    ),

    powerline('color2', 'color4'),

    icon(bg="color2", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color2'), format='%H:%M - %d/%m '),

    powerline('color1', 'color2'),

    icon(bg="color1", text=' '), # Icon: nf-fa-volume_up

    widget.Volume(**base(bg='color1')),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),

    widget.Battery(**base(bg='dark', fg='light'), update_interval=1, format=' {percent:2.0%}'),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    icon(bg="color2", fontsize=22, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Memory(**base(bg="color2"), padding=5),

    powerline('color3', 'color2'),

    icon(bg="color3", text=" "), # Icon: nf-fa-feed

    widget.Net(**base(bg='color3'), format="{down} | {up}"),

    powerline('color4', 'color3'),

    icon(bg="color4", text=' '), # Icon: nf-weather-thermometer

    widget.OpenWeather(**base(bg='color4'), format="{location_city} {main_temp}°{units_temperature} [{weather_details}]", cityid='3893894', language='es', update_interval=60),

    powerline('dark', 'color4'),

    widget.ThermalSensor(**base(bg='dark', fg='light')),

]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()
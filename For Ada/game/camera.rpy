################################################################################
## Background Camera
################################################################################

default debug_editor_camera_locked = False
default debug_editor_camera_x = 0.0
default debug_editor_camera_y = 0.0

default background_frozen_x = None
default background_frozen_y = None


init python:

    def get_camera_offset():

        mouse_x, mouse_y = renpy.get_mouse_pos()

        x = (mouse_x / float(config.screen_width) - 0.5) * 2.0
        y = (mouse_y / float(config.screen_height) - 0.5) * 2.0

        x = max(-1.0, min(1.0, x))
        y = max(-1.0, min(1.0, y))

        max_x = 190
        max_y = 60

        return (-x * max_x, -y * max_y)


    def background_pan_function(trans, st, at):

        renpy.store.background_frozen_x = None
        renpy.store.background_frozen_y = None

        if debug_editor_camera_locked:

            trans.xoffset = debug_editor_camera_x
            trans.yoffset = debug_editor_camera_y

        else:

            trans.xoffset, trans.yoffset = get_camera_offset()

        return 0


    def background_freeze_function(trans, st, at):

        if renpy.store.background_frozen_x is None:

            if debug_editor_camera_locked:

                x = debug_editor_camera_x
                y = debug_editor_camera_y

            else:

                x, y = get_camera_offset()

            renpy.store.background_frozen_x = x
            renpy.store.background_frozen_y = y

        trans.xoffset = renpy.store.background_frozen_x
        trans.yoffset = renpy.store.background_frozen_y

        return None


    def make_headshot(headshot, center_x=0.5):

        return Fixed(

            Transform(
                Solid("#00000099"),
                xysize=(550, 300),
                xpos=0,
                ypos=150
            ),

            Transform(
                headshot,
                xalign=center_x,
                yalign=1.0
            ),

            xysize=(550, 450)
        )


################################################################################
## Background Views
################################################################################

transform background_fixed:
    xalign 0.5
    yalign 0.5
    xoffset 0
    yoffset 0


transform background_pan:
    xalign 0.5
    yalign 0.5
    function background_pan_function


transform background_freeze:
    xalign 0.5
    yalign 0.5
    function background_freeze_function


################################################################################
## Blur Effects
################################################################################

label single_blur(intensity=12, duration=0.2, hold=0.15):

    show layer master:
        blur 0
        linear duration blur intensity
        pause hold
        linear duration blur 0

    $ renpy.pause(duration * 2 + hold, hard=True)

    show layer master

    return


################################################################################
## Character Positions
################################################################################

transform sprite_left(x=0, y=0, scale=1.0):
    xalign 0.1
    yalign 0.6
    xoffset x
    yoffset y
    zoom scale


transform sprite_middle(x=0, y=0, scale=1.0):
    xalign 0.5
    yalign 0.6
    xoffset x
    yoffset y
    zoom scale


transform sprite_right(x=0, y=0, scale=1.0):
    xalign 0.9
    yalign 0.6
    xoffset x
    yoffset y
    zoom scale


################################################################################
## Speaker Highlighting
################################################################################

transform speaking:
    matrixcolor BrightnessMatrix(0.0)


transform not_speaking:
    matrixcolor BrightnessMatrix(-0.2)


################################################################################
## Headshot Positions
################################################################################

transform headshot_left:
    xanchor 0.0
    xpos 210

    yanchor 1.0
    ypos 785


transform headshot_right:
    xanchor 1.0
    xpos 1710

    yanchor 1.0
    ypos 785

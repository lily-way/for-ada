################################################################################
## Cursor Settings
################################################################################

define cursor_size = 2

define cursor_brightness = 0.15
define cursor_contrast = 1.0

define gui.cursor_optional_color = "#C9824D"
define gui.cursor_mandatory_color = "#E8C500"
define gui.cursor_done_color = "#D3D3D3"

################################################################################
## Mouse Cursor
################################################################################

define config.mouse_displayable = MouseDisplayable(
    "default", 0, 0
).add(
    "observe_optional", "observe_optional", 16, 16
).add(
    "observe_mandatory", "observe_mandatory", 16, 16
).add(
    "interact_optional", "interact_optional", 2, 2
).add(
    "interact_mandatory", "interact_mandatory", 2, 2
).add(
    "observe_done", "observe_done", 16, 16
).add(
    "interact_done", "interact_done", 2, 2
)


################################################################################
## Cursor Images
################################################################################

image default = Transform(
    Transform(
        "images/cursors/Normal.png",
        matrixcolor=BrightnessMatrix(cursor_brightness) * ContrastMatrix(cursor_contrast) * SaturationMatrix(0.0)
    ),
    zoom=cursor_size,
    matrixcolor=ColorizeMatrix("#222222", gui.cursor_done_color)
)


image observe_optional = Transform(
    Transform(
        "images/cursors/Help Select 2.png",
        matrixcolor=BrightnessMatrix(cursor_brightness) * ContrastMatrix(cursor_contrast) * SaturationMatrix(0.0)
    ),
    zoom=cursor_size,
    matrixcolor=ColorizeMatrix("#222222", gui.cursor_optional_color)
)


image observe_mandatory = Transform(
    Transform(
        "images/cursors/Help Select 2.png",
        matrixcolor=BrightnessMatrix(cursor_brightness) * ContrastMatrix(cursor_contrast) * SaturationMatrix(0.0)
    ),
    zoom=cursor_size,
    matrixcolor=ColorizeMatrix("#222222", gui.cursor_mandatory_color)
)


image interact_optional = Transform(
    Transform(
        "images/cursors/Link 2.png",
        matrixcolor=BrightnessMatrix(cursor_brightness) * ContrastMatrix(cursor_contrast) * SaturationMatrix(0.0)
    ),
    zoom=cursor_size,
    matrixcolor=ColorizeMatrix("#222222", gui.cursor_optional_color)
)


image interact_mandatory = Transform(
    Transform(
        "images/cursors/Link 2.png",
        matrixcolor=BrightnessMatrix(cursor_brightness) * ContrastMatrix(cursor_contrast) * SaturationMatrix(0.0)
    ),
    zoom=cursor_size,
    matrixcolor=ColorizeMatrix("#222222", gui.cursor_mandatory_color)
)


image observe_done = Transform(
    Transform(
        "images/cursors/Help Select 2.png",
        matrixcolor=BrightnessMatrix(cursor_brightness) * ContrastMatrix(cursor_contrast) * SaturationMatrix(0.0)
    ),
    zoom=cursor_size,
    matrixcolor=ColorizeMatrix("#222222", gui.cursor_done_color)
)


image interact_done = Transform(
    Transform(
        "images/cursors/Link 2.png",
        matrixcolor=BrightnessMatrix(cursor_brightness) * ContrastMatrix(cursor_contrast) * SaturationMatrix(0.0)
    ),
    zoom=cursor_size,
    matrixcolor=ColorizeMatrix("#222222", gui.cursor_done_color)
)

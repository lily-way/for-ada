# ################################################################################
# ## Interaction Bounding Box Editor
# ################################################################################
# ##
# ## Controls:
# ##
# ## B       - Open / close editor
# ## Mouse   - Click and drag to create bounding box
# ## ESC     - Close editor
# ##
# ## Coordinates are calculated relative to the original
# ## 2300x1200 background image.
# ##
# ################################################################################


# ################################################################################
# ## State
# ################################################################################

# default debug_box_start = None
# default debug_box_end = None
# default debug_box_result = None


# ################################################################################
# ## Configuration
# ################################################################################

# define DEBUG_BACKGROUND_WIDTH = 2300
# define DEBUG_BACKGROUND_HEIGHT = 1200


# ################################################################################
# ## Functions
# ################################################################################

# init python:

#     ########################################################################
#     ## Camera Controls
#     ########################################################################

#     def debug_editor_open():

#         global debug_editor_camera_locked
#         global debug_editor_camera_x
#         global debug_editor_camera_y

#         global debug_box_start
#         global debug_box_end
#         global debug_box_result

#         # Capture camera position before locking.
#         offset_x, offset_y = get_camera_offset()

#         debug_editor_camera_x = offset_x
#         debug_editor_camera_y = offset_y

#         debug_editor_camera_locked = True

#         # Reset editor state.
#         debug_box_start = None
#         debug_box_end = None
#         debug_box_result = None

#         renpy.show_screen("interaction_box_editor")
#         renpy.restart_interaction()


#     def debug_editor_close():

#         global debug_editor_camera_locked

#         debug_editor_camera_locked = False

#         renpy.hide_screen("interaction_box_editor")
#         renpy.restart_interaction()


#     ########################################################################
#     ## Coordinate Conversion
#     ########################################################################

#     def debug_screen_to_background(screen_x, screen_y):

#         # Centered background's original top-left position.
#         base_x = (
#             config.screen_width - DEBUG_BACKGROUND_WIDTH
#         ) / 2.0

#         base_y = (
#             config.screen_height - DEBUG_BACKGROUND_HEIGHT
#         ) / 2.0

#         # Add frozen camera offsets.
#         camera_x = debug_editor_camera_x
#         camera_y = debug_editor_camera_y

#         # Convert screen coordinates into background coordinates.
#         background_x = screen_x - base_x - camera_x
#         background_y = screen_y - base_y - camera_y

#         return (
#             int(round(background_x)),
#             int(round(background_y))
#         )


#     ########################################################################
#     ## Bounding Box Controls
#     ########################################################################

#     def debug_box_begin():

#         global debug_box_start
#         global debug_box_end
#         global debug_box_result

#         # Record starting position in screen coordinates.
#         debug_box_start = renpy.get_mouse_pos()

#         debug_box_end = debug_box_start
#         debug_box_result = None

#         renpy.restart_interaction()


#     def debug_box_finish():

#         global debug_box_start
#         global debug_box_end
#         global debug_box_result

#         if debug_box_start is None:
#             return

#         # Get end position.
#         debug_box_end = renpy.get_mouse_pos()

#         x1, y1 = debug_box_start
#         x2, y2 = debug_box_end

#         # Convert both corners into background coordinates.
#         bg_x1, bg_y1 = debug_screen_to_background(x1, y1)
#         bg_x2, bg_y2 = debug_screen_to_background(x2, y2)

#         # Normalize coordinates.
#         x = min(bg_x1, bg_x2)
#         y = min(bg_y1, bg_y2)

#         width = abs(bg_x2 - bg_x1)
#         height = abs(bg_y2 - bg_y1)

#         debug_box_result = (x, y, width, height)

#         # Stop dragging.
#         debug_box_start = None

#         renpy.restart_interaction()


# ################################################################################
# ## Bounding Box Editor Screen
# ################################################################################

# screen interaction_box_editor():

#     modal True
#     zorder 1000

#     # Refresh preview while moving mouse.
#     timer 0.03 repeat True action Function(renpy.restart_interaction)

#     # Keyboard controls.
#     key "K_b" action Function(debug_editor_close)
#     key "K_ESCAPE" action Function(debug_editor_close)

#     # Mouse controls.
#     key "mousedown_1" action Function(debug_box_begin)
#     key "mouseup_1" action Function(debug_box_finish)

#     # Current mouse position.
#     $ mouse_x, mouse_y = renpy.get_mouse_pos()

#     # Convert to background coordinates.
#     $ bg_mouse_x, bg_mouse_y = debug_screen_to_background(mouse_x, mouse_y)


#     ########################################################################
#     ## Live Bounding Box Preview
#     ########################################################################

#     if debug_box_start is not None:

#         $ start_x, start_y = debug_box_start

#         $ box_x = min(start_x, mouse_x)
#         $ box_y = min(start_y, mouse_y)

#         $ box_width = max(1, abs(mouse_x - start_x))
#         $ box_height = max(1, abs(mouse_y - start_y))

#         # Fill.
#         add Solid("#00FF0044"):
#             xpos box_x
#             ypos box_y
#             xysize (box_width, box_height)

#         # Border.
#         add Solid("#00FF00"):
#             xpos box_x
#             ypos box_y
#             xysize (box_width, 2)

#         add Solid("#00FF00"):
#             xpos box_x
#             ypos box_y + box_height - 2
#             xysize (box_width, 2)

#         add Solid("#00FF00"):
#             xpos box_x
#             ypos box_y
#             xysize (2, box_height)

#         add Solid("#00FF00"):
#             xpos box_x + box_width - 2
#             ypos box_y
#             xysize (2, box_height)


#     ########################################################################
#     ## Completed Bounding Box
#     ########################################################################

#     if debug_box_result is not None:

#         $ result_x, result_y, result_w, result_h = debug_box_result

#         # Convert background coordinates back to screen coordinates
#         # using the frozen camera offset.

#         $ base_x = (config.screen_width - DEBUG_BACKGROUND_WIDTH) / 2.0
#         $ base_y = (config.screen_height - DEBUG_BACKGROUND_HEIGHT) / 2.0

#         $ screen_x = int(round(result_x + base_x + debug_editor_camera_x))
#         $ screen_y = int(round(result_y + base_y + debug_editor_camera_y))

#         # Fill.
#         add Solid("#00FF0044"):
#             xpos screen_x
#             ypos screen_y
#             xysize (max(1, result_w), max(1, result_h))

#         # Border.
#         add Solid("#00FF00"):
#             xpos screen_x
#             ypos screen_y
#             xysize (max(1, result_w), 2)

#         add Solid("#00FF00"):
#             xpos screen_x
#             ypos screen_y + result_h - 2
#             xysize (max(1, result_w), 2)

#         add Solid("#00FF00"):
#             xpos screen_x
#             ypos screen_y
#             xysize (2, max(1, result_h))

#         add Solid("#00FF00"):
#             xpos screen_x + result_w - 2
#             ypos screen_y
#             xysize (2, max(1, result_h))


#     ########################################################################
#     ## Debug Information Panel
#     ########################################################################

#     frame:

#         xpos 20
#         ypos 20

#         background "#000000DD"

#         padding (20, 15)

#         vbox:

#             spacing 8

#             text "BOUNDING BOX EDITOR":
#                 size 26
#                 color "#00FF00"

#             null height 5

#             text "SCREEN COORDINATES":
#                 size 18
#                 color "#AAAAAA"

#             text "X: [mouse_x]   Y: [mouse_y]":
#                 size 20
#                 color "#FFFFFF"

#             null height 5

#             text "BACKGROUND COORDINATES":
#                 size 18
#                 color "#AAAAAA"

#             text "X: [bg_mouse_x]   Y: [bg_mouse_y]":
#                 size 20
#                 color "#FFFFFF"

#             null height 5

#             text "CAMERA OFFSET":
#                 size 18
#                 color "#AAAAAA"

#             text "X: [debug_editor_camera_x:.0f]   Y: [debug_editor_camera_y:.0f]":
#                 size 20
#                 color "#FFFFFF"

#             null height 10

#             text "Click and drag to draw a box.":
#                 size 18
#                 color "#CCCCCC"

#             text "Press B or ESC to exit.":
#                 size 18
#                 color "#CCCCCC"

#             if debug_box_result is not None:

#                 null height 15

#                 text "GENERATED BOUNDING BOX":
#                     size 22
#                     color "#00FF00"

#                 $ x, y, width, height = debug_box_result

#                 text "X: [x]":
#                     color "#FFFFFF"

#                 text "Y: [y]":
#                     color "#FFFFFF"

#                 text "Width: [width]":
#                     color "#FFFFFF"

#                 text "Height: [height]":
#                     color "#FFFFFF"

#                 null height 10

#                 text "COPY THIS:":
#                     size 20
#                     color "#00FF00"

#                 text "area=([x], [y], [width], [height])":
#                     size 22
#                     color "#FFFF00"

################################################################################
## Scene 4 - Interaction 1 — Explore Living Room and Kitchen
################################################################################


################################################################################
## State
################################################################################

default scene_4_interaction_1_room = "living_room"

default scene_4_interaction_1_armchair_done = False
default scene_4_interaction_1_radio_done = False
default scene_4_interaction_1_window_done = False

default scene_4_interaction_1_kitchen_door_done = False
default scene_4_interaction_1_kitchen_floor_done = False


################################################################################
## Backgrounds
################################################################################

init python:

    def scene_4_interaction_1_background(room):

        return Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_4",
            (0, 0), "bg {}".format(room)
        )


################################################################################
## Living Room Interactions
################################################################################

define scene_4_interaction_1_living_room_objects = [

    Interaction(
        name="armchair",
        interaction_type="observe",
        area=(266, 487, 506, 533),
        action="scene_4_interaction_1_armchair",
        completed="scene_4_interaction_1_armchair_done",
        mandatory=False
    ),

    Interaction(
        name="radio",
        interaction_type="observe",
        area=(2059, 239, 229, 135),
        action="scene_4_interaction_1_radio",
        completed="scene_4_interaction_1_radio_done",
        mandatory=False
    ),

    Interaction(
        name="small_window",
        interaction_type="observe",
        area=(1350, 123, 106, 464),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_door",
        interaction_type="interact",
        area=(1640, 126, 187, 746),
        action="scene_4_interaction_1_go_to_kitchen",
        mandatory=False
    ),

]


################################################################################
## Kitchen Interactions
################################################################################

define scene_4_interaction_1_kitchen_objects = [

    Interaction(
        name="living_room_door",
        interaction_type="interact",
        area=(149, 59, 203, 837),
        action="scene_4_interaction_1_go_to_living_room",
        mandatory=False
    ),

    Interaction(
        name="kitchen_floor",
        interaction_type="interact",
        area=(529, 840, 772, 256),
        action="scene_4_interaction_1_kitchen_floor",
        completed="scene_4_interaction_1_kitchen_floor_done",
        mandatory=True
    ),

    Interaction(
        name="kitchen_small_window_1",
        interaction_type="observe",
        area=(528, 140, 99, 459),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_2",
        interaction_type="observe",
        area=(1979, 161, 140, 375),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_3",
        interaction_type="observe",
        area=(2221, 141, 78, 368),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_1:

    $ scene_4_interaction_1_room = "living_room"
    $ progress_interactions = scene_4_interaction_1_living_room_objects
    $ progress_open = False

    scene expression scene_4_interaction_1_background("living_room") as bg at background_pan

    while not scene_4_interaction_1_kitchen_floor_done:

        if scene_4_interaction_1_room == "living_room":

            $ progress_interactions = scene_4_interaction_1_living_room_objects

            call screen interaction_screen(
                scene_4_interaction_1_living_room_objects
            )

        elif scene_4_interaction_1_room == "kitchen":

            $ progress_interactions = scene_4_interaction_1_kitchen_objects

            call screen interaction_screen(
                scene_4_interaction_1_kitchen_objects
            )

        call expression _return

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Room Navigation - Kitchen
################################################################################

label scene_4_interaction_1_go_to_kitchen:

    if not scene_4_interaction_1_kitchen_door_done:

        show expression scene_4_interaction_1_background("living_room") as bg at background_freeze

        call single_blur

        show headshot_cait PO at headshot_left, speaking
        cait "(Ugh!)"

        hide headshot_cait

        call single_blur

        show headshot_cait PO at headshot_left, speaking
        cait "(Stay focused!)"

        hide headshot_cait

        call single_blur

        menu:

            "Remember…":
                call scene_4_memory_next

            "Stay focused":
                pass

            "Remember…":
                call scene_4_memory_next

        $ scene_4_interaction_1_kitchen_door_done = True

        # TODO: Sound - Drag body

    $ scene_4_interaction_1_room = "kitchen"

    $ progress_interactions = scene_4_interaction_1_kitchen_objects

    scene expression scene_4_interaction_1_background("kitchen") as bg at background_pan
    with fade

    return


################################################################################
## Room Navigation - Living Room
################################################################################

label scene_4_interaction_1_go_to_living_room:

    $ scene_4_interaction_1_room = "living_room"

    $ progress_interactions = scene_4_interaction_1_living_room_objects

    scene expression scene_4_interaction_1_background("living_room") as bg at background_pan
    with fade

    return


################################################################################
## Armchair
################################################################################

label scene_4_interaction_1_armchair:

    if scene_4_interaction_1_armchair_done:
        return

    show expression scene_4_interaction_1_background("living_room") as bg at background_freeze

    show headshot_cait sweet at headshot_left, speaking
    cait "Just a little longer, baby…"

    hide headshot_cait

    $ scene_4_interaction_1_armchair_done = True

    show expression scene_4_interaction_1_background("living_room") as bg at background_pan

    return


################################################################################
## Radio
################################################################################

label scene_4_interaction_1_radio:

    if scene_4_interaction_1_radio_done:
        return

    show expression scene_4_interaction_1_background("living_room") as bg at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(It’s just static.)"

    cait "(Tuned to a dead channel.)"

    hide headshot_cait

    $ scene_4_interaction_1_radio_done = True

    show expression scene_4_interaction_1_background("living_room") as bg at background_pan

    return


################################################################################
## Small Windows
################################################################################

label scene_4_interaction_1_window:

    if scene_4_interaction_1_window_done:
        return

    show expression scene_4_interaction_1_background(
        scene_4_interaction_1_room
    ) as bg at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(The storm’s coming down hard.)"

    cait "(It’ll be weeks before any new ships can dock planetside.)"

    hide headshot_cait

    $ scene_4_interaction_1_window_done = True

    show expression scene_4_interaction_1_background(
        scene_4_interaction_1_room
    ) as bg at background_pan

    return


################################################################################
## Kitchen Floor — Start Extraction
################################################################################

label scene_4_interaction_1_kitchen_floor:

    $ scene_4_interaction_1_kitchen_floor_done = True

    return

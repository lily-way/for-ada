################################################################################
## Scene 2 - Interaction 4
################################################################################


################################################################################
## State
################################################################################

default scene_2_interaction_4_room = "living_room"
default scene_2_interaction_4_door_done = False
default scene_2_interaction_4_armchair_done = False


################################################################################
## Living Room Interactions
################################################################################

define scene_2_interaction_4_living_room_objects = [

    Interaction(
        name="armchair",
        interaction_type="observe",
        area=(266, 487, 506, 533),
        action="scene_2_interaction_4_armchair",
        completed="scene_2_interaction_4_armchair_done",
        mandatory=False
    ),

    Interaction(
        name="radio",
        interaction_type="observe",
        area=(2059, 239, 229, 135),
        action="scene_2_interaction_4_observation",
        mandatory=False
    ),

    Interaction(
        name="doctorate",
        interaction_type="observe",
        area=(402, 116, 172, 167),
        action="scene_2_interaction_4_observation",
        mandatory=False
    ),

    Interaction(
        name="front_door",
        interaction_type="interact",
        area=(0, 96, 158, 773),
        action="scene_2_interaction_4_door",
        completed="scene_2_interaction_4_door_done",
        mandatory=True
    ),

    Interaction(
        name="kitchen_entrance",
        interaction_type="interact",
        area=(1640, 126, 187, 746),
        action="scene_2_interaction_4_go_kitchen",
        mandatory=False
    ),

]


################################################################################
## Kitchen Interactions
################################################################################

define scene_2_interaction_4_kitchen_objects = [

    Interaction(
        name="stovetop",
        interaction_type="observe",
        area=(1622, 619, 272, 307),
        action="scene_2_interaction_4_observation",
        mandatory=False
    ),

    Interaction(
        name="wine_bottle",
        interaction_type="observe",
        area=(1039, 494, 56, 128),
        action="scene_2_interaction_4_observation",
        mandatory=False
    ),

    Interaction(
        name="living_room_entrance",
        interaction_type="interact",
        area=(149, 59, 203, 837),
        action="scene_2_interaction_4_go_living_room",
        mandatory=False
    ),

]


################################################################################
## Progress Interactions
################################################################################

define scene_2_interaction_4_progress_objects = [
    scene_2_interaction_4_living_room_objects[0],
    scene_2_interaction_4_living_room_objects[3]
]


################################################################################
## Scene
################################################################################

label scene_2_interaction_4:

    $ scene_2_interaction_4_room = "living_room"
    $ progress_interactions = scene_2_interaction_4_progress_objects
    $ progress_open = False

    scene expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_4",
        (0, 0), "bg living_room"
    ) as bg at background_pan

    while not scene_2_interaction_4_door_done:

        if scene_2_interaction_4_room == "living_room":

            call screen interaction_screen(scene_2_interaction_4_living_room_objects)

        elif scene_2_interaction_4_room == "kitchen":

            call screen interaction_screen(scene_2_interaction_4_kitchen_objects)

        call expression _return

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Room Navigation
################################################################################

label scene_2_interaction_4_go_kitchen:

    $ scene_2_interaction_4_room = "kitchen"
    $ progress_interactions = scene_2_interaction_4_kitchen_objects

    scene expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_4",
        (0, 0), "bg kitchen"
    ) as bg at background_pan
    with Fade(0.3, 0.2, 0.3)

    return


label scene_2_interaction_4_go_living_room:

    $ scene_2_interaction_4_room = "living_room"
    $ progress_interactions = scene_2_interaction_4_progress_objects

    scene expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_4",
        (0, 0), "bg living_room"
    ) as bg at background_pan
    with Fade(0.3, 0.2, 0.3)

    return

################################################################################
## Optional Observation - Armchair
################################################################################

label scene_2_interaction_4_armchair:

    if scene_2_interaction_4_armchair_done:
        return

    show expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_4",
        (0, 0), "bg living_room"
    ) as bg at background_freeze

    show headshot_cait broken_sweet at headshot_left, speaking
    cait "Don’t worry, baby…"
    cait "I’m going to get you help."

    hide headshot_cait

    $ scene_2_interaction_4_armchair_done = True

    show expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_4",
        (0, 0), "bg living_room"
    ) as bg at background_pan

    return


################################################################################
## Optional Observation - Other Objects
################################################################################

label scene_2_interaction_4_observation:

    if scene_2_interaction_4_room == "living_room":
        show expression Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_4",
            (0, 0), "bg living_room"
        ) as bg at background_freeze
    else:
        show expression Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_4",
            (0, 0), "bg kitchen"
        ) as bg at background_freeze

    show headshot_cait broken_focus at headshot_left, speaking
    cait "..."
    cait "(Nothing matters without her.)"

    hide headshot_cait

    if scene_2_interaction_4_room == "living_room":
        show expression Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_4",
            (0, 0), "bg living_room"
        ) as bg at background_pan
    else:
        show expression Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_4",
            (0, 0), "bg kitchen"
        ) as bg at background_pan

    return


################################################################################
## Mandatory Interaction - Front Door
################################################################################

label scene_2_interaction_4_door:

    if scene_2_interaction_4_door_done:
        return

    show expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_4",
        (0, 0), "bg living_room"
    ) as bg at background_freeze

    show headshot_cait broken_focus at headshot_left, speaking
    cait "(The storm…)"

    hide headshot_cait

    menu:

        "Put on rain clothes":

            # play sound "audio/zipper.mp3"

            show headshot_cait broken_raincoat_focus at headshot_left, speaking
            cait "(Don’t worry, Ada…)"
            cait "(I’ll save you.)"

            hide headshot_cait

    scene expression Solid("#000000")
    with Dissolve(0.5)

    $ scene_2_interaction_4_door_done = True

    return

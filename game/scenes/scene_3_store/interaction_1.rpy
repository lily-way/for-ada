################################################################################
## Scene 3 - Interaction 1
################################################################################


################################################################################
## State
################################################################################

default scene_3_interaction_1_door_done = False
default scene_3_interaction_1_window_knocked = False
default scene_3_interaction_1_window_broken = False
default scene_3_interaction_1_window_done = False


################################################################################
## Interactions
################################################################################

define scene_3_interaction_1_door_objects = [

    Interaction(
        name="door",
        interaction_type="interact",
        area=(604, 73, 242, 987),
        action="scene_3_interaction_1_door",
        completed="scene_3_interaction_1_door_done",
        mandatory=True
    ),

]

define scene_3_interaction_1_window_objects = [

    Interaction(
        name="window",
        interaction_type="interact",
        area=(912, 351, 138, 345),
        action="scene_3_interaction_1_window",
        completed="scene_3_interaction_1_window_knocked",
        mandatory=True
    ),

]

define scene_3_interaction_1_smash_window_objects = [

    Interaction(
        name="window",
        interaction_type="interact",
        area=(912, 351, 138, 345),
        action="scene_3_interaction_1_smash_window",
        completed="scene_3_interaction_1_window_broken",
        mandatory=True
    ),

]

define scene_3_interaction_1_broken_window_objects = [

    Interaction(
        name="broken_window",
        interaction_type="interact",
        area=(912, 351, 138, 345),
        action="scene_3_interaction_1_enter_window",
        completed="scene_3_interaction_1_window_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_3_interaction_1:

    $ progress_interactions = scene_3_interaction_1_door_objects
    $ progress_open = False

    play music "audio/loops/rainstorm.mp3" fadein 1.0

    pause 2.0

    scene bg storefront_window at background_freeze
    with fade

    pause 1.0

    show headshot_cait focus at headshot_left, speaking
    cait "(He must be inside with his family…)"
    cait "(I need to wake them up.)"

    hide headshot_cait

    show bg storefront_window at background_pan

    while not scene_3_interaction_1_window_done:

        if not scene_3_interaction_1_door_done:

            $ progress_interactions = scene_3_interaction_1_door_objects

            call screen interaction_screen(scene_3_interaction_1_door_objects)

        elif not scene_3_interaction_1_window_knocked:

            $ progress_interactions = scene_3_interaction_1_window_objects

            call screen interaction_screen(scene_3_interaction_1_window_objects)

        elif not scene_3_interaction_1_window_broken:

            $ progress_interactions = scene_3_interaction_1_smash_window_objects

            call screen interaction_screen(scene_3_interaction_1_smash_window_objects)

        else:

            $ progress_interactions = scene_3_interaction_1_broken_window_objects

            call screen interaction_screen(scene_3_interaction_1_broken_window_objects)

        call expression _return

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Mandatory Interaction - Door
################################################################################

label scene_3_interaction_1_door:

    if scene_3_interaction_1_door_done:
        return

    show bg storefront_window at background_freeze

    menu:

        "Bang on door":

            play sound "audio/sound_effects/door_bang.mp3"

            pause 1.0

            show headshot_cait focus at headshot_left, speaking
            cait "(Nothing.)"

            hide headshot_cait

            $ scene_3_interaction_1_door_done = True

    show bg storefront_window at background_pan

    return


################################################################################
## Mandatory Interaction - Window
################################################################################

label scene_3_interaction_1_window:

    if scene_3_interaction_1_window_knocked:
        return

    show bg storefront_window at background_freeze

    menu:

        "Bang on window":

            play sound "audio/sound_effects/window_bang.mp3"

            pause 1.0

            show headshot_cait focus at headshot_left, speaking
            cait "(Nothing.)"

            show headshot_cait PO at headshot_left, speaking
            cait "(Fuck!)"

            hide headshot_cait

            $ scene_3_interaction_1_window_knocked = True

    show bg storefront_window at background_pan

    return


################################################################################
## Mandatory Interaction - Smash Window
################################################################################

label scene_3_interaction_1_smash_window:

    if scene_3_interaction_1_window_broken:
        return

    show bg storefront_window at background_freeze

    menu:

        "Smash window":

            play sound "audio/sound_effects/window_smash.mp3"

            scene bg storefront_no_window at background_freeze

            pause 1.0

            show headshot_cait focus at headshot_left, speaking
            cait "(There we go.)"

            hide headshot_cait

            $ scene_3_interaction_1_window_broken = True

    show bg storefront_no_window at background_pan

    return


################################################################################
## Mandatory Interaction - Broken Window
################################################################################

label scene_3_interaction_1_enter_window:

    if scene_3_interaction_1_window_done:
        return

    scene expression Solid("#000000")
    with Dissolve(0.5)

    stop music fadeout 1.0

    $ scene_3_interaction_1_window_done = True

    return

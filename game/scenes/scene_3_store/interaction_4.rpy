################################################################################
## Scene 3 - Interaction 4
################################################################################


################################################################################
## State
################################################################################

default scene_3_interaction_4_clothed_torso_done = False
default scene_3_interaction_4_exposed_torso_done = False
default scene_3_interaction_4_exposed_organs_done = False


################################################################################
## Interactions
################################################################################

define scene_3_interaction_4_clothed_torso_objects = [

    Interaction(
        name="wife_clothed_torso",
        interaction_type="interact",
        area=(763, 5, 695, 1073),
        action="scene_3_interaction_4_clothed_torso",
        completed="scene_3_interaction_4_clothed_torso_done",
        mandatory=True
    ),

]

define scene_3_interaction_4_exposed_torso_objects = [

    Interaction(
        name="wife_exposed_torso",
        interaction_type="interact",
        area=(829, 211, 619, 891),
        action="scene_3_interaction_4_exposed_torso",
        completed="scene_3_interaction_4_exposed_torso_done",
        mandatory=True
    ),

]

define scene_3_interaction_4_exposed_organs_objects = [

    Interaction(
        name="wife_exposed_organs",
        interaction_type="interact",
        area=(961, 234, 219, 382),
        action="scene_3_interaction_4_exposed_organs",
        completed="scene_3_interaction_4_exposed_organs_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_3_interaction_4:

    scene bg wife_clothed_torso at background_pan
    with fade

    show headshot_cait bloody_focus at headshot_left, speaking
    cait "(Now I can focus.)"

    hide headshot_cait

    $ progress_interactions = scene_3_interaction_4_clothed_torso_objects

    while not scene_3_interaction_4_clothed_torso_done:

        call screen interaction_screen(
            scene_3_interaction_4_clothed_torso_objects
        )

        call expression _return

    $ progress_interactions = scene_3_interaction_4_exposed_torso_objects

    while not scene_3_interaction_4_exposed_torso_done:

        call screen interaction_screen(
            scene_3_interaction_4_exposed_torso_objects
        )

        call expression _return

    $ progress_interactions = scene_3_interaction_4_exposed_organs_objects

    while not scene_3_interaction_4_exposed_organs_done:

        call screen interaction_screen(
            scene_3_interaction_4_exposed_organs_objects
        )

        call expression _return

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Wife - Clothed Torso
################################################################################

label scene_3_interaction_4_clothed_torso:

    if scene_3_interaction_4_clothed_torso_done:
        return

    show bg wife_clothed_torso at background_freeze

    menu:

        "Cut through clothing":

            play sound "audio/sound_effects/tear_fabric.mp3"

            pause 0.5

            scene bg wife_exposed_torso at background_pan

            $ scene_3_interaction_4_clothed_torso_done = True

    return


################################################################################
## Wife - Exposed Torso
################################################################################

label scene_3_interaction_4_exposed_torso:

    if scene_3_interaction_4_exposed_torso_done:
        return

    show bg wife_exposed_torso at background_freeze

    menu:

        "Open chest cavity":

            play sound "audio/sound_effects/chop_meat.mp3"

            scene bg wife_exposed_organs at background_pan
            with Fade(0.3, 1.0, 0.3)

            show headshot_cait bloody_focus at headshot_left, speaking
            cait "(A brand-new heart.)"

            cait "(Just like Martin said.)"

            hide headshot_cait

            $ scene_3_interaction_4_exposed_torso_done = True

    return


################################################################################
## Wife - Exposed Organs
################################################################################

label scene_3_interaction_4_exposed_organs:

    if scene_3_interaction_4_exposed_organs_done:
        return

    show bg wife_exposed_organs at background_freeze

    menu:

        "Take heart":

            pause 0.1

            play sound "audio/sound_effects/organ_removal.mp3"

            pause 0.3

            scene bg wife_no_heart at background_freeze

            menu:

                "Place heart in cooler":

                    play sound "audio/sound_effects/gas_release.mp3"
    
                    pause 1.0

                    show bg wife_no_heart at background_pan

                    $ scene_3_interaction_4_exposed_organs_done = True

    return

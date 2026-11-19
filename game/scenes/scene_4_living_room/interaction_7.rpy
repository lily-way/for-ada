################################################################################
## Scene 4 - Interaction 7 — Give Ada New Lungs
################################################################################


################################################################################
## State
################################################################################

default scene_4_interaction_7_torso_done = False


################################################################################
## Interactions
################################################################################

define scene_4_interaction_7_objects = [

    Interaction(
        name="ada_torso",
        interaction_type="interact",
        area=(1048, 163, 201, 391),
        action="scene_4_interaction_7_torso",
        completed="scene_4_interaction_7_torso_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_7:

    $ progress_interactions = scene_4_interaction_7_objects
    $ progress_open = False

    scene bg ada_healthy_neither at background_pan
    with fade

    while not scene_4_interaction_7_torso_done:

        call screen interaction_screen(
            scene_4_interaction_7_objects
        )

        call expression _return

    hide headshot_cait

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Ada's Torso
################################################################################

label scene_4_interaction_7_torso:

    if scene_4_interaction_7_torso_done:
        return

    show bg ada_healthy_neither at background_freeze

    menu:

        "Give Ada new lungs":
            pass

    scene bg ada_healthy_lungs at background_fixed
    with fade

    show headshot_cait bloody_sweet at headshot_left, speaking
    cait "Breathe easy, baby."

    cait "Soon we’ll be together again."

    cait "I’m sure you’ll be laughing, like you always are."

    hide headshot_cait

    $ scene_4_interaction_7_torso_done = True

    return

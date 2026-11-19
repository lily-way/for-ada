################################################################################
## Scene 4 - Interaction 9 — Give Ada a New Heart
################################################################################


################################################################################
## State
################################################################################

default scene_4_interaction_9_torso_done = False


################################################################################
## Interactions
################################################################################

define scene_4_interaction_9_objects = [

    Interaction(
        name="ada_torso",
        interaction_type="interact",
        area=(1054, 638, 174, 293),
        action="scene_4_interaction_9_torso",
        completed="scene_4_interaction_9_torso_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_9:

    $ progress_interactions = scene_4_interaction_9_objects
    $ progress_open = False

    scene bg ada_healthy_lungs at background_pan
    with fade

    while not scene_4_interaction_9_torso_done:

        call screen interaction_screen(
            scene_4_interaction_9_objects
        )

        call expression _return

    hide headshot_cait

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Ada's Torso
################################################################################

label scene_4_interaction_9_torso:

    if scene_4_interaction_9_torso_done:
        return

    show bg ada_healthy_lungs at background_freeze

    menu:

        "Give Ada a new heart":
            pass

    scene bg ada_healthy_both at background_fixed
    with fade

    show headshot_cait sweet at headshot_left, speaking
    cait "You and your heart."

    cait "You’ve always worn it on your sleeve."

    cait "I can’t believe I ever got this lucky."

    hide headshot_cait

    $ scene_4_interaction_9_torso_done = True

    return

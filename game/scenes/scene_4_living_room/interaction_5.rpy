################################################################################
## Scene 4 - Interaction 5
################################################################################


################################################################################
## State
################################################################################

default scene_4_interaction_5_torso_done = False


################################################################################
## Interactions
################################################################################

define scene_4_interaction_5_objects = [

    Interaction(
        name="ada_torso",
        interaction_type="interact",
        area=(891, 140, 511, 836),
        action="scene_4_interaction_5_torso",
        completed="scene_4_interaction_5_torso_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_5:

    $ progress_interactions = scene_4_interaction_5_objects
    $ progress_open = False

    scene bg ada_healthy_neither at background_fixed
    with fade

    show headshot_cait bloody_worry at headshot_left, speaking
    cait "What a horrible night…"

    cait "I’m glad you aren’t awake to see all this."

    cait "You deserve better."

    show headshot_cait bloody_sweet at headshot_left, speaking
    cait "You always have."

    hide headshot_cait

    show bg ada_healthy_neither at background_pan

    while not scene_4_interaction_5_torso_done:

        call screen interaction_screen(
            scene_4_interaction_5_objects
        )

        call expression _return

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Ada's Torso
################################################################################

label scene_4_interaction_5_torso:

    if scene_4_interaction_5_torso_done:
        return

    $ scene_4_interaction_5_torso_done = True

    return

################################################################################
## Scene 4 - Interaction 11 — Restore Ada
################################################################################


################################################################################
## Images
################################################################################

image bg ada_tubes = Composite(
    (2300, 1200),
    (0, 0), "bg ada_healthy_both",
    (0, 0), "bg ada_tube_1",
    (0, 0), "bg ada_tube_2",
    (0, 0), "bg ada_tube_3",
    (0, 0), "bg ada_tube_4",
    (0, 0), "bg ada_tube_5"
)


################################################################################
## State
################################################################################

default scene_4_interaction_11_torso_done = False


################################################################################
## Interactions
################################################################################

define scene_4_interaction_11_objects = [

    Interaction(
        name="ada_torso",
        interaction_type="interact",
        area=(750, 250, 850, 850),
        action="scene_4_interaction_11_torso",
        completed="scene_4_interaction_11_torso_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_11:

    $ progress_interactions = scene_4_interaction_11_objects
    $ progress_open = False

    scene bg ada_healthy_both at background_pan
    with fade

    while not scene_4_interaction_11_torso_done:

        call screen interaction_screen(
            scene_4_interaction_11_objects
        )

        call expression _return

    hide headshot_cait

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Ada's Torso
################################################################################

label scene_4_interaction_11_torso:

    if scene_4_interaction_11_torso_done:
        return

    show bg ada_healthy_both at background_freeze

    menu:

        "Hook up Ada to D9’s fluids":
            pass

    scene bg ada_tubes at background_fixed
    with fade

    show headshot_cait sweet at headshot_left, speaking
    cait "Come back to me, Ada."

    cait "I’ll remake your body as many times as it takes."

    scene bg ada_restored_open at background_fixed
    with fade

    show headshot_cait sweet at headshot_left, speaking
    cait "All I want is to see you being your whole self."

    cait "You love it almost as much as I do."

    hide headshot_cait

    menu:

        "Sew her up":
            pass

    scene bg ada_restored_sealed at background_fixed
    with fade

    show headshot_cait sweet at headshot_left, speaking
    cait "You’re good as new, baby."

    scene bg ada_restored_sealed_hand at background_fixed
    with fade

    show headshot_cait sweet at headshot_left, speaking
    cait "I can’t wait to see you again."

    hide headshot_cait

    $ scene_4_interaction_11_torso_done = True

    return

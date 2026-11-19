################################################################################
## Scene 3 - Interaction 3
################################################################################


################################################################################
## State
################################################################################

default scene_3_interaction_3_clothed_torso_done = False
default scene_3_interaction_3_exposed_torso_done = False
default scene_3_interaction_3_exposed_ribcage_done = False
default scene_3_interaction_3_exposed_organs_done = False


################################################################################
## Interactions
################################################################################

define scene_3_interaction_3_clothed_torso_objects = [

    Interaction(
        name="martin_clothed_torso",
        interaction_type="interact",
        area=(747, 118, 758, 958),
        action="scene_3_interaction_3_clothed_torso",
        completed="scene_3_interaction_3_clothed_torso_done",
        mandatory=True
    ),

]

define scene_3_interaction_3_exposed_torso_objects = [

    Interaction(
        name="martin_exposed_torso",
        interaction_type="interact",
        area=(842, 223, 571, 751),
        action="scene_3_interaction_3_exposed_torso",
        completed="scene_3_interaction_3_exposed_torso_done",
        mandatory=True
    ),

]

define scene_3_interaction_3_exposed_ribcage_objects = [

    Interaction(
        name="martin_exposed_ribcage",
        interaction_type="interact",
        area=(977, 70, 257, 831),
        action="scene_3_interaction_3_exposed_ribcage",
        completed="scene_3_interaction_3_exposed_ribcage_done",
        mandatory=True
    ),

]

define scene_3_interaction_3_exposed_organs_objects = [

    Interaction(
        name="martin_exposed_organs",
        interaction_type="interact",
        area=(872, 77, 472, 408),
        action="scene_3_interaction_3_exposed_organs",
        completed="scene_3_interaction_3_exposed_organs_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_3_interaction_3:

    $ progress_interactions = scene_3_interaction_3_clothed_torso_objects
    $ progress_open = False

    scene expression Solid("#000000")
    with Dissolve(0.5)

    scene bg martin_clothed_torso at background_fixed
    with Dissolve(0.5)

    show headshot_cait focus at headshot_left, speaking
    cait "(That was loud. I’ll have to work quickly.)"

    hide headshot_cait

    show bg martin_clothed_torso at background_fixed

    while not scene_3_interaction_3_clothed_torso_done:

        call screen interaction_screen(scene_3_interaction_3_clothed_torso_objects)
        call expression _return

    $ progress_interactions = scene_3_interaction_3_exposed_torso_objects

    while not scene_3_interaction_3_exposed_torso_done:

        call screen interaction_screen(scene_3_interaction_3_exposed_torso_objects)
        call expression _return

    $ progress_interactions = scene_3_interaction_3_exposed_ribcage_objects

    while not scene_3_interaction_3_exposed_ribcage_done:

        call screen interaction_screen(scene_3_interaction_3_exposed_ribcage_objects)
        call expression _return

    $ progress_interactions = scene_3_interaction_3_exposed_organs_objects

    while not scene_3_interaction_3_exposed_organs_done:

        call screen interaction_screen(scene_3_interaction_3_exposed_organs_objects)
        call expression _return

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Mandatory Interaction - Clothed Torso
################################################################################

label scene_3_interaction_3_clothed_torso:

    scene bg martin_exposed_torso at background_fixed

    # play sound "audio/tearing_fabric.mp3"

    martins_wife "Martin?!"
    martins_wife "What’s going on down there?!"

    $ scene_3_interaction_3_clothed_torso_done = True

    show bg martin_exposed_torso at background_fixed

    return


################################################################################
## Mandatory Interaction - Exposed Torso
################################################################################

label scene_3_interaction_3_exposed_torso:

    show bg martin_exposed_torso at background_fixed

    menu:

        "Butcher Martin":

            scene bg martin_exposed_ribcage at background_fixed
            with Fade(0.3, 0.5, 0.3)

            # play sound "audio/fleshpeel.mp3"

            martins_wife "This better not be another one of your practical jokes!"

            $ scene_3_interaction_3_exposed_torso_done = True

            show bg martin_exposed_ribcage at background_fixed

    return


################################################################################
## Mandatory Interaction - Exposed Ribcage
################################################################################

label scene_3_interaction_3_exposed_ribcage:

    scene bg martin_exposed_organs at background_fixed

    # play sound "audio/bonesaw.mp3"

    show headshot_cait smile at headshot_left, speaking
    cait "(Look at those beautiful new lungs.)"

    hide headshot_cait

    martins_wife "Martin, I’m coming down!"

    $ scene_3_interaction_3_exposed_ribcage_done = True

    show bg martin_exposed_organs at background_fixed

    return


################################################################################
## Mandatory Interaction - Exposed Organs
################################################################################

label scene_3_interaction_3_exposed_organs:

    scene bg martin_no_lungs at background_fixed

    # play sound "audio/fleshscoop.mp3"

    show headshot_cait smile at headshot_left, speaking
    cait "(Thank you, Martin…)"

    hide headshot_cait

    # play sound "audio/footsteps.mp3"

    martins_wife "Martin…?"

    $ scene_3_interaction_3_exposed_organs_done = True

    return

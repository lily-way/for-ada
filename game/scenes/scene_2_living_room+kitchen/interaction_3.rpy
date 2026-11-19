################################################################################
## Scene 2 - Interaction 3
################################################################################


################################################################################
## State
################################################################################

default scene_2_interaction_3_armchair_done = False


################################################################################
## Interactions
################################################################################

define scene_2_interaction_3_objects = [

    Interaction(
        name="armchair",
        interaction_type="interact",
        area=(273, 457, 491, 546),
        action="scene_2_interaction_3_armchair",
        completed="scene_2_interaction_3_armchair_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_2_interaction_3:

    $ progress_interactions = scene_2_interaction_3_objects
    $ progress_open = False

    scene expression Solid("#000000")
    with Dissolve(0.5)

    scene expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_3",
        (0, 0), "bg kitchen"
    ) as bg at background_fixed
    with Dissolve(0.5)

    show headshot_cait focus at headshot_left, speaking
    cait "(I’ll leave this to simmer for a little while.)"

    show headshot_cait sweet at headshot_left, speaking
    cait "(Now I can keep relaxing with Ada.)"

    hide headshot_cait

    scene expression Solid("#000000")
    with Dissolve(0.5)

    scene expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_3",
        (0, 0), "bg living_room"
    ) as bg at background_pan
    with Dissolve(0.5)

    while not scene_2_interaction_3_armchair_done:

        call screen interaction_screen(scene_2_interaction_3_objects)
        call expression _return

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Mandatory Interaction - Armchair
################################################################################

label scene_2_interaction_3_armchair:

    if scene_2_interaction_3_armchair_done:
        return

    show expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_3",
        (0, 0), "bg living_room"
    ) as bg at background_freeze

    show ada deathly at sprite_right, speaking
    ada "Back so soon…?"

    show ada deathly at sprite_right, not_speaking
    show headshot_cait worry at headshot_left, speaking
    cait "I’m just softening the meat…"
    cait "What’s wrong, baby?"

    hide headshot_cait
    show ada deathly at sprite_right, speaking
    ada "Hurts…"

    show ada deathly at sprite_right, not_speaking
    show headshot_cait worry at headshot_left, speaking
    cait "Tell me where it hurts?"

    hide headshot_cait
    show ada deathly at sprite_right, speaking
    ada "I…"

    show ada deathly at sprite_right, speaking
    ada "*hack* *hack*"

    show ada deathly at sprite_right, not_speaking
    show headshot_cait panic at headshot_left, speaking
    cait "(There’s blood…)"

    hide headshot_cait

    play music "audio/loops/heartbeat_fast.mp3" loop

    "Cait places her hand on Ada’s chest."
    "Her feeble heart beats wildly."

    show headshot_cait panic at headshot_left, speaking
    cait "(Not this… Please…)"

    show headshot_cait worry at headshot_left, speaking
    cait "Stay still, baby. Let me get something for your throat."

    hide headshot_cait
    show ada deathly at sprite_right, speaking
    ada "*hack* *gasp*"
    ada "Hurts…"

    show ada deathly at sprite_right, speaking
    ada "Hurts…"

    show ada deathly at sprite_right, not_speaking

    show headshot_cait panic at headshot_left, speaking
    cait "Ada?"
    cait "Hey. Ada!"

    hide headshot_cait
    show ada deathly at sprite_right, speaking
    ada "*gasp*"
    ada "..."

    show ada deathly at sprite_right, not_speaking
    show headshot_cait panic at headshot_left, speaking
    cait "No, no, no, no, no!"

    hide headshot_cait
    hide ada

    scene expression Solid("#000000")
    with Dissolve(0.5)

    play music "audio/loops/heartbeat_medium.mp3" loop

    play sound "audio/human_sounds/cait_breath1.mp3"

    pause 2.0

    cait "..."

    play sound "audio/human_sounds/cait_breath2.mp3"

    pause 2.0

    cait "..."

    play sound "audio/human_sounds/cait_breath3.mp3"

    pause 2.0

    stop music

    cait "..."

    pause 1.0

    play sound "audio/human_sounds/cait_scream2.mp3"

    pause 6.0

    $ scene_2_interaction_3_armchair_done = True

    return

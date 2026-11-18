################################################################################
## Scene 4 - Interaction 2 — Extract D9 and Return to Ada
################################################################################


################################################################################
## State
################################################################################

default scene_4_interaction_2_d9_neck_done = False
default scene_4_interaction_2_d9_clothed_done = False
default scene_4_interaction_2_d9_exposed_done = False

default scene_4_interaction_2_living_room_door_done = False
default scene_4_interaction_2_return_armchair_done = False


################################################################################
## Final Armchair Interaction
################################################################################

define scene_4_interaction_2_return_armchair_objects = [

    Interaction(
        name="armchair",
        interaction_type="interact",
        area=(266, 487, 506, 533),
        action="scene_4_interaction_2_return_armchair",
        completed="scene_4_interaction_2_return_armchair_done",
        mandatory=True
    ),

]


################################################################################
## Final Living Room Entryway Interaction
################################################################################

define scene_4_interaction_2_return_door_objects = [

    Interaction(
        name="living_room_door",
        interaction_type="interact",
        area=(149, 59, 203, 837),
        action="scene_4_interaction_2_return_to_living_room",
        completed="scene_4_interaction_2_living_room_door_done",
        mandatory=True
    ),

]


################################################################################
## D9 Interactions
################################################################################

define scene_4_interaction_2_d9_neck_objects = [

    Interaction(
        name="d9_neck",
        interaction_type="interact",
        area=(1046, 42, 217, 176),
        action="scene_4_interaction_2_d9_neck",
        completed="scene_4_interaction_2_d9_neck_done",
        mandatory=True
    ),

]


define scene_4_interaction_2_d9_clothed_objects = [

    Interaction(
        name="d9_clothed_torso",
        interaction_type="interact",
        area=(929, 185, 479, 901),
        action="scene_4_interaction_2_d9_clothed",
        completed="scene_4_interaction_2_d9_clothed_done",
        mandatory=True
    ),

]


define scene_4_interaction_2_d9_exposed_objects = [

    Interaction(
        name="d9_exposed_torso",
        interaction_type="interact",
        area=(929, 185, 479, 901),
        action="scene_4_interaction_2_d9_exposed",
        completed="scene_4_interaction_2_d9_exposed_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_2:

    call scene_4_interaction_2_kitchen_floor

    $ progress_interactions = scene_4_interaction_2_return_door_objects

    while not scene_4_interaction_2_living_room_door_done:

        call screen interaction_screen(
            scene_4_interaction_2_return_door_objects
        )

        call expression _return

    $ progress_interactions = scene_4_interaction_2_return_armchair_objects

    while not scene_4_interaction_2_return_armchair_done:

        call screen interaction_screen(
            scene_4_interaction_2_return_armchair_objects
        )

        call expression _return

    hide headshot_cait

    show expression scene_4_interaction_1_background("living_room") as bg at background_fixed

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Kitchen Floor
################################################################################

label scene_4_interaction_2_kitchen_floor:

    show expression scene_4_interaction_1_background("kitchen") as bg at background_freeze

    menu:

        "Dump D9":
            pass

    # TODO: Sound - Thud

    "Cait kneels over the paralyzed body."

    show headshot_cait focus at headshot_left, speaking
    cait "(This might get messy.)"

    hide headshot_cait

    menu:

        "Glove up":
            pass

    # TODO: Sound - Latex gloves

    show headshot_cait focus at headshot_left, speaking
    cait "(Much better.)"

    hide headshot_cait

    scene bg d9_clothed_torso at background_pan
    with fade

    $ progress_interactions = scene_4_interaction_2_d9_neck_objects

    while not scene_4_interaction_2_d9_neck_done:

        call screen interaction_screen(
            scene_4_interaction_2_d9_neck_objects
        )

        call expression _return

    $ progress_interactions = scene_4_interaction_2_d9_clothed_objects

    while not scene_4_interaction_2_d9_clothed_done:

        call screen interaction_screen(
            scene_4_interaction_2_d9_clothed_objects
        )

        call expression _return

    $ progress_interactions = scene_4_interaction_2_d9_exposed_objects

    while not scene_4_interaction_2_d9_exposed_done:

        call screen interaction_screen(
            scene_4_interaction_2_d9_exposed_objects
        )

        call expression _return

    scene expression scene_4_interaction_1_background("kitchen") as bg at background_freeze
    with fade

    show headshot_cait panic at headshot_left, speaking
    cait "(*huff* *huff*)"

    cait "(Ada.)"

    cait "(I need to get these to Ada.)"

    hide headshot_cait

    show expression scene_4_interaction_1_background("kitchen") as bg at background_pan

    $ progress_interactions = scene_4_interaction_2_return_door_objects

    return


################################################################################
## D9 Neck
################################################################################

label scene_4_interaction_2_d9_neck:

    if scene_4_interaction_2_d9_neck_done:
        return

    show bg d9_clothed_torso at background_freeze

    # TODO: Sound - Heartbeat

    show headshot_cait focus at headshot_left, speaking
    cait "(Still alive. That’s good.)"

    hide headshot_cait

    call single_blur

    show headshot_cait panic at headshot_left, speaking
    cait "(Can’t…)"

    hide headshot_cait

    call single_blur

    show headshot_cait panic at headshot_left, speaking
    cait "(Ugh…!)"

    hide headshot_cait

    call single_blur

    $ scene_4_interaction_2_memory_before = scene_4_memories_played

    menu:

        "Remember…":
            call scene_4_memory_next

        "Remember…":
            call scene_4_memory_next

        "Remember…":
            call scene_4_memory_next

        "Stay focused":
            pass

        "Remember…":
            call scene_4_memory_next

    if scene_4_memories_played > scene_4_interaction_2_memory_before:

        scene bg d9_clothed_torso at background_freeze
        with fade

    show headshot_cait panic at headshot_left, speaking
    cait "(Enough already!)"

    hide headshot_cait

    show bg d9_clothed_torso at background_pan

    $ scene_4_interaction_2_d9_neck_done = True

    return


################################################################################
## D9 Clothed Torso
################################################################################

label scene_4_interaction_2_d9_clothed:

    if scene_4_interaction_2_d9_clothed_done:
        return

    show bg d9_cut_torso at background_freeze

    # TODO: Sound - Tearing fabric

    $ renpy.pause(0.3, hard=True)

    show bg d9_exposed_torso at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(Liquid-access ports aren’t always in standard locations.)"

    cait "(I’ll need to find each of D9’s and pump her biofluids to Ada.)"

    show headshot_cait worry at headshot_left, speaking
    cait "(There’s not enough fluid for each of them…)"

    cait "(...)"

    cait "(I’m sorry.)"

    cait "(I wish I could have known you better.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(At least you won’t be in pain.)"

    hide headshot_cait

    show bg d9_exposed_torso at background_pan

    $ scene_4_interaction_2_d9_clothed_done = True

    return


################################################################################
## D9 Exposed Torso
################################################################################

label scene_4_interaction_2_d9_exposed:

    if scene_4_interaction_2_d9_exposed_done:
        return

    show bg d9_ports_torso at background_freeze

    # TODO: Sound - Gas release

    menu:

        "Hook up transfer tubes":
            pass

    show bg d9_tubes_torso at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(Thank you, D9.)"

    cait "(Now I can–)"

    hide headshot_cait

    call single_blur

    show headshot_cait panic at headshot_left, speaking
    cait "(Fuck!)"

    hide headshot_cait

    call single_blur

    show headshot_cait panic at headshot_left, speaking
    cait "(I–)"

    hide headshot_cait

    call single_blur

    $ scene_4_interaction_2_memories_to_play = 2 if scene_4_memories_played < 2 else 1

    menu:

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

    while scene_4_interaction_2_memories_to_play > 0:

        call scene_4_memory_next

        $ scene_4_interaction_2_memories_to_play -= 1

    $ scene_4_interaction_2_d9_exposed_done = True

    return


################################################################################
## Mandatory Return to Living Room
################################################################################

label scene_4_interaction_2_return_to_living_room:

    show expression scene_4_interaction_1_background("kitchen") as bg at background_freeze

    call single_blur

    show headshot_cait panic at headshot_left, speaking
    cait "(*huff* *huff*)"

    hide headshot_cait

    call single_blur

    show headshot_cait panic at headshot_left, speaking
    cait "(Just hold on…)"

    hide headshot_cait

    call single_blur

    $ scene_4_interaction_2_memories_to_play = 2 if scene_4_memories_played == 2 else 1

    menu:

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

        "REMEMBER.":
            pass

    while scene_4_interaction_2_memories_to_play > 0:

        call scene_4_memory_next

        $ scene_4_interaction_2_memories_to_play -= 1

    $ scene_4_interaction_2_living_room_door_done = True

    $ scene_4_interaction_2_room = "living_room"
    $ progress_interactions = scene_4_interaction_2_return_armchair_objects

    scene expression scene_4_interaction_1_background("living_room") as bg at background_pan
    with fade

    return


################################################################################
## Return to Armchair
################################################################################

label scene_4_interaction_2_return_armchair:

    if scene_4_interaction_2_return_armchair_done:
        return

    show expression scene_4_interaction_1_background("living_room") as bg at background_freeze

    show headshot_cait sweet at headshot_left, speaking
    cait "Hey there, baby."

    cait "I’ve got everything you need right here."

    cait "Let’s get you down on the floor so I can take care of you."

    hide headshot_cait

    $ scene_4_interaction_2_return_armchair_done = True

    show expression scene_4_interaction_1_background("living_room") as bg at background_fixed

    return

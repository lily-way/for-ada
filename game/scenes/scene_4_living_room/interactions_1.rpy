################################################################################
## Scene 4 - Interaction 1
################################################################################


################################################################################
## State
################################################################################

default scene_4_interaction_1_room = "living_room"

default scene_4_interaction_1_armchair_done = False
default scene_4_interaction_1_radio_done = False
default scene_4_interaction_1_window_done = False

default scene_4_interaction_1_kitchen_door_done = False
default scene_4_interaction_1_kitchen_floor_done = False

default scene_4_interaction_1_d9_neck_done = False
default scene_4_interaction_1_d9_clothed_done = False
default scene_4_interaction_1_d9_exposed_done = False

default scene_4_interaction_1_living_room_door_done = False
default scene_4_interaction_1_return_armchair_done = False


################################################################################
## Backgrounds
################################################################################

init python:

    def scene_4_interaction_1_background(room):

        return Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_4",
            (0, 0), "bg {}".format(room)
        )


################################################################################
## Living Room Interactions
################################################################################

define scene_4_interaction_1_living_room_objects = [

    Interaction(
        name="armchair",
        interaction_type="observe",
        area=(266, 487, 506, 533),
        action="scene_4_interaction_1_armchair",
        completed="scene_4_interaction_1_armchair_done",
        mandatory=False
    ),

    Interaction(
        name="radio",
        interaction_type="observe",
        area=(2059, 239, 229, 135),
        action="scene_4_interaction_1_radio",
        completed="scene_4_interaction_1_radio_done",
        mandatory=False
    ),

    Interaction(
        name="small_window",
        interaction_type="observe",
        area=(1350, 123, 106, 464),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_door",
        interaction_type="interact",
        area=(1640, 126, 187, 746),
        action="scene_4_interaction_1_go_to_kitchen",
        mandatory=False
    ),

]


################################################################################
## Living Room Interactions - After Extraction
################################################################################

define scene_4_interaction_1_living_room_return_objects = [

    Interaction(
        name="armchair",
        interaction_type="interact",
        area=(266, 487, 506, 533),
        action="scene_4_interaction_1_return_armchair",
        completed="scene_4_interaction_1_return_armchair_done",
        mandatory=True
    ),

    Interaction(
        name="radio",
        interaction_type="observe",
        area=(2059, 239, 229, 135),
        action="scene_4_interaction_1_radio",
        completed="scene_4_interaction_1_radio_done",
        mandatory=False
    ),

    Interaction(
        name="small_window",
        interaction_type="observe",
        area=(1350, 123, 106, 464),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_door",
        interaction_type="interact",
        area=(1640, 126, 187, 746),
        action="scene_4_interaction_1_go_to_kitchen",
        mandatory=False
    ),

]


################################################################################
## Kitchen Interactions
################################################################################

define scene_4_interaction_1_kitchen_objects = [

    Interaction(
        name="living_room_door",
        interaction_type="interact",
        area=(149, 59, 203, 837),
        action="scene_4_interaction_1_go_to_living_room",
        mandatory=False
    ),

    Interaction(
        name="kitchen_floor",
        interaction_type="interact",
        area=(650, 600, 1000, 500),
        action="scene_4_interaction_1_kitchen_floor",
        completed="scene_4_interaction_1_kitchen_floor_done",
        mandatory=True
    ),

    Interaction(
        name="kitchen_small_window_1",
        interaction_type="observe",
        area=(528, 140, 99, 459),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_2",
        interaction_type="observe",
        area=(1979, 161, 140, 375),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_3",
        interaction_type="observe",
        area=(2221, 141, 78, 368),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

]


################################################################################
## Kitchen Interactions - After Extraction
################################################################################

define scene_4_interaction_1_kitchen_return_objects = [

    Interaction(
        name="living_room_door",
        interaction_type="interact",
        area=(149, 59, 203, 837),
        action="scene_4_interaction_1_go_to_living_room",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_1",
        interaction_type="observe",
        area=(528, 140, 99, 459),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_2",
        interaction_type="observe",
        area=(1979, 161, 140, 375),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_3",
        interaction_type="observe",
        area=(2221, 141, 78, 368),
        action="scene_4_interaction_1_window",
        completed="scene_4_interaction_1_window_done",
        mandatory=False
    ),

]


################################################################################
## D9 Interactions
################################################################################

define scene_4_interaction_1_d9_neck_objects = [

    Interaction(
        name="d9_neck",
        interaction_type="interact",
        area=(800, 100, 500, 350),
        action="scene_4_interaction_1_d9_neck",
        completed="scene_4_interaction_1_d9_neck_done",
        mandatory=True
    ),

]


define scene_4_interaction_1_d9_clothed_objects = [

    Interaction(
        name="d9_clothed_torso",
        interaction_type="interact",
        area=(650, 350, 900, 650),
        action="scene_4_interaction_1_d9_clothed",
        completed="scene_4_interaction_1_d9_clothed_done",
        mandatory=True
    ),

]


define scene_4_interaction_1_d9_exposed_objects = [

    Interaction(
        name="d9_exposed_torso",
        interaction_type="interact",
        area=(650, 350, 900, 650),
        action="scene_4_interaction_1_d9_exposed",
        completed="scene_4_interaction_1_d9_exposed_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_1:

    $ scene_4_interaction_1_room = "living_room"
    $ progress_interactions = scene_4_interaction_1_living_room_objects
    $ progress_open = False

    scene expression scene_4_interaction_1_background("living_room") as bg at background_pan

    while not scene_4_interaction_1_return_armchair_done:

        if scene_4_interaction_1_room == "living_room":

            if scene_4_interaction_1_kitchen_floor_done:

                $ progress_interactions = scene_4_interaction_1_living_room_return_objects

                call screen interaction_screen(
                    scene_4_interaction_1_living_room_return_objects
                )

            else:

                $ progress_interactions = scene_4_interaction_1_living_room_objects

                call screen interaction_screen(
                    scene_4_interaction_1_living_room_objects
                )

        elif scene_4_interaction_1_room == "kitchen":

            if scene_4_interaction_1_kitchen_floor_done:

                $ progress_interactions = scene_4_interaction_1_kitchen_return_objects

                call screen interaction_screen(
                    scene_4_interaction_1_kitchen_return_objects
                )

            else:

                $ progress_interactions = scene_4_interaction_1_kitchen_objects

                call screen interaction_screen(
                    scene_4_interaction_1_kitchen_objects
                )

        call expression _return

    hide headshot_cait

    show expression scene_4_interaction_1_background("living_room") as bg at background_fixed

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Room Navigation - Kitchen
################################################################################

label scene_4_interaction_1_go_to_kitchen:

    if not scene_4_interaction_1_kitchen_door_done:

        show expression scene_4_interaction_1_background("living_room") as bg at background_freeze

        call single_blur

        show headshot_cait broken_extrabloody_pissed at headshot_left, speaking
        cait "(Ugh!)"

        hide headshot_cait

        call single_blur

        show headshot_cait broken_extrabloody_pissed at headshot_left, speaking
        cait "(Stay focused!)"

        hide headshot_cait

        call single_blur

        menu:

            "Remember…":
                call scene_4_memory_next

            "Stay focused":
                pass

            "Remember…":
                call scene_4_memory_next

        $ scene_4_interaction_1_kitchen_door_done = True

        play sound "audio/drag_body.ogg"

    $ scene_4_interaction_1_room = "kitchen"

    if scene_4_interaction_1_kitchen_floor_done:
        $ progress_interactions = scene_4_interaction_1_kitchen_return_objects
    else:
        $ progress_interactions = scene_4_interaction_1_kitchen_objects

    scene expression scene_4_interaction_1_background("kitchen") as bg at background_pan
    with fade

    return


################################################################################
## Room Navigation - Living Room
################################################################################

label scene_4_interaction_1_go_to_living_room:

    if (
        scene_4_interaction_1_kitchen_floor_done
        and not scene_4_interaction_1_living_room_door_done
    ):

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

        $ scene_4_interaction_1_memories_to_play = 2 if scene_4_memories_played == 2 else 1

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

        while scene_4_interaction_1_memories_to_play > 0:

            call scene_4_memory_next

            $ scene_4_interaction_1_memories_to_play -= 1

        $ scene_4_interaction_1_living_room_door_done = True

    $ scene_4_interaction_1_room = "living_room"

    if scene_4_interaction_1_kitchen_floor_done:
        $ progress_interactions = scene_4_interaction_1_living_room_return_objects
    else:
        $ progress_interactions = scene_4_interaction_1_living_room_objects

    scene expression scene_4_interaction_1_background("living_room") as bg at background_pan
    with fade

    return


################################################################################
## Armchair
################################################################################

label scene_4_interaction_1_armchair:

    if scene_4_interaction_1_armchair_done:
        return

    show expression scene_4_interaction_1_background("living_room") as bg at background_freeze

    show headshot_cait broken_extrabloody_sweet at headshot_left, speaking
    cait "Just a little longer, baby…"

    hide headshot_cait

    $ scene_4_interaction_1_armchair_done = True

    show expression scene_4_interaction_1_background("living_room") as bg at background_pan

    return


################################################################################
## Radio
################################################################################

label scene_4_interaction_1_radio:

    if scene_4_interaction_1_radio_done:
        return

    show expression scene_4_interaction_1_background("living_room") as bg at background_freeze

    show headshot_cait broken_extrabloody_focus at headshot_left, speaking
    cait "(It’s just static.)"

    cait "(Tuned to a dead channel.)"

    hide headshot_cait

    $ scene_4_interaction_1_radio_done = True

    show expression scene_4_interaction_1_background("living_room") as bg at background_pan

    return


################################################################################
## Small Windows
################################################################################

label scene_4_interaction_1_window:

    if scene_4_interaction_1_window_done:
        return

    show expression scene_4_interaction_1_background(
        scene_4_interaction_1_room
    ) as bg at background_freeze

    show headshot_cait broken_extrabloody_focus at headshot_left, speaking
    cait "(The storm’s coming down hard.)"

    cait "(It’ll be weeks before any new ships can dock planetside.)"

    hide headshot_cait

    $ scene_4_interaction_1_window_done = True

    show expression scene_4_interaction_1_background(
        scene_4_interaction_1_room
    ) as bg at background_pan

    return


################################################################################
## Kitchen Floor
################################################################################

label scene_4_interaction_1_kitchen_floor:

    if scene_4_interaction_1_kitchen_floor_done:
        return

    show expression scene_4_interaction_1_background("kitchen") as bg at background_freeze

    menu:

        "Dump D9":
            pass

    play sound "audio/thud.ogg"

    "Cait kneels over the paralyzed body."

    show headshot_cait broken_extrabloody_focus at headshot_left, speaking
    cait "(This might get messy.)"

    hide headshot_cait

    menu:

        "Glove up":
            pass

    play sound "audio/latex.ogg"

    show headshot_cait broken_extrabloody_focus at headshot_left, speaking
    cait "(Much better.)"

    hide headshot_cait

    scene bg kitchen_floor at background_fixed
    show d9 clothed_torso at truecenter
    with fade

    $ progress_interactions = scene_4_interaction_1_d9_neck_objects

    while not scene_4_interaction_1_d9_neck_done:

        call screen interaction_screen(
            scene_4_interaction_1_d9_neck_objects
        )

        call expression _return

    $ progress_interactions = scene_4_interaction_1_d9_clothed_objects

    while not scene_4_interaction_1_d9_clothed_done:

        call screen interaction_screen(
            scene_4_interaction_1_d9_clothed_objects
        )

        call expression _return

    $ progress_interactions = scene_4_interaction_1_d9_exposed_objects

    while not scene_4_interaction_1_d9_exposed_done:

        call screen interaction_screen(
            scene_4_interaction_1_d9_exposed_objects
        )

        call expression _return

    hide d9

    scene expression scene_4_interaction_1_background("kitchen") as bg at background_pan
    with fade

    show headshot_cait panic at headshot_left, speaking
    cait "(*huff* *huff*)"

    cait "(Ada.)"

    cait "(I need to get these to Ada.)"

    hide headshot_cait

    $ scene_4_interaction_1_kitchen_floor_done = True

    $ progress_interactions = scene_4_interaction_1_kitchen_return_objects

    return


################################################################################
## D9 Neck
################################################################################

label scene_4_interaction_1_d9_neck:

    if scene_4_interaction_1_d9_neck_done:
        return

    show bg kitchen_floor at background_fixed

    play sound "audio/heartbeat.ogg"

    show headshot_cait broken_extrabloody_focus at headshot_left, speaking
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

    $ scene_4_interaction_1_memory_before = scene_4_memories_played

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

    if scene_4_memories_played > scene_4_interaction_1_memory_before:

        scene bg kitchen_floor at background_fixed
        show d9 clothed_torso at truecenter
        with fade

    show headshot_cait panic at headshot_left, speaking
    cait "(Enough already!)"

    hide headshot_cait

    $ scene_4_interaction_1_d9_neck_done = True

    return


################################################################################
## D9 Clothed Torso
################################################################################

label scene_4_interaction_1_d9_clothed:

    if scene_4_interaction_1_d9_clothed_done:
        return

    show bg kitchen_floor at background_fixed

    hide d9

    show d9 cut_torso at truecenter

    play sound "audio/tearing_fabric.ogg"

    $ renpy.pause(0.3, hard=True)

    hide d9

    show d9 exposed_torso at truecenter

    show headshot_cait broken_extrabloody_focus at headshot_left, speaking
    cait "(Liquid-access ports aren’t always in standard locations.)"

    cait "(I’ll need to find each of D9’s and pump her biofluids to Ada.)"

    show headshot_cait worry at headshot_left, speaking
    cait "(There’s not enough fluid for each of them…)"

    cait "(...)"

    cait "(I’m sorry.)"

    cait "(I wish I could have known you better.)"

    show headshot_cait broken_extrabloody_focus at headshot_left, speaking
    cait "(At least you won’t be in pain.)"

    hide headshot_cait

    $ scene_4_interaction_1_d9_clothed_done = True

    return


################################################################################
## D9 Exposed Torso
################################################################################

label scene_4_interaction_1_d9_exposed:

    if scene_4_interaction_1_d9_exposed_done:
        return

    show bg kitchen_floor at background_fixed

    hide d9

    show d9 ports_torso at truecenter

    play sound "audio/gas_release.ogg"

    menu:

        "Hook up transfer tubes":
            pass

    hide d9

    show d9 tubes_torso at truecenter

    show headshot_cait broken_extrabloody_focus at headshot_left, speaking
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

    $ scene_4_interaction_1_memories_to_play = 2 if scene_4_memories_played < 2 else 1

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

    while scene_4_interaction_1_memories_to_play > 0:

        call scene_4_memory_next

        $ scene_4_interaction_1_memories_to_play -= 1

    $ scene_4_interaction_1_d9_exposed_done = True

    return


################################################################################
## Return to Armchair
################################################################################

label scene_4_interaction_1_return_armchair:

    if scene_4_interaction_1_return_armchair_done:
        return

    show expression scene_4_interaction_1_background("living_room") as bg at background_freeze

    show headshot_cait broken_extrabloody_sweet at headshot_left, speaking
    cait "Hey there, baby."

    cait "I’ve got everything you need right here."

    cait "Let’s get you down on the floor so I can take care of you."

    hide headshot_cait

    $ scene_4_interaction_1_return_armchair_done = True

    show expression scene_4_interaction_1_background("living_room") as bg at background_fixed

    return

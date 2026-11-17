################################################################################
## Scene 2 - Interaction 2
################################################################################


################################################################################
## State
################################################################################

default scene_2_interaction_2_small_window_done = False
default scene_2_interaction_2_oven_done = False
default scene_2_interaction_2_counter_done = False

default scene_2_interaction_2_menu_card_done = False
default scene_2_interaction_2_rabbit_selected = False

default scene_2_interaction_2_rabbit_done = False
default scene_2_interaction_2_broth_done = False
default scene_2_interaction_2_vegetables_done = False

default scene_2_interaction_2_apiaceae_cut = False
default scene_2_interaction_2_crucifer_cut = False

default scene_2_interaction_2_pot_done = False


################################################################################
## Countertop Composition
################################################################################

init python:

    def scene_2_interaction_2_countertop(*overlays):

        layers = [
            (0, 0), "bg countertop_pot_open"
        ]

        if scene_2_interaction_2_vegetables_done:
            layers.extend([
                (0, 0), "ingredient_veggies_pot"
            ])

        if scene_2_interaction_2_broth_done:
            layers.extend([
                (0, 0), "ingredient_broth"
            ])

        if scene_2_interaction_2_rabbit_done:
            layers.extend([
                (0, 0), "ingredient_rabbit_pot"
            ])

        for overlay in overlays:
            layers.extend([
                (0, 0), overlay
            ])

        return Composite(
            (2300, 1200),
            *layers
        )


################################################################################
## Interactions
################################################################################

define scene_2_interaction_2_objects = [

    Interaction(
        name="kitchen_small_window_1",
        interaction_type="observe",
        area=(528, 140, 99, 459),
        action="scene_2_interaction_2_small_window",
        completed="scene_2_interaction_2_small_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_2",
        interaction_type="observe",
        area=(1979, 161, 140, 375),
        action="scene_2_interaction_2_small_window",
        completed="scene_2_interaction_2_small_window_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_3",
        interaction_type="observe",
        area=(2221, 141, 78, 368),
        action="scene_2_interaction_2_small_window",
        completed="scene_2_interaction_2_small_window_done",
        mandatory=False
    ),

    Interaction(
        name="oven",
        interaction_type="observe",
        area=(1670, 715, 210, 192),
        action="scene_2_interaction_2_oven",
        completed="scene_2_interaction_2_oven_done",
        mandatory=False
    ),

    Interaction(
        name="kitchen_counter",
        interaction_type="interact",
        area=(1471, 537, 574, 116),
        action="scene_2_interaction_2_counter",
        completed="scene_2_interaction_2_counter_done",
        mandatory=True
    ),

]


################################################################################
## Cooking Interactions
################################################################################

define scene_2_interaction_2_menu_card_objects = [

    Interaction(
        name="menu_card",
        interaction_type="interact",
        area=(352, 9, 301, 188),
        action="scene_2_interaction_2_menu_card",
        completed="scene_2_interaction_2_menu_card_done",
        mandatory=True
    ),

]

define scene_2_interaction_2_rabbit_objects = [

    Interaction(
        name="rabbit",
        interaction_type="interact",
        area=(372, 444, 694, 404),
        action="scene_2_interaction_2_rabbit_cut",
        completed="scene_2_interaction_2_rabbit_selected",
        mandatory=True
    ),

]

define scene_2_interaction_2_rabbit_cut_objects = [

    Interaction(
        name="rabbit_cut",
        interaction_type="interact",
        area=(314, 311, 855, 651),
        action="scene_2_interaction_2_rabbit_pot",
        completed="scene_2_interaction_2_rabbit_done",
        mandatory=True
    ),

]

define scene_2_interaction_2_apiaceae_objects = [

    Interaction(
        name="apiaceae",
        interaction_type="interact",
        area=(370, 202, 330, 761),
        action="scene_2_interaction_2_cut_apiaceae",
        completed="scene_2_interaction_2_apiaceae_cut",
        mandatory=True
    ),

]

define scene_2_interaction_2_crucifer_objects = [

    Interaction(
        name="crucifer",
        interaction_type="interact",
        area=(648, 352, 546, 556),
        action="scene_2_interaction_2_cut_crucifer",
        completed="scene_2_interaction_2_crucifer_cut",
        mandatory=True
    ),

]

define scene_2_interaction_2_vegetables_cut_objects = [

    Interaction(
        name="vegetables_cut",
        interaction_type="interact",
        area=(442, 334, 599, 522),
        action="scene_2_interaction_2_vegetables_pot",
        completed="scene_2_interaction_2_vegetables_done",
        mandatory=True
    ),

]

define scene_2_interaction_2_pot_objects = [

    Interaction(
        name="pot",
        interaction_type="interact",
        area=(1374, 367, 585, 583),
        action="scene_2_interaction_2_pot",
        completed="scene_2_interaction_2_pot_done",
        mandatory=True
    ),

]


################################################################################
## Progress Interactions
################################################################################

define scene_2_interaction_2_kitchen_progress_objects = [
    scene_2_interaction_2_objects[0],
    scene_2_interaction_2_objects[3],
    scene_2_interaction_2_objects[4]
]


define scene_2_interaction_2_vegetable_progress_objects = (
    scene_2_interaction_2_apiaceae_objects
    + scene_2_interaction_2_crucifer_objects
)


################################################################################
## Kitchen Exploration
################################################################################

label scene_2_interaction_2:

    $ progress_interactions = scene_2_interaction_2_kitchen_progress_objects
    $ progress_open = False

    if scene_2_interaction_1_room == "living_room":

        scene expression Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_3",
            (0, 0), "bg kitchen"
        ) as bg at background_pan
        with fade

    else:

        show expression Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_3",
            (0, 0), "bg kitchen"
        ) as bg at background_pan

    while not scene_2_interaction_2_counter_done:

        call screen interaction_screen(scene_2_interaction_2_objects)
        call expression _return

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Optional Observation - Small Windows
################################################################################

label scene_2_interaction_2_small_window:

    if scene_2_interaction_2_small_window_done:
        return

    show expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_3",
        (0, 0), "bg kitchen"
    ) as bg at background_freeze

    show headshot_cait worry at headshot_left, speaking
    cait "(Looks like a storm’s rolling in tonight...)"

    show headshot_cait focus at headshot_left, speaking
    cait "(It’s getting late. I should get started on dinner.)"

    hide headshot_cait

    $ scene_2_interaction_2_small_window_done = True

    show expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_3",
        (0, 0), "bg kitchen"
    ) as bg at background_pan

    return


################################################################################
## Optional Observation - Oven
################################################################################

label scene_2_interaction_2_oven:

    if scene_2_interaction_2_oven_done:
        return

    show expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_3",
        (0, 0), "bg kitchen"
    ) as bg at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(I don’t need to toast the bread until just before we eat.)"

    hide headshot_cait

    $ scene_2_interaction_2_oven_done = True

    show expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_3",
        (0, 0), "bg kitchen"
    ) as bg at background_pan

    return


################################################################################
## Mandatory Interaction - Kitchen Counter
################################################################################

label scene_2_interaction_2_counter:

    if scene_2_interaction_2_counter_done:
        return

    scene expression scene_2_interaction_2_countertop() as bg at background_fixed
    with fade

    show headshot_cait focus at headshot_left, speaking
    cait "(I need to slice up the vegetables, as well as the g-13.)"
    cait "(Where to start?)"

    hide headshot_cait

    label .ingredient_menu:

        if (
            scene_2_interaction_2_vegetables_done
            and scene_2_interaction_2_broth_done
            and scene_2_interaction_2_rabbit_done
        ):
            jump .close_pot

        $ scene_2_interaction_2_menu_card_done = False
        $ progress_interactions = scene_2_interaction_2_menu_card_objects

        show expression scene_2_interaction_2_countertop() as bg at background_pan

        call screen interaction_screen(scene_2_interaction_2_menu_card_objects)
        call expression _return

        menu:

            "Vegetables" if not scene_2_interaction_2_vegetables_done:
                show expression scene_2_interaction_2_countertop() as bg at background_pan
                call scene_2_interaction_2_vegetables
                jump .ingredient_menu

            "Soup stock" if not scene_2_interaction_2_broth_done:
                show expression scene_2_interaction_2_countertop() as bg at background_pan
                call scene_2_interaction_2_broth
                jump .ingredient_menu

            "G-13 carcass" if not scene_2_interaction_2_rabbit_done:
                show expression scene_2_interaction_2_countertop() as bg at background_pan
                call scene_2_interaction_2_rabbit
                jump .ingredient_menu

    label .close_pot:

        $ progress_interactions = scene_2_interaction_2_pot_objects

        show expression scene_2_interaction_2_countertop() as bg at background_pan

        while not scene_2_interaction_2_pot_done:

            call screen interaction_screen(scene_2_interaction_2_pot_objects)
            call expression _return

        $ scene_2_interaction_2_counter_done = True

        return


################################################################################
## Cooking Interaction - Menu Card
################################################################################

label scene_2_interaction_2_menu_card:

    show expression scene_2_interaction_2_countertop() as bg at background_freeze

    $ scene_2_interaction_2_menu_card_done = True

    return


################################################################################
## Cooking Interaction - Rabbit
################################################################################

label scene_2_interaction_2_rabbit:

    $ progress_interactions = scene_2_interaction_2_rabbit_objects

    show expression scene_2_interaction_2_countertop(
        "ingredient_rabbit"
    ) as bg at background_pan

    call screen interaction_screen(scene_2_interaction_2_rabbit_objects)
    call expression _return

    return


label scene_2_interaction_2_rabbit_cut:

    $ scene_2_interaction_2_rabbit_selected = True

    show expression scene_2_interaction_2_countertop(
        "ingredient_rabbit"
    ) as bg at background_freeze

    menu:

        "Butcher G-13":

            $ progress_interactions = scene_2_interaction_2_rabbit_cut_objects

            show expression scene_2_interaction_2_countertop(
                "ingredient_rabbit_cut"
            ) as bg at background_pan
            with Fade(0.3, 0.5, 0.3)

            call screen interaction_screen(scene_2_interaction_2_rabbit_cut_objects)
            call expression _return

    return


label scene_2_interaction_2_rabbit_pot:

    $ scene_2_interaction_2_rabbit_done = True

    show expression scene_2_interaction_2_countertop() as bg at background_pan

    return


################################################################################
## Cooking Interaction - Broth
################################################################################

label scene_2_interaction_2_broth:

    $ scene_2_interaction_2_broth_done = True

    show expression scene_2_interaction_2_countertop() as bg at background_pan

    return


################################################################################
## Cooking Interaction - Vegetables
################################################################################

label scene_2_interaction_2_vegetables:

    $ progress_interactions = scene_2_interaction_2_vegetable_progress_objects

    show expression scene_2_interaction_2_countertop(
        "ingredient_apiaceae",
        "ingredient_crucifer"
    ) as bg at background_pan

    while not (
        scene_2_interaction_2_apiaceae_cut
        and scene_2_interaction_2_crucifer_cut
    ):

        $ vegetable_interactions = []

        if not scene_2_interaction_2_apiaceae_cut:
            $ vegetable_interactions += scene_2_interaction_2_apiaceae_objects

        if not scene_2_interaction_2_crucifer_cut:
            $ vegetable_interactions += scene_2_interaction_2_crucifer_objects

        call screen interaction_screen(vegetable_interactions)
        call expression _return

    $ progress_interactions = scene_2_interaction_2_vegetables_cut_objects

    show expression scene_2_interaction_2_countertop(
        "ingredient_apiaceae_cut",
        "ingredient_crucifer_cut"
    ) as bg at background_pan

    call screen interaction_screen(scene_2_interaction_2_vegetables_cut_objects)
    call expression _return

    return


label scene_2_interaction_2_cut_apiaceae:

    $ scene_2_interaction_2_apiaceae_cut = True

    if scene_2_interaction_2_crucifer_cut:

        show expression scene_2_interaction_2_countertop(
            "ingredient_apiaceae_cut",
            "ingredient_crucifer_cut"
        ) as bg at background_pan

    else:

        show expression scene_2_interaction_2_countertop(
            "ingredient_apiaceae_cut",
            "ingredient_crucifer"
        ) as bg at background_pan

    return


label scene_2_interaction_2_cut_crucifer:

    $ scene_2_interaction_2_crucifer_cut = True

    if scene_2_interaction_2_apiaceae_cut:

        show expression scene_2_interaction_2_countertop(
            "ingredient_apiaceae_cut",
            "ingredient_crucifer_cut"
        ) as bg at background_pan

    else:

        show expression scene_2_interaction_2_countertop(
            "ingredient_apiaceae",
            "ingredient_crucifer_cut"
        ) as bg at background_pan

    return


label scene_2_interaction_2_vegetables_pot:

    $ scene_2_interaction_2_vegetables_done = True

    show expression scene_2_interaction_2_countertop() as bg at background_pan

    return


################################################################################
## Mandatory Interaction - Pot
################################################################################

label scene_2_interaction_2_pot:

    scene bg countertop_pot_closed at background_freeze

    # play sound "audio/pot_clank.mp3"

    show headshot_cait smile at headshot_left, speaking
    cait "(And it all goes in the dutch oven.)"

    show headshot_cait sweet at headshot_left, speaking
    cait "(Ada told me once about the history of this pot’s name.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(According to her, ‘Dutch’ refers to an ancient, warring civilization on homeworld.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(I’ve never understood how people could fight over a region as small as a planet.)"
    cait "(Take Chaff-6, for example.)"
    cait "(Sure, homesteads might have their squabbles…)"
    cait "(But war takes money. Influence. Reach.)"
    cait "(People.)"
    cait "(How could one person go to war against another, even if they wanted to?)"
    cait "(It seems far more likely that an act of violence would simply go unnoticed rather than be repaid in kind.)"

    hide headshot_cait

    $ scene_2_interaction_2_pot_done = True

    return

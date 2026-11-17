################################################################################
## Scene 2 - Dialogue 2
################################################################################

label scene_2_dialogue_2:
    if scene_2_interaction_1_room == "living_room":
        scene expression Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_3",
            (0, 0), "bg living_room"
        ) as bg at background_freeze
    else:
        scene expression Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_3",
            (0, 0), "bg kitchen"
        ) as bg at background_freeze

    show headshot_ada neutral at headshot_right, speaking
    ada "Cait?"

    hide headshot_ada
    show headshot_cait focus at headshot_left, speaking
    cait "Yes, baby?"

    hide headshot_cait
    show headshot_ada neutral at headshot_right, speaking
    ada "I think I’m feeling well enough to eat."

    ada "Do you need any help in the kitchen?"

    hide headshot_ada
    show headshot_cait sweet at headshot_left, speaking
    cait "Absolutely not."

    cait "Stay right where you are."

    show headshot_cait smile at headshot_left, speaking
    cait "I’ll have dinner ready in about an hour."

    hide headshot_cait
    show headshot_ada thoughtful at headshot_right, speaking
    ada "Feels so weird to not be doing any of the cooking…"

    ada "Are you sure I can’t whip up a flatbread or something?"

    hide headshot_ada
    show headshot_cait sweet at headshot_left, speaking
    cait "No."

    hide headshot_cait
    show headshot_ada thoughtful at headshot_right, speaking
    ada "I guess I’ll just keep reading…"

    hide headshot_ada

    return

################################################################################
## Scene 3 - Dialogue 3
################################################################################

label scene_3_dialogue_3:

    scene expression Solid("#000000")
    with Dissolve(0.5)

    "Cait didn’t look up when she heard the footsteps coming down the staircase."
    "Or even when she heard the guttural scream that followed."
    "All the grocer’s wife saw a dark figure hunched over the bloodied body of her husband, pulling sinewy organs from his open chest."
    "Cait finished relieving the man of his lungs and stood up to her full height over him."
    "She looked old, strong, and weathered."
    "Every year of farm work was visible in her arms and shoulders."
    "The reserved academic that the grocers knew before seemed to have disappeared."

    scene bg interior_grocery_store_night at background_fixed
    with Dissolve(0.5)

    show martins_wife horror at sprite_middle, speaking
    martins_wife "Martin!!!!!!!"
    martins_wife "D9, protection mode!!!"

    show martins_wife horror at sprite_middle, not_speaking
    show headshot_cait focus at headshot_left, speaking
    cait "(Better pack these up.)"

    hide headshot_cait

    menu:
        "Place lungs in cooler":
            pass

    # play sound "audio/gas_release.mp3"

    show martins_wife horror at sprite_middle, speaking
    martins_wife "D9!!! Priority one, protection mode!!!"

    show martins_wife horror at sprite_middle, not_speaking
    show headshot_cait focus at headshot_left, speaking
    cait "(And I need my tools.)"

    hide headshot_cait

    menu:
        "Retrieve garden spade from Martin’s neck":
            pass

    # play sound "audio/stab.mp3"

    show martins_wife horror at sprite_middle, speaking
    martins_wife "D9, please–"

    show martins_wife horror at sprite_middle, not_speaking
    show headshot_cait focus at headshot_left, speaking
    cait "Don’t bother."
    cait "She can’t hear you."

    hide headshot_cait

    menu:

        "Hit her in the head":

            # play sound "audio/crack_thunk.mp3"

            show martins_wife headbleed at sprite_middle, speaking
            martins_wife "Huhhhhh…"

            show martins_wife headbleed at sprite_middle, not_speaking

            menu:
                "Hit her again":
                    pass

            # play sound "audio/crunch.mp3"

            show martins_wife headbleed at sprite_middle, speaking
            martins_wife "Hnnnnhhh…"

        "Stab her in the eye":

            # play sound "audio/eyesquish.mp3"

            show martins_wife eyebleed at sprite_middle, speaking
            martins_wife "EeeeaaAAAAAA!!!!"

            show martins_wife eyebleed at sprite_middle, not_speaking

            menu:
                "Push it deeper":
                    pass

            # play sound "audio/brainsquish.mp3"

            show martins_wife eyebleed at sprite_middle, speaking
            martins_wife "Eeeeeeeuhhhhh…"

    hide martins_wife

    "(Cait catches the body before it falls, setting it gently on the floor.)"

    scene expression Solid("#000000")
    with Dissolve(0.5)

    return

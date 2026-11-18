################################################################################
## Scene 4 - Dialogue 2 — Taking Ada to Bed
################################################################################


################################################################################
## Scene
################################################################################

label scene_4_dialogue_2:

    scene expression Solid("#000000")
    with fade

    menu:

        "Take her to bed":
            pass

    "Cait gently picked up Ada and carried her back to their bedroom."

    "She dressed her in pajamas and laid her delicately in a nest of blankets before opening the curtains to let the morning light in."

    "The weight of the day was heavy on Cait’s shoulders."

    "It chained her feet to the floor, caused her back to slouch and her knees to buckle."

    "But still she was not done."

    "Cait walked back towards the bed."

    "She placed both hands on Ada’s chest in the way she had so many times before."

    "Briefly, her chest pulsed with blue light."

    show headshot_ada sleepy at headshot_right, speaking
    ada "..."

    ada "Hnnh..."

    hide headshot_ada

    # TODO: Fade to bedtime_still and pan upward when artwork is available.
    # For now, keep the background black.

    "Ada briefly squinted her eyes open to see Cait haggard and exhausted above her."

    "Blindly, she grabbed her and pulled her deep into bed."

    "Cait’s body relaxed against hers as they drifted into early morning sleep."

    return

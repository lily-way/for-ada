################################################################################
## Scene 2 - Dialogue 3
################################################################################

label scene_2_dialogue_3:
    scene expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_4",
        (0, 0), "bg living_room"
    ) as bg at background_fixed
    with Dissolve(0.5)

    show headshot_cait focus at headshot_left, speaking
    cait "..."
    cait "(How long has it been…)"
    cait "(Martin.)"
    cait "(He can help.)"
    cait "(He has to help…)"
    cait "(I need to get my tools…)"

    hide headshot_cait

    menu:

        "Grab tools":

            play sound "audio/sound_effects/gather_tools.mp3"
            play sound "audio/sound_effects/zipper.mp3"

            pause 6.0

            show headshot_cait focus at headshot_left, speaking
            cait "(I have what I need.)"
            cait "(I need to go.)"
            cait "(Now.)"

            hide headshot_cait

    return

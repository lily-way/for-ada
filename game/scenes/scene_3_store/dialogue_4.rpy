################################################################################
## Scene 3 - Dialogue 4
################################################################################

label scene_3_dialogue_4:

    scene bg store at background_fixed
    with fade

    show headshot_cait smile at headshot_left, speaking
    cait "(Now I can save her…)"

    show headshot_cait focus at headshot_left, speaking
    cait "(But she’ll need live fluids…)"
    cait "(Hm…)"

    hide headshot_cait

    menu:
        "Drag D9 away":
            pass

    show headshot_cait focus at headshot_left, speaking
    cait "(You’ll do.)"

    hide headshot_cait

    # play sound "audio/thud.mp3"

    show headshot_cait focus at headshot_left, speaking
    cait "(I’m coming home, baby…)"

    show headshot_cait smile at headshot_left, speaking
    cait "(You’ll be alright.)"

    hide headshot_cait

    scene expression Solid("#000000")
    with fade

    # play music "audio/body_drag_loop.mp3"
    # play sound "audio/rainstorm.mp3" loop

    show headshot_cait focus at headshot_left, speaking
    cait "*huff* *huff*"

    show headshot_cait panic at headshot_left, speaking
    cait "(Fuck…)"
    cait "(Martin…)"
    cait "(They’re all dead…)"
    cait "(I’m a monster…)"
    cait "(...)"

    show headshot_cait focus at headshot_left, speaking
    cait "(...)"
    cait "(It’s worth it.)"
    cait "(For Ada.)"
    cait "(My Ada.)"

    hide headshot_cait

    return

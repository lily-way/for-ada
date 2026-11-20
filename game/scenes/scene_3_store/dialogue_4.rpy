################################################################################
## Scene 3 - Dialogue 4
################################################################################

label scene_3_dialogue_4:

    scene bg store at background_fixed
    with fade

    show headshot_cait bloody_focus at headshot_left, speaking
    cait "(It's done.)"

    show headshot_cait bloody_smile at headshot_left, speaking
    cait "(Now I can save her…)"

    show headshot_cait bloody_focus at headshot_left, speaking
    cait "(But she’ll need live fluids…)"
    cait "(Hm…)"

    hide headshot_cait

    menu:
        "Drag D9 away":
            pass

    show headshot_cait bloody_focus at headshot_left, speaking
    cait "(You’ll do.)"

    hide headshot_cait

    play sound "audio/sound_effects/drag_body.mp3"

    pause 1.0

    show headshot_cait bloody_focus at headshot_left, speaking
    cait "(I’m coming home, baby…)"

    show headshot_cait bloody_smile at headshot_left, speaking
    cait "(You’ll be alright.)"

    hide headshot_cait

    scene expression Solid("#000000")
    with fade

    play sound "audio/loops/drag_body_loop.mp3" loop
    play sound "audio/loops/rainstorm.mp3" loop

    pause 3.0

    show headshot_cait bloody_focus at headshot_left, speaking
    cait "*huff* *huff*"

    show headshot_cait bloody_panic at headshot_left, speaking
    cait "(Fuck…)"
    cait "(Martin…)"
    cait "(They’re all dead…)"
    cait "(I’m a monster…)"
    cait "(...)"

    show headshot_cait bloody_focus at headshot_left, speaking
    cait "(...)"
    cait "(It’s worth it.)"
    cait "(For Ada.)"
    cait "(My Ada.)"

    hide headshot_cait

    pause 2.0

    return

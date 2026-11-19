################################################################################
## Scene 4 - Dialogue 1
################################################################################

label scene_4_dialogue_1:
    scene expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_4",
        (0, 0), "bg living_room"
    ) as bg at background_fixed
    with fade

    show headshot_cait focus at headshot_left, speaking
    cait "*huff* *huff*"

    show headshot_cait sweet at headshot_left, speaking
    cait "Baby, I’m home."

    cait "Let’s get you some fluids, yeah?"

    cait "This will be over soon."

    hide headshot_cait

    call single_blur

    show headshot_cait PO at headshot_left, speaking
    cait "(Ugh…)"

    hide headshot_cait

    call single_blur

    show headshot_cait PO at headshot_left, speaking
    cait "(I can’t get distracted…)"

    hide headshot_cait

    call single_blur

    show headshot_cait PO at headshot_left, speaking
    cait "(Not now…)"

    hide headshot_cait

    show layer master:
        linear 0.2 blur 12

    $ renpy.pause(0.2, hard=True)

    menu:

        "Stay focused":

            $ renpy.pause(0.2, hard=True)

            show layer master:
                linear 0.2 blur 0

            $ renpy.pause(0.2, hard=True)

            show layer master

    show headshot_cait focus at headshot_left, speaking
    cait "(Come on. I can do this.)"

    cait "(I’ll set up in the kitchen.)"

    hide headshot_cait

    return

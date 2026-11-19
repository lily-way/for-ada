################################################################################
## Scene 4 - Interaction 3 — Opening Ada
################################################################################


################################################################################
## Camera
################################################################################

transform scene_4_interaction_3_pan_down:

    xalign 0.5
    yalign 0.0

    linear 1.0 yalign 1.0


################################################################################
## Scene
################################################################################

label scene_4_interaction_3:

    $ progress_interactions = None
    $ progress_open = False

    scene bg ada_hand_1 at background_fixed
    with fade

    show headshot_cait sweet at headshot_left, speaking
    cait "There you are."

    cait "My Ada."

    cait "Show me how you’re doing, yeah?"

    hide headshot_cait

    menu:

        "Open her up":
            pass

    scene bg ada_hand_2 at background_fixed
    with fade

    call single_blur

    show headshot_cait sweet at headshot_left, speaking
    cait "You’re perfect."

    hide headshot_cait

    call single_blur

    show headshot_cait sweet at headshot_left, speaking
    cait "So full of life."

    hide headshot_cait

    call single_blur

    menu:

        "REMEMBER.":
            call scene_4_memory_next

    scene bg ada_hand_2 at background_fixed
    with fade

    show headshot_cait sweet at headshot_left, speaking
    cait "I’ll never get tired of doing this, Ada."

    cait "No matter the cost."

    cait "Nothing could be worth more than two more years with you."

    hide headshot_cait

    menu:

        "Fix Ada":
            pass

    scene bg ada_hand_2 at scene_4_interaction_3_pan_down

    $ renpy.pause(1.0, hard=True)

    scene bg ada_healthy_neither at background_fixed
    with fade

    show headshot_cait worry at headshot_left, speaking
    cait "My poor baby."

    cait "I should have taken care of this sooner."

    show headshot_cait sweet at headshot_left, speaking
    cait "Don’t worry now, okay?"

    hide headshot_cait

    call single_blur

    show headshot_cait sweet at headshot_left, speaking
    cait "We’ve come so far together."

    hide headshot_cait

    call single_blur

    show headshot_cait sweet at headshot_left, speaking
    cait "We’ve grown so much."

    hide headshot_cait

    call single_blur

    show headshot_cait sweet at headshot_left, speaking
    cait "I’ll save you every time."

    hide headshot_cait

    return

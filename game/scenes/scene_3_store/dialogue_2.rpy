################################################################################
## Scene 3 - Dialogue 2
################################################################################

label scene_3_dialogue_2:

    hide D9_eye_whites

    scene bg interior_grocery_store_night at background_fixed
    with fade

    show headshot_cait focus at headshot_left, speaking
    cait "(Now D9 is calm…)"
    cait "(But Ada still needs help.)"
    cait "(Martin can help us.)"

    show headshot_cait panic at headshot_left, speaking
    cait "Martin?! Are you there?!"

    hide headshot_cait

    martin "Shit! Cait, is that you?"

    show headshot_cait panic at headshot_left, speaking
    cait "Ada has taken a turn for the worse. I need your help!"

    hide headshot_cait

    play sound "audio/sound_effects/stairs_martin.mp3"

    pause 4.5

    show martin PJs_concerned at sprite_middle, not_speaking

    show martin PJs_concerned at sprite_middle, speaking
    martin "What happened? Is she okay?"

    show martin PJs_concerned at sprite_middle, not_speaking
    show headshot_cait panic at headshot_left, speaking
    cait "She just started coughing and coughing…"
    cait "And then…"
    cait "There was so much blood, Martin!"

    hide headshot_cait

    show martin PJs_concerned at sprite_middle, speaking
    martin "Hey, hey, hey."

    "(Martin swoops Cait into a tight hug.)"

    show martin PJs_concerned at sprite_middle, speaking
    martin "We’re going to figure this out."
    martin "We won’t let her die."
    martin "She deserves better, and you are going to give that to her."

    show martin PJs_concerned at sprite_middle, not_speaking
    show headshot_cait smile at headshot_left, speaking
    cait "Yeah?"

    hide headshot_cait

    show martin PJs_neutral at sprite_middle, speaking
    martin "Absolutely."

    show martin PJs_neutral at sprite_middle, not_speaking
    show headshot_cait smile at headshot_left, speaking
    cait "(He’s so kind…)"
    cait "(Together, we can save her.)"
    cait "(I can save her.)"

    hide headshot_cait

    show martin PJs_neutral at sprite_middle, speaking
    martin "Now, use that big, educated brain of yours."
    martin "What does she need?"

    show martin PJs_neutral at sprite_middle, speaking
    show headshot_cait focus at headshot_left, speaking
    cait "Lungs."

    hide headshot_cait

    menu:
        "Stab him":
            pass

    play sound "audio/sound_effects/stab_martin_1.mp3"

    show martin horror_1 at sprite_middle, speaking
    martin "Hrrk!"

    menu:
        "Stab him":
            pass

    play sound "audio/sound_effects/stab_martin_2.mp3"

    show martin horror_2 at sprite_middle, speaking
    martin "Ghhhhhhhk!"
    
    menu:
        "Stab him":
            pass

    play sound "audio/sound_effects/stab_martin_3.mp3"

    show martin horror_3 at sprite_middle, speaking
    martin "hhhhAAAAAAAAAAAAA!!!!!!!!!!!!!!!"

    hide martin

    play sound "audio/sound_effects/body_thud.mp3"

    pause 1.5

    return

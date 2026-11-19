################################################################################
## Scene 1 - Dialogue 1
################################################################################

label scene_1_dialogue_1:

    pause 3.0

    scene expression Solid("#000000")
    show expression Text("Chaff-6", size=100, color="#FFFFFF") as chapter_title:
        xalign 0.5
        yalign 0.5
    with fade

    pause 3.0

    scene expression Solid("#000000")

    play sound "audio/sound_effects/shop_door_bell.mp3"
    $ duration = renpy.music.get_duration("sound")
    $ renpy.pause(duration, hard=True)

    scene bg store at background_fixed
    with fade

    show martin laugh at sprite_middle(y=45), speaking
    with fade

    $ renpy.pause(0.1, hard=True)

    martin "There she is! My favorite recluse!"

    show martin neutral at sprite_middle(y=45), speaking
    martin "It's good to see you, Cait."

    show martin neutral at sprite_middle(y=45), not_speaking
    show headshot_cait smile at headshot_left, speaking
    cait "Morning, Martin. You're looking well."

    hide headshot_cait
    show martin laugh at sprite_middle(y=45), speaking
    martin "I should hope so! Kicked the old smokin' habit, and the doctor gave me a fresh set of lungs just last week."

    show martin laugh at sprite_middle(y=45), not_speaking
    show headshot_cait smile at headshot_left, speaking
    cait "Well, I'm glad you're feeling better."
    cait "Say, do you happen to have any homeworld wine in stock today? Ada and I are celebrating an anniversary."

    hide headshot_cait
    show martin laugh at sprite_middle(y=45), speaking
    martin "It's your lucky day! We should still have a few cases on the back shelf from the last shipment, if I didn't nab too many for myself and the missus."

    show martin neutral at sprite_middle(y=45), speaking
    martin "And send my congratulations to Ada. How long has it been? A decade? More?"

    show martin neutral at sprite_middle(y=45), not_speaking
    show headshot_cait smile at headshot_left, speaking
    cait "Fifteen years. Thanks, Martin. I'll let her know."

    hide headshot_cait
    
    hide martin
    with fade

    return

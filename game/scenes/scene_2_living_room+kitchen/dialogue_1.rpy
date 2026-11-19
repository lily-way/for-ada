################################################################################
## Scene 2 - Dialogue 1
################################################################################

label scene_2_dialogue_1:

    pause 1.0

    scene expression Solid("#000000")
    with fade
    play sound "audio/sound_effects/door_close.mp3"
    pause 0.8

    scene expression Composite(
        (2300, 1200),
        (0, 0), "bg light_cycle_0",
        (0, 0), "bg living_room"
    ) as bg at background_fixed
    with fade

    show ada sleepy at sprite_right, speaking

    show headshot_cait smile at headshot_left, speaking
    cait "Ada? Are you awake?"

    hide headshot_cait
    show ada sleepy at sprite_right, speaking
    ada "Zzz… Hnnnh?"

    show ada sleepy at sprite_right, not_speaking
    show headshot_cait sweet at headshot_left, speaking
    cait "Oh, I see."

    hide headshot_cait
    show ada sleepy at sprite_right, speaking
    ada "No… I’m awake…"
    ada "I must have dozed off while reading…"

    show ada sick at sprite_right, speaking
    ada "*cough* *cough*"

    show ada sick at sprite_right, not_speaking
    show headshot_cait worry at headshot_left, speaking
    cait "Poor thing. Let me check your temperature."

    hide headshot_cait

    "Cait presses her cupped hand over Ada’s forehead."

    show headshot_cait worry at headshot_left, speaking
    cait "(She’s burning up. Seems like the sickness is getting worse.)"
    cait "Are you feeling any better today?"

    hide headshot_cait
    show ada mischief at sprite_right, speaking
    ada "Much better now that you’re here."

    show ada mischief at sprite_right, not_speaking
    show headshot_cait sweet at headshot_left, speaking
    cait "..."
    cait "Whatever you say, heartbreaker."

    show headshot_cait focus at headshot_left, speaking
    cait "Are you feeling hungry? I picked some things up for dinner tonight."

    hide headshot_cait
    show ada happy at sprite_right, speaking
    ada "Dinner...!"

    show ada sick at sprite_right, speaking
    ada "*cough*"

    show ada happy at sprite_right, speaking
    ada "What’re you making?"

    show ada happy at sprite_right, not_speaking
    show headshot_cait smile at headshot_left, speaking
    cait "It’s a secret. You have to wait and see."

    hide headshot_cait
    show ada thoughtful at sprite_right, speaking
    ada "Well, can I have a hint?"

    show ada thoughtful at sprite_right, not_speaking
    show headshot_cait smile at headshot_left, speaking
    cait "No."

    hide headshot_cait
    show ada shock at sprite_right, speaking
    ada "What?!"
    ada "Why?!"

    show ada shock at sprite_right, not_speaking
    show headshot_cait smile at headshot_left, speaking
    cait "You’re too clever."
    cait "Whenever I give you a hint, you figure it out right away."

    hide headshot_cait
    show ada shock at sprite_right, speaking
    ada "No fair!"

    show ada shock at sprite_right, not_speaking
    show headshot_cait sweet at headshot_left, speaking
    cait "You’ll find out at dinnertime."
    cait "Some secrets are worth keeping."

    show headshot_cait smile at headshot_left, speaking
    cait "Should I start cooking?"

    hide headshot_cait
    show ada happy at sprite_right, speaking
    ada "Maybe–"

    show ada sick at sprite_right, speaking
    ada "*cough* *hack*"

    show ada sleepy at sprite_right, speaking
    ada "Maybe in a little while…"
    ada "I’m still feeling nauseous."

    show ada sleepy at sprite_right, not_speaking
    show headshot_cait sweet at headshot_left, speaking
    cait "Sure thing, baby."

    hide headshot_cait
    show ada sick at sprite_right, speaking
    ada "I’m sorry I feel so bad. We’re supposed to be celebrating."

    show ada sick at sprite_right, not_speaking
    show headshot_cait sweet at headshot_left, speaking
    cait "Don’t apologize."
    cait "You just rest. I’ll do some chores around the house until you’re ready."

    hide headshot_cait
    show ada thoughtful at sprite_right, speaking
    ada "Won’t you take a nap with me?"

    show ada thoughtful at sprite_right, not_speaking
    show headshot_cait sweet at headshot_left, speaking
    cait "Tempting…"
    cait "I’ll see what I can do."

    hide headshot_cait
    show ada happy at sprite_right, speaking
    ada "...!"

    hide ada

    show headshot_cait focus at headshot_left, speaking
    cait "(I have a few hours to kill before I should start making dinner.)"
    cait "(I need to pull up some fresh vegetables for the soup tonight.)"

    show headshot_cait PO at headshot_left, speaking
    cait "(And I really should try to skim the latest research journal.)"

    show headshot_cait sweet at headshot_left, speaking
    cait "(But Ada is right there…)"

    show headshot_cait worry at headshot_left, speaking
    cait "(I hope she feels well enough to eat tonight.)"

    hide headshot_cait

    return

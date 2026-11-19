################################################################################
## Scene 4 - Memories
################################################################################


################################################################################
## State
################################################################################

default scene_4_memories_played = 0


################################################################################
## Memory Playback
################################################################################

label scene_4_memory_next:

    if scene_4_memories_played == 0:
        call scene_4_memory_1

    elif scene_4_memories_played == 1:
        call scene_4_memory_2

    elif scene_4_memories_played == 2:
        call scene_4_memory_3

    elif scene_4_memories_played == 3:
        call scene_4_memory_4

    elif scene_4_memories_played == 4:
        call scene_4_memory_5

    if scene_4_memories_played < 5:
        $ scene_4_memories_played += 1

    return


################################################################################
## Memory 1
################################################################################

label scene_4_memory_1:

    scene expression Solid("#000000")
    with fade

    cait "Where would I be without you, baby?"

    cait "All I knew before was running."

    cait "Running from the research labs, the colleagues, the investors…"

    cait "All of it."

    cait "Just to wash up on this nowhere border planet."

    cait "Figured I’d buy a farm and take a sabbatical."

    cait "Enjoy a few months of solitude before crawling back to my work."

    cait "And then I met you."

    cait "My lovely Ada."

    cait "My anchor."

    cait "You held me and loved me and kept me grounded to this impossibly gentle life."

    return


################################################################################
## Memory 2
################################################################################

label scene_4_memory_2:

    scene expression Solid("#000000")
    with fade

    cait "I’m certain that you don’t remember when we first met, baby, even if I do."

    cait "You were introduced to me on Chaff-6 as a neurological puzzle."

    cait "I found you perfectly capable at first. But there was one small exception."

    cait "Every eight hours, you forgot everyone and everything you’d just encountered."

    cait "In other words, short-term memory loss."

    cait "Whoever cared for you before we met was long gone, as far as I could tell."

    cait "But I thought you were fascinating."

    return


################################################################################
## Memory 3
################################################################################

label scene_4_memory_3:

    scene expression Solid("#000000")
    with fade

    cait "The curious thing about your memory loss was how consistently you you were."

    cait "No matter how often your memory reset, you still had the same tastes."

    cait "The same favorite meals…"

    cait "The same curiosities about the world…"

    cait "Even the same questions about me."

    cait "To know someone like this, at their most vulnerable and raw, is a privilege that very few people get to have."

    cait "And I got to have it with you."

    cait "Over and over and over again."

    cait "It’s because of this experience that I can conclusively say,"

    cait "that right down to your very core,"

    cait "you were good."

    cait "You were someone to hold onto."

    return


################################################################################
## Memory 4
################################################################################

label scene_4_memory_4:

    scene expression Solid("#000000")
    with fade

    cait "It took me an embarrassingly long time to figure out what was wrong with your memory."

    cait "You certainly made it hard for me to focus."

    cait "You just always had something charming to say."

    cait "You’d tell me something about the etymology of the words I use…"

    cait "...Or the history of the furniture we were sitting on…"

    cait "...Even the color of my eyes that you found so beautiful."

    cait "I remember seeing how you’d always devour the novels I left on your nightstand."

    cait "You’d finish one before I managed to find you another."

    cait "You brought me so much joy, every day."

    cait "Who wouldn’t have fallen in love?"

    return


################################################################################
## Memory 5
################################################################################

label scene_4_memory_5:

    scene expression Solid("#000000")
    with fade

    cait "In the end, it was localized damage to your synthetic neurons that caused the memory loss."

    cait "My fix was trivial."

    cait "Essentially a biosynthetic memory card. Nothing that hadn’t been thoroughly established in my field"

    cait "The only difference is that I included space for sixty years’ worth of memories, not two."

    cait "I understood the laws about android lifespans, of course."

    cait "And if anyone had asked, it was just a proof-of-concept."

    cait "A prototype."

    cait "Never to be used."

    cait "But it seemed too cruel that someone so good–"

    cait "–this D4 android–"

    cait "–you–"

    cait "Could be lost from the world after only two years."

    cait "I couldn’t let that happen to you, Ada."

    cait "I couldn’t lose you so quickly."

    return

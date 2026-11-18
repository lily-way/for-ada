################################################################################
## Scene 3 - Dialogue 1
################################################################################

label scene_3_dialogue_1:

    scene bg store at background_fixed
    with Dissolve(0.5)

    show d9 alarmed at sprite_right, speaking
    d9 "...!"

    hide d9

    # play sound "audio/footsteps.mp3"

    "(D9 sprints up the stairs.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(She’ll get him.)"
    cait "(I need to unpack.)"

    hide headshot_cait

    martin "You stupid piece of scrap!"
    martin "What the hell are you doing up here?"
    martin "All I asked is for you to guard the storefront, and you can’t even do that right!"
    martin "Go back downstairs!"

    show headshot_cait focus at headshot_left, speaking
    cait "(Androids are not automatons.)"
    cait "(D9’s vocal function may be disabled, but she’s still capable of understanding Martin’s requests.)"
    cait "(And free to interpret them herself.)"
    cait "(She’ll figure out how to alert him somehow.)"

    show headshot_cait PO at headshot_left, speaking
    cait "(Whether or not he understands is a separate matter entirely.)"

    hide headshot_cait

    martin "Why the hell aren’t you listening to me?"
    martin "Fine, then!"
    martin "D9, automaton mode!"
    martin "Priority one task: Go downstairs!"

    # play sound "audio/footsteps.mp3"

    show d9 automaton at sprite_right, speaking
    d9 "..."

    show d9 automaton at sprite_right, not_speaking
    martin "Sit."

    show d9 automaton at sprite_right, speaking
    d9 "..."

    show d9 automaton at sprite_right, not_speaking

    "(D9 sits at the base of the stairs.)"

    martin "Stay."

    show d9 automaton at sprite_right, speaking
    d9 "..."

    show d9 automaton at sprite_right, not_speaking
    martin "Priority one task: Don’t move!"
    martin "Return to android mode."

    show d9 automaton at sprite_right, speaking
    d9 "..."

    show d9 neutral at sprite_right, speaking
    d9 "..."

    show d9 fear at sprite_right, speaking
    d9 "...!"

    show d9 fear at sprite_right, not_speaking

    show headshot_cait focus at headshot_left, speaking
    cait "(Most people think androids can’t feel emotions.)"

    show headshot_cait PO at headshot_left, speaking
    cait "(I know better.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(My laboratory prototyped one of the first models, after all.)"
    cait "(Every one of D9’s subcomponents probably cites my research papers.)"
    cait "(Everything from the synaptic computers in her head…)"
    cait "(To the novel thoughts they’re generating…)"
    cait "(Down to the endocrinal signals that respond to those thoughts.)"
    cait "(Right now, D9 is terrified.)"

    show headshot_cait PO at headshot_left, speaking
    cait "(Let’s see if I can fix that.)"

    hide headshot_cait
    hide d9

    return

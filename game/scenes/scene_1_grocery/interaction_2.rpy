################################################################################
## Scene 1 - Interaction 2
################################################################################


################################################################################
## State
################################################################################

default scene_1_interaction_2_stairs_done = False
default scene_1_interaction_2_register_done = False


################################################################################
## Interactions
################################################################################

define scene_1_interaction_2_objects = [

    Interaction(
        name="stairs",
        interaction_type="observe",
        area=(933, 452, 148, 368),
        action="scene_1_interaction_2_stairs",
        completed="scene_1_interaction_2_stairs_done",
        mandatory=False
    ),

    Interaction(
        name="cash_register",
        interaction_type="interact",
        area=(449, 817, 328, 184),
        action="scene_1_interaction_2_register",
        completed="scene_1_interaction_2_register_done",
        mandatory=True
    ),

]


################################################################################
## Grocery Store Exploration
################################################################################

label scene_1_interaction_2:

    $ progress_interactions = scene_1_interaction_2_objects
    $ progress_open = False

    show bg store at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(That's everything I needed for dinner tonight. I should talk to Martin to check out.)"

    hide headshot_cait

    show bg store at background_pan

    while not scene_1_interaction_2_register_done:

        call screen interaction_screen(scene_1_interaction_2_objects)
        call expression _return

    show bg store at background_freeze

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Optional Observation - Stairs
################################################################################

label scene_1_interaction_2_stairs:

    if scene_1_interaction_2_stairs_done:
        return

    show bg store at background_freeze

    show d9 neutral at sprite_middle, not_speaking

    show headshot_cait focus at headshot_left, speaking
    cait "..."

    hide headshot_cait
    show d9 neutral at sprite_middle, speaking
    d9 "..."

    show d9 neutral at sprite_middle, not_speaking
    show headshot_cait focus at headshot_left, speaking
    cait "..."

    show headshot_cait smile at headshot_left, speaking
    cait "Thank you again for the stock, D9."

    hide headshot_cait
    show d9 neutral at sprite_middle, speaking
    d9 "..."

    show d9 neutral at sprite_middle, not_speaking
    show headshot_cait focus at headshot_left, speaking
    cait "..."
    cait "(D8 was so full of life.)"
    cait "(What a waste...)"
    cait "(What would you say if you could speak to me, D9?)"
    cait "..."

    hide headshot_cait
    show d9 neutral at sprite_middle, speaking
    d9 "..."

    hide d9

    $ scene_1_interaction_2_stairs_done = True

    show bg store at background_pan

    return


################################################################################
## Mandatory Interaction - Cash Register
################################################################################

label scene_1_interaction_2_register:

    if scene_1_interaction_2_register_done:
        return

    show bg store at background_freeze

    show headshot_martin neutral at headshot_right, speaking
    martin "Have you found everything you needed?"

    hide headshot_martin
    show headshot_cait smile at headshot_left, speaking
    cait "That's right. How much do I owe you?"

    hide headshot_cait
    show headshot_martin laugh at headshot_right, speaking
    martin "Oh, nothing at all!"

    show headshot_martin neutral at headshot_right, speaking
    martin "Consider it a gift to Ada. I hope she feels better soon."

    hide headshot_martin
    show headshot_cait smile at headshot_left, speaking
    cait "You're too kind, Martin."

    hide headshot_cait
    show headshot_martin rage at headshot_right, speaking
    martin "Some people are too good to suffer. I wish the world would just protect them, but instead we have to."

    hide headshot_martin
    show headshot_cait smile at headshot_left, speaking
    cait "My thoughts exactly. I'm sure she'll have me ferrying more baked goods soon."

    show headshot_cait focus at headshot_left, speaking
    cait "Good day to you as well, D9."

    hide headshot_cait
    show d9 neutral at sprite_middle, speaking
    d9 "..."

    hide d9

    $ scene_1_interaction_2_register_done = True

    return

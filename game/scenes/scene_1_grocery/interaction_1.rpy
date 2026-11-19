################################################################################
## Scene 1 - Interaction 1
################################################################################


################################################################################
## State
################################################################################

default scene_1_interaction_1_cigarettes_done = False
default scene_1_interaction_1_deli_done = False

default scene_1_interaction_1_wine_done = False
default scene_1_interaction_1_bread_done = False
default scene_1_interaction_1_soup_done = False


################################################################################
## Interactions
################################################################################

define scene_1_interaction_1_objects = [

    Interaction(
        name="cigarettes",
        interaction_type="observe",
        area=(564, 800, 54, 39),
        action="scene_1_interaction_1_cigarettes",
        completed="scene_1_interaction_1_cigarettes_done",
        mandatory=False
    ),

    Interaction(
        name="deli",
        interaction_type="observe",
        area=(330, 904, 280, 228),
        action="scene_1_interaction_1_deli",
        completed="scene_1_interaction_1_deli_done",
        mandatory=False
    ),

    Interaction(
        name="wine",
        interaction_type="interact",
        area=(1612, 424, 74, 531),
        action="scene_1_interaction_1_wine",
        completed="scene_1_interaction_1_wine_done",
        mandatory=True
    ),

    Interaction(
        name="bread",
        interaction_type="interact",
        area=(1882, 480, 332, 155),
        action="scene_1_interaction_1_bread",
        completed="scene_1_interaction_1_bread_done",
        mandatory=True
    ),

    Interaction(
        name="soup",
        interaction_type="interact",
        area=(2068, 334, 103, 125),
        action="scene_1_interaction_1_soup",
        completed="scene_1_interaction_1_soup_done",
        mandatory=True
    ),

]


################################################################################
## Grocery Store Exploration
################################################################################

label scene_1_interaction_1:

    $ progress_interactions = scene_1_interaction_1_objects
    $ progress_open = False

    scene bg store at background_fixed

    "(Use the mouse to look around!)"
    "(Your cursor will highlight certain objects and people you can inspect.)"
    "(Click on those things to interact with them!)"
    "(Bronze objects are optional, while gold objects are mandatory.)"
    "(Press Q to view how many mandatory and optional interactions you've completed.)"
    "(Warning! Once you've completed all mandatory interactions, you won't be able to go back.)"

    while not (
        scene_1_interaction_1_wine_done
        and scene_1_interaction_1_bread_done
        and scene_1_interaction_1_soup_done
    ):

        show bg store at background_pan

        call screen interaction_screen(scene_1_interaction_1_objects)

        show bg store at background_freeze

        call expression _return

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Optional Observation - Cigarettes
################################################################################

label scene_1_interaction_1_cigarettes:

    if scene_1_interaction_1_cigarettes_done:
        return

    show headshot_cait smile at headshot_left, speaking
    cait "Didn't you say you quit smoking?"
    cait "I suppose even lung cancer can't keep you down."

    hide headshot_cait
    show headshot_martin laugh at headshot_right, speaking
    martin "Damn straight!"

    show headshot_martin neutral at headshot_right, speaking
    martin "The Mrs. told me to call it quits, but she just got a new heart, so I think she can handle my antics."

    show headshot_martin laugh at headshot_right, speaking
    martin "Besides, what's the point of new lungs if I can't have any fun with them?"

    hide headshot_martin
    show headshot_cait smile at headshot_left, speaking
    cait "Technology is a beautiful thing..."

    hide headshot_cait

    $ scene_1_interaction_1_cigarettes_done = True

    return


################################################################################
## Optional Observation - Deli Display Case
################################################################################

label scene_1_interaction_1_deli:

    if scene_1_interaction_1_deli_done:
        return

    show headshot_cait focus at headshot_left, speaking
    cait "(Ada and I raise our own g-13 rabbits, so there's no need to buy meat here.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(I modified the strain myself.)"
    cait "(Livestock editing is trivial; it's something I could have done in my undergrad years.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(Martin's offered to sell my g-13 cuts here before, but...)"
    cait "(I'd rather not commercialize my skillset.)"
    cait "(That was a past life.)"

    hide headshot_cait

    $ scene_1_interaction_1_deli_done = True

    return


################################################################################
## Mandatory Interaction - Wine Shelf
################################################################################

label scene_1_interaction_1_wine:

    if scene_1_interaction_1_wine_done:
        return

    show headshot_cait focus at headshot_left, speaking
    cait "(If it were up to me, I'd just get the cheapest bottle and move on.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(But Ada loves this sort of thing.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(Historical homeworld culture, literature, food... It just appeals to her.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(She finds it so fascinating.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(Now, let's see if I can find those cases Martin mentioned.)"
    cait "(Homeworld... Homeworld...)"
    cait "(Aha.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(Ada will love this.)"

    hide headshot_cait

    $ scene_1_interaction_1_wine_done = True

    return


################################################################################
## Mandatory Interaction - Bread
################################################################################

label scene_1_interaction_1_bread:

    if scene_1_interaction_1_bread_done:
        return

    show headshot_cait focus at headshot_left, speaking
    cait "(Normally, Ada would be baking bread for us, but she hasn't been feeling well recently.)"
    cait "(I suppose this will have to do for tonight...)"

    hide headshot_cait

    $ scene_1_interaction_1_bread_done = True

    return


################################################################################
## Mandatory Interaction - Soup Shelf
################################################################################

label scene_1_interaction_1_soup:

    if scene_1_interaction_1_soup_done:
        return

    show headshot_cait focus at headshot_left, speaking
    cait "Martin, do you have any more chicken stock? Ada is feeling under the weather..."

    hide headshot_cait
    show headshot_martin neutral at headshot_right, speaking
    martin "Should have some in the back! One second."

    show headshot_martin rage at headshot_right, speaking
    martin "D9?! Chicken stock!!"

    hide headshot_martin
    show d9 neutral at sprite_middle, speaking

    "A slim android emerges from the back of the store, carrying a few large jars of bone broth."

    show d9 neutral at sprite_middle, speaking
    d9 "..."

    show d9 neutral at sprite_middle, not_speaking
    show headshot_cait smile at headshot_left, speaking
    cait "Thank you very much, D9."
    cait "I don't think we've met before. I'm Cait."

    hide headshot_cait
    show d9 neutral at sprite_middle, speaking
    d9 "..."

    show d9 neutral at sprite_middle, not_speaking
    show headshot_martin neutral at headshot_right, speaking
    martin "Oh, don't bother. I haven't enabled its vocal functions yet."

    show headshot_martin laugh at headshot_right, speaking
    martin "And given how chatty D8 was, I think I'll keep it like this!"

    hide headshot_martin
    show headshot_cait focus at headshot_left, speaking
    cait "Ah, I see."
    cait "I can't believe two years have passed already. I felt like I just met D8."

    hide headshot_cait
    show headshot_martin neutral at headshot_right, speaking
    martin "Two and a half, actually. I tried to hold out as long as I could before buying a new one."

    show headshot_martin rage at headshot_right, speaking
    martin "Piece of junk was leaking biofluids all over my hardwood by the end."

    hide headshot_martin
    show headshot_cait focus at headshot_left, speaking
    cait "(Poor D8...)"

    hide headshot_cait
    hide d9

    $ scene_1_interaction_1_soup_done = True

    return

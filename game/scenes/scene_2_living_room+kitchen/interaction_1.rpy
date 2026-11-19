################################################################################
## Scene 2 - Interaction 1
################################################################################


################################################################################
## State
################################################################################

default scene_2_interaction_1_room = "living_room"

default scene_2_interaction_1_armchair_done = False
default scene_2_interaction_1_journal_done = False
default scene_2_interaction_1_window_done = False

default scene_2_interaction_1_stovetop_done = False
default scene_2_interaction_1_wine_bottle_done = False
default scene_2_interaction_1_knives_sharpened = False
default scene_2_interaction_1_doctorate_done = False
default scene_2_interaction_1_mystery_novels_done = False

default scene_2_interaction_1_radio_intro_done = False
default scene_2_interaction_1_radio_965_done = False
default scene_2_interaction_1_radio_1051_done = False
default scene_2_interaction_1_radio_1070_done = False
default scene_2_interaction_1_radio_done = False

################################################################################
## Light Cycles
################################################################################

init python:

    def scene_2_interaction_1_background(room):

        completed = sum([
            scene_2_interaction_1_armchair_done,
            scene_2_interaction_1_journal_done,
            scene_2_interaction_1_window_done
        ])

        cycle = min(3, completed)

        return Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_{}".format(cycle),
            (0, 0), "bg {}".format(room)
        )

################################################################################
## Living Room Interactions
################################################################################

define scene_2_interaction_1_living_room_objects = [

    Interaction(
        name="kitchen_door",
        interaction_type="interact",
        area=(1640, 126, 187, 746),
        action="scene_2_interaction_1_go_to_kitchen",
        mandatory=False
    ),

    Interaction(
        name="armchair",
        interaction_type="interact",
        area=(266, 487, 506, 533),
        action="scene_2_interaction_1_armchair",
        completed="scene_2_interaction_1_armchair_done",
        mandatory=True
    ),

    Interaction(
        name="scientific_journal",
        interaction_type="observe",
        area=(837, 853, 100, 80),
        action="scene_2_interaction_1_journal",
        completed="scene_2_interaction_1_journal_done",
        mandatory=True
    ),

    Interaction(
        name="living_room_small_window",
        interaction_type="observe",
        area=(1350, 123, 106, 464),
        action="scene_2_interaction_1_small_window",
        mandatory=False
    ),

    Interaction(
        name="doctorate",
        interaction_type="observe",
        area=(402, 116, 172, 167),
        action="scene_2_interaction_1_doctorate",
        completed="scene_2_interaction_1_doctorate_done",
        mandatory=False
    ),

    Interaction(
        name="mystery_novels",
        interaction_type="observe",
        area=(1845, 542, 452, 84),
        action="scene_2_interaction_1_mystery_novels",
        completed="scene_2_interaction_1_mystery_novels_done",
        mandatory=False
    ),

    Interaction(
        name="radio",
        interaction_type="interact",
        area=(2059, 239, 229, 135),
        action="scene_2_interaction_1_radio",
        completed="scene_2_interaction_1_radio_done",
        mandatory=False
    ),

]


################################################################################
## Kitchen Interactions
################################################################################

define scene_2_interaction_1_kitchen_objects = [

    Interaction(
        name="living_room_door",
        interaction_type="interact",
        area=(149, 59, 203, 837),
        action="scene_2_interaction_1_go_to_living_room",
        mandatory=False
    ),

    Interaction(
        name="large_kitchen_window",
        interaction_type="observe",
        area=(832, 93, 357, 414),
        action="scene_2_interaction_1_window",
        completed="scene_2_interaction_1_window_done",
        mandatory=True
    ),

    Interaction(
        name="kitchen_small_window_1",
        interaction_type="observe",
        area=(528, 140, 99, 459),
        action="scene_2_interaction_1_small_window",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_2",
        interaction_type="observe",
        area=(1979, 161, 140, 375),
        action="scene_2_interaction_1_small_window",
        mandatory=False
    ),

    Interaction(
        name="kitchen_small_window_3",
        interaction_type="observe",
        area=(2221, 141, 78, 368),
        action="scene_2_interaction_1_small_window",
        mandatory=False
    ),

    Interaction(
        name="kitchen_stovetop",
        interaction_type="observe",
        area=(1622, 619, 272, 307),
        action="scene_2_interaction_1_stovetop",
        completed="scene_2_interaction_1_stovetop_done",
        mandatory=False
    ),

    Interaction(
        name="wine_bottle",
        interaction_type="observe",
        area=(1039, 494, 56, 128),
        action="scene_2_interaction_1_wine_bottle",
        completed="scene_2_interaction_1_wine_bottle_done",
        mandatory=False
    ),

    Interaction(
        name="knife_block",
        interaction_type="interact",
        area=(2109, 557, 80, 82),
        action="scene_2_interaction_1_knife_block",
        completed="scene_2_interaction_1_knives_sharpened",
        mandatory=False
    ),

]

################################################################################
## Scene
################################################################################

label scene_2_interaction_1:

    $ scene_2_interaction_1_room = "living_room"
    $ progress_interactions = scene_2_interaction_1_living_room_objects
    $ progress_open = False

    scene expression scene_2_interaction_1_background("living_room") as bg at background_pan

    while not (
        scene_2_interaction_1_armchair_done
        and scene_2_interaction_1_journal_done
        and scene_2_interaction_1_window_done
    ):

        if scene_2_interaction_1_room == "living_room":

            call screen interaction_screen(
                scene_2_interaction_1_living_room_objects
            )

        elif scene_2_interaction_1_room == "kitchen":

            call screen interaction_screen(
                scene_2_interaction_1_kitchen_objects
            )

        call expression _return

    hide headshot_ada
    hide headshot_cait

    if scene_2_interaction_1_room == "living_room":
        show expression scene_2_interaction_1_background("living_room") as bg at background_fixed
    else:
        show expression scene_2_interaction_1_background("kitchen") as bg at background_fixed

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Room Navigation
################################################################################

label scene_2_interaction_1_go_to_kitchen:

    $ scene_2_interaction_1_room = "kitchen"
    $ progress_interactions = scene_2_interaction_1_kitchen_objects

    scene expression scene_2_interaction_1_background("kitchen") as bg at background_pan
    with Fade(0.3, 0.2, 0.3)

    return


label scene_2_interaction_1_go_to_living_room:

    $ scene_2_interaction_1_room = "living_room"
    $ progress_interactions = scene_2_interaction_1_living_room_objects

    scene expression scene_2_interaction_1_background("living_room") as bg at background_pan
    with Fade(0.3, 0.2, 0.3)

    return

################################################################################
## Mandatory Interaction - Armchair
################################################################################

label scene_2_interaction_1_armchair:

    if scene_2_interaction_1_armchair_done:
        return

    show expression scene_2_interaction_1_background("living_room") as bg at background_freeze

    show headshot_ada happy at headshot_right, speaking
    ada "I knew you’d give in."

    hide headshot_ada
    show headshot_cait sweet at headshot_left, speaking
    cait "Yeah, yeah…"
    cait "Just for a little while."

    hide headshot_cait

    menu:

        "Take a nap with Ada":

            scene expression Solid("#000000")
            with Fade(0.3, 0.2, 0.3)

            "(Time passes…)"

            show headshot_cait PO at headshot_left, speaking
            cait "Guh…"

            hide headshot_cait
            show headshot_ada sleepy at headshot_right, speaking
            ada "Hey…"
            ada "Hope my coughing didn’t keep you up…"

            hide headshot_ada
            show headshot_cait PO at headshot_left, speaking
            cait "No, no…"
            cait "Why do naps always make me more tired…?"

            hide headshot_cait
            show headshot_ada sleepy at headshot_right, speaking
            ada "Maybe you need to sleep more…?"

            hide headshot_ada
            show headshot_cait PO at headshot_left, speaking
            cait "That can’t be it…"
            cait "I’m getting up now…"

            hide headshot_cait

            $ scene_2_interaction_1_armchair_done = True

            scene expression scene_2_interaction_1_background("living_room") as bg at background_pan
            with Fade(0.3, 0.2, 0.3)

    return


################################################################################
## Mandatory Interaction - Scientific Journal
################################################################################

label scene_2_interaction_1_journal:

    if scene_2_interaction_1_journal_done:
        return

    show expression scene_2_interaction_1_background("living_room") as bg at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(Here’s the latest issue of {i}Bioelectrical Intergalaxy{/i}.)"
    cait "(I still have some older volumes featuring my work.)"
    cait "(Somewhere around here...)"
    cait "(I’ll try and read a few articles before dinner.)"

    hide headshot_cait

    scene expression Solid("#000000")
    with Fade(0.3, 0.2, 0.3)

    "(Time passes…)"

    # play sound "audio/page_flip.mp3"

    show headshot_cait PO at headshot_left, speaking
    cait "(Idiotic.)"

    # play sound "audio/page_flip.mp3"
    cait "(Poorly sourced.)"

    # play sound "audio/page_flip.mp3"
    cait "(We’ve known that for decades!)"

    # play sound "audio/page_flip.mp3"
    cait "(I remember you…)"
    cait "(I should have failed you at your dissertation.)"

    # play sound "audio/book_thud.mp3"

    show headshot_cait focus at headshot_left, speaking
    cait "(Well, that’s enough of that.)"

    hide headshot_cait

    $ scene_2_interaction_1_journal_done = True

    scene expression scene_2_interaction_1_background("living_room") as bg at background_pan
    with Fade(0.3, 0.2, 0.3)

    return


################################################################################
## Mandatory Interaction - Large Kitchen Window
################################################################################

label scene_2_interaction_1_window:

    if scene_2_interaction_1_window_done:
        return

    show expression scene_2_interaction_1_background("kitchen") as bg at background_freeze

    show headshot_cait smile at headshot_left, speaking
    cait "(There’s our garden.)"
    cait "(Looks like we’ll have plenty of fresh ingredients for dinner tonight.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(I’ll just gather up the root vegetables while Ada catches a–)"
    cait "(Oh.)"

    show headshot_cait PO at headshot_left, speaking
    cait "(Oh, no.)"
    cait "(*sigh*)"

    show headshot_cait focus at headshot_left, speaking
    cait "Ada, baby?"

    hide headshot_cait
    show headshot_ada neutral at headshot_right, speaking
    ada "Yeah?"

    hide headshot_ada
    show headshot_cait worry at headshot_left, speaking
    cait "Is there any chance you’re up for catching a g-13 for me?"

    hide headshot_cait
    show headshot_ada neutral at headshot_right, speaking
    ada "Um…"
    ada "Let me try and stand–"

    show headshot_ada sick at headshot_right, speaking
    ada "*cough*!!!!!"
    ada "*hack*!!!!!"
    ada "*cough*!!!!!!"

    hide headshot_ada
    show headshot_cait worry at headshot_left, speaking
    cait "Never mind! Stay where you are!"

    show headshot_cait focus at headshot_left, speaking
    cait "I’m very capable. I’m sure I can catch one."

    show headshot_cait PO at headshot_left, speaking
    cait "Eventually…"

    hide headshot_cait
    show headshot_ada happy at headshot_right, speaking
    ada "It’s not so bad! They’re just skittish."

    show headshot_ada neutral at headshot_right, speaking
    ada "Try approaching with food."
    ada "They let me pick them up just because I feed them every day."

    show headshot_ada mischief at headshot_right, speaking
    ada "Reminds me of someone I know…"

    hide headshot_ada
    show headshot_cait PO at headshot_left, speaking
    cait "It won’t work for me."
    cait "They associate me with death."

    hide headshot_cait
    show headshot_ada thoughtful at headshot_right, speaking
    ada "Well…"

    show headshot_ada neutral at headshot_right, speaking
    ada "Do your best!"

    hide headshot_ada

    scene expression Solid("#000000")
    with Fade(0.3, 0.2, 0.3)

    "(Time passes…)"

    show headshot_cait PO at headshot_left, speaking
    cait "*Huff…* *Huff…*"
    cait "I finally got you…"

    hide headshot_cait

    "G-13" "Wheek! Wheek! Wheek!"

    show headshot_cait PO at headshot_left, speaking
    cait "Bastard."

    hide headshot_cait

    # play sound "audio/crunch.mp3"

    "(*CRUNCH*)"

    $ scene_2_interaction_1_window_done = True

    scene expression scene_2_interaction_1_background("kitchen") as bg at background_pan
    with Fade(0.3, 0.2, 0.3)

    return


################################################################################
## Optional Observation - Small Windows
################################################################################

label scene_2_interaction_1_small_window:

    if scene_2_interaction_1_room == "living_room":
        show expression scene_2_interaction_1_background("living_room") as bg at background_freeze
    else:
        show expression scene_2_interaction_1_background("kitchen") as bg at background_freeze

    $ tasks_done = sum([
        scene_2_interaction_1_armchair_done,
        scene_2_interaction_1_journal_done,
        scene_2_interaction_1_window_done
    ])

    if tasks_done == 0:

        show headshot_cait smile at headshot_left, speaking
        cait "(It’s a beautiful day today.)"

        show headshot_cait focus at headshot_left, speaking
        cait "(I still have a few hours to kill before I need to make dinner.)"

    elif tasks_done == 1:

        show headshot_cait focus at headshot_left, speaking
        cait "(It’s still quite light out.)"
        cait "(I still have some time to kill before I need to make dinner.)"

    elif tasks_done == 2:

        show headshot_cait smile at headshot_left, speaking
        cait "(What a beautiful sunset.)"

        show headshot_cait focus at headshot_left, speaking
        cait "(I have a little bit of time to kill before I need to make dinner.)"

    hide headshot_cait

    if scene_2_interaction_1_room == "living_room":
        show expression scene_2_interaction_1_background("living_room") as bg at background_pan
    else:
        show expression scene_2_interaction_1_background("kitchen") as bg at background_pan

    return


################################################################################
## Optional Observation - Kitchen Stovetop
################################################################################

label scene_2_interaction_1_stovetop:

    if scene_2_interaction_1_stovetop_done:
        return

    show expression scene_2_interaction_1_background("kitchen") as bg at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(It’s still too early to start cooking.)"

    hide headshot_cait

    $ scene_2_interaction_1_stovetop_done = True

    show expression scene_2_interaction_1_background("kitchen") as bg at background_pan

    return


################################################################################
## Optional Observation - Wine Bottle
################################################################################

label scene_2_interaction_1_wine_bottle:

    if scene_2_interaction_1_wine_bottle_done:
        return

    show expression scene_2_interaction_1_background("kitchen") as bg at background_freeze

    show headshot_cait smile at headshot_left, speaking
    cait "(Good thing Ada was so out of it when I came in.)"
    cait "(This will be the perfect surprise for tonight.)"

    hide headshot_cait

    $ scene_2_interaction_1_wine_bottle_done = True

    show expression scene_2_interaction_1_background("kitchen") as bg at background_pan

    return


################################################################################
## Optional Interaction - Knife Block
################################################################################

label scene_2_interaction_1_knife_block:

    if scene_2_interaction_1_knives_sharpened:
        return

    show expression scene_2_interaction_1_background("kitchen") as bg at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(I’d better sharpen these knives before I forget.)"
    cait "(One should always keep their tools clean and ready for use.)"

    hide headshot_cait

    menu:

        "Sharpen knives":

            # play sound "audio/knife_sharpening.mp3"

            "Cait sharpens each knife methodically before returning it to the block."

            show headshot_cait focus at headshot_left, speaking
            cait "Much better."

            hide headshot_cait

            $ scene_2_interaction_1_knives_sharpened = True

    show expression scene_2_interaction_1_background("kitchen") as bg at background_pan

    return


################################################################################
## Optional Observation - Doctorate
################################################################################

label scene_2_interaction_1_doctorate:

    if scene_2_interaction_1_doctorate_done:
        return

    show expression scene_2_interaction_1_background("living_room") as bg at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(My doctoral diploma.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(Biosynthetics.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(It feels like a lifetime ago now.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(I was at the top of my field back then.)"

    show headshot_cait PO at headshot_left, speaking
    cait "(Not many of my colleagues understood why I left that life behind.)"
    cait "(But it was the field that betrayed me, not the other way around.)"
    cait "(And I wasn’t content with my research being relegated to third-rate journals, or going on disgraced ‘sabbaticals’.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(By the time I met Ada, I’d been on my way out for years.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(I think that was for the best.)"

    hide headshot_cait

    $ scene_2_interaction_1_doctorate_done = True

    show expression scene_2_interaction_1_background("living_room") as bg at background_pan

    return


################################################################################
## Optional Observation - Mystery Novels
################################################################################

label scene_2_interaction_1_mystery_novels:

    if scene_2_interaction_1_mystery_novels_done:
        return

    show expression scene_2_interaction_1_background("living_room") as bg at background_freeze

    show headshot_cait smile at headshot_left, speaking
    cait "(Looks like Ada’s already finished {i}Murder on Medina Station{/i}.)"

    show headshot_cait sweet at headshot_left, speaking
    cait "(How many books has she read today…?)"

    show headshot_cait focus at headshot_left, speaking
    cait "(She’s tried to get me to read these homeworld mysteries before, but…)"

    show headshot_cait PO at headshot_left, speaking
    cait "(To be honest, they’re a little trashy for me.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(I just couldn’t get through {i}Helium Expressway{/i}, even though Ada loved it.)"

    show headshot_cait worry at headshot_left, speaking
    cait "(And the depiction of android researchers in {i}Hot Engines, Cold Nights{/i} was {i}very{/i} uncouth.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(Personally, I’d rather just read a paper from the latest {i}Bioelectrical Intergalaxy{/i} publication.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(Not that Ada doesn’t devour those as well.)"
    cait "(I always thought I’d let my skills rust, when I walked away from academic life…)"
    cait "(But she’s kept me sharp.)"
    cait "(I’m so grateful for that.)"

    hide headshot_cait

    $ scene_2_interaction_1_mystery_novels_done = True

    show expression scene_2_interaction_1_background("living_room") as bg at background_pan

    return


################################################################################
## Optional Interaction - Radio
################################################################################

label scene_2_interaction_1_radio:

    $ scene_2_interaction_1_radio_done = True

    show expression scene_2_interaction_1_background("living_room") as bg at background_freeze

    if not scene_2_interaction_1_radio_intro_done:

        show headshot_cait focus at headshot_left, speaking
        cait "(Let’s see what’s going on in the news today.)"

        hide headshot_cait

        # play sound "audio/radio_static.mp3"

        "Radio" "Bzzt!"

        $ scene_2_interaction_1_radio_intro_done = True

    while True:

        menu:

            "Channel 96.5":
                call scene_2_interaction_1_radio_965

            "Channel 105.1":
                call scene_2_interaction_1_radio_1051

            "Channel 107.0":
                call scene_2_interaction_1_radio_1070

            "Turn off radio":

                # stop music fadeout 1.0

                hide headshot_cait
                hide headshot_ada

                show expression scene_2_interaction_1_background("living_room") as bg at background_pan

                return


################################################################################
## Radio - Channel 96.5
################################################################################

label scene_2_interaction_1_radio_965:

    # play sound "audio/radio_static.mp3"

    "Radio" "Bzzt!"

    if not scene_2_interaction_1_radio_965_done:

        "Radio" "--clear skies for now, but watch out for heavy rainfall later tonight!"

        "Radio" "The monsoon season is starting, so homesteaders across Chaff-6 can expect these conditions to continue for several weeks at least."

        "Radio" "And good timing at that! If the rain had hit any earlier, Chaff-6’s last fleet of grain ships could have been grounded for the season."

        "Radio" "Luckily, the grain’s made it off-planet, so Chaff-sixers can head into the quiet months knowing that their crops will feed mouths across the galaxy."

        "Radio" "We hope you’ve stocked up on off-planet goods, because you won’t be seeing a foreign ship for another few cycles at least!"

        "Radio" "That’s it for today’s weather. Stay tuned for our local Chaff-6 bluegrass hour!"

        # play music "audio/bluegrass.mp3" fadein 1.0

        show headshot_cait focus at headshot_left, speaking
        cait "(Thank goodness for the monsoon.)"
        cait "(Ada and I raise crops year-around, just enough to feed ourselves and barter a bit – but we don’t sell anything off-planet.)"
        cait "(That means that for us, the wet season isn’t slow business.)"

        show headshot_cait smile at headshot_left, speaking
        cait "(It’s just peaceful.)"
        cait "(A few months of rain… No planetside ships…)"

        show headshot_cait sweet at headshot_left, speaking
        cait "(It’s a nice excuse to cozy up indoors with your lover.)"

        hide headshot_cait

        $ scene_2_interaction_1_radio_965_done = True

    else:

        "Radio" "That’s it for today’s weather. Stay tuned for our local Chaff-6 bluegrass hour!"

        # play music "audio/bluegrass.mp3" fadein 1.0

    return


################################################################################
## Radio - Channel 105.1
################################################################################

label scene_2_interaction_1_radio_1051:

    # play sound "audio/radio_static.mp3"

    "Radio" "Bzzt!"

    if not scene_2_interaction_1_radio_1051_done:

        "Radio" "--authorities uncovered an illegal android regrafting operation just two systems away from Chaff."

        "Radio" "Organs meant for new android frames were found implanted in older models past the legal two-year limit."

        "Radio" "All androids found at the site were immediately dismantled and the operators have been apprehended."

        "Radio" "They are now en route to homeworld, where they will stand trial."

        "Radio" "That’s it for today’s intergalaxy news report."

        "Radio" "Stay tuned for {i}Under the Stars{/i}, our classical jazz program!"

        # play music "audio/jazz.mp3" fadein 1.0

        show headshot_cait worry at headshot_left, speaking
        cait "(...)"
        cait "(What a waste…)"

        hide headshot_cait
        show headshot_ada thoughtful at headshot_right, speaking
        ada "Yeesh."
        ada "What an unsettling story."

        hide headshot_ada
        show headshot_cait focus at headshot_left, speaking
        cait "What? The dismantling?"

        hide headshot_cait
        show headshot_ada thoughtful at headshot_right, speaking
        ada "Huh?"
        ada "No, just all the android stuff in general."
        ada "They really give me the creeps."
        ada "Human parts without a soul…"

        hide headshot_ada
        show headshot_cait focus at headshot_left, speaking
        cait "..."
        cait "I don’t know. I always found D8 so charming, don’t you think?"

        hide headshot_cait
        show headshot_ada thoughtful at headshot_right, speaking
        ada "If you say so…"

        hide headshot_ada

        $ scene_2_interaction_1_radio_1051_done = True

    else:

        "Radio" "That’s it for today’s intergalaxy news report."

        "Radio" "Stay tuned for {i}Under the Stars{/i}, our classical jazz program!"

        # play music "audio/jazz.mp3" fadein 1.0

    return


################################################################################
## Radio - Channel 107.0
################################################################################

label scene_2_interaction_1_radio_1070:

    # play sound "audio/radio_static.mp3"

    "Radio" "Bzzt!"

    if not scene_2_interaction_1_radio_1070_done:

        "Radio" "--looking for your next holiday getaway?"

        "Radio" "Consider a trip to your great planet of origin, Earth!"

        "Radio" "Visit beautiful cities with histories stretching back thousands of years!"

        "Radio" "Take a tour of the capitol and see how an entire galaxy is governed in just one metro!"

        "Radio" "Explore archeological sites such as The Great Wall, the Acropolis, and Houston!"

        "Radio" "So buy your tickets now at your local Enterprise Starliners office!"

        "Radio" "Special fares apply for those who book using the promo code, ‘HOMEWORLD’!"

        "Radio" "That’s it for today in entertainment."

        "Radio" "Stay tuned for the newest, hottest sounds in synthwave."

        # play music "audio/synthwave.mp3" fadein 1.0

        show headshot_ada shock at headshot_right, speaking
        ada "Whoa!"
        ada "Cait, I’ve wanted to visit homeworld for ages!"

        show headshot_ada mischief at headshot_right, speaking
        ada "Could this be our moment?"

        hide headshot_ada
        show headshot_cait PO at headshot_left, speaking
        cait "Believe me, it’s not all it’s cracked up to be."
        cait "It’s stuffy…"
        cait "Bureaucratic…"
        cait "Locals are always trying to play an angle…"

        hide headshot_cait
        show headshot_ada thoughtful at headshot_right, speaking
        ada "Haven’t you only been to Earth for academic conferences?"
        ada "No wonder it felt stuffy. You were just attending lectures the whole time."

        hide headshot_ada
        show headshot_cait PO at headshot_left, speaking
        cait "..."

        show headshot_cait focus at headshot_left, speaking
        cait "Fair enough."

        hide headshot_cait
        show headshot_ada happy at headshot_right, speaking
        ada "Think about it!"

        show headshot_ada neutral at headshot_right, speaking
        ada "You’ve never actually visited Earth as a tourist."
        ada "And…"

        show headshot_ada happy at headshot_right, speaking
        ada "You’ve never visited with me!"

        hide headshot_ada
        show headshot_cait sweet at headshot_left, speaking
        cait "Hm."

        hide headshot_cait
        show headshot_ada neutral at headshot_right, speaking
        ada "How about this?"
        ada "You tell me your least favorite thing about visiting homeworld, and I’ll propose an alternative."

        hide headshot_ada
        show headshot_cait focus at headshot_left, speaking
        cait "Well, that’s easy."
        cait "It definitely has to be…"

        hide headshot_cait

        menu:

            "The landscape":
                call scene_2_interaction_1_radio_landscape

            "The people":
                call scene_2_interaction_1_radio_people

            "The transportation":
                call scene_2_interaction_1_radio_transportation
        
        hide headshot_ada
        show headshot_cait sweet at headshot_left, speaking
        cait "Alright, I’m convinced."

        hide headshot_cait
        show headshot_ada_happy at headshot_right, speaking
        ada "Heck yes!"
        ada "Once I’m feeling better, I’ll start looking into details."

        show headshot_ada_mischief at headshot_right, speaking
        ada "Just you wait…"

        hide headshot_ada
        show headshot_cait sweet at headshot_left, speaking
        cait "..."


        $ scene_2_interaction_1_radio_1070_done = True

    else:

        "Radio" "That’s it for today in entertainment."

        "Radio" "Stay tuned for the newest, hottest sounds in synthwave."

        # play music "audio/synthwave.mp3" fadein 1.0

    return


################################################################################
## Radio 107.0 - The Landscape
################################################################################

label scene_2_interaction_1_radio_landscape:

    show headshot_cait PO at headshot_left, speaking
    cait "...The landscape."
    cait "No other planet has such abysmal urban sprawl."

    show headshot_cait focus at headshot_left, speaking
    cait "I much prefer Chaff-6."
    cait "There’s nothing like being surrounded by so much nature."

    hide headshot_cait
    show headshot_ada thoughtful at headshot_right, speaking
    ada "That’s true…"
    ada "No matter what you do on Earth, you’re going to be in a concrete jungle."
    ada "Even the rural parts are just miles of dark factories."
    ada "You’d think more homeworlders would come out here and live in the sticks."

    hide headshot_ada
    show headshot_cait PO at headshot_left, speaking
    cait "Be glad they don’t."

    hide headshot_cait
    show headshot_ada neutral at headshot_right, speaking
    ada "It’s pretty incredible to think that all the people on Chaff-6 wouldn’t amount to more than a mid-sized city over there."

    hide headshot_ada
    show headshot_cait focus at headshot_left, speaking
    cait "Sounds like it’s a no for a trip to homeworld, then."

    hide headshot_cait
    show headshot_ada shock at headshot_right, speaking
    ada "Hold on, now!"

    show headshot_ada neutral at headshot_right, speaking
    ada "If we’re already making the trip, then…"

    show headshot_ada happy at headshot_right, speaking
    ada "We’ll also stop by Mars!"

    hide headshot_ada
    show headshot_cait focus at headshot_left, speaking
    cait "Oh?"

    hide headshot_cait
    show headshot_ada neutral at headshot_right, speaking
    ada "Come on, you’d love that."

    hide headshot_ada
    show headshot_cait smile at headshot_left, speaking
    cait "It {i}would{/i} be a treat to see humanity’s first terraforming efforts…"

    hide headshot_cait
    show headshot_ada neutral at headshot_right, speaking
    ada "Right."
    ada "Plus, we could stop by the ancient preservation sites!"
    ada "Don’t you want to see how Mars {i}really{/i} looks? Like, originally?"

    hide headshot_ada
    show headshot_cait smile at headshot_left, speaking
    cait "That is quite compelling…"

    hide headshot_cait
    show headshot_ada happy at headshot_right, speaking
    ada "So it’s decided!"

    show headshot_ada neutral at headshot_right, speaking
    ada "Mars for you and Earth for me."

    hide headshot_ada

    return


################################################################################
## Radio 107.0 - The People
################################################################################

label scene_2_interaction_1_radio_people:

    show headshot_cait PO at headshot_left, speaking
    cait "...The people."
    cait "Everyone’s very snotty about being from homeworld."
    cait "They have absolutely no respect for anything going on beyond their own solar system."
    cait "And worse, they don’t have the guts to say it to your face."
    cait "So many mind games…"

    hide headshot_cait
    show headshot_ada neutral at headshot_right, speaking
    ada "Well, that’s an easy fix."

    show headshot_ada happy at headshot_right, speaking
    ada "I’ll just do all of the talking for both of us!"
    ada "Sounds like a much more pleasant trip now, doesn’t it?"

    hide headshot_ada
    show headshot_cait focus at headshot_left, speaking
    cait "Are you sure you’re up to the task?"
    cait "Not everyone is as nice as you, you know."

    hide headshot_cait
    show headshot_ada neutral at headshot_right, speaking
    ada "Of course."
    ada "But I’m not as wound up as you are."

    hide headshot_ada
    show headshot_cait PO at headshot_left, speaking
    cait "Choose your next words carefully."

    hide headshot_cait
    show headshot_ada mischief at headshot_right, speaking
    ada "Hey now!"

    show headshot_ada neutral at headshot_right, speaking
    ada "All I mean is that it’s hard to get under my nerves."

    show headshot_ada happy at headshot_right, speaking
    ada "I’ll expertly dodge their backhanded compliments with the art of not caring!"

    show headshot_ada neutral at headshot_right, speaking
    ada "...Leaving you to sit back and enjoy a quiet vacation."

    hide headshot_ada
    show headshot_cait sweet at headshot_left, speaking
    cait "I do see your vision…"

    hide headshot_cait

    return


################################################################################
## Radio 107.0 - The Transportation
################################################################################

label scene_2_interaction_1_radio_transportation:

    show headshot_cait PO at headshot_left, speaking
    cait "...The transportation."
    cait "The central spaceport is fine, but the interplanetary transit is ridiculously slow."

    show headshot_cait focus at headshot_left, speaking
    cait "They still use airplanes, for goodness’ sake!"

    hide headshot_cait
    show headshot_ada neutral at headshot_right, speaking
    ada "Your problem is that you’re trying to speed up, but really, we should slow down."

    show headshot_ada mischief at headshot_right, speaking
    ada "With…"

    show headshot_ada happy at headshot_right, speaking
    ada "Boats!!!"

    hide headshot_ada
    show headshot_cait sweet at headshot_left, speaking
    cait "Boats…?"
    cait "You do have a point…"

    hide headshot_cait
    show headshot_ada happy at headshot_right, speaking
    ada "Right!"
    ada "How many other planets can claim to have {i}that{/i} much liquid surface?"
    ada "Travel by ship is reason enough to go."

    hide headshot_ada
    show headshot_cait sweet at headshot_left, speaking
    cait "Compelling."

    show headshot_cait smile at headshot_left, speaking
    cait "Alright, I’m convinced."

    hide headshot_cait
    show headshot_ada happy at headshot_right, speaking
    ada "Heck yes!"
    ada "Once I’m feeling better, I’ll start looking into details."

    show headshot_ada mischief at headshot_right, speaking
    ada "Just you wait…"

    hide headshot_ada
    show headshot_cait sweet at headshot_left, speaking
    cait "..."

    hide headshot_cait

    return

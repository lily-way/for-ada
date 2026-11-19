################################################################################
## Scene 4 - Interaction 10 — Final Hospital Flashback
################################################################################


################################################################################
## State
################################################################################

default scene_4_interaction_10_calendar_done = False
default scene_4_interaction_10_window_done = False
default scene_4_interaction_10_file_done = False
default scene_4_interaction_10_bed_done = False


################################################################################
## Interactions — Before Repair File
################################################################################

define scene_4_interaction_10_file_objects = [

    Interaction(
        name="hospital_calendar",
        interaction_type="observe",
        area=(167, 77, 188, 278),
        action="scene_4_interaction_10_calendar",
        completed="scene_4_interaction_10_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_window",
        interaction_type="observe",
        area=(523, 0, 844, 654),
        action="scene_4_interaction_10_window",
        completed="scene_4_interaction_10_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_repair_file",
        interaction_type="interact",
        area=(1514, 606, 116, 71),
        action="scene_4_interaction_10_file",
        completed="scene_4_interaction_10_file_done",
        mandatory=True
    ),

]


################################################################################
## Interactions — After Repair File
################################################################################

define scene_4_interaction_10_bed_objects = [

    Interaction(
        name="hospital_calendar",
        interaction_type="observe",
        area=(167, 77, 188, 278),
        action="scene_4_interaction_10_calendar",
        completed="scene_4_interaction_10_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_window",
        interaction_type="observe",
        area=(523, 0, 844, 654),
        action="scene_4_interaction_10_window",
        completed="scene_4_interaction_10_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_bed_1",
        interaction_type="interact",
        area=(913, 773, 1162, 417),
        action="scene_4_interaction_10_bed",
        completed="scene_4_interaction_10_bed_done",
        mandatory=True
    ),

    Interaction(
        name="hospital_bed_2",
        interaction_type="interact",
        area=(1725, 550, 412, 259),
        action="scene_4_interaction_10_bed",
        completed="scene_4_interaction_10_bed_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_10:

    $ progress_interactions = None
    $ progress_open = False

    scene expression scene_4_interaction_4_background() as bg at background_pan
    with Fade(0.5, 2.0, 0.5)

    $ progress_interactions = scene_4_interaction_10_file_objects

    while not scene_4_interaction_10_file_done:

        call screen interaction_screen(
            scene_4_interaction_10_file_objects
        )

        call expression _return

    $ progress_interactions = scene_4_interaction_10_bed_objects

    while not scene_4_interaction_10_bed_done:

        call screen interaction_screen(
            scene_4_interaction_10_bed_objects
        )

        call expression _return

    hide headshot_cait
    hide headshot_ada

    show expression scene_4_interaction_4_background() as bg at background_fixed

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Calendar — Optional Observation
################################################################################

label scene_4_interaction_10_calendar:

    if scene_4_interaction_10_calendar_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(...)"

    young_cait "(I missed the grant proposal deadline.)"

    young_cait "(I won’t have funding for the next term.)"

    young_cait "(...)"

    show headshot_cait young_smile at headshot_left, speaking
    young_cait "(...)"

    hide headshot_cait

    $ scene_4_interaction_10_calendar_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Window — Optional Observation
################################################################################

label scene_4_interaction_10_window:

    if scene_4_interaction_10_window_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(Smells like rain today.)"

    young_cait "(Maybe Ada and I will go for a walk after our session.)"

    young_cait "(I’d like to pick up some more reading material for her.)"

    hide headshot_cait

    $ scene_4_interaction_10_window_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Repair File — Mandatory Interaction
################################################################################

label scene_4_interaction_10_file:

    if scene_4_interaction_10_file_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(I should review my notes.)"

    young_cait "(...)"

    young_cait "(But why?)"

    show headshot_cait young_worry at headshot_left, speaking
    young_cait "(It’s not like anyone is actually reading them.)"

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(...)"

    young_cait "(I think I’ll just see what Ada thinks.)"

    hide headshot_cait

    $ scene_4_interaction_10_file_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Hospital Bed — Mandatory Interaction
################################################################################

label scene_4_interaction_10_bed:

    if scene_4_interaction_10_bed_done:
        return

    if not scene_4_interaction_10_file_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_ada young_thoughtful at headshot_right, speaking
    young_ada "I wish I wasn’t an android."

    hide headshot_ada

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "What makes you say that?"

    hide headshot_cait

    show headshot_ada young_thoughtful at headshot_right, speaking
    young_ada "Well, I’ll use you for an example."

    young_ada "You’ve been studying me for weeks now…"

    young_ada "But it’s only because you’re this great biosyntheticist and there’s something wrong with me."

    young_ada "...Maybe I wish you were just interested in me."

    hide headshot_ada

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "..."

    young_cait "Why do you care about me?"

    young_cait "You’ve only known me for eight hours."

    hide headshot_cait

    show headshot_ada young_thoughtful at headshot_right, speaking
    young_ada "Yes, but you’ve known me for much longer."

    show headshot_ada young_neutral at headshot_right, speaking
    young_ada "I can tell by the way you treat me."

    young_ada "And if I’ve liked you this much in these past few hours…"

    young_ada "Then presumably I’ve also liked you in all of my eight-hour increments."

    show headshot_ada young_thoughtful at headshot_right, speaking
    young_ada "We basically have a relationship of many hours."

    hide headshot_ada

    show headshot_cait young_smile at headshot_left, speaking
    young_cait "I don’t think that’s how it works."

    hide headshot_cait

    show headshot_ada young_neutral at headshot_right, speaking
    young_ada "I just wish you were interested in me for non-android reasons."

    hide headshot_ada

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "..."

    young_cait "Maybe I am."

    hide headshot_cait

    show headshot_ada young_neutral at headshot_right, speaking
    young_ada "Heh."

    young_ada "I wish I wasn’t an android so that I could believe you."

    young_ada "Or even that I didn’t know."

    hide headshot_ada

    $ scene_4_interaction_10_bed_done = True

    show expression scene_4_interaction_4_background() as bg at background_fixed

    return

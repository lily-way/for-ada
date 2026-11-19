################################################################################
## Scene 4 - Interaction 6 — Hospital Flashback #2
################################################################################


################################################################################
## State
################################################################################

default scene_4_interaction_6_window_done = False
default scene_4_interaction_6_calendar_done = False
default scene_4_interaction_6_file_done = False
default scene_4_interaction_6_bed_done = False


################################################################################
## Interactions — Before Reading Repair File
################################################################################

define scene_4_interaction_6_file_objects = [

    Interaction(
        name="hospital_window",
        interaction_type="observe",
        area=(523, 0, 844, 654),
        action="scene_4_interaction_6_window",
        completed="scene_4_interaction_6_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_calendar",
        interaction_type="observe",
        area=(167, 77, 188, 278),
        action="scene_4_interaction_6_calendar",
        completed="scene_4_interaction_6_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_repair_file",
        interaction_type="interact",
        area=(1514, 606, 116, 71),
        action="scene_4_interaction_6_file",
        completed="scene_4_interaction_6_file_done",
        mandatory=True
    ),

]


################################################################################
## Interactions — After Reading Repair File
################################################################################

define scene_4_interaction_6_bed_objects = [

    Interaction(
        name="hospital_window",
        interaction_type="observe",
        area=(523, 0, 844, 654),
        action="scene_4_interaction_6_window",
        completed="scene_4_interaction_6_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_calendar",
        interaction_type="observe",
        area=(167, 77, 188, 278),
        action="scene_4_interaction_6_calendar",
        completed="scene_4_interaction_6_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_bed_1",
        interaction_type="interact",
        area=(913, 773, 1162, 417),
        action="scene_4_interaction_6_bed",
        completed="scene_4_interaction_6_bed_done",
        mandatory=True
    ),

    Interaction(
        name="hospital_bed_2",
        interaction_type="interact",
        area=(1725, 550, 412, 259),
        action="scene_4_interaction_6_bed",
        completed="scene_4_interaction_6_bed_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_6:

    $ progress_interactions = None
    $ progress_open = False

    scene expression scene_4_interaction_4_background() as bg at background_pan
    with Fade(0.5, 2.0, 0.5)

    $ progress_interactions = scene_4_interaction_6_file_objects

    while not scene_4_interaction_6_file_done:

        call screen interaction_screen(
            scene_4_interaction_6_file_objects
        )

        call expression _return

    $ progress_interactions = scene_4_interaction_6_bed_objects

    while not scene_4_interaction_6_bed_done:

        call screen interaction_screen(
            scene_4_interaction_6_bed_objects
        )

        call expression _return

    hide headshot_cait
    hide young_ada

    show expression scene_4_interaction_4_background() as bg at background_fixed

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Window — Optional Observation
################################################################################

label scene_4_interaction_6_window:

    if scene_4_interaction_6_window_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(This project has been a nice break from farm work.)"

    show headshot_cait young_pissed at headshot_left, speaking
    young_cait "(The latest generation of rabbits has been so hostile.)"

    young_cait "(The first trait I’ll breed for in the g-3s will have to be agreeability.)"

    hide headshot_cait

    $ scene_4_interaction_6_window_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Calendar — Optional Observation
################################################################################

label scene_4_interaction_6_calendar:

    if scene_4_interaction_6_calendar_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(Has a month passed already?)"

    young_cait "(...)"

    show headshot_cait young_smile at headshot_left, speaking
    young_cait "(Hm.)"

    young_cait "(I could definitely get used to Chaff-6.)"

    hide headshot_cait

    $ scene_4_interaction_6_calendar_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Repair File — Mandatory Interaction
################################################################################

label scene_4_interaction_6_file:

    if scene_4_interaction_6_file_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(I should review my notes.)"

    hide headshot_cait

    menu:

        "Read repair file":
            pass

    # TODO: Sound - Page flip

    "File" "Log Entry #11."

    "File" "She calls herself Ada."

    "File" "Ada is much calmer than originally reported by her owners."

    "File" "Particularly after being supplied with hair clippers and cutting shears."

    "File" "Her memory problems are persistent, but short-term."

    "File" "She retains and builds knowledge about the world, even as she forgets her circumstances."

    "File" "To further test this, she’ll be presented with novels and other reading materials beginning this week."

    "File" "This is anticipated to reveal more information on the nature of her memory loss."

    "File" "It may also help improve her mood."

    $ scene_4_interaction_6_file_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Hospital Bed — Mandatory Interaction
################################################################################

label scene_4_interaction_6_bed:

    if scene_4_interaction_6_bed_done:
        return

    if not scene_4_interaction_6_file_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show young_ada neutral at sprite_right, speaking
    young_ada "So you’re telling me that we’ve met before, only I don’t remember."

    show young_ada neutral at sprite_right, not_speaking
    show headshot_cait young_focus at headshot_left, speaking
    young_cait "That’s exactly right."

    hide headshot_cait

    show young_ada neutral at sprite_right, speaking
    young_ada "Nope."

    young_ada "I don’t buy it."

    show young_ada neutral at sprite_right, not_speaking
    show headshot_cait young_pissed at headshot_left, speaking
    young_cait "What do you mean you don’t buy it?"

    young_cait "I’m a licensed medical professional."

    hide headshot_cait

    show young_ada mischief at sprite_right, speaking
    young_ada "I just think you’re a little too life-changing to forget."

    show young_ada mischief at sprite_right, not_speaking
    show headshot_cait young_focus at headshot_left, speaking
    young_cait "Coming on a little strong, don’t you think?"

    hide headshot_cait

    show young_ada mischief at sprite_right, speaking
    young_ada "Not my problem if I forget this all tomorrow."

    hide young_ada

    $ scene_4_interaction_6_bed_done = True

    show expression scene_4_interaction_4_background() as bg at background_fixed

    return

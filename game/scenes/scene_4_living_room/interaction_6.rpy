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
        area=(520, 23, 841, 606),
        action="scene_4_interaction_6_window",
        completed="scene_4_interaction_6_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_calendar",
        interaction_type="observe",
        area=(267, 158, 163, 213),
        action="scene_4_interaction_6_calendar",
        completed="scene_4_interaction_6_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_repair_file",
        interaction_type="interact",
        area=(1419, 597, 107, 59),
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
        area=(520, 23, 841, 606),
        action="scene_4_interaction_6_window",
        completed="scene_4_interaction_6_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_calendar",
        interaction_type="observe",
        area=(267, 158, 163, 213),
        action="scene_4_interaction_6_calendar",
        completed="scene_4_interaction_6_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_bed_1",
        interaction_type="interact",
        area=(910, 736, 978, 308),
        action="scene_4_interaction_6_bed",
        completed="scene_4_interaction_6_bed_done",
        mandatory=True
    ),

    Interaction(
        name="hospital_bed_2",
        interaction_type="interact",
        area=(1591, 547, 386, 279),
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
    with fade

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
    hide headshot_ada

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
    cait "(This project has been a nice break from farm work.)"

    show headshot_cait young_pissed at headshot_left, speaking
    cait "(The latest generation of rabbits has been so hostile.)"

    cait "(The first trait I’ll breed for in the g-3s will have to be agreeability.)"

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
    cait "(Has a month passed already?)"

    cait "(...)"

    show headshot_cait young_smile at headshot_left, speaking
    cait "(Hm.)"

    cait "(I could definitely get used to Chaff-6.)"

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
    cait "(I should review my notes.)"

    hide headshot_cait

    menu:

        "Read repair file":
            pass

    # TODO: Sound - Page flip

    "Log Entry #11."

    "She calls herself Ada."

    "Ada is much calmer than originally reported by her owners."

    "Particularly after being supplied with hair clippers and cutting shears."

    "Her memory problems are persistent, but short-term."

    "She retains and builds knowledge about the world, even as she forgets her circumstances."

    "To further test this, she’ll be presented with novels and other reading materials beginning this week."

    "This is anticipated to reveal more information on the nature of her memory loss."

    "It may also help improve her mood."

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

    show headshot_ada young_neutral at headshot_right, speaking
    ada "So you’re telling me that we’ve met before, only I don’t remember."

    hide headshot_ada

    show headshot_cait young_focus at headshot_left, speaking
    cait "That’s exactly right."

    hide headshot_cait

    show headshot_ada young_neutral at headshot_right, speaking
    ada "Nope."

    ada "I don’t buy it."

    hide headshot_ada

    show headshot_cait young_pissed at headshot_left, speaking
    cait "What do you mean you don’t buy it?"

    cait "I’m a licensed medical professional."

    hide headshot_cait

    show headshot_ada young_mischief at headshot_right, speaking
    ada "I just think you’re a little too life-changing to forget."

    hide headshot_ada

    show headshot_cait young_focus at headshot_left, speaking
    cait "Coming on a little strong, don’t you think?"

    hide headshot_cait

    show headshot_ada young_mischief at headshot_right, speaking
    ada "Not my problem if I forget this all tomorrow."

    hide headshot_ada

    $ scene_4_interaction_6_bed_done = True

    show expression scene_4_interaction_4_background() as bg at background_fixed

    return

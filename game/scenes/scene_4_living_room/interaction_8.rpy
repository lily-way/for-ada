################################################################################
## Scene 4 - Interaction 8 — Hospital Flashback #3
################################################################################


################################################################################
## State
################################################################################

default scene_4_interaction_8_calendar_done = False
default scene_4_interaction_8_window_done = False
default scene_4_interaction_8_file_done = False
default scene_4_interaction_8_bed_done = False


################################################################################
## Interactions — Before Reading Repair File
################################################################################

define scene_4_interaction_8_file_objects = [

    Interaction(
        name="hospital_calendar",
        interaction_type="observe",
        area=(267, 158, 163, 213),
        action="scene_4_interaction_8_calendar",
        completed="scene_4_interaction_8_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_window",
        interaction_type="observe",
        area=(520, 23, 841, 606),
        action="scene_4_interaction_8_window",
        completed="scene_4_interaction_8_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_repair_file",
        interaction_type="interact",
        area=(1419, 597, 107, 59),
        action="scene_4_interaction_8_file",
        completed="scene_4_interaction_8_file_done",
        mandatory=True
    ),

]


################################################################################
## Interactions — After Reading Repair File
################################################################################

define scene_4_interaction_8_bed_objects = [

    Interaction(
        name="hospital_calendar",
        interaction_type="observe",
        area=(267, 158, 163, 213),
        action="scene_4_interaction_8_calendar",
        completed="scene_4_interaction_8_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_window",
        interaction_type="observe",
        area=(520, 23, 841, 606),
        action="scene_4_interaction_8_window",
        completed="scene_4_interaction_8_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_bed_1",
        interaction_type="interact",
        area=(910, 736, 978, 308),
        action="scene_4_interaction_8_bed",
        completed="scene_4_interaction_8_bed_done",
        mandatory=True
    ),

    Interaction(
        name="hospital_bed_2",
        interaction_type="interact",
        area=(1591, 547, 386, 279),
        action="scene_4_interaction_8_bed",
        completed="scene_4_interaction_8_bed_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_8:

    $ progress_interactions = None
    $ progress_open = False

    scene expression scene_4_interaction_4_background() as bg at background_pan
    with fade

    $ progress_interactions = scene_4_interaction_8_file_objects

    while not scene_4_interaction_8_file_done:

        call screen interaction_screen(
            scene_4_interaction_8_file_objects
        )

        call expression _return

    $ progress_interactions = scene_4_interaction_8_bed_objects

    while not scene_4_interaction_8_bed_done:

        call screen interaction_screen(
            scene_4_interaction_8_bed_objects
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

label scene_4_interaction_8_calendar:

    if scene_4_interaction_8_calendar_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_worry at headshot_left, speaking
    cait "(The deadline for grant proposals is coming up fast.)"

    cait "(I’ll need to start drafting if I want funding for the upcoming term.)"

    cait "(But who would fund me, at this point…?)"

    cait "(…)"

    hide headshot_cait

    $ scene_4_interaction_8_calendar_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Window — Optional Observation
################################################################################

label scene_4_interaction_8_window:

    if scene_4_interaction_8_window_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    cait "(I wonder if Ada would like to see the farm.)"

    show headshot_cait young_smile at headshot_left, speaking
    cait "(I’m sure the g-3s would love her.)"

    show headshot_cait young_pissed at headshot_left, speaking
    cait "(More than me, anyway…)"

    show headshot_cait young_focus at headshot_left, speaking
    cait "(I just wouldn’t want her to feel disoriented.)"

    show headshot_cait young_smile at headshot_left, speaking
    cait "(Maybe we can think about it when I get closer to a working prototype.)"

    hide headshot_cait

    $ scene_4_interaction_8_window_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Repair File — Mandatory Interaction
################################################################################

label scene_4_interaction_8_file:

    if scene_4_interaction_8_file_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    cait "(I should review my notes.)"

    hide headshot_cait

    menu:

        "Read repair file":
            pass

    # TODO: Sound - Page flip

    "Log Entry #30."

    "Ada’s owners have moved off-planet."

    "I think I’m close to a breakthrough, but they didn’t want to stick around."

    "But maybe this is the best for everyone."

    "For one, I no longer need their permission to modify Ada’s physical frame."

    "I’ve made surgical improvements to the base D4 model that Ada seems much more comfortable with."

    "Once I can correct her memory, she’ll be able to choose where she goes next."

    "I look forward to helping her become independent."

    $ scene_4_interaction_8_file_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Hospital Bed — Mandatory Interaction
################################################################################

label scene_4_interaction_8_bed:

    if scene_4_interaction_8_bed_done:
        return

    if not scene_4_interaction_8_file_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_ada young_smile at headshot_right, speaking
    ada "Stop me if you’ve heard this one before."

    hide headshot_ada

    show headshot_cait young_smile at headshot_left, speaking
    cait "You think I haven’t heard them all before yet?"

    hide headshot_cait

    show headshot_ada young_thoughtful at headshot_right, speaking
    ada "Well, maybe…"

    show headshot_ada young_smile at headshot_right, speaking
    ada "but I still want to try to entertain you!"

    show headshot_ada young_mischief at headshot_right, speaking
    ada "I promise I’m more interesting than whatever’s wrong with my brain."

    hide headshot_ada

    show headshot_cait young_sweet at headshot_left, speaking
    cait "I believe you."

    hide headshot_cait

    $ scene_4_interaction_8_bed_done = True

    show expression scene_4_interaction_4_background() as bg at background_fixed

    return

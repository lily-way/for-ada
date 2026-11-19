################################################################################
## Scene 4 - Interaction 4 — Hospital Flashback #1
################################################################################


################################################################################
## State
################################################################################

default scene_4_interaction_4_window_done = False
default scene_4_interaction_4_bed_done = False
default scene_4_interaction_4_calendar_done = False
default scene_4_interaction_4_file_done = False


################################################################################
## Background
################################################################################

init python:

    def scene_4_interaction_4_background():

        return Composite(
            (2300, 1200),
            (0, 0), "bg light_cycle_1",
            (0, 0), "bg hospital"
        )


################################################################################
## Interactions
################################################################################

define scene_4_interaction_4_objects = [

    Interaction(
        name="hospital_window",
        interaction_type="observe",
        area=(523, 0, 844, 654),
        action="scene_4_interaction_4_window",
        completed="scene_4_interaction_4_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_bed_1",
        interaction_type="observe",
        area=(913, 773, 1162, 417),
        action="scene_4_interaction_4_bed",
        completed="scene_4_interaction_4_bed_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_bed_2",
        interaction_type="observe",
        area=(1725, 550, 412, 259),
        action="scene_4_interaction_4_bed",
        completed="scene_4_interaction_4_bed_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_calendar",
        interaction_type="observe",
        area=(167, 77, 188, 278),
        action="scene_4_interaction_4_calendar",
        completed="scene_4_interaction_4_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_repair_file",
        interaction_type="interact",
        area=(1514, 606, 116, 71),
        action="scene_4_interaction_4_file",
        completed="scene_4_interaction_4_file_done",
        mandatory=True
    ),

]


################################################################################
## Scene
################################################################################

label scene_4_interaction_4:

    $ progress_interactions = scene_4_interaction_4_objects
    $ progress_open = False

    scene expression scene_4_interaction_4_background() as bg at background_pan
    with Fade(0.5, 2.0, 0.5)

    while not scene_4_interaction_4_file_done:

        call screen interaction_screen(
            scene_4_interaction_4_objects
        )

        call expression _return

    hide headshot_cait

    show expression scene_4_interaction_4_background() as bg at background_fixed

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Window — Optional Observation
################################################################################

label scene_4_interaction_4_window:

    if scene_4_interaction_4_window_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_smile at headshot_left, speaking
    young_cait "(Chaff-6 is so peaceful.)"

    young_cait "(It’s nice to finally have a breath of fresh air.)"

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(Still, it’s good to keep my skills sharp.)"

    show headshot_cait young_pissed at headshot_left, speaking
    young_cait "(I don’t want to be rusty when I go back to work.)"

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(This job should do the trick.)"

    hide headshot_cait

    $ scene_4_interaction_4_window_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Hospital Bed — Optional Observation
################################################################################

label scene_4_interaction_4_bed:

    if scene_4_interaction_4_bed_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(The android should be arriving soon…)"

    young_cait "(Its owners seem exasperated.)"

    young_cait "(If I can’t resolve its issues before they move off-planet…)"

    show headshot_cait young_worry at headshot_left, speaking
    young_cait "(Quite frankly, I don’t know where it’ll end up.)"

    hide headshot_cait

    $ scene_4_interaction_4_bed_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Calendar — Optional Observation
################################################################################

label scene_4_interaction_4_calendar:

    if scene_4_interaction_4_calendar_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(Six months of sabbatical on a farming planet.)"

    show headshot_cait young_worry at headshot_left, speaking
    young_cait "(Is this really what I want?)"

    young_cait "(...)"

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(No, I need the break.)"

    young_cait "(And maybe even more than that…)"

    show headshot_cait young_pissed at headshot_left, speaking
    young_cait "(Academia needs a break from me.)"

    hide headshot_cait

    $ scene_4_interaction_4_calendar_done = True

    show expression scene_4_interaction_4_background() as bg at background_pan

    return


################################################################################
## Repair File — Mandatory Interaction
################################################################################

label scene_4_interaction_4_file:

    if scene_4_interaction_4_file_done:
        return

    show expression scene_4_interaction_4_background() as bg at background_freeze

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(I may as well review my notes while I have time.)"

    hide headshot_cait

    menu:

        "Read repair file":
            pass

    # TODO: Sound - Page flip

    "File" "Log Entry #1."

    "File" "Owners report major memory and behavioral issues."

    "File" "The D4 android possesses a consistent sense of self and worldly knowledge, but no memory of its immediate surroundings or duties."

    "File" "Loss of memory is coupled with non-compliant activity, including the following:"

    "File" "Cutting or shaving its hair,"

    "File" "Reading books and news articles,"

    "File" "Self-destruction to breast tissue."

    "File" "The D4 is non-responsive to verbal and physical instruction."

    # TODO: Sound - Page flip

    show headshot_cait young_worry at headshot_left, speaking
    young_cait "(...)"

    young_cait "(This android is very afraid.)"

    young_cait "(I’ll need to speak to it myself to understand.)"

    hide headshot_cait

    $ scene_4_interaction_4_file_done = True

    show expression scene_4_interaction_4_background() as bg at background_fixed

    return

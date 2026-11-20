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
        area=(167, 77, 188, 278),
        action="scene_4_interaction_8_calendar",
        completed="scene_4_interaction_8_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_window",
        interaction_type="observe",
        area=(523, 0, 844, 654),
        action="scene_4_interaction_8_window",
        completed="scene_4_interaction_8_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_repair_file",
        interaction_type="interact",
        area=(1514, 606, 116, 71),
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
        area=(167, 77, 188, 278),
        action="scene_4_interaction_8_calendar",
        completed="scene_4_interaction_8_calendar_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_window",
        interaction_type="observe",
        area=(523, 0, 844, 654),
        action="scene_4_interaction_8_window",
        completed="scene_4_interaction_8_window_done",
        mandatory=False
    ),

    Interaction(
        name="hospital_bed_1",
        interaction_type="interact",
        area=(913, 773, 1162, 417),
        action="scene_4_interaction_8_bed",
        completed="scene_4_interaction_8_bed_done",
        mandatory=True
    ),

    Interaction(
        name="hospital_bed_2",
        interaction_type="interact",
        area=(1725, 550, 412, 259),
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
    with Fade(0.5, 2.0, 0.5)

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
    hide young_ada

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
    young_cait "(The deadline for grant proposals is coming up fast.)"

    young_cait "(I’ll need to start drafting if I want funding for the upcoming term.)"

    young_cait "(But who would fund me, at this point…?)"

    young_cait "(…)"

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
    young_cait "(I wonder if Ada would like to see the farm.)"

    show headshot_cait young_smile at headshot_left, speaking
    young_cait "(I’m sure the g-3s would love her.)"

    show headshot_cait young_pissed at headshot_left, speaking
    young_cait "(More than me, anyway…)"

    show headshot_cait young_focus at headshot_left, speaking
    young_cait "(I just wouldn’t want her to feel disoriented.)"

    show headshot_cait young_smile at headshot_left, speaking
    young_cait "(Maybe we can think about it when I get closer to a working prototype.)"

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
    young_cait "(I should review my notes.)"

    hide headshot_cait

    menu:

        "Read repair file":
            pass
    
    play sound "audio/sound_effects/page_flip.mp3"

    "File" "Log Entry #30."
    
    play sound "audio/sound_effects/page_flip.mp3"

    "File" "Ada’s owners have moved off-planet."
    
    play sound "audio/sound_effects/page_flip.mp3"

    "File" "I think I’m close to a breakthrough, but they didn’t want to stick around."
    
    play sound "audio/sound_effects/page_flip.mp3"

    "File" "But maybe this is the best for everyone."
    
    play sound "audio/sound_effects/page_flip.mp3"

    "File" "For one, I no longer need their permission to modify Ada’s physical frame."
    
    play sound "audio/sound_effects/page_flip.mp3"

    "File" "I’ve made surgical improvements to the base D4 model that Ada seems much more comfortable with."
    
    play sound "audio/sound_effects/page_flip.mp3"

    "File" "Once I can correct her memory, she’ll be able to choose where she goes next."
    
    play sound "audio/sound_effects/page_flip.mp3"

    "File" "I look forward to helping her become independent."
    
    play sound "audio/sound_effects/page_close.mp3"

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

    show young_ada smile at sprite_right, speaking
    young_ada "Stop me if you’ve heard this one before."

    show young_ada smile at sprite_right, not_speaking
    show headshot_cait young_smile at headshot_left, speaking
    young_cait "You think I haven’t heard them all before yet?"

    hide headshot_cait

    show young_ada thoughtful at sprite_right, speaking
    young_ada "Well, maybe…"

    show young_ada smile at sprite_right, speaking
    young_ada "but I still want to try to entertain you!"

    show young_ada mischief at sprite_right, speaking
    young_ada "I promise I’m more interesting than whatever’s wrong with my brain."

    show young_ada mischief at sprite_right, not_speaking
    show headshot_cait young_sweet at headshot_left, speaking
    young_cait "I believe you."

    hide headshot_cait
    hide young_ada

    $ scene_4_interaction_8_bed_done = True

    show expression scene_4_interaction_4_background() as bg at background_fixed

    return

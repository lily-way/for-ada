################################################################################
## Scene 3 - Interaction 2
################################################################################


################################################################################
## State
################################################################################

default scene_3_interaction_2_cheek_ear_done = False
default scene_3_interaction_2_nose_mouth_done = False
default scene_3_interaction_2_eyes_done = False
default scene_3_interaction_2_neck_done = False


################################################################################
## Interactions
################################################################################

define scene_3_interaction_2_objects = [

    Interaction(
        name="cheek",
        interaction_type="observe",
        area=(1045, 469, 348, 350),
        action="scene_3_interaction_2_cheek_ear",
        completed="scene_3_interaction_2_cheek_ear_done",
        mandatory=False
    ),

    Interaction(
        name="ear",
        interaction_type="observe",
        area=(1496, 140, 225, 395),
        action="scene_3_interaction_2_cheek_ear",
        completed="scene_3_interaction_2_cheek_ear_done",
        mandatory=False
    ),

    Interaction(
        name="nose",
        interaction_type="observe",
        area=(662, 486, 214, 219),
        action="scene_3_interaction_2_nose_mouth",
        completed="scene_3_interaction_2_nose_mouth_done",
        mandatory=False
    ),

    Interaction(
        name="mouth",
        interaction_type="observe",
        area=(709, 768, 241, 156),
        action="scene_3_interaction_2_nose_mouth",
        completed="scene_3_interaction_2_nose_mouth_done",
        mandatory=False
    ),

    Interaction(
        name="left_eye",
        interaction_type="observe",
        area=(553, 305, 164, 135),
        action="scene_3_interaction_2_eyes",
        completed="scene_3_interaction_2_eyes_done",
        mandatory=False
    ),

    Interaction(
        name="right_eye",
        interaction_type="observe",
        area=(832, 199, 319, 167),
        action="scene_3_interaction_2_eyes",
        completed="scene_3_interaction_2_eyes_done",
        mandatory=False
    ),

    Interaction(
        name="neck_box_1",
        interaction_type="interact",
        area=(962, 1069, 685, 130),
        action="scene_3_interaction_2_neck",
        completed="scene_3_interaction_2_neck_done",
        mandatory=True
    ),

    Interaction(
        name="neck_box_2",
        interaction_type="interact",
        area=(1291, 857, 360, 213),
        action="scene_3_interaction_2_neck",
        completed="scene_3_interaction_2_neck_done",
        mandatory=True
    ),

]


################################################################################
## Progress Interactions
################################################################################

define scene_3_interaction_2_progress_objects = [
    scene_3_interaction_2_objects[0],
    scene_3_interaction_2_objects[2],
    scene_3_interaction_2_objects[4],
    scene_3_interaction_2_objects[6]
]


################################################################################
## Scene
################################################################################

label scene_3_interaction_2:

    $ progress_interactions = scene_3_interaction_2_progress_objects
    $ progress_open = False

    hide port
    scene bg d9_closeup_aware at background_pan
    with fade

    # TODO: Sound - breathing

    while not scene_3_interaction_2_neck_done:

        call screen interaction_screen(scene_3_interaction_2_objects)
        call expression _return

    $ progress_interactions = None
    $ progress_open = False

    return


################################################################################
## Optional Observation - Cheek / Ear
################################################################################

label scene_3_interaction_2_cheek_ear:

    if scene_3_interaction_2_cheek_ear_done:
        return

    show bg d9_closeup_aware at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(If only I knew what thoughts were running through your head, D9…)"
    cait "(Are you angry with me?)"
    cait "(Frustrated with Martin?)"
    cait "(Ashamed of yourself?)"
    cait "(I can’t know without you telling me.)"
    cait "(Each android is different, after all.)"
    cait "(You have your own personalities…)"
    cait "(Dreams…)"
    cait "(Fears…)"
    cait "(You’re complicated.)"
    cait "(Just like us.)"
    cait "(Whatever you’re thinking, I hope this helps.)"

    hide headshot_cait

    $ scene_3_interaction_2_cheek_ear_done = True

    show bg d9_closeup_aware at background_pan

    return


################################################################################
## Optional Observation - Nose / Mouth
################################################################################

label scene_3_interaction_2_nose_mouth:

    if scene_3_interaction_2_nose_mouth_done:
        return

    show bg d9_closeup_aware at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(D9 is in excellent homeostatic condition.)"
    cait "(Not a surprise. Martin’s always taken good care of his androids.)"
    cait "(Still, nothing can prevent the decay of human organics.)"
    cait "(Even with so many advancements in biosynthetics, human tissue simply can’t persist in an android frame for very long.)"
    cait "(Two years, to be exact.)"
    cait "(Of course, there are no scientific barriers to replacing an android’s human organics.)"

    show headshot_cait PO at headshot_left, speaking
    cait "(Just legal ones.)"
    cait "(According to the review boards, maintaining a tool capable of original thought for too long was an ethical concern.)"
    cait "(In other words…)"

    show headshot_cait focus at headshot_left, speaking
    cait "(They feared sentience.)"

    show headshot_cait PO at headshot_left, speaking
    cait "(And because of their fears…)"
    cait "(Their waste…)"
    cait "(We lose good beings.)"
    cait "({i}Kind{/i} beings.)"
    cait "(Beings like D8.)"
    cait "(...)"

    show headshot_cait focus at headshot_left, speaking
    cait "(But you still have so much life, D9.)"
    cait "(You still hold such potential.)"

    hide headshot_cait

    $ scene_3_interaction_2_nose_mouth_done = True

    show bg d9_closeup_aware at background_pan

    return


################################################################################
## Optional Observation - Eyes
################################################################################

label scene_3_interaction_2_eyes:

    if scene_3_interaction_2_eyes_done:
        return

    show bg d9_closeup_aware at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(For a long time, eyes were the trickiest human organ to industrially reproduce.)"
    cait "(Hearts, lungs, stomachs…)"
    cait "(Corporate tissue-farming worlds cranked those out by the ton and had them across the galaxy in a week.)"
    cait "(But not eyes.)"

    show headshot_cait PO at headshot_left, speaking
    cait "(In the early days, my lab would have to place orders months in advance if we wanted to prototype with a set of them.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(It was only because of advancements in precision stem cell manufacturing that we could start reliably creating sighted android designs.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(We were the first to show plastic adaptation of the human eye to android synethics.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(At this point, critical human-to-android grafts like the heart or the digestives had long been operational, but this…)"

    show headshot_cait smile at headshot_left, speaking
    cait "(This was revolutionary.)"

    show headshot_cait focus at headshot_left, speaking
    cait "(D9 is evidence of how far the field has come since those early days.)"
    cait "(When I look at you, D9, I can’t say I’m not proud.)"
    cait "(Whichever manufacturer produced you does impressive work.)"

    show headshot_cait smile at headshot_left, speaking
    cait "(You are impressive.)"

    hide headshot_cait

    $ scene_3_interaction_2_eyes_done = True

    show bg d9_closeup_aware at background_pan

    return


################################################################################
## Mandatory Interaction - Neck
################################################################################

label scene_3_interaction_2_neck:

    if scene_3_interaction_2_neck_done:
        return

    show bg d9_closeup_aware at background_freeze

    show headshot_cait focus at headshot_left, speaking
    cait "(I’ve opened up these panels so many times, I could do it with my eyes closed.)"

    hide headshot_cait

    menu:

        "Reveal flash ports":

            play sound "audio/sound_effects/d9_port_reveal.mp3"

            show expression "images/backgrounds/d9_empty_port.png" as port zorder 10 at background_freeze

            pause 0.5

            show headshot_cait focus at headshot_left, speaking
            cait "(Less sensory input should reduce your stress responses.)"
            cait "(I have a crude fix on hand that should do the trick.)"
            cait "(Just try to relax, D9…)"

            hide headshot_cait

    menu:

        "Insert damping drive":

            play sound "audio/sound_effects/d9_port_insert.mp3"

            show bg d9_closeup_auto at background_freeze
            show expression "images/backgrounds/d9_full_port.png" as port zorder 10 at background_freeze

            pause 0.5

            show headshot_cait smile at headshot_left, speaking
            cait "(Much better.)"

            hide headshot_cait

    $ scene_3_interaction_2_neck_done = True

    return

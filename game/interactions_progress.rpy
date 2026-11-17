################################################################################
## Interaction Progress
################################################################################

default progress_open = False
default progress_interactions = None


################################################################################
## Progress Tracking
################################################################################

init python:

    if "interaction_progress_overlay" not in config.overlay_screens:
        config.overlay_screens.append("interaction_progress_overlay")


    def get_interaction_progress(objects, mandatory):

        interactions = [
            obj for obj in objects
            if obj.mandatory == mandatory and getattr(obj, "completed", None)
        ]

        completed = sum(
            1 for obj in interactions
            if getattr(renpy.store, obj.completed, False)
        )

        return completed, len(interactions)


    def toggle_progress():

        renpy.store.progress_open = not renpy.store.progress_open


################################################################################
## Progress Display
################################################################################

screen interaction_progress_overlay():

    zorder 200

    if progress_interactions is not None:

        key "K_q" action Function(toggle_progress)

        if progress_open:

            $ mandatory_done, mandatory_total = get_interaction_progress(progress_interactions, True)
            $ optional_done, optional_total = get_interaction_progress(progress_interactions, False)

            frame:
                xalign 0.98
                yalign 0.03

                background "#161616DD"
                padding (20, 15)

                vbox:
                    spacing 10

                    text "Mandatory: [mandatory_done]/[mandatory_total]":
                        color gui.cursor_mandatory_color
                        size 26

                    text "Optional: [optional_done]/[optional_total]":
                        color gui.cursor_optional_color
                        size 26

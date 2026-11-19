################################################################################
## Interaction System
################################################################################

init python:

    class Interaction:

        def __init__(
            self,
            name,
            interaction_type,
            area,
            action,
            completed=None,
            mandatory=None
        ):
            self.name = name
            self.type = interaction_type
            self.area = area
            self.action = action
            self.completed = completed

            if mandatory is None:
                mandatory = interaction_type == "interact"

            self.mandatory = mandatory


        def is_completed(self):

            if self.completed is None:
                return False

            return getattr(store, self.completed, False)


        def get_cursor(self):

            if self.is_completed():
                return self.type + "_done"

            if self.mandatory:
                return self.type + "_mandatory"

            return self.type + "_optional"


################################################################################
## Interaction Screen
################################################################################

screen interaction_screen(interactions):
    key "K_b" action Function(debug_editor_open)
    fixed:
        xsize 2300
        ysize 1200

        at background_pan

        for interaction in interactions:

            button:
                xpos interaction.area[0]
                ypos interaction.area[1]
                xsize interaction.area[2]
                ysize interaction.area[3]

                padding (0, 0)

                background Solid("#00FF0066")
                hover_background Solid("#00FF0099")

                mouse interaction.get_cursor()

                action Return(interaction.action)

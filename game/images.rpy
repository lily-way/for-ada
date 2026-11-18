################################################################################
## Backgrounds
################################################################################

image bg store = "images/backgrounds/Grocery_BC.png"
image bg kitchen = "images/backgrounds/Kitchen_BC.png"
image bg living_room = "images/backgrounds/Living_room_BC.png"
image bg kitchen_floor = "images/backgrounds/Floor_Sketch.png"
image bg countertop_pot_closed = "images/backgrounds/Kitchen_Counter_Closed_BC.png"
image bg countertop_pot_open = "images/backgrounds/Kitchen_Counter_Open_BC.png"
image bg storefront_window = "images/backgrounds/Storefront_BC_Window.png"
image bg storefront_no_window = "images/backgrounds/Storefront_BC_No_Window.png"
image bg interior_grocery_store_night = "images/backgrounds/Grocery_BC.png"


################################################################################
## Light Cycles
################################################################################

image bg light_cycle_0 = "images/backgrounds/Light_Cycles(0).png"
image bg light_cycle_1 = "images/backgrounds/Light_Cycles(1).png"
image bg light_cycle_2 = "images/backgrounds/Light_Cycles(2).png"
image bg light_cycle_3 = "images/backgrounds/Light_Cycles(3).png"
image bg light_cycle_4 = "images/backgrounds/Light_Cycles(4).png"

################################################################################
## Cait Headshots
################################################################################

image headshot_cait focus = make_headshot("images/characters/headshots/cait_focus_headshot.png")
image headshot_cait smile = make_headshot("images/characters/headshots/cait_smile_headshot.png")
image headshot_cait sweet = make_headshot("images/characters/headshots/cait_sweet_headshot.png")
image headshot_cait PO = make_headshot("images/characters/headshots/cait_pissed_headshot.png")
image headshot_cait worry = make_headshot("images/characters/headshots/cait_worry_headshot.png")
image headshot_cait panic = make_headshot("images/characters/headshots/cait_sob_headshot.png")

image headshot_cait sweet = make_headshot("images/characters/headshots/Cait_sweet_hs.png")
image headshot_cait focus = make_headshot("images/characters/headshots/Cait_focus_hs.png")
image headshot_cait PO = make_headshot("images/characters/headshots/Cait_PO_hs.png")
image headshot_cait focus = make_headshot("images/characters/headshots/Cait_focus_hs.png")
image headshot_cait PO = make_headshot("images/characters/headshots/Cait_PO_hs.png")
image headshot_cait smile = make_headshot("images/characters/headshots/Cait_smile_hs.png")
image headshot_cait panic = make_headshot("images/characters/headshots/Cait_panic_hs.png")

image headshot_cait focus = make_headshot("images/characters/headshots/Cait_focus_hs.png")
image headshot_cait sweet = make_headshot("images/characters/headshots/Cait_sweet_hs.png")
image headshot_cait PO = make_headshot("images/characters/headshots/Cait_PO_hs.png")


################################################################################
## Martin Sprites
################################################################################

image martin neutral = "images/characters/Martin_Neutral.png"
image martin laugh = "images/characters/Martin_Happy.png"

image martin PJs_concerned = "images/characters/Martin_PJs_Concern.png"
image martin PJs_neutral = "images/characters/Martin_PJs_Neutral.png"
image martin PJs_horror = "images/characters/Martin_PJs_Horror.png"


################################################################################
## Martin Headshots
################################################################################

image headshot_martin neutral = make_headshot("images/characters/headshots/Martin_Neutral_Headshot.png", center_x=0.55)
image headshot_martin laugh = make_headshot("images/characters/headshots/Martin_Happy_Headshot.png", center_x=0.55)
image headshot_martin rage = make_headshot("images/characters/headshots/Martin_Rage_Headshot.png", center_x=0.55)


################################################################################
## Martin's Wife Sprites
################################################################################

image martins_wife horror = "images/characters/Wife_Horror.png"
image martins_wife headbleed = "images/characters/Wife_Head.png"
image martins_wife eyebleed = "images/characters/Wife_Eye.png"


################################################################################
## D9 Expressions
################################################################################

image d9 neutral = "images/characters/D9_Neutral.png"
image d9 alarmed = "images/characters/D9_Alarmed.png"
image d9 automaton = "images/characters/D9_Automaton.png"
image d9 fear = "images/characters/D9_Fear.png"

################################################################################
## Ada Sprites (Temporary Debug)
################################################################################

init python:

    def ada_debug_sprite(expression):

        return Composite(
            (800, 1200),
            (0, 0), "images/characters/Ada.png",
            (300, 50), Text(
                expression.upper(),
                size=50,
                color="#00FF00",
                outlines=[(3, "#000000", 0, 0)]
            )
        )


################################################################################
## Ada Expressions
################################################################################

image ada neutral = ada_debug_sprite("neutral")
image ada sleepy = ada_debug_sprite("sleepy")
image ada sick = ada_debug_sprite("sick")
image ada mischief = ada_debug_sprite("mischief")
image ada happy = ada_debug_sprite("happy")
image ada shock = ada_debug_sprite("shock")
image ada thoughtful = ada_debug_sprite("thoughtful")
image ada deathly_eyes_open = ada_debug_sprite("deathly_eyes_open")
image ada deathly_eyes_closed = ada_debug_sprite("deathly_eyes_closed")


################################################################################
## Ada Headshots (Temporary Debug)
################################################################################

init python:

    def ada_debug_headshot(expression):

        return make_headshot(
            Composite(
                (500, 450),
                (0, 0), "images/characters/headshots/Ada_hs.png",
                (150, 50), Text(
                    expression.upper(),
                    size=40,
                    color="#00FF00",
                    outlines=[(3, "#000000", 0, 0)]
                )
            )
        )


################################################################################
## Ada Headshot Expressions
################################################################################

image headshot_ada neutral = make_headshot("images/characters/headshots/ada_neutral_headshot.png")
image headshot_ada sleepy = make_headshot("images/characters/headshots/ada_sleepy_headshot.png")
image headshot_ada sick = make_headshot("images/characters/headshots/ada_sick_headshot.png")
image headshot_ada mischief = make_headshot("images/characters/headshots/ada_mischief_headshot.png")
image headshot_ada happy = make_headshot("images/characters/headshots/ada_neutral_headshot.png")
image headshot_ada shock = make_headshot("images/characters/headshots/ada_shock_headshot.png")
image headshot_ada thoughtful = make_headshot("images/characters/headshots/ada_thoughtful_headshot.png")


################################################################################
## Cooking Ingredients
################################################################################

image ingredient_apiaceae = "images/cooking_ingredients/Apiaceae.png"
image ingredient_apiaceae_cut = "images/cooking_ingredients/Apiaceae_Cut.png"

image ingredient_crucifer = "images/cooking_ingredients/Crucifer.png"
image ingredient_crucifer_cut = "images/cooking_ingredients/Crucifer_Cut.png"

image ingredient_broth = "images/cooking_ingredients/Broth.png"

image ingredient_rabbit = "images/cooking_ingredients/Rabbit.png"
image ingredient_rabbit_cut = "images/cooking_ingredients/Rabbit_Cut.png"
image ingredient_rabbit_pot = "images/cooking_ingredients/Rabbit_Pot.png"

image ingredient_veggies_pot = "images/cooking_ingredients/Veggies_Pot.png"


################################################################################
## Martin Dissection Backgrounds
################################################################################

image bg martin_clothed_torso = "images/backgrounds/martin_clothed_torso.png"
image bg martin_exposed_torso = "images/backgrounds/martin_exposed_torso.png"
image bg martin_exposed_ribcage = "images/backgrounds/MartinFloor3.png"
image bg martin_exposed_organs = "images/backgrounds/MartinFloor4.png"
image bg martin_no_lungs = "images/backgrounds/MartinFloor5.png"

################################################################################
## Martin's Wife Dissection Backgrounds
################################################################################

image bg wife_clothed_torso = "images/backgrounds/wife_clothed_torso.png"
image bg wife_exposed_torso = "images/backgrounds/wife_exposed_torso.png"
image bg wife_exposed_organs = "images/backgrounds/wife_exposed_organs.png"
image bg wife_no_heart = "images/backgrounds/wife_no_heart.png"

################################################################################
## D9 Dissection Backgrounds
################################################################################

image bg d9_clothed_torso = "images/backgrounds/d9_clothed_torso.png"
image bg d9_cut_torso = "images/backgrounds/d9_cut_clothed_torso.png"
image bg d9_exposed_torso = "images/backgrounds/d9_exposed_torso.png"
image bg d9_ports_torso = "images/backgrounds/d9_ports_torso.png"
image bg d9_tubes_torso = "images/backgrounds/d9_tubes_torso.png"

################################################################################
## D9 Close-up Backgrounds
################################################################################

image bg d9_closeup_auto = "images/backgrounds/d9_close_automation.png"
image bg d9_closeup_aware = "images/backgrounds/d9_close_fear.png"
    
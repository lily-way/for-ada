################################################################################
## Dialogue Blips
################################################################################

define blip_fadeout = 0.05
define blip_volume = 0.7

init python:

    renpy.music.register_channel(
        "blips",
        mixer="sfx",
        loop=False,
        stop_on_mute=True
    )

    def dialogue_blip(event, interact=True, blip=None, blip_delay=0.05, **kwargs):

        if blip is None:
            return

        if event == "show_done" and interact:

            renpy.music.play(
                [
                    blip,
                    "<silence {}>".format(blip_delay)
                ],
                channel="blips",
                loop=True,
                fadeout=blip_fadeout,
                relative_volume=blip_volume
            )

        elif event in ("slow_done", "interact_done", "end"):

            renpy.music.stop(
                channel="blips",
                fadeout=blip_fadeout
            )

################################################################################
## Character Colors
################################################################################

define cait_color = "#00FFFF"
define martin_color = "#FFFF00"
define ada_color = "#FF2C2C"
define d9_color = "#C4C4C4"
define martins_wife_color = "#C9A7FF"
define temp_1_color = "#63D9FF"
define temp_2_color = "#FF8FA3"


################################################################################
## Characters
################################################################################

define cait = Character(
    "Cait",
    who_color=cait_color,
    show_accent_color=cait_color,
    callback=dialogue_blip,
    cb_blip="audio/characters/cait.wav",
    cb_blip_delay=0.05
)

define ada = Character(
    "Ada",
    who_color=ada_color,
    show_accent_color=ada_color,
    callback=dialogue_blip,
    cb_blip="audio/characters/ada.wav",
    cb_blip_delay=0.04
)

define martin = Character(
    "Martin",
    who_color=martin_color,
    show_accent_color=martin_color,
    callback=dialogue_blip,
    cb_blip="audio/characters/martin.wav",
    cb_blip_delay=0.07
)

define d9 = Character(
    "D9",
    who_color=d9_color,
    show_accent_color=d9_color,
    callback=dialogue_blip,
)

define martins_wife = Character(
    "Martin's Wife",
    who_color=martins_wife_color,
    show_accent_color=martins_wife_color,
    callback=dialogue_blip,
    cb_blip="audio/characters/wife.wav",
    cb_blip_delay=0.04
)

init python:

    def dialogue_blip(event, interact=True, blip=None, **kwargs):

        if not interact or blip is None:
            return

        if event == "show":
            renpy.sound.play(blip, loop=True)

        elif event == "slow_done":
            renpy.sound.stop()

# =============================================================================
# CHARACTERS
# =============================================================================

define cait_color = "#00FFFF"
define martin_color = "#FFFF00"
define ada_color = "#FF2C2C"
define d9_color = "#C4C4C4"
define martins_wife_color = "#C9A7FF"
define temp_1_color = "#63D9FF"
define temp_2_color = "#FF8FA3"

define cait = Character(
    "Cait",
    who_color=cait_color,
    show_accent_color=cait_color,
    callback=dialogue_blip,
    cb_blip="audio/temp_voice_1.wav"
)

define ada = Character(
    "Ada",
    who_color=ada_color,
    show_accent_color=ada_color,
    callback=dialogue_blip,
    cb_blip="audio/temp_voice_1.wav"
)

define martin = Character(
    "Martin",
    who_color=martin_color,
    show_accent_color=martin_color,
    callback=dialogue_blip,
    cb_blip="audio/temp_voice_2.wav"
)

define d9 = Character(
    "D9",
    who_color=d9_color,
    show_accent_color=d9_color,
    callback=dialogue_blip,
    cb_blip="audio/temp_voice_1.wav"
)

define martins_wife = Character(
    "Martin's Wife",
    who_color=martins_wife_color,
    show_accent_color=martins_wife_color,
    callback=dialogue_blip,
    cb_blip="audio/temp_voice_5.wav"
)

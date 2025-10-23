label episode21:

    $ Fnum = 21
    $ save_name = "Episode 21: The Adventures of Toshibo"

    $ bgfx ('sora01')
    $ bgm (2)

    "Hello, everybody."
    "My name is 'Nina-Francoise.'"
    "You can just call me Nina."
    "However, nobody calls me by that name..."
    "Since I have this special opportunity, I'll talk about my strange friends."
    "Please forgive me if it takes longer than expected."


    call ep_start from _call_ep_start_4

    if F015 == 0:
        jump episode21_asumi

    elif F015 == 1:
        jump episode21_tomoe

    elif F015 == 2:
        jump episode21_marumu

label episode21_b:

    call ep_middle from _call_ep_middle_4

    if F015 == 0:
        jump episode21_asumi_b

    elif F015 == 1:
        jump episode21_tomoe_b

    elif F015 == 2:
        jump episode21_marumu_b

label episode21_end:

    $ char ('tts001')

    voice ts0043
    nina "I appreciate this lucky encounter."


    call ep_finish from _call_ep_finish_3

    $ renpy.end_replay()
    $ unlock_episode (21)

    jump episode22
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

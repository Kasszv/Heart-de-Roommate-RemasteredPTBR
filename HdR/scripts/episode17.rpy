label episode17:

    $ Fnum = 17
    $ save_name = "Episode 17: One Fine Weekend"

    if F015 == 0:
        jump episode17_asumi

    elif F015 == 1:
        jump episode17_tomoe

    elif F015 == 2:
        jump episode17_marumu

label episode17_end:


    call ep_finish from _call_ep_finish_9

    $ renpy.end_replay()
    $ unlock_episode (17)

    jump episode18
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

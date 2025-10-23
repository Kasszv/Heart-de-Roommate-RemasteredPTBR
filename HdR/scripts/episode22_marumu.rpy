label episode22_marumu:

    $ bgfx ('bg01c')

    "Marumu doesn't want to leave Toshibo alone."
    "She's really worried about Toshibo. I know they're good buddies."
    "When I stand beside her, she asks me a question,"

    $ char ('tma101')
    $ bgm (9)

    voice ma0525
    marumu "Toshibo, okay?"
    yusuke "She'll be fine. Don't you think so, Marutan?"
    "I say this as if I'm trying to persuade myself."
    "She nods."

    $ char ('tma102')

    voice ma0526
    marumu "Yeah."

    voice ma0527
    marumu "I believe you."
    "I'm really glad to hear she trusts me."
    "Okay, then let's root for Toshibo!"

    call blackout from _call_blackout_93
    $ bgfx ('bg01c')

    jump episode22_b

label episode22_marumu_b:

    $ char ('tma010')
    $ bgm (2)

    voice ma0528
    marumu "Toshibo's clones."
    yusuke "I don't think that is the right term."

    jump episode22_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

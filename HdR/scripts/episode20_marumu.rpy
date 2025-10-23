label episode20_marumu_d:

    $ cg ('em_0102', pos=[ALIGN(0.0, 0.0)])
    $ bgm (14)

    voice ma0520
    marumu "Yusuke."
    yusuke "Yes?"
    "Marumu tells me something unexpected."

    voice ma0521
    marumu "I want to have an arranged marriage meeting."
    yusuke "Why?"

    voice ma0522
    marumu "It sounds fun."
    "How can she say that when she and I are a couple?"
    "Is this her usual joking around? Maybe not."
    "Her eyes are serious."
    "I droop down, and she pats me on the shoulder."
    "She happily tells me,"

    call cg_slide (picture='em_0102', tm=3.0, kind='v', start=0.0, end=1.0, cls=diss_fast) from _call_cg_slide_25

    voice ma0523
    marumu "Because you'll come and ruin the meeting."
    yusuke "Huh..."

    voice ma0524
    marumu "I'll wait for you, Yusuke."
    "I have to ruin the meeting then."
    "I decide to be ready for the X day."

    jump episode20_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

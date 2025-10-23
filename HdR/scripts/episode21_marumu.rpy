label episode21_marumu:

    $ bgfx ('bg12a')
    $ char ('tma001')
    $ bgm (6)

    "Her name is Marumu Ogumayama."
    "I feel completely at ease in her presence."
    "She's one of Tomoe's friends."
    "I don't know how they communicate with each other."
    "She spends more time with me."

    $ bgfx ('black')
    $ music_stop ()
    $ bgfx ('bg01a')
    $ char ('tma101')
    $ bgm (2)

    voice ma0342
    marumu "Yusuke, why don't you go out?"
    yusuke "Huh, why?"

    $ char ('tma108')

    voice ma0343
    marumu "Toshibo and I will stay home today."

    voice ts0043
    nina "Staying home with her...I have a bad feeing about this."
    yusuke "I can do that, but would I bother you if I stayed?"

    $ char ('tma104')

    voice ma0065a
    marumu "......(nod)"

    $ char ()

    "They probably look good to other people."
    "But there're unseen problems..."

    call blackout from _call_blackout_61
    $ vox ('ts0074')

    "I was scared."
    "I had a new experience."
    "However..."

    $ vox (delay=0.3)

    "An unbelievable thing happened."
    "A male is attracted to this weird female."

    jump episode21_b

label episode21_marumu_b:

    $ cg ('es_0107')

    "The male's name is Yusuke Sawada."
    "This mysterious creature dresses like a female sometimes."
    "As their sexual desires rise, they'll probably have intercourse."
    "It'll bring 'Love' to them."
    "And I want to know what that 'Love' is."
    "If I stay here and watch them 'Making Love,' perhaps I'll understand."

    $ bgfx ('black')
    $ cg ('hm_0201')

    voice ma0356
    marumu "I'll do my best."
    yusuke "Do...what?"

    voice ma0357
    marumu "I'll try what I learned today."
    yusuke "H...hey...mmm."

    $ cg ('hm_0301')

    marumu "......"
    nina "??"

    $ bgm (7)

    voice ma0358
    marumu "Kiss..."
    yusuke "Marumu?"

    voice ma0359
    marumu "Snap..."

    $ cg ('hm_0303')

    yusuke "Ugh...uh."
    nina "!!"

    $ bgfx ('black')

    voice ma0360
    marumu "Chomp..."
    yusuke "Ouch! Don't bite it..."
    nina "@%%$#!"

    voice ma0361
    marumu "It's too big to fit in my mouth."
    yusuke "......"

    voice ts0051
    nina "What is this?"

    $ music_stop ()

    "It's impossible to get an answer."
    "Because I have no idea what they're doing."
    "I should find the answer by myself... Oh?"

    $ bgfx ('bg02a')
    $ char ('tku001')
    $ empat ('j6')
    $ bgm (14)

    blackcat "......"
    nina "......"
    "What is this strange feeling?"
    "Will this male be able to grant my wish?"
    "Will he be able to tell me what 'Love' is?"
    "I notice something."
    "This feeling...it's the legendary 'Falling in love at first sight.'"
    "I'm crazy for him."

    jump episode21_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

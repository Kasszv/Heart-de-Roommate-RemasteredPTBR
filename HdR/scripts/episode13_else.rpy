label episode13_else:

    $ music_stop ()

    "In the end, I still don't know what my true feelings are."
    "I can't see my heart."
    "I love, I love someone, I love her..."
    "I can almost see...but I can't."
    "I think that I'm just too inexperienced."
    "However, I can't leave it the way it is."
    "I still have problems with the three of them."
    "I have to make a decision."
    "I change into my girl's uniform and leave the school."
    "If I'm going to Ms. Yagami's place, I don't have to change."
    "But I'm going where I must dress like a girl."

    $ bgfx ('bg01a')
    $ char ('tas044')
    $ bgm (8)

    asumi "......"
    "Asumi quietly looks at me."
    "The others too."
    "I feel a lot of pressure."
    "I want to run away now, but I fight the urge and tell them,"
    yusuke "I have something to tell you girls."

    $ char ('tas006')

    voice as1302
    asumi "What is it? Tell us!"

    $ char ('tto002')

    tomoe "......"
    "I notice that Tomoe's eyes are shaking."
    "Then Marumu mutters before I say anything,"

    $ char ('tma007')

    voice ma0502
    marumu "Are you announcing our engagement?"

    $ music_stop ()

    everyone "!!!"
    "An uncomfortable atmosphere spreads in the room."
    "All of us are surprised and are at a loss for words except Marumu."
    "But I am more surprised than anyone."

    $ bgm (7)
    $ bgfx ('sora01')

    "It takes time to recover from Marumu's words."
    "Asumi and Tomoe won't believe whatever I have to say."
    "And Marumu, she seems to be having fun waving a flag."
    "It takes an hour for all of us to calm down."
    "Finally, I tell them,"

    $ music_stop ()
    $ bgm (13)
    $ bgfx ('bg01a')
    $ char ('tas044')

    yusuke "I've been thinking, but I can't find an answer."
    yusuke "I like all of you, but I don't know what the 'like' means."
    yusuke "I don't think I'm mature enough to love someone."
    everyone "......"
    "Asumi and the other two quietly listen to me."
    "I especially appreciate Marumu's keeping silent."
    "I feel everyone's eyes are more piercing than before I began."
    "But I can't take it back."
    yusuke "I'm sorry, but I..."
    yusuke "I want to know more about all of you, so I'd like to continue this relationship with all of you, and..."
    "I don't know what to say."
    "I thought I could tell them better, but I can't."
    "I look up at the ceiling, searching for something to say."
    "Then someone helps me. Believe it or not, that person is Asumi."

    $ music_stop ()
    $ char ('tas001')

    voice as1303
    asumi "Stupid Yusuke! What are you thinking about all by yourself?"
    yusuke "Huh?"
    "Her serious look has totally disappeared."
    "She smiles at me."

    $ bgm (10)
    $ char ('tas044')

    voice as1304
    asumi "Everybody is the same. Sometimes, I don't know what my true feelings are either."

    $ char ('tto001')

    voice to0962
    tomoe "Yes, I agree. Me too. But for now, I like things the way they are."
    yusuke "Asumi, Tomoe."
    "The last few days, there were ill feelings between us."
    "But their words have taken that away."

    $ char ('tas012')

    voice as1305
    asumi "Well, youth is not that easy! Let's learn more!"

    $ char ('tto025')

    voice to0963
    tomoe "Perhaps we're all still immature."
    marumu "......"
    "I'm comfortable now."
    "I think life has returned to normal."
    "It might not be good."
    "I may have to step ahead, even though it will hurt somebody."
    "But I'm comfortable now."
    "Why don't I take some time to think about it. Honestly, that's what I think."

    $ char ('tas001')

    voice as1306
    asumi "But Yusuke,"
    yusuke "Yes?"

    voice as1307
    asumi "I'm really curious about why you brought this up so suddenly."

    $ char ('tto001')

    voice to0964
    tomoe "Me too."
    yusuke "It's...ah..."

    $ char ('tma008')

    voice ma0503
    marumu "Yusuke kissed me!"

    $ music_stop ()

    "Everybody freezes again."
    "Asumi, Tomoe, and me."
    "Only Marumu innocently smiles."

    $ bgm (7)
    $ chars ('tas006', 'tto022')

    voice as1308
    asumi_tomoe "Ehhh!? Did you kiss Marumu too?"
    "They look at each other."

    $ chars ('tas037', 'tto002')

    "And their four eyes look at me."
    yusuke "......(sweat)"

    call blackout from _call_blackout_52

    "After that..."

    $ sfx ('SE10', loop=True)

    "I have a horrible experience."
    "Not only Asumi, but Tomoe does it too...sob."
    "But I was able to return..."
    "...Here, to this room."

    $ sfx (delay=0.5)

    "I can spend more of my youth with them here. I'm satisfied."

    $ sfx ('SE51')
    $ bgfx ('bg04a')
    $ char ('tyo002')
    $ bgm (4)

    voice yo0375
    yagami "OK! The first semester's over! Enjoy your summer vacation!"
    "With Ms. Yagami's words, the first semester ends."

    $ sfx (delay=0.5)

    "Summer vacation will start tomorrow."
    "After the vacation, the second semester will begin. What's in store for me?"
    "What's ahead of me?"
    "It'll start after the long summer vacation."
    "It's time to go home for now."
    "My home. I kind of miss my damn parents."

    $ bgfx ('bg02a')
    $ char ('tas002')

    voice as1309
    asumi "See you next semester!"

    call blackout from _call_blackout_53
    if F019 >= 5:
        $ unlock_episode (27)
    if F01A >= 5:
        $ unlock_episode (28)
    jump game_over
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

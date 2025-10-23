label episode19_marumu:

    $ bgfx ('bg12b')

    "On the way back to the dorm,"
    "Someone pats me on the shoulder."

    $ bgm (2)
    $ char ('tma004')

    yusuke "Oh, it's you, Marutan."

    voice ma0372
    marumu "Yusuke...you're done."
    yusuke "Done...what?"

    voice ma0373
    marumu "As my boyfriend. You're fired."
    "Is she kidding me?"
    "But she looks serious."
    "Her eyes are telling me it's the truth."
    "I'm shocked!"
    yusuke "W...why? Did I do something wrong? Are you seeing someone else?"

    $ char ('tma019')

    voice ma0374
    marumu "Misaki..."

    $ empat ('SE49')

    "Her shocking news makes me cry."

    $ empat ()
    $ bgm (9)

    yusuke "Oh no..."

    $ char ('tma017')

    voice ma0375
    marumu "Just kidding..."
    yusuke "...Okay."

    $ music_stop ()

    "Marumu's really strange."
    "I deeply sigh."

    $ bgm (2)
    $ char ('tma001')

    yusuke "Marutan, do people call you strange?"

    voice ma0376
    marumu "I'm an ordinary girl."
    yusuke "What part of you...?"

    $ char ('tma002')

    voice ma0377
    marumu "Everything about me is normal."
    yusuke "...Okay."
    "Asumi, Tomoe, and Marumu."
    "They're completely different."
    "Marumu is super unique among them."
    "Her personality doesn't have many common characteristics with other people."
    "How come they get along with each other?"
    "My curiosity is triggered."
    yusuke "By the way, were all three of you girls good friends from the beginning?"

    $ char ('tma001')

    voice ma0378
    marumu "Three...?"
    yusuke "Asumin, Moe-Moe, and you, Marutan."
    marumu "......"
    yusuke "Marutan?"

    $ bgm (10)
    $ bgfx ('sora05')

    "She suddenly looks up at the sky."
    "Then she murmurs,"

    voice ma0380
    marumu "That was a long trip..."
    yusuke "Huh...?"
    "She starts telling me how they met and became friends."


    call ep_middle from _call_ep_middle_15

    $ cg ('raf_01')
    $ unlock_gallery ('g6e4')

    $ bgm (16)

    voice as1113
    asumi "I'm Asumi Hirota. I'm becoming the leader of this room! The Asumin administration has begun. Ha ha ha."

    $ cg ('raf_02')

    voice to0860
    tomoe "I...I'm Tomoe..."

    voice ma0381
    marumu "I'm Marutan!"

    $ bgfx ('black')

    "The oppressive days began."

    $ cg ('raf_03')

    voice as1114
    asumi "Work hard, Moe-Moe! You'll work for me until you die!"

    voice to0861
    tomoe "Awww...hic... I'll spend the rest of my life crying..."
    marumu "......"
    "I couldn't stand watching it any longer. I wanted to help her."
    "Someone had to stand up."

    $ bgfx ('black')

    "I talked to a wise woman (Ms. Yagami),"

    $ cg ('raf_04')
    $ bgm (4)

    voice yo0221
    yagami "I see...but the only one who can save her is you! You need to fight in the cause of justice!"
    marumu "......(nod)"
    "The destiny of the room was in my hands."

    call blackout from _call_blackout_91

    "Though I might lose the fight, someone had to start the revolution."
    "I decided to fight against the power."

    $ cg ('raf_05')
    $ bgm (16)

    voice as1115
    asumi "Are you against me? You forget your place. Fine, bring it on!"

    voice ma0382
    marumu "I'll never give up!"

    voice to0862
    tomoe "Oh, Marutan...our last hope."

    $ cg ('raf_06')

    "The heroic battle lasted for three days and three nights."
    "The room was messed up, and the citizen was in sorrow."

    $ bgfx ('white', diss_long)
    $ bgfx ('black', diss_long)
    $ music_stop ()

    "However,"
    "The sun rose again!"
    "The night didn't last forever!"
    "I finished the fight under the flag of justice."
    "With a bright victory."

    $ cg ('raf_01')
    $ bgm (10)

    voice as1116
    asumi "You win, Marutan! I'll care about you and foster our friendship."

    voice to0863
    tomoe "I'll make efforts to spend days with hope."

    voice ma0383
    marumu "Have a nice day."

    voice as1117
    asumi "Oh wait."
    "The ex-tyrant and the citizen prevented me from leaving."

    $ cg ('raf_07')

    voice as1118
    asumi "We can live together happily! This is proof of our friendship!"

    voice to0864
    tomoe "Thank you, Asumin...what a leader."
    "The ex-tyrant gave us treasures."
    "I became even stronger with the new power, 'a big stag beetle hairstyle.'"

    $ cg ('raf_08')

    voice ma0384
    marumu "Marumu...the brain."

    voice as1119
    asumi "I know. It's all thanks to you. Hurrah, the brain Marutan!"

    voice to0865
    tomoe "Hurray...uhh...I'm chocked with tears of joy."

    voice ma0385
    marumu "What a good ending..."

    call blackout from _call_blackout_92
    $ bgm (6)
    $ bgfx ('bg02b')
    $ char ('tma001')

    marumu "......"
    yusuke "......"

    voice ma0386
    marumu "Did you get it, Yusuke?"
    yusuke "Ah...yes and no..."

    $ bg ('bg02b')
    $ char ('tma017')

    voice ma0387
    marumu "The legend of the brain, Marumu."
    yusuke "Okay, okay."
    "I don't need to deal with her seriously."
    "What part of her story can I believe?"
    "I have to ask the other girls to find out the truth."

    $ bgm (3)
    $ bgfx ('sora05')

    "I understand they had a hard time in the beginning."
    "They got over various difficulties together and fostered their friendship."
    "I clearly understand it from her story."
    "Friendship is a precious thing after all."

    jump episode19_b
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

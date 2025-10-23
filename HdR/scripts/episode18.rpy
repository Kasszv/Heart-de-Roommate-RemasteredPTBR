label episode18:

    $ Fnum = 18
    $ save_name = "Episode 18: The Day the Earth Falls"

    call blackout from _call_blackout_135

    narration "It comes out of the blue."

    $ cg ('raf_09')
    $ unlock_gallery ('g6e2')

    voice as1310
    asumi "Everybody, listen! It's horrible!"

    $ cg ('raf_10')

    voice to0966
    tomoe "What happened, Asumin?"

    voice ma0504
    marumu "What's wrong?"

    $ cg ('raf_09')

    voice as1311
    asumi "D...do you know what tomorrow is?"

    $ cg ('raf_10')

    voice to1001
    tomoe "Tomorrow is... Oh, the special sale at Kakuetsu market!"

    voice ma0539
    marumu "It's trash day..."

    $ cg ('raf_09')

    voice as1312
    asumi "It's not such an optimistic day. Tomorrow is Judgment Day!!"

    $ cg ('raf_11')
    $ empat ('SE49')

    voice to0967
    tomoe_marumu "...Oh my goodness!!"
    marumu "..Wow!!"

    $ empat ()


    call ep_start from _call_ep_start_21

    narration "The great leader Asumi explains to her roommates."

    $ cg ('raf_12', diss_long)

    narration "A big, huge, tremendously big meteor."
    narration "It's coming toward our beautiful, blue planet Earth."

    $ bgm (9)
    $ cg ('raf_09')

    voice as1313
    asumi "Even the UN, UNICEF, and the Defense Agency of Earth have given up!"

    $ cg ('raf_11')

    voice to0968
    tomoe "I don't think UNICEF can do anything about this situation."

    voice ma0506
    marumu "Is this the end of Earth?"

    voice to0969
    tomoe "That's right! The Earth will be gone...oh no! I want to buy more pretty dresses, eat good food, and find a nice boyfriend..."

    $ cg ('raf_09')

    voice as1314
    asumi "Don't cry, Moe-Moe! Don't give up! If you keep up your hopes..."

    $ cg ('raf_11')

    voice ma0507
    marumu "Then what?"

    voice as1315
    asumi "Well, uh..."

    $ music_stop ()

    voice ts0088
    unknown "Don't give up, meow!!"

    voice as1316
    asumi "Who's that!?"

    voice to0970
    tomoe "Is that you, Toshibo?"

    $ bgm (5)
    $ cg ('raf_13')
    $ empat ('j4')

    voice ts0089
    toshibo "This is a test of the universe! A rigorous destiny for humanity."

    voice as1317
    asumi "Toshibo...who are you!?"

    $ empat ()
    $ cg ('raf_14')

    voice ts0090
    toshibo "That's not important. Let's think how to save the Earth together!"

    voice as1318
    asumi "Yeah...he's right! Let's think!"

    $ bgfx ('black')

    narration "An hour later..."

    $ cg ('raf_12')
    $ bgm (9)

    voice to0971
    tomoe "We can't make it! We're all going to die in two hours!"

    voice ma0508
    marumu "Vanish..."

    voice as1319
    asumi "Why are you giving up? We still have two more hours! We can do it..."

    voice to0972
    tomoe "I don't think so! Whatever we do, it's useless... Whaaa!"

    voice as1320
    asumi "Fine! I'll save the Earth alone! I'll never ever give up."

    $ cg ('raf_10')

    toshibo "......"

    voice to0973
    tomoe "Wait, Asumin! I was wrong. Looking at you, I think there is something we still can do."

    voice ma0509
    marumu "Save the Earth..."

    $ cg ('raf_15')

    voice as1321
    asumi "Yes! I can't make it alone, but if we work together, we can make a miracle happen!"

    voice to0974
    tomoe "That's right, Asumin! We can do it!"

    voice ma0510
    marumu "Oh yeah."

    $ bgfx ('black')
    $ music_stop ()

    voice ts0091
    toshibo "You girls are great. I entrust you with Earth's future! If you get together and use your powers, a miracle might happen..."
    narration "These three girls decide to save the planet with their frantic efforts."
    narration "However, the huge meteor is heading closer and closer to Earth."
    narration "And they don't have much time left until the collision."

    $ cg ('raf_12')
    $ bgm (8)

    voice as1322
    asumi "We need to use this as our last resort!"

    voice to0975
    tomoe "Last...resort?"

    voice as1323
    asumi "We'll be a pillar between Earth and the meteor to prevent the collision!"

    voice to0976
    tomoe "I understand, Asumin."
    marumu "......(nod)"
    narration "The two girls know the strategy is helpless."
    narration "However, they believe in their friendship and Asumin and fight together for Mother Earth."

    $ music_stop ()
    $ cg ('raf_16')

    voice as1324
    asumi "Are you ready!? Give me your power... Whaaa!"

    voice to0977
    tomoe "Ahh, my hands are burning...but..."

    voice ma0511
    marumu "I...I won't give up!"

    $ empat ('j6')
    $ bgfx ('white', diss_long)
    $ bgfx ('black', diss_long)

    narration "Just before the girls fall down, the meteor explodes. A miracle has happened!"
    narration "The power of the miracle is,"

    $ empat ()
    $ cg ('raf_17')
    $ bgm (10)

    voice ts0092
    toshibo "Friendship. Your friendship produced a miracle and saved the Earth! Meow!"

    voice to0978
    tomoe "Wonderful...friendship is such a wonderful thing, Asumin!"

    voice ma0512
    marumu "Hurrah for friendship!"

    voice as1325
    asumi "I couldn't have made it without you girls...Moe-Moe and Marutan! Viva friendship! Superb!"

    $ music_stop ()
    $ say_hide ()
    $ voice_stop (0.2)
    $ empat ('j4')
    $ cg ('raf_18')
    $ wait (3.0)
    $ bgfx ('black')
    $ wait (2.0)
    $ empat ()
    $ bgm (6)
    $ bgfx ('bg02a')
    $ char ('tma007')

    "Marumu holds out the lollipop (she's been licking it) to the girl in front of her."

    voice ma0513
    marumu "This is for you."

    $ char ('thi001')

    voice hi0100
    hikaru "No thanks..."
    "The candy must have been handed out before the picture-story show."
    "But the show is over."
    "What kind of picture-story artist gives her half-eaten candy to the audience?"
    "The weird Marumu steps aside, and Asumi the leader steps forward."

    $ char ('tas005')

    voice as1326
    asumi "What do you think, Hikaru? Even a girl with a cold heart like you is moved, right?"

    $ char ('thi001')

    hikaru "......"

    $ char ('tas015')

    voice as1327
    asumi "Friendship is brilliant! Let's become friends and foster our friendship together!"

    $ char ('thi001')

    voice hi0101
    hikaru "Bye..."

    $ char ()
    $ music_stop ()

    "Asumi's 'Make the cold fish Hikaru be moved' plan took three whole days."
    "In spite of her efforts, the plan failed. But I knew it was going to be unsuccessful."
    "I'm at a loss with disgust."
    "However, Tomoe is crying next to me."

    $ bgm (10)
    $ char ('tto050')

    voice to0979
    tomoe "Asumin...I didn't know how magnificent friendship is... Sorry, I'm sorry."

    voice to0980
    tomoe "Oh, forever friendship! Whaa..."

    $ char ('tma008')

    voice ma0514
    marumu "Moe-Moe is touched! Mission accomplished."

    $ char ('tas010')
    $ music_stop ()
    $ empat ('j7')

    voice as1328
    asumi "Noooo! It didn't work on Hikaru...but I won't give up! Ever!"
    yusuke "I think you'll fail again if you continue the same way."

    $ empat ()


    call ep_finish from _call_ep_finish_17

    $ renpy.end_replay()
    $ unlock_episode (18)

    jump episode19
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

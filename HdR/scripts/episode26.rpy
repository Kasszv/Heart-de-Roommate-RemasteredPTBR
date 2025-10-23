label episode26:

    $ Fnum = 26
    $ save_name = "Episode 26: Roommates Forever"

    if F015 == 0:
        jump episode26_asumi

    $ bgfx ('white', diss_long)
    $ bgm (9)
    $ bg ('sora04', tag=0)
    $ bg ('sora02', tag=1, pos=[HIDE(3.5, 0.5)])
    $ _fx (diss_long)
    $ wait (2.0)

    yusuke "It feels like everything is moving so slow here."
    "Until two hours ago, I was so busy."
    "But now I'm not."
    "Little by little, the memories of my high school days come back to me."
    "Time quietly passes on."
    "Time with her quietly passes on."
    "The time with my best friends in the whole world has become a part of my past."
    "But I know nothing has changed here."
    "There's air."
    "And our wonderful memories."
    "It's almost time for our reunion."
    "Without realizing it, I start recalling my faded memories."


    call ep_start from _call_ep_start_31

    yusuke "...A year has passed from that day."
    "Today, I'm going to reunite with my beloved friends."
    "We all promised to meet here again a year later."
    "And today is the day of our reunion."
    "I arrive a bit earlier than I expected, so I started looking around at the unchanged surroundings."

    if F015 == 1:
        jump episode26_tomoe
    else:

        jump episode26_marumu

label episode26_b:

    call blackout from _call_blackout_198
    $ bgm (12)

    "It's such a pleasant time."
    "We keep talking, waiting for the one last person to join us."
    "Asumi hasn't showed up, even though the appointed time has come and gone."

    $ bgfx ('bg03a')
    $ char ('tto604')

    voice to0801
    tomoe "Where's Asumi?"

    $ char ('tma501')

    voice ma0250
    marumu "Asumin is late!"
    yusuke "I guess she couldn't come, after all."

    $ char ('tto601')

    voice to0802
    tomoe "What do you mean, 'after all?'"

    $ bgfx ('sora04')

    "I close my eyes for a moment."
    "Then I start explaining what happened to her after graduation."
    "When she told me she was going to Greenland, I was at a loss for words."
    "But at the same time, I felt it was so like her, moving along with her decision."
    "I've heard she's busy and studying hard over there."
    "That's why she sent me a letter saying that she might not be able to attend our first reunion."
    "After Tomoe and Marumu hear everything, they space out for a while."
    "They probably never expected Asumi would study abroad."
    "After a long silence, someone starts giggling."
    "Because we all agree it's not like her to go to Greenland to study."

    call blackout from _call_blackout_199

    "We aimlessly start walking around."
    "Of course, we wanted everyone to hang out together."

    $ bgm (10)

    "We dawdle around our second hometown and talk about our high school days."
    "As we chat, the memories come back to us."

    $ cg ('e3_0301', pos=[ALIGN(0.0, 0.0)])

    "Happy memories."

    $ cg ('es_0107')

    "Bitter memories."

    $ cg ('e3_05')

    "Sad memories."

    $ cg ('e3_0101')

    "And treasured memories."

    if F015 == 1:
        jump episode26_tomoe_b
    else:

        jump episode26_marumu_b

label episode26_c:

    "After eating, we have some tea and relax for a while. Then, I remember something very important."

    $ music_stop ()

    yusuke "Oh, shoot!"

    $ char ('tma501')

    voice ma0251
    marumu "What, Yusuke?"
    yusuke "I totally forgot. Let's see. Ah...where is it?"
    "I dig out a large envelope from my bag."
    "It's from Asumi."
    "She enclosed a letter and..."
    "I take out a videotape from the envelope."
    yusuke "Asumi sent me this. She told me to watch it with everybody if she couldn't make it."

    $ char ('tto601')

    voice to0803
    tomoe "What's on the tape?"
    yusuke "Actually, I haven't watched it yet because she told me to watch it with you."
    yusuke "But where can we go to watch it?"

    $ char ('tma501')

    voice ma0252
    marumu "I want to watch the video from Asumin!"
    yusuke "Okay, then how about I make copies and send them to you?"

    voice ma0253
    marumu "Let's watch it together!"
    "Marumu doesn't seem ready to give up."
    "Well, it's true Asumi wanted us to watch it together."
    yusuke "Okay, but..."

    $ char ('tto601')

    voice to0804
    tomoe "I'd like to watch it too."
    "Tomoe modestly whispers."
    "I'd love to manage it, but how?"
    yusuke "Alright, then how about we..."
    "All of sudden, a bright idea pops into my mind."
    "I make a phone call with my fingers crossed."

    $ bgfx ('black')

    "I talked to Ms. Yagami over the phone. I don't know why, but she's been working during spring break."
    "It seems I called her at just the right moment."
    "We head toward the school."
    "To our beloved Aiho School."

    $ bgfx ('bg04a')
    $ char ('tyo007')
    $ bgm (4)

    voice yo0213
    yagami "Hello, guys. How have you been?"
    yusuke "Fine, I guess."

    $ char ('tma504')

    voice ma0247
    marumu "A super girl, never sick!"
    "Ms. Yagami looks so happy to hear Marumu's humor again."
    "And..."

    $ char ('tto619')

    voice to0805
    tomoe "It's very nice to see you, Ms. Yagami."

    voice yo0214
    yagami "Tomoe, you look so grown up."

    voice to0806
    tomoe "Yes, ma'am."
    "The slightly more mature Tomoe smiles at her."
    "Then she looks at me."

    $ char ('tyo002')

    voice yo0215
    yagami "Congratulations, Yusuke! You're officially a college student now. To tell you the truth, I was really worried about you, you know."
    yusuke "Really?"
    "Even after graduation, she was concerned about me."
    "Then she realizes somebody is missing."

    $ music_stop ()
    $ char ('tyo001')

    voice yo0216
    yagami "By the way, where is Asumi?"
    yusuke "Ah, you know..."
    "Then I tell her the story."
    "For a few seconds, she looks gloomy. Am I just imagining things?"

    $ bgfx ('black')
    $ bgfx ('bg05a')
    $ char ('tyo001')

    yusuke "By the way, do you remember what I asked you over the phone?"

    $ char ('tyo019')

    voice yo0217
    yagami "Oh, yes. Well, are you sure you guys want to watch the video at my house? If you like, I have another place in my mind."
    yusuke "Where?"

    $ bgfx ('black')

    "The situation takes an unexpected turn."
    "The place she takes us is..."

    $ bgfx ('bg17')
    $ bgm (9)

    "We all know the place very well."
    "Ms. Yagami borrowed the key and took us to our old dormitory."

    $ say_hide ()
    $ bgfx ('bg15a', Dissolve (3.0))

    "Because of the new residents, it looks a bit different than before."
    "But still, I feel nostalgic."
    "I even feel the memories of the scenes gradually come back to me."

    $ music_stop ()
    $ char ('tyo002')

    voice yo0218
    yagami "Since it's spring break, I got permission to use the room."
    yusuke "Thank you so much, Ms. Yagami!"
    "I really appreciate what she's doing for us."

    $ char ('tyo019')

    voice yo0219
    yagami "You're very welcome. Anyway, if I tell the current residents that Yusuke was here, they'll probably be shocked. You're a legend at Harukaze Dorm, you know."
    yusuke "What?"

    $ char ('tyo002')

    voice yo0220
    yagami "You lived here for a year, though it's for girls only. You're quite the legend."

    $ char ('tto619')

    voice to0807
    tomoe "Yusuke, you really amaze me, you know."

    $ char ('tma504')

    voice ma0254
    marumu "Yusuke, the legend!"
    yusuke "...Oh no."
    "I don't think I can be very proud of such a legend."

    $ bgfx ('black')

    "Ms. Yagami tells us to return the key after our meeting is over. "
    "After she leaves, we put the video in the VCR."
    "Then I press the play button."

    $ cg ('ea_0826', diss_long, cls=True)
    $ sfx ('SE11', loop=True)
    $ cg ('ea_0827', diss_long)

    "After a minute, Asumi appears on the screen."
    "It doesn't look like she's changed much, and she's wearing our old school uniform."

    $ sfx (delay=0.5)
    $ cg ('ea_0824')
    $ set_vol (TAPE)

    "Then she starts talking, as if we were in front of her."

    voice as1036
    asumi "Dad, can I start?"

    voice as1037
    asumi "Hello, everybody! Do you remember Asumin, the leader of the funky group?"

    $ vox ('to0988')

    voice as1038
    asumi "How are you, Moe-Moe and Marutan? Oh, and you too, Yusuke."

    $ vox ('ma0517')
    $ cg ('ea_0823')

    voice as1039
    asumi "You guys are watching this, and that means I couldn't go to see you. I'm so sorry."

    $ cg ('ea_0822')
    $ vox (delay=0.3)

    voice as1040
    asumi "I know you wanted to see me. I'm such a bad, bad chick, huh!?"

    $ vox ('to0989')
    $ cg ('ea_0821')

    voice as1041
    asumi "I want to see you guys too. Well, if I could fly, I'd be there right now."

    $ cg ('ea_0820')
    $ vox (delay=0.3)

    voice as1042
    asumi "Anyway, I just want to tell you thanks a lot for hanging around with me, even though I was a little selfish at times."

    $ cg ('ea_0819')

    voice as1043
    asumi "I appreciate what you guys did for me, I really do. If I hadn't met you, I probably couldn't have had such a wonderful three years! Well, with Yusuke, it was a year."

    $ cg ('ea_0818')

    voice as1044
    asumi "Anyway, I had so much fun with you guys. The time with you became my treasure, and nothing can beat it."

    voice as1045
    asumi "I don't think I could feel such a sense of fulfillment without you."

    if F015 == 1:
        jump episode26_tomoe_c
    else:

        jump episode26_marumu_c

label episode26_d:

    $ cg ('ea_0816')

    voice as1063
    asumi "And lastly, please say hi to Hikaru, Toshibo, and the Trio de bitches. Oh, and Namiki and Yoshiko too. Okay, guys?"

    $ cg ('ea_0809')

    voice as1064
    asumi "Well, adios!"

    $ cg ('ea_0801')
    $ unlock_gallery ('g2e1')
    $ cg ('ea_0808')

    voice as1065
    asumi "Huh? Are you still recording?"

    $ cg ('ea_0825')
    $ vox ('to0992')
    $ wait (0.3)
    $ cg ('ea_0811')

    voice as1066
    asumi "Okay, then I'd like to give you a speech."

    $ cg ('ea_0807')
    $ vox (delay=0.3)

    voice as1067
    asumi "I will never forget you guys...your voices, your faces, nor the days we spent together."

    voice as1068
    asumi "We did so many things together, like staying up all night studying for exams, cooking and eating Okonomiyaki, and taking baths in the hot spring at Tomoe's house."

    voice as1069
    asumi "We really did so many silly and reckless things. Now, these have become the most precious memories of my life."

    voice as1070
    asumi "I won't forget any of them, so please keep remembering them too, okay?"

    voice as1071
    asumi "And bear the passion in mind!"

    $ cg ('ea_0818')

    voice as1072
    asumi "Also, please remember me."

    $ vox ('ma0532')
    $ cg ('ea_0807')

    voice as1073
    asumi "Although I'm miles away from you guys, I'll always be your friend!"

    $ cg ('ea_0825')
    $ vox (delay=0.3)

    asumi "......"

    if F015 == 1:
        jump episode26_tomoe_e
    else:

        jump episode26_marumu_e

label episode26_end:

    call blackout (True) from _call_blackout_200
    $ unlock_episode (26)

    jump credits
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

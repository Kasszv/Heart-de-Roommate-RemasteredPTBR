label episode15:

    $ Fnum = 15
    $ save_name = "Episode 15: A New Semester: Transfer Student"

    $ bgfx ('bg13a')
    $ char ('tyu001')
    $ bgm (4)

    voice yu0045
    akane "Everybody, we'll start with a special presentation to celebrate our new series!"

    $ char ('tfu001')

    voice fu0022
    midori "The title is: 'Naze Nani Hato Roo.'"

    $ bgfx ('bg20b')
    $ char ('ths001')

    voice hs0023
    kaoru "What's 'Hato Roo?'"

    $ char ('tyu001')

    voice yu0046
    akane "This special presentation is a Q&A about 'Heart de Roommate.'"

    $ char ('ths003')

    voice hs0024
    kaoru "You don't have to completely ignore me...hic..."

    $ char ('tyu001')
    $ bgm (5)

    voice yu0047
    akane "Let's go to the first question: Why does Namiki make Yusuke call her 'Sis,' even though they're the same age?"

    $ char ('ths001')

    voice hs0025
    kaoru "If you play Namiki's extra scenario, you'll understand the reason."

    $ char ('tyu001')

    voice yu0048
    akane "Yeah...I guess so. Okay, let's go to the next question."

    $ char ('ths001')

    voice hs0026
    kaoru "Who cares about such things...?"

    $ char ('tyu001')

    voice yu0049
    akane "If you keep acting like a bitch, you'll only get small parts...in fact, your parts are already small."

    $ char ('ths003')

    voice hs0027
    kaoru "Oh no...ahhh, that bothers me! What kind of past does she have?"

    $ char ('tfu001')

    voice fu0023
    midori "If you play Namiki's extra, you'll find out about her past."

    $ char ('tyu003')

    voice yu0050
    akane "You're throwing a damper on the festivities again... Okay, next!"

    $ char ('tfu001')
    $ bgm (6)

    voice fu0024
    midori "The next question is: Is Toshibo really a cat?"

    $ char ('ths001')

    voice hs0028
    kaoru "He's a cat I guess."

    $ char ('tyu001')

    voice yu0051
    akane "Yet, he's not an ordinary cat...he's really weird."

    $ char ('tfu001')

    voice fu0025
    midori "This question will be cleared up later."

    $ char ('ths001')

    voice hs0029
    kaoru "He's just a cat..."

    $ char ('tyu001')
    $ bgm (2)

    voice yu0052
    akane "The last question is: Is Marutan, the mysterious beautiful girl, smart or not?"

    $ char ('ths001')

    voice hs0030
    kaoru "I don't agree with the 'beautiful girl' part. Her face isn't outstanding at all! I can do a better job than she can!"

    $ char ('tfu001')

    voice fu0026
    midori "We won't talk about her face now. Does someone know her IQ?"

    $ char ('tma016')

    voice ma0533
    marumu "36 bugs..."

    $ char ('tfu001')

    voice fu0027
    midori "36...bugs?"

    $ char ('tma017')

    voice ma0534
    marumu "1 bug equals 1 stag beetle brain."

    $ char ('tyu002')

    voice yu0053
    akane "Hmm, is that so? What are you doing here?"

    $ char ('tma401')

    voice ma0535
    marumu "Let's start the second half."

    call blackout (True) from _call_blackout_43
    call breakskip from _call_breakskip_3
    $ quick_menu = False
    $ _skipping = False
    $ movie ('hr_op2')


    call ep_start from _call_ep_start_8

    $ quick_menu = True
    $ _skipping = True

    if F015 == 0:
        jump episode15_asumi

    elif F015 == 1:
        jump episode15_tomoe

    elif F015 == 2:
        jump episode15_marumu

label episode15_b:

    voice yu0017
    unknown "What is this pervert doing here?"
    yusuke "Who called me a pervert... Oh!"

    $ bgm (16)
    $ char ('tik999')

    "Our neighbors are standing behind me."
    "We call them the 'Trio de Bitches.'"
    "Before I ask them why they're already wearing their school uniforms, they give me dirty looks and attitudes."

    voice yu0018
    akane "What is he smiling about? Creepy thin man! Does he have any idea where he's standing?"

    voice hs0018
    kaoru "I'll bet he knows; that's why he's smirking. This is the Aiho School dorm, where all the beautiful young girls live."

    voice fu0017
    midori "This isn't a place for a nerd like you! Don't get within 150 feet of this place!"

    voice hs0019
    kaoru "Yeah! You can't walk in front of the building! Detour! If we see you here again, we'll call the police! You got it?"

    voice yu0019
    akane "Only girls and good looking guys like Misaki are allowed on this street."
    yusuke "Ah...do you like Misaki?"

    $ char ('tyu004')

    voice yu0020
    akane "What...? Uh...well, I just mentioned him as an example. That's it!"

    $ char ('tfu001')

    voice fu0018
    midori "Based on my input, Misaki is your type. Why don't you admit it?"

    $ char ('tyu004')

    voice yu0021
    akane "I told you... Whatever!"
    yusuke "I feel left out..."

    $ music_stop ()

    "I quietly walk away feeling abused."

    $ bgfx ('black')
    $ bgfx ('bg12a')

    yusuke "Damn it! I don't think I deserve that. When I'm wearing my girl's uniform, they say, 'You're cute' or 'We're friends.'"
    yusuke "Should I have been born a girl...? Am I not attractive as a male? Ohh!!"
    "I realize an important fact."
    "I am a 'MAN.'"
    "I almost enter the building with guys' clothes on."
    "Guys are prohibited from entering the Harukaze Dorm."

    $ bgfx ('black')
    $ bgm (3)
    $ bgfx ('bg01a')

    yusuke "I'm home!"

    $ char ('tto222')

    voice to0244
    tomoe "Wow, Yusuke! Long time no see. Hey, look at you!"

    $ char ('tto213')

    "Tomoe suddenly walks toward me and fixes my scarf and ribbon."

    $ char ('tto220')

    voice to0245
    tomoe "Okay...umm. You look cute."
    yusuke "Well, I wanted to change my clothes."

    $ char ('tto222')

    voice to0246
    tomoe "Oops...sorry."
    "I'm happy to see Tomoe again."

    $ bgfx ('black')
    $ bgfx ('bg01c')
    $ char ('tto201')

    yusuke "By the way, where's Marutan and Asumi?"
    "This is the first time for just the two of us to have dinner."
    "It's late, but I don't know where they are."

    $ char ('tto219')

    voice to0247
    tomoe "Yeah, they're late. I made a lot, so please eat it all, Yusuke."
    yusuke "Y...yeah."
    "Her innocent smile arouses me."
    "We look like we're living together."
    "If she seduces me now, I'll lose control."

    $ music_stop ()
    $ char ('tto222')

    voice to0248
    tomoe "Whaaaaa!!"
    yusuke "Wha...what!?"

    if F015 == 2:
        jump episode15_marumu_b
    else:

        jump episode15_asumi_b

label episode15_c:

    $ bgfx ('bg04a')
    $ char ('tyo001')
    $ bgm (4)

    voice yo0149
    yagami "Okay, everybody. Let's start our homeroom. But before we do..."
    "She waves her hand at the door and cheerfully tells us,"

    $ char ('tyo007')

    voice yo0150
    yagami "We have a new friend! Come on in, Ms. Saeki."

    $ char ('thi001')

    girl "......"
    "Everyone is momentarily captivated with the new girl."
    "She has a unique atmosphere that nobody in this class or even in the school has."
    "The reason why most guys look at her is because she's drop-dead gorgeous."
    "Tomoe talks to Asumi after the initial shock wears off."

    voice to0253
    tomoe "Another one? This school has a lot of transfer students."

    voice as0517
    asumi "Yes, it seems this school's becoming a correctional institution for problem students."
    yusuke "......"
    "Hmm? Something bothers me about what she said..."

    voice as0518
    asumi "Hmm...Yusuke, Namiki... I can see they're problem students. Then that girl must also be...?"
    yusuke "Namiki is, but which part of me is a problem!?"
    "I tell her back."
    "I think I'm a quiet, serious student compared to Asumi or Namiki. My only problem is that I live in a girls' dorm."
    "But my opinion is thrown out right away."

    $ char ('tyo004')

    voice yo0151
    yagami "Shut up, Yusuke!"
    yusuke "Okay...sob, sob."
    "I'm not that bad... I inwardly murmur as I stare at Asumi."
    "Then, the introduction of the transfer student begins."

    $ music_stop ()
    $ char ('tyo001')

    voice yo0152
    yagami "Her name's Hikaru Saeki. She transferred schools because of her father's job. She's going to study with you guys."

    voice as0519
    asumi "Let's enjoy our youth together!"
    yusuke "Okay, okay."
    "I throw my answer back at Asumi."
    "Because I want to hear the new student's story."
    "I think most of the male classmates think so too."
    "But our dreams are quickly smashed."

    $ char ('tyo007')

    voice yo0153
    yagami "Hikaru, introduce yourself..."

    $ char ('thi001')

    voice hi0001
    hikaru "Where can I sit?"
    "Surprised, Ms. Yagami tilts her head to the side."
    "And then tells her again,"

    $ char ('tyo014')

    voice yo0154
    yagami "How about introducing yourself?"

    $ char ('thi001')

    hikaru "......"
    "No answer. She remains silent."
    "Everybody's amazed at her attitude. However, Ms. Yagami points to one of the available desks."

    $ char ('tyo014')

    voice yo0155
    yagami "You can sit there by the window."

    $ char ('thi001')

    hikaru "......"

    $ bgfx ('sora01')
    $ bgm (12)

    "Because of their first impression, nobody talks to her for a while, even though we're on a break."
    "Some girls and boys, who were interested in her, tried to talk to her, but they quickly move away."
    "Even our leader Asumi gives up."

    $ bgfx ('bg04a')
    $ char ('tas006')

    voice as0520
    asumi "What kind of girl is she? She must be dead already."

    $ char ('tto011')

    voice to0254
    tomoe "Don't say that. She's just not used to us yet."

    $ char ('tma017')

    voice ma0111
    marumu "No response."
    "Asumi's shaking madly."

    $ char ('tas036')

    voice as0521
    asumi "She bothers me."
    yusuke "......"
    "Some beautiful girls are snobbish, but she's even worse than that."
    "She has a mood that puts people off."
    "No matter who talks to her, she just ignores them with no reaction at all."
    "She might even change the mood of the class. She's weird."

    $ music_stop ()
    $ bgfx ('sora01')

    "Whatever it is, school life continues."
    "Today's the first day of a new semester, so we don't have any real classes."
    "But we have a long homeroom, talk about new classes and how to prepare for them...something like that."
    "'...And please start thinking about what you're going to do after graduation.' Ms. Yagami's words remind me of something."
    "I'm only a student and inexperienced at that."

    $ bgfx ('black')

    "The next break comes."
    "Asumi goes to the new student Hikaru again."

    $ bgfx ('bg04a')
    $ char ('tas002')
    $ bgm (5)

    voice as1350
    asumi "Hey, can I call you Hikaru?"

    $ char ('thi001')

    hikaru "......"
    "No answer. Maybe she's just shy."
    "But Asumi doesn't care."

    $ char ('tas001')

    voice as1351
    asumi "Let's go back together after school, Hikaru! I'll show you around town."

    $ char ('thi002')

    voice hi0116
    hikaru "No thank you."

    $ char ()

    "That's all."
    "As soon as she says this, she leaves the classroom."
    "Looking at her, Asumi says,"

    $ char ('tas010')

    voice as1352
    asumi "H...hey! ...What an attitude!"
    "Hikaru's attitude arouses Asumi's combative instincts. I hope she doesn't cause problems..."

    if F015 == 0:
        jump episode15_asumi_c

    elif F015 == 1:
        jump episode15_tomoe_c

    elif F015 == 2:
        jump episode15_marumu_c

label episode15_d:

    call blackout from _call_blackout_44
    $ bgfx ('sora08')

    "We all smack our lips over Moe-Moe's cooking."
    "It's been a while for the four of us to have dinner together."
    "After dinner, we chat while doing homework."

    $ bgm (13)
    $ cg ('e3_0210')

    voice as0527
    asumi "We have a lot to do this semester. Let's do our best!"

    voice ma0113
    marumu "Best, best."

    voice to0257
    tomoe "And we have to think about after graduation also, like Ms. Yagami said in homeroom."
    yusuke "Yes. She mentioned it. I'd forgotten about it because nobody pushed us to study for college exams in our school."

    $ cg ('e3_0211')

    voice as0528
    asumi "The school's policies are to develop student independence. Well, everything will be fine if we do our best everyday."
    yusuke "Asumi, you're too optimistic. I have to think about it... How about you, Tomoe?"

    voice to0258
    tomoe "I think I'll go to a college in Tokyo."

    $ cg ('e3_0210')

    voice ma0114
    marumu "I'll do my best too."
    yusuke "Are you going to go somewhere for college?"

    voice ma0115
    marumu "It's a secret."
    "Everybody's thinking about it differently, and someone has a secret."
    "I forgot that a turning point in life is coming soon."
    "I've gotten soft since transferring here."

    call blackout from _call_blackout_45

    if F015 == 0:
        jump episode15_asumi_d

    elif F015 == 1:
        jump episode15_tomoe_d

    elif F015 == 2:
        jump episode15_marumu_d

label episode15_end:


    call ep_finish from _call_ep_finish_7

    $ renpy.end_replay()
    $ unlock_episode (15)

    jump episode16
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

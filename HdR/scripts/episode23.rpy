label episode23:

    $ Fnum = 23
    $ save_name = "Episode 23: Fading Friendship"

    $ bgfx ('black')

    "The word freezes my heart."
    "...It was the scariest word I've ever heard."

    $ bgm (16)
    $ bgfx ('bg05a')
    $ char ('tyu002')

    voice yu0035
    akane "...You're a girl, aren't you!?"
    yusuke "What are you talking about? Are you mad?"
    "Akane points at me,"
    "although I'm not pretending to be a girl now."
    "But still, she says I'm a chick!"

    voice yu0036
    akane "If you weren't a girl, how come Misaki was attracted to you! Show your true self!"
    yusuke "Stop it. Aaaa!!"

    $ sfx ('SE13', loop=True)

    "At top speed, I scuttle through the hallway where running is prohibited."

    $ sfx (delay=1.0)
    $ bgfx ('black')
    $ bgm (7)
    $ bgfx ('bg11a')
    $ char ('tyu003')

    voice yu0037
    akane "I remember I saw you near the girls' dormitory."
    yusuke "Are you sure?"

    voice yu0038
    akane "Oh, I got it! I've solved all of your mysteries!"

    $ music_stop ()

    "Akane breathes hard and solves a riddle."

    $ char ('tyu001')

    voice yu0039
    akane "You're the girl wearing glasses, who always hangs around those three stooges!"
    yusuke "......"
    "It seems like she hit the nail on the head, but somehow, it's beside the point."
    "As matter of fact, she knows almost everything."
    "When she sees I'm agitated by what she said, she smiles with a sense of satisfaction."

    $ char ('tyu002')

    voice yu0040
    akane "That's enough for now! Little by little, I'll reveal your true identity, so watch out!"

    $ char ()

    "After threatening me a bit, she leaves."
    "Yet I think she left me alone because she felt the limit of her strength. Honestly, I felt the same."
    "Anyway, she's caught me by the scruff of my neck. I can't trick her anymore."


    call ep_start from _call_ep_start_12

    $ bgfx ('sora08')

    yusuke "Under the circumstances, I should confide in my wonderful big sister."
    "Of course, I'm not talking about Namiki."
    "Instead, I head toward Ms. Yagami's apartment."
    "Recently I've been so busy, I haven't gone to see her."
    "I think this is a good chance to spend time with her and talk about the current problem."
    "However, an unexpected incident is waiting for me."

    $ bgm (4)
    $ bgfx ('bg10c')
    $ char ('tyo101')

    yusuke "Is that true?"

    voice yo0170
    yagami "Yep. What reason would I have to lie to you? Just think about it."
    yusuke "50 brownie points to Ms. Yagami!"

    $ char ('tyo102')

    voice yo0171
    yagami "Oh, I get 50 points? Then...hey, what are we talking about? Anyway, you must decide right away."
    yusuke "Why?"

    voice yo0172
    yagami "Because I know a lot of guys want to apply to the boys' dormitory."
    "That's right!"
    "The first thing Ms. Yagami has told me is that there is an opening in the Kogarashi Dorm."
    "If I fill out the form and hand it in by tomorrow, I'll be able to have a normal life as a boy."

    $ char ('tyo114')

    voice yo0173
    yagami "Yusuke, what would you like to do?"
    yusuke "Of course, I would like to..."

    $ music_stop ()

    "For some reason, I can't finish the sentence."
    "What am I hesitating for?"
    "First thing in the morning, I should dive into the boys' dormitory."
    "I know I've been waiting for the offer for a long time, but..."

    $ bgfx ('black')

    "Why?"
    "Why am I hesitating?"
    "What am I waiting for?"

    $ bgm (9)
    $ bgfx ('bg01d')

    yusuke "I like my life here, but I guess it's still inconvenient."
    "I can't show my true identity in the girls' dormitory."
    "I have to be careful and act like a girl all the time."
    "In addition, my room is a closet!"
    "I'm getting used to living in the closet, but still, I'd rather have my own room than stay in a cage! Moreover, I can live as a guy in the guys' dormitory. That means I don't need to wear a girl's uniform anymore."
    "Akane may reveal my true identity anytime too..."
    "If she discloses my secret, it may put Asumi and the others in trouble."

    call blackout (True, 1.5) from _call_blackout_72

    if F015 == 0:
        jump episode23_asumi

    elif F015 == 1:
        jump episode23_tomoe

    elif F015 == 2:
        jump episode23_marumu

label episode23_b:

    $ bgfx ('black')

    yusuke "But..."
    "I don't get it."
    "I don't know why I'm hesitating to move."
    "What I do know is something is bothering me."
    "What is it?"

    $ bgm (13)
    $ bgfx ('bg01a')

    yusuke "...Morning."

    $ char ('tma101')

    voice ma0180
    marumu "Yusuke, sleepy?"
    yusuke "...A little. By the way, where's Asumin?"
    "If Tomoe's not awake yet, I can understand because she sleeps like a baby. But Asumi always gets up earlier than the others."
    "Where is she?"
    "But somehow, our breakfast is ready on the dining table."
    "If I recall correctly, it was Asumi's turn to get breakfast ready."

    $ char ('tto128')

    voice to0323
    tomoe "Good morning. Ah...where's Asumi?"

    $ char ('tma101')

    voice ma0181
    marumu "Gone."

    $ music_stop ()

    "Tomoe heads toward the front door looking for clues."
    "After she comes back totally awake, she whispers,"

    $ char ('tto102')

    voice to0324
    tomoe "...She's already left."
    yusuke "What?"

    $ bgm (8)
    $ bgfx ('black')
    $ bgfx ('bg04a')

    yusuke "I don't see her here."

    voice to0325
    tomoe "Asumi..."
    "We hurriedly rush to our classroom."
    "However, Asumi's not here either."
    "There's something terribly desperate about the fact we can't find her anywhere."

    $ bgfx ('black')

    yusuke "The last place I can think of is..."
    "First of all, we decide to split into groups and go search for her."
    "I head directly towards our secret spot."
    "When I open the door, I accidentally run into someone."

    $ bgfx ('bg07a')
    $ char ('thi004')

    yusuke "Oh, sorry."

    $ char ('thi001')

    hikaru "......"
    "Soon, her surprised looks returns to her expressionless one."

    $ char ()

    "Hikaru passes me by as if I don't even exist."
    yusuke "What's with her?"

    voice as0759
    asumi "...Yusuke."

    $ char ('tas043')

    "Someone calls my name."
    "She sounds so blue."

    call blackout from _call_blackout_73

    "From this day on,"
    "Asumi is gone a lot of the time."
    "Even in the morning, she goes to school earlier than everyone else and doesn't come back until late."
    "She's been struggling with something, but I don't know what her secret is."
    "But I believe Hikaru is somehow involved."

    $ bgfx ('bg01c')
    $ char ('tto001')

    voice to0326
    tomoe "Hey, Asumin."

    $ char ('tas043')

    voice as0760
    asumi "What?"

    $ char ('tto002')

    voice to0327
    tomoe "You're acting strange... What's wrong?"

    $ char ('tas043')

    voice as0761
    asumi "No...nothing really."

    $ char ('tto013')

    voice to0328
    tomoe "I don't believe that! I think you're hiding something from me!"

    $ char ('tas006')

    voice as0762
    asumi "If so, what are you going to do about it? It's none of your business, anyway!"

    $ char ('tto004')

    voice to0329
    tomoe "Asumi!?"
    "Tomoe falls silent as Asumi barks."
    "Asumi is our friend and roommate."
    "If something seems amiss, of course we'll worry about her."
    "Nevertheless..."
    "Her words, 'It's none of your business,' circulates through my and perhaps Tomoe's minds with a rather cold tone."

    if F015 == 2:
        jump episode23_marumu_b

label episode23_c:

    call blackout (False, 0.5) from _call_blackout_74

    "The relationships in our room seem to have become strained."
    "But I still think we'll be okay."
    "For more than six months, I've been hanging around these three girls."
    "I believe this much of a thing won't affect our friendship."
    "But up until now, I haven't been aware of an impending friendship crisis."

    $ bgfx ('bg04a')
    $ char ('tma001')

    yusuke "Marumu?"
    "It's an unusual sight."
    "I see Marumu walking toward Hikaru's desk."
    "Our other classmates also notice it."

    $ bgm (2)
    $ char ('tas042')

    voice as0763
    asumi "Marutan?"

    $ char ('tma001')

    "She stops right in front of Hikaru."
    "Then, Hikaru gives her a cold look."

    $ chars ('tma001', 'thi001')

    hikaru "......"
    marumu "......"

    voice hi0002
    hikaru "What?"

    $ char1 ('tma016')

    voice ma0182
    marumu "...For you."
    "Marumu abruptly holds out her hand."
    "I see a handmade yellow pin in her hand."

    voice hi0003
    hikaru "What the hell is it?"

    $ char1 ('tma017')

    voice ma0183
    marumu "A yellow lucky charm."
    hikaru "A lucky what!?"

    $ music_stop ()

    "If I remember right, I think Asumi mentioned it."
    "Asumi, Tomoe, Marumu always wear yellow combs. Yellow...the color of happiness?"
    "Hikaru just stares at the pin."
    "Without warning, she slaps Marumu's hand."

    $ say_hide ()
    $ cg ('sde_0701')
    $ unlock_gallery ('g5e11')

    call cgeffect (sound_source='SE56', graphics=['sde_0702', 'sde_0703'], fx=dissolve) from _call_cgeffect_7

    yusuke "Ah!?"
    "The pin falls to the floor and makes a dull thud."
    "It breaks into pieces."

    $ bgfx ('bg04a')
    $ chars ('tma019', 'thi001')

    voice hi0004
    hikaru "Happiness? I don't need your psycho crap!"
    marumu "......"
    "Other classmates start whispering."
    "The atmosphere in here seems so tense."
    "Everybody stares at Hikaru with a scornful look."
    "It seems nobody is on her side, and then I notice somebody walking towards her."
    "It's Asumi."
    "What is she going to do?"
    "Contrary to my expectations, she doesn't do anything. I mean she doesn't slap Hikaru or anything."
    "Instead, she whispers,"

    $ char ('tas043')

    voice as0764
    asumi "Get out of here, Hikaru."

    $ char ('thi001')

    hikaru "......"

    $ char ()

    "I don't know if Hikaru is taking her advice or not."
    "Anyway, she leaves without saying a word."


    call ep_middle from _call_ep_middle_12

    if F015 == 0:
        jump episode23_asumi_c

    elif F015 == 1:
        jump episode23_tomoe_c

    elif F015 == 2:
        jump episode23_marumu_c

label episode23_end:


    call ep_finish from _call_ep_finish_11

    $ renpy.end_replay()
    $ unlock_episode (23)

    jump episode24
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

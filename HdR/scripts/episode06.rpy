label episode06:

    $ Fnum = 6
    $ save_name = "Episode 6: Code Name/U-SUKE"

    $ bgm (6)
    $ bgfx ('bg01a')
    $ char ('tts002')

    voice ts0017
    toshibo "Meow!"

    $ char ('tto016')

    voice to0063
    tomoe "Oh, welcome Toshibo."

    $ char ('tma017')

    voice ma0034
    marumu "...Welcome Toshibo."

    $ char ('tts001')

    "My apprentice Toshibo, a.k.a. Parasite Two, comes and goes most unexpectedly. He is ubiquitous."
    "How can he get up to the balcony...? Wait a minute!"
    yusuke "Hey, Asumi?"

    $ char ('tas001')

    voice as0194
    asumi "What is it, Parasite One?"
    yusuke "Since when did you start calling him Toshibo instead of Parasite Two?"

    voice as0195
    asumi "Since he was promoted to a regular roommate two days ago. Didn't you know?"

    $ char ('tma010')

    voice ma0035
    marumu "...Toshibo, Toshibo."

    $ char ('tas002')

    voice as0196
    asumi "You're our roommate now. You can call us by our nicknames, Toshibo!"

    $ char ('tts001')

    voice ts0018
    toshibo "Meow meow meow!"

    $ char ('tas012')

    voice as0197
    asumi "Yep, that's right! I'm 'Asumin.'"
    yusuke "Did he really say 'Asumin?'"

    $ char ('tas007')

    voice as0198
    asumi "You! You're not my roommate, so don't call me by that name!"
    yusuke "...Sure. (I'll never ever call you by that name!)"


    call ep_start from _call_ep_start_16

    "So I thought, but to be honest..."

    $ bgm (9)
    $ bgfx ('bg01a')

    yusuke "I'm mad! I'm very, very mad!! How could a cat go over my head like that! What is wrong with me!?"

    $ char ('tma001')

    voice ma0036
    marumu "...You're not making enough effort."
    yusuke "Is that right, Marutan?"

    $ char ('tma013')

    voice ma0037
    marumu "...Not 'Marutan!'"
    yusuke "Ohhh...sob-sob."
    "I cry as I swear at myself."
    "If they say I'm not making enough effort, I'll just have to try harder! I'll do my best and make them recognize me!"
    "I can't let a cat get ahead of me!"

    call blackout from _call_blackout_94
    $ bgfx ('sora01')

    yusuke "...Mmm."
    "I've worked hard this past week."
    "I mean HARD."
    "1. I cleaned up the room, inside and out."
    "2. I prepared breakfast everyday with different menus."
    "3. I did Asumi's and Marumu's homework (Tomoe is smart, so she doesn't need my help)."
    "4. I gave Asumi a massage (when I touched her thigh, she kicked me pretty hard)."
    "Etcetera, etcetera."
    "Quite honestly, I've become a slave around here."
    "However, they still haven't promoted me."
    yusuke "Why? I don't understand this...oh?"
    "A cat shows up at my feet."

    $ char ('tts003')

    "It's my rival, Toshibo. He's holding something in his paw."
    yusuke "What are you holding, Toshibo?"

    voice ts0007
    toshibo "Meow!"
    "Toshibo passes it to me."
    "'Please come see me. Tomoe'"
    "It's a letter from Tomoe."
    "Toshibo is able to deliver letters. He's quite the messenger cat."

    $ bgm (3)
    $ bg ('bg02a')
    $ char ('tto001', diss_long)

    voice to0064
    tomoe "Yusuke..."
    "Tomoe hesitantly calls out my name."
    "I know she feels uncomfortable talking to me person to person."
    "Still, she wants to tell me something, and she calls me."
    "It's about my recent efforts."
    yusuke "What's wrong with me? Do you have any suggestions, Tomoe?"

    $ char ('tto013')

    voice to0065
    tomoe "I know you've been working very hard. I really appreciate it, but..."
    yusuke "But...?"

    voice to0066
    tomoe "Your roommate promotion... Asumi is the only decision-maker."
    yusuke "Really!?"

    $ char ('tto004')

    voice to0067
    tomoe "And she's quite upset that you touched her...thigh."

    $ char ('tma018')

    voice ma0038
    marumu "...Sexual harassment."
    yusuke "It was not! But I see your point."
    "Hmm. Asumi is such a dictator around here."
    "If Asumi says it's black, it's black."
    "So, what I need to do is please Asumi... Wait a minute!"
    yusuke "What about Toshibo then? How did be become a regular?"

    $ char ('tto001')

    voice to0068
    tomoe "Because Toshibo caught a roach in Asumi's room."
    yusuke "...I see."
    "Should I look for roaches now?"

    call blackout from _call_blackout_95
    $ bgm (4)
    $ bgfx ('bg05a')
    $ char ('tyo001')

    voice yo0007
    yagami "Hey, Yusuke. Is there something bothering you?"
    yusuke "Uh, Ms. Yagami. No, nothing in particular."

    $ char ('tyo013')

    voice yo0008
    yagami "Are you sure? You look exhausted and depressed."

    menu:
        " "
        "Talk to Ms. Yagami.":


            yusuke "Well...I do have some concerns."
            "Ms. Yagami smiles at me like an angel."

            $ F01A += 1
        "Leave her without saying anything.":


            yusuke "...I'm alright. I'm okay."
            yagami "......"
            "Ms. Yagami stops me and talks to me gently."

    $ char ('tyo007')

    voice yo0009
    yagami "Yes, I understand your circumstances. You're still adjusting to your new environment. Should I go visit your room and have a meeting?"
    yusuke "P...please, don't do that! I mean, my room is still quite a mess, and...I can't invite any women yet."

    $ char ('tyo002')

    voice yo0010
    yagami "I can help you clean up your room then. I once participated in the Clean-up-a-Mess Championship in Tokyo."
    yusuke "...What the hell is that?"

    $ char ('tyo007')

    voice yo0011
    yagami "I was a bit naive. Heh heh."
    yusuke "I don't understand what you're talking about."

    $ char ('tyo001')

    voice yo0012
    yagami "Anyway, I'll visit your place after school today."
    yusuke "I'm sorry, but today isn't good! Bye!!"

    $ bgfx ('black')

    "I run away from Ms. Yagami."
    "Then she kindly shouts at me,"

    voice yo0013
    yagami "Remember, no pain, no gain!"
    yusuke "Thanks for your advice. You still don't need to come to my place, though."
    "Ms. Yagami gives me some energy."
    "That's right; no pain, no gain. I'll beat Asumi!"

    $ music_stop ()
    $ bgfx ('bg01a')
    $ char ('tas015')

    voice as0199
    asumi "I don't buy it, Parasite One."
    yusuke "Oh noooo!"

    $ bgfx ('black')

    yusuke "Hic hic."
    "The next morning..."
    "It's still very early, yet I'm awakened by Asumi's scream."

    $ bgm (7)

    voice as0200
    asumi "What's going on...?"
    "It's noisy outside, and the origin of the noise is closing in."
    "The closet door bursts open."

    $ bgfx ('bg01a')
    $ char ('tas130')

    yusuke "Asumi!? What's going on?"

    voice as0201
    asumi "Get out of there! Move!!"
    "She forcibly drives me out of my room (closet)."
    "She enters and starts throwing my personal belongings out."

    $ sfx ('SE01', loop=True)

    yusuke "What the hell are you doing!?"

    $ char ('tas110')

    voice as0202
    asumi "I can't find it...I can't find it!"

    $ char ()
    $ sfx (delay=1.0)

    "She jumps out of the closet and runs back to her room."
    "It's 5:00 am."
    "I can't stop yawning. My stuff is everywhere."

    $ music_stop ()
    $ bgfx ('sora01')

    "Asumi busily runs around until she leaves for school."
    "It's rather rare to see her skip breakfast."

    $ bgm (6)
    $ cg ('e3_0205')

    yusuke "What the hell is wrong with her?"

    voice ma0039
    marumu "...She's lost something important."
    yusuke "Something important? Which is?"

    voice ma0040
    marumu "...MUMBLE-MUMBLE."
    "Marumu's answering alright. I just don't understand what she's saying since her mouth is full of her breakfast."
    "Well, I can ask her later."

    $ cg ('e3_0206')

    voice to0069
    tomoe "YAWN... Good morning, everybody."
    yusuke "How could she sleep with all that fuss?"

    voice to0070
    tomoe "MUNCH-MUNCH. Wow, this bread is tasty!"
    yusuke "You're really something, Tomoe."

    $ bgm (12)
    $ bgfx ('sora01')

    "Marumu explains on our way to school:"

    $ ev ('ka_03')

    "Asumi lost her accessory, which used to be attached to her school bag."
    "It's gone now."
    "She doesn't know where she lost it."
    "And that's why Asumi's searching everywhere like crazy."
    "By now, she must be crawling around everywhere in the school."

    $ bgfx ('bg03a')

    yusuke "So, Asumi broke into Marumu's room, too. Oh my, my."

    $ char ('tto001')

    voice to0071
    tomoe "Sorry to hear that. She didn't come to my room, though."
    yusuke "...I'm pretty sure she did."
    "Tomoe just didn't know it."
    "Yep, she's a sleeping beauty."
    "Anyway,"
    "I know what Asumi's accessory looks like."
    "It's a small, pretty yellow one with two brooches attached. It doesn't become Asumi at all."
    "Looking at her panicking, it must be very important to her."
    "If I find it, then..."
    yusuke "I'll be promoted to a roommate without a doubt!"
    "I won't be a slave anymore!"
    "They'll treat me as a human!"

    $ bgm (5)

    yusuke "Yes! I'll find it... I'm going to find it!!"

    $ char ('tma002')

    voice ma0041
    marumu "...Oh, yeah."
    "I don't know why Marumu answers me, but I thank her anyway. I'll find Asumi's missing accessory, no matter what!!"

    $ bgfx ('sora01')

    "From the first floor to the third."
    "The stairways, the rooftop, and the basement."
    "The gym, the school yard, and the pool outside."
    "The path we take to and from school,"
    "And every inch of our room."

    $ bgfx ('sora05')

    "I haven't found it yet."
    "I search harder than a regular detective."
    "Unfortunately, I can't find a clue."

    $ bgm (9)
    $ bgfx ('sora09')

    yusuke "Clue...a clue for what?"
    "I cuss at myself and sink my face into my futon."
    "I'm exhausted."
    "It'd be a waste of time to look for it any further."
    "And I still can't deny the biggest possibility, which is 'Asumi's misunderstanding.'"
    "She was such a scatter-brain, and she still is."
    "I've still got a long way until becoming a roommate, I guess."
    "While I'm feeling sorry for myself, I fall asleep."


    call ep_middle from _call_ep_middle_16

    $ bgfx ('bg01a')
    $ char ('tas024')

    "Asumi must have given up looking for it as well."
    "Asumi seems calm down today."
    "I worried about her yesterday, but she looks okay now."

    $ bgfx ('black')
    $ bgfx ('bg04a')
    $ bgm (12)
    $ pause (0.5)
    $ char ('tma017')

    yusuke "What's the deal with that accessory anyway? It must be very important, I assume."

    voice ma0042
    marumu "...It's very expensive!"
    yusuke "Sorry, but it didn't look all that fancy."

    $ char ('tma004')

    voice ma0043
    marumu "...It's a keepsake!"
    yusuke "Still, it looked kind of childish. And something like a keepsake doesn't match Asumi's character at all."

    $ char ('tma016')

    voice ma0044
    marumu "...It contains a secret code!"
    yusuke "Huh? I don't think so."

    $ char ('tto001')

    voice to0072
    tomoe "When you hold it towards the sun, it'll discharge a mysterious light. And you'll find a legendary ancient city when you follow that light."
    yusuke "What the hell are you talking about!?"

    $ char ('tto007')

    voice to0073
    tomoe "Heh, I'm sorry."
    "I thought Marumu had been talking, but it's Tomoe."
    "What Tomoe just said is something I wasn't expecting from a person like her."
    yusuke "Anyway, she'll forget about it in a couple of days. She was acting normal this morning... Where's Asumi?"

    $ char ('tto001')

    voice to0074
    tomoe "She just went out. It's only lunch break."
    yusuke "Yeah, sure."
    "Still, something disturbs me."
    "The fact that Asumi isn't here disturbs me."
    "Alright. I'll find Asumi and ask her about the accessory."
    "Then my anxiety will be disappear."

    $ music_stop ()
    $ bgfx ('bg07a')

    yusuke "There she is. Hey, Asu...mi?"

    $ bgm (8)

    "I stop calling her name."
    "She looks gloomy."

    $ char ('tas021')

    "Her hair is swirling in the wind. She's staring out in the distance."
    "Somewhere, very far away."
    "Her profile looks so..."

    $ bgfx ('black')

    yusuke "Okay."
    "I don't talk to her."
    "I head back to the school building."
    "And I run down the stairs."
    "I still don't know what the accessory is."
    "But I do know..."
    "...how important that accessory is to Asumi."
    "It strikes my heart."
    "She needs it. It must be very important to her!"

    $ music_stop ()
    $ bgfx ('bg04b')
    $ char ('tto001')

    voice to0075
    tomoe "Yusuke, aren't you going home yet?"
    yusuke "No, I have something to take care of. You go home without me."

    voice to0076
    tomoe "Okay. I'll see you later."

    $ char ()

    "I lay down flat on the floor."
    "I was serious yesterday."
    "But I guess I wasn't serious enough."
    "I just didn't know how desperate Asumi was."
    "I've never seen her look so sad."
    "Of course, I still hate her sometimes."
    "Today, she looks so fragile and weak."
    "That's not the Asumi I know."
    "Again, the accessory must mean a lot to her."
    "That's why I must find it!!"

    $ bgfx ('bg12b')

    "I haven't covered everything."
    "I need to look in other places as well."
    "Asumi always swings her school bag while she walks."
    "If she lost it somewhere around here, she wouldn't notice it."
    "Those bushes on the side of the road."
    "I step into the bushes."
    "This will take an eternity."
    "The sun is setting. It's getting dark."
    "Still, I start pushing the bushes away and looking inside."
    "I remember Asumi's sad profile."

    $ bgfx ('black')
    $ bgfx ('sora08')

    yusuke "Whew, whew...man, I'm dying."
    "I crouch down in the bushes and look up at the night sky."
    "I see a beautiful sea of stars."
    "It's late and dark."

    menu:
        " "
        "Give up and go home.":


            yusuke "It's really dark outside. I can't see a thing."
            "I tell myself as I lift up my leg, which is now covered in mud."
            "Then, all of a sudden, a sense of terror runs through my spine."
            "Something unknown is closing in. It's flying very low."

            $ bgfx ('bg12c')
            $ sfx ('SE37', loop=True)

            "RUSTLE-RUSTLE..."
            yusuke "What...what is it!?"
            "I shiver."
            "In the country side like this place,"
            yusuke "It could be a huge, poisonous snake or something...!"

            $ sfx (delay = 0.3)
            $ char ('tma010')

            voice ma0045
            marumu "...Bah."
            yusuke "Hyuh... EEEEEEK!!"
            "The shadow of an animal jumps out of the bushes."
            "It's actually...a small human."

            $ bgm (2)

            yusuke "Is that...Marumu?"

            $ char ('tma017')

            voice ma0047
            marumu "...Marumu, this side. Number One, that side."
            yusuke "You're looking for it too."

            $ char ()

            "The presence I felt was Marumu."
            "Yes, Marumu has been searching for Asumi's accessory too. Now, I can't give up until I find it."
            "I'll be so uncool if I leave here without any results."
            "I fire myself up and force my way into the bushes again."
        "Search some more.":


            yusuke "Should I stop now and go home? No...a little more!"
            "I should move to the other side of the road. I walk across the pavement and step into the bushes. Then..."

            $ bgfx ('bg12c')
            $ sfx ('SE37', loop=True)

            "RUSTLE-RUSTLE..."
            yusuke "What...what is it!?"
            "I hear something crawling on the dark ground."
            "I can't see it, but it sounds very quick."
            "I shudder in terror."
            "In the middle of nowhere like this."
            yusuke "Is this...Tsuchinoko, the legendary snake!?"

            $ sfx (delay = 0.3)
            $ char ('tma010')

            voice ma0045
            marumu "...Bah."
            yusuke "EEEEEK! Tsuchinoko...speaks!!"

            $ char ('tma003')

            voice ma0046
            marumu "...Where is the Tsuchinoko?"
            yusuke "...Huh?"
            "The shadow of an animal jumps out of the bushes."
            "Actually, it's a small human."

            $ bgm (2)

            yusuke "Marumu? Is that you!?"

            $ char ('tma017')

            voice ma0047
            marumu "...Marumu, this side. Number One, that side."
            yusuke "...Okay."

            $ char ()

            "Marumu dives into the bushes again."
            "Marumu has been helping me look for the accessory."
            "That's right. I didn't see her when Tomoe left school."
            yusuke "Still...she doesn't need to call me by a number, you know. Sob-sob."

            $ F018 += 1

    call blackout from _call_blackout_96

    "I'm covered with mud completely."
    "And I'm tired."
    "But it doesn't matter. What matters is that I can't find the accessory."
    "I don't want to see Asumi's sad face again."

    $ bgfx ('bg01c')

    yusuke "...I'm back."

    $ char ('tto201')

    voice to0077
    tomoe "Welcome back, Yusuke...what happened to you!?"
    yusuke "I got stuck in a puddle."

    voice to0078
    tomoe "Marumu told me the same thing. She's taking a bath right now."

    $ char ('tma103')

    voice ma0048
    marumu "...Welcome back, Number One."
    yusuke "Hey, there you are."
    "I see that dinner is already on the table."

    $ char ('tto225')

    "Tomoe is in charge of dinner."
    "However, I see the menu is quite unbalanced tonight."
    yusuke "These are Asumi's favorites."

    $ char ('tto234')

    voice to0079
    tomoe "That's right. She's pretty depressed, so I want to cheer her up."
    "Tomoe knows it."
    "Everybody knows it."
    "They all worry about Asumi."
    "I'm happy to know that. I'm very happy."

    $ char ('tto225')

    voice to0080
    tomoe "Hey, Marumu. Could you please call Asumi and tell her that dinner's ready?"

    $ char ('tma101')

    voice ma0049
    marumu "...She's coming!"

    $ sfx ('SE52')
    $ char ('tma103')
    $ char ('tma101')

    "FLASH!! Marumu's round hair ornaments shine (no meaning at all)."
    "Then, the door explosively opens, and Asumi jumps out of her room."

    $ sfx (delay=0.3)
    $ bgm (10)
    $ char ('tas105')

    voice as0203
    asumi "I found it. I found it!!"

    voice to0081
    tomoe "Asumi, did you...?"

    $ char ('tas112')

    voice as0204
    asumi "Yes, I found it! Ohh."
    "She expresses her happiness with a big smile."
    "She's so excited."

    $ char ('tma101')

    voice ma0050
    marumu "...Where was it?"

    $ char ('tas127')

    voice as0205
    asumi "W...well, I found this in..."

    $ bgm (12)
    $ bgfx ('black')
    $ bgfx ('bg01c')
    $ char ('tas127')

    yusuke "It was in your bag, wasn't it?"

    voice as0206
    asumi "Y...yes. Ha ha, I'm so stupid!"
    "The lock was loose, so it fell inside of her bag."
    "She found it when she was taking everything out of her bag in order to put in something new for the next week."

    $ char ('tto213')

    voice to0082
    tomoe "See? I told you to check your bag everyday."

    $ char ('tas142')

    voice as0207
    asumi "I'm sorry. I really apologize, Moe-Moe."
    "She droops for a second, but she can't hide her smile. She must be really happy."
    "And Marumu and my efforts were in vain."
    "There's a thing or two, no...a lot of things I want to tell Asumi."
    "When my eyes meet hers, I naturally say,"
    yusuke "I'm glad you found it. That's great!"

    $ char ('tas145')

    voice as0208
    asumi "...Yeah, thanks."
    "Everything is solved now. Her smile is back."

    call blackout from _call_blackout_97
    $ bgfx ('sora05')

    "The next week, Asumi summons us to a meeting."
    "She wants to have a party at Okonomidama to commemorate the finding of her accessory."
    "I don't know why we have to have a party, but I have nothing against having dinner at Okonomidama either. They serve delicious meals."
    "However, I'm a half-hour late for this meeting because Ms. Yagami asked me to help her Amateur Acting club's preparation."

    $ cg ('e3_0109')
    $ bgm (3)
    $ sfx ('SE14')

    yusuke "Sorry, I'm late."

    $ sfx (delay=0.3)

    voice as0209
    asumi "Yes, you're late. I want to fine you for that!!"

    voice to0083
    tomoe "Hi, Yusuke."

    voice ma0051
    marumu "...Yusuke, sit."
    "I sense something unusual, but I sit down at the table anyway."
    "I was expecting them to start the party without me."
    "But they haven't even ordered yet."

    $ bgfx ('black')
    $ cg ('e3_0110')

    voice as0210
    asumi "Okay, let's eat!"

    voice to0084
    tomoe "...Let's start."

    voice ma0052
    marumu "CHOMP-CHOMP... I'm already eating."
    "Marumu is a strange girl alright. Anyway, everybody starts eating at once."
    "Asumi keeps talking while she's eating as usual."
    "This is Asumi alright, but..."
    yusuke "Hey, Asumi. Is that accessory..."

    $ cg ('e3_0109')

    voice as0211
    asumi "No, Yusuke. It's Asumin!"
    yusuke "Oh, I'm sorry. I'm such a...wait a second!"

    voice as0212
    asumi "This is Moe-Moe. The girl who's so busy eating is Marutan. You got that?"

    voice to0085
    tomoe "P...pleasure to meet you, Yusuke."

    $ cg ('e3_0111')

    voice ma0053
    marumu "...Yusuke, good."
    "Marumu doesn't stop swinging her flag as she eats."
    "They look at me with smiles. I don't understand this."

    $ bgm (5)
    $ cg ('e3_0112')

    voice as0213
    asumi "I haven't told you yet, but you've been promoted to a regular roommate."

    voice to0086
    tomoe "This is actually a celebration for you."

    $ cg ('e3_0109')

    voice as0214
    asumi "You! You speak too much."

    voice to0087
    tomoe "Oops. I'm sorry."
    "I can't hide my surprise at the sudden promotion."
    "But why?"

    $ cg ('e3_0112')

    voice as0215
    asumi "You don't need to know the reason. Now don't go on a spree, got that!? You're still a parasite, you know."
    yusuke "Understood, Asumin!"

    voice as0216
    asumi "Good! Moe-Moe, watch him and learn from him!"

    voice to0088
    tomoe "Y...yes, ma'am."
    "I try to comfort Tomoe and ask Asumi a question."
    yusuke "By the way, what's my nickname going to be?"

    $ cg ('e3_0110')

    voice ma0054
    marumu "...Yusuke."
    yusuke "That's not a nickname. Well, whatever."
    "Why was I promoted to a regular roommate?"
    "And what's all that about Asumi's accessory?"
    "I have tons of questions, but what the hell, I'll let them go."
    "Because I'm finally able to step forward as their official roommate, even though the cat got there ahead of me (sob-sob)."

    voice ts0019
    toshibo "Meow!"
    yusuke "Okay, okay. You're still my superior."


    call ep_finish from _call_ep_finish_15

    $ renpy.end_replay()
    $ unlock_episode (6)
    jump episode07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

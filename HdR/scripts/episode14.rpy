label episode14:

    $ Fnum = 14
    $ save_name = "Episode 14: The All Girls Secret Meeting"

    $ music_stop ()
    $ bgfx ('sora09')

    "...One night."
    "I'm relaxing just before going to sleep in my room (closet)."
    "But there's something bothering me."

    $ bgfx ('black')
    $ sfx ('SE37', loop=True)

    "The weird sounds."
    "From the next room? No, from the room below us?"
    "But there's nobody living down there."
    yusuke "Nooo, I wish the boys' dorm had an available room like there is here. Anyway...?"
    "There shouldn't be any sound coming from a room that's supposed to be empty."
    "What is it then!?"
    yusuke "A thief, a ghost, a mysterious underground world, or... WAAAAAH!!"
    "As soon as I press my ear against the wall to listen,"
    "My body starts floating upward."
    "And the wall has disappeared."

    $ sfx (delay=0.5)

    "And then, I drop all the way down in the dark... THUMP!!!"

    $ sfx ('SE45')

    yusuke "EEEEKS!!! Ouch! Ouch! Where am I?"

    $ sfx (delay=0.1)

    "Last time, when I found a secret door and the steps to the roof that Marumu uses, I was really surprised."
    "But how many secrets can there be in this dorm?"
    yusuke "Hmm, I see a light over there..."
    "I don't want to stay in this weird place any longer!"
    "I follow the light to get out of the darkness."
    "And I see..."


    call ep_start from _call_ep_start_27

    $ bgfx ('white')
    $ bgfx ('bg18a')
    $ char ('tas709', chibi=1)

    voice as0469
    asumi "Hello, everybody! I'm Asumin!"

    $ char ('tma602', chibi=1)

    voice ma0086
    marumu "...I'm Marutan."

    $ char ('tto711', chibi=1)

    voice to0215
    tomoe "Ah... I'm Moe-Moe."

    $ chars ('tas704', 'tto711', chibi=1)

    voice as0470
    asumi "This is a special event!"

    $ char2 ('tto710', chibi=1)

    voice to0216
    tomoe "Eh? But...wh..."

    $ char ('tma603', chibi=1)

    voice ma0087
    marumu "...Special."

    $ char ('tas706', chibi=1)

    voice as0471
    asumi "Anyway, let's start!"

    voice as1237
    everyone "A special event! Akemashi te Roommate!"

    $ bgm (5)
    $ chars ('tas704', 'tma606', chibi=1)

    voice as0472
    asumi "CLAP CLAP CLAP!"

    voice ma0088
    marumu "RUB-A DUB!"

    $ char ('tto711', chibi=1)

    voice to0217
    tomoe "You don't need to say that..."

    $ char ('tas710', chibi=1)

    voice as0473
    asumi "Huh? Why are you so difficult today, Moe-Moe?"

    $ char ('tto707', chibi=1)

    voice to0218
    tomoe "No, I'm not..."

    $ bgfx ('bg18b')
    $ char ('tas709', chibi=1)

    voice as0474
    asumi "Let's see, the first half of 'Heart de Roommate' has finished! I'm glad this isn't the end."

    $ char ('tma604', chibi=1)

    voice ma0089
    marumu "...How's our audience rating?"

    $ char ('tas709', chibi=1)

    voice as0475
    asumi "There's no such thing. This is a game, Marutan."

    $ char ('tto712', chibi=1)

    voice to0219
    tomoe "Thank you for playing this game."

    $ char ('tas708', chibi=1)

    voice as0476
    asumi "Let's look back at the stories you've been through so far."

    $ char ('tma606', chibi=1)

    voice ma0090
    marumu "Is this a summary or what?"

    $ char ('tto712', chibi=1)

    voice to0220
    tomoe "Actually, this is just a break. It doesn't have any meaning in the game."

    $ char ('tas703', chibi=1)

    voice as0477
    asumi "Don't say that! This is an evaluation meeting! Did you guys work hard?"

    $ bgfx ('bg18c')
    $ chars ('tas708', 'tma621', chibi=1)

    voice ma0091
    marumu "...I did."

    voice as0478
    asumi "You didn't talk much, so it's hard to tell whether you did or not, Marutan."

    $ bgfx ('bg18d')
    $ chars ('tas708', 'tto711', chibi=1)

    voice to0221
    tomoe "I...I just tried not to bother anybody."

    voice as0479
    asumi "Well, I think you worked hard since we became roommates."

    $ char2 ('tma602', chibi=1)

    voice ma0092
    marumu "...There might be stories of how we met after this..."

    $ char1 ('tas703', chibi=1)

    voice as0480
    asumi "Don't give it away, Marutan!"

    voice ma0093
    marumu "...Did you work hard?"

    $ bgfx ('bg18e')
    $ chars ('tas706', 'tma602', chibi=1)

    voice as0481
    asumi "Of course! I don't want to waste a minute of my youth!"

    $ char2 ('tto713', chibi=1)

    voice to0222
    tomoe "By the way Asumi..."

    $ chars ('tas703', 'tto703', chibi=1)

    voice as0482
    asumi "A S U M I N! I'm tired of this phrase! I expect you guys to remember after this!"

    $ chars ('tas710', 'tto711', chibi=1)

    voice to0223
    tomoe "O...okay, Asumin. You use the word 'youth' so often, why is that?"

    $ char1 ('tas706', chibi=1)

    voice as0483
    asumi "What a good question! Yes! Of course I have a reason. You'll cry if you hear the story."

    $ char ('tma624')

    voice ma0094
    marumu "...Whatever. Let's go next."


    call ep_middle from _call_ep_middle_28

    $ bgfx ('bg18a')
    $ bgm (9)
    $ chars ('tas707', 'tto707', chibi=1)

    voice as0484
    asumi "...That's why."

    voice to0224
    tomoe "Ohhh, I see...Asumin. You had a hard time...sob!"

    $ char ('tma606', chibi=1)

    voice ma0095
    marumu "...Most of her stories aren't true."

    $ bgm (5)
    $ char ('tas710', chibi=1)

    voice as0485
    asumi "Why are you also being so difficult, Marutan! By the way, where's the noisy woman?"

    $ char ('tto713', chibi=1)

    voice to0225
    tomoe "Oh, are you talking about Namiki? She went to the hot springs with Ms. Yagami, so she's taking some time off."

    $ char ('tma622', chibi=1)

    voice ma0096
    marumu "...Budget cuts."

    $ char ('tas709', chibi=1)

    voice as0486
    asumi "The older women are absent... Older women get more talent fees than we do."

    $ char ('tto714', chibi=1)

    voice ts0033
    toshibo "Meow! Meow, meow!"

    $ char ('tto715', chibi=1)

    voice to0226
    tomoe "Hey, Toshibo. There you are! Huh? Did you say, 'Let me talk more!?'"

    $ char ('tas706', chibi=1)

    voice as0487
    asumi "We have to translate when you speak, so let's not waste our time! Go eat the can of tuna over there!"

    $ char ('tto714', chibi=1)

    voice ts0034
    toshibo "Meow, meow!"

    voice to0227
    tomoe "Yes, I put some 'Boiled Eggs' for you over there."

    $ char ('tto716', chibi=1)

    voice ts0035
    toshibo "Meow!!!"

    $ char ('tas708', chibi=1)

    voice as0488
    asumi "OK, he's gone. By the way, I want to ask you girls something."

    $ char ('tto713', chibi=1)

    voice to0228
    tomoe "Huh? What is it?"

    $ char ('tas704', chibi=1)

    voice as0489
    asumi "About Yusuke! What do you think of him?"

    if F015 == 0:
        jump episode14_asumi

    elif F015 == 1:
        jump episode14_tomoe

    elif F015 == 2:
        jump episode14_marumu

label episode14_b:


    $ char ('tto713', chibi=1)

    voice to0232
    tomoe "OK! We have to wrap this up pretty soon, so let's think about what's coming up later on in this game!"

    if F015 == 0:
        jump episode14_asumi_b

    elif F015 == 1:
        jump episode14_tomoe_b

    elif F015 == 2:
        jump episode14_marumu_b

label episode14_c:

    $ bgfx ('bg18a')
    $ music_stop ()
    $ char ('tas708', chibi=1)

    voice as0499
    asumi "Enjoy the rest of the game!"

    $ char ('tto705', chibi=1)

    voice to0236
    tomoe "Is it true that the game title is going to be changed?"

    $ char ('tma623', chibi=1)

    voice ma0103
    marumu "Change, change!"

    $ char ('tas708', chibi=1)

    voice as0500
    asumi "All right, you'll see something new in 'Heart de Roommate!'"



    $ bg ('bg01c')
    $ char ('tas002')

    voice as0501
    asumi "Ohh, I'm tired. But actually, I've enjoyed this."

    $ chars ('tto020', 'tma001')

    voice to0237
    tomoe "If we're going to do Episode 26, why don't we summarize what it's about?"

    voice ma0104
    marumu "Discuss it, discuss it."

    $ char ('tas005')

    voice as0502
    asumi "That doesn't mean we're stalling for time because we only made 25 episodes. This will really be fun!"

    $ char ('tto007')

    voice to0238
    tomoe "But aren't you embarrassed that someone might actually read our conversations?"

    $ char ('tas018')

    voice as0503
    asumi "For example, Yusuke? If he sees this, why don't we erase him and make a new hero?"

    $ char ('tto020')

    voice to0239
    tomoe "Poor Yusuke. But it might not be a bad idea. The hero robot usually changes in the second half!"

    $ char ('tas007')

    voice as0504
    asumi "Huh? The hero robot!? Anyway, who could be the next hero? I don't think Kosuke can do it."

    $ char ('tto020')

    voice to0240
    tomoe "How about Misaki? Girls like guys who have secrets."

    $ char ('tas037')

    voice as0505
    asumi "No. He's psycho actually...oops, that was a secret."

    $ char ('tas001')

    voice as0506
    asumi "Whatever, it's just in case Yusuke sees all of this."

    $ char ('tma401')

    voice ma0105
    marumu "Yusuke's watching us."

    $ chars ('tas030', 'tto022')

    voice as0507
    asumi_tomoe "...Oh no!?"
    yusuke "H...hello..."

    $ bgfx ('sora09')

    "The three of them gradually close in on me."
    "I didn't see it on purpose!"
    "I just got lost and came here accidentally!"
    "Will you erase me? Am I dismissed?"
    "HEEEE!"

    voice as0508
    asumi "Good night, Yusuke...forever."

    $ bgfx ('black')
    call effect (graphics=['red']) from _call_effect_46
    $ empat ('j5')

    yusuke "WAAAAAH!"

    $ empat ()
    $ bgfx ('bg01a')
    $ char ('tas105')
    $ bgm (12)

    voice as0509
    asumi "Why are you screaming, Yusuke?"

    $ char ('tto219')

    voice to0242
    tomoe "Oh, good morning, Yusuke!"

    $ char ('tma101')

    voice ma0106
    marumu "...Good morning."

    $ char ('tts002')

    voice ts0036
    toshibo "Meow!"
    yusuke "Hmm? I see, it was all just a dream. I thought so."

    $ char ('tas112')

    voice as0510
    asumi "It's all right, Yusuke. You were reborn again!"

    $ char ('tto220')

    voice to0243
    tomoe "I think the new version of Yusuke's prettier. Hee hee."

    $ char ('tma108')

    voice ma0107
    marumu "New version."
    yusuke "What are you talking about? Are you girls kidding me?"

    $ char ('tts002')

    voice ts0037
    toshibo "Look at your room, meow!"
    yusuke "A...alright."

    $ bgfx ('black')
    $ music_stop ()

    "I open the door of my room (closet) as Toshibo suggested."
    "I find something unbelievable inside."
    "The body, it looks just like me."
    "But it doesn't move at all. It's like a corpse."
    "And there's a memo on its forehead. It says..."
    yusuke "The old version of Yusuke."

    voice as0511
    asumi "You were reborn as a new hero. Be happy, Yusuke!"
    yusuke "I DON'T THINK SO!!"

    voice ma0108
    marumu "Great."


    call ep_finish from _call_ep_finish_21

    $ renpy.end_replay()
    $ unlock_episode (14)

    jump episode15
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

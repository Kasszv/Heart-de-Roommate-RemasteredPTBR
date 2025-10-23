label episode03:

    $ Fnum = 3
    $ save_name = "Episode 3: The Name is Toshibo"

    $ bgfx ('black')
    $ bgm (6)
    $ bgfx ('bg01a')
    $ sfx ('SE37', loop=True)

    "RATTLE-RATTLE..."
    yusuke "...Oh?"
    "RATTLE-RATTLE-RATTLE..."
    yusuke "...What is it?"
    "The usual quiet morning...but the silence was broken by some noise."
    "RATTLE-RATTLE...Sssssss...."
    yusuke "Man, it's such an annoying noise."
    "I stop preparing breakfast."
    "The sound comes from the balcony."
    "But I can't see a thing through the curtain."
    yusuke "...Should I check it out?"
    "I'm the bodyguard here, you know."
    "Hence, it's my responsibility to find out what's causing the mysterious sound on the balcony."
    yusuke "Otherwise...Asumi will kick my ass."
    "I head to the window as I sigh."
    "I move closer to the curtain with some curiosity."


    call ep_start from _call_ep_start_13

    $ bgm (7)
    $ bgfx ('bg01a')
    $ char ('tts016')

    yusuke "......"

    voice ts0001
    uc "...mew."
    yusuke "......"

    voice ts0002
    uc "...mew...me...mew."
    yusuke "Wh...whoooooa!!"
    "When I'm scared, I'm scared...even if I am a bodyguard."
    "Because I don't know how to deal with this mysterious monster!"
    "It's barely alive...the dried up UMA (Unidentified Mysterious Animal)."
    "I'm too scared to get closer to that THING."
    "Is that some kind of local animal...?"

    $ chars ('tas105', 'tma101')

    voice as0091
    asumi "Hey, what are you doing, Parasite One?"

    voice ma0020
    marumu "...What are you doing?"
    yusuke "Oh, Asumi and Marumu, come over here and look at that! Do you see that THING? Is that some kind of local animal in this region!?"

    $ char ('tas139')

    voice as0092
    asumi "Well, let's see... YAAAAAA!!"

    $ sfx ('SE01', loop=True)

    voice ma0021
    marumu "...Must be the Thing."
    "Oh gosh, Asumi's screaming."
    "That must be something people have never seen before!"

    $ char ('tas130')
    $ sfx (delay=1.0)

    voice as0093
    asumi "H...hey, you! Do something! You're the bodyguard!!"
    yusuke "But I don't know how to fight with this...thing."

    $ char ('tts016')

    voice ts0003
    uc "...meow."

    voice ma0022
    marumu "...It meowed."
    "Judging from its voice, this animal must be weakened."
    "Still, I don't know what it is. I must be careful...oh?"

    $ char ('tas111')

    voice as0094
    asumi "Here, use this! Now go get it!"
    yusuke "This is...just a broom! How am I supposed to fight this beast with a damned broom!?"

    $ char ('tma108')

    voice ma0023
    marumu "...Swing at full force?"
    yusuke "But still..."

    $ char ('tas111')

    voice as0095
    asumi "Shut up and go, Parasite One!"
    yusuke "Ohhh..."

    menu:
        " "
        "What the hell! Face it!":


            "I walk slowly towards the creature, step by step..."
            "Then, the creature growls at me."

            $ char ('tts016')

            voice ts0004
            uc "...mew...meow...meow!!"
            yusuke "Waaah! Help me, please...!"

            voice to0020
            tomoe "To...Toshibo!?"
            "Somebody bumps into me as I get ready to escape."

            $ F016 += 1
            $ F018 += 1
        "No way. Just run away!??":


            "Fighting this creature with a broom is more like committing suicide."
            "I decide to retreat. I want to see the sunrise tomorrow, you know."
            yusuke "Th... I'm sorry, ladies."

            $ char ('tts016')

            voice ts0004
            uc "...mew...me...meow!!"
            yusuke "Waaaaaah!!"

            $ sfx ('SE13', loop=True)

            "Somebody rushes into the room as I escape."

            voice to0020
            tomoe "To...Toshibo!?"

            $ sfx (delay=0.5)

    $ music_stop ()
    $ char ('tto213')

    "She wasn't here a few minutes ago."
    "She's always gentle and has long hair...she's Tomoe. She opens her eyes wide and without hesitating, holds the dried up creature in her arms."

    $ char ('tto207')
    $ bgm (10)

    voice to0021
    tomoe "Yes, it's you, Toshibo!! What happened to you!? Toshibo!!"

    $ char ('tts016')

    voice ts0005
    uc "...mew...meow...mew."
    yusuke "Wha...what's going on?"

    $ char ('tas124')

    voice as0096
    asumi "One thing is for certain...that creature is some kind of animal called Toshibo."

    $ char ('tma103')

    voice ma0024
    marumu "...Toshibo."

    $ bgfx ('black')

    "We're astounded to see Tomoe and the mysterious, dried up animal hugging each other."

    $ music_stop ()
    $ bgfx ('bg01a')
    $ char ('tts001')
    $ bgm (6)

    yusuke "...This isn't real."

    voice as0097
    asumi "...I have to agree."

    voice ma0025
    marumu "...Unbelievable."
    "We're looking at the Thing in front of our eyes."
    "It's an animal with a spherical shape. Gosh, it's fat!"
    "'The Thing' already consumed milk, French bread, sausages, eggs, and whole chunks of ham."
    "Tomoe enthusiastically keeps feeding the mysterious 'Toshibo' creature."
    "They were all food items which were supposed to be our breakfast."
    "The dried up jerky changed its shape while being fed."
    "It's some kind of feline...maybe a cat, but I'm not too sure about that."
    "Tomoe cleans up Toshibo's leftover scraps and tenderly talks to him."

    $ char ('tto216')

    voice to0022
    tomoe "Anyway, Toshibo...why did you come here?"

    $ char ('tts002')

    voice ts0006
    toshibo "Meow!"
    yusuke "Hey, Tomoe...is this cat your friend or something?"

    voice ts0007
    toshibo "Meow!"
    yusuke "I'm not asking you!"
    "The fat cat suddenly jumps into Tomoe's plump breasts."
    "I envy him...no, I mean the cat is imprudent. Tomoe, however, gently hugs the fatty."

    $ bgfx ('black')
    $ bgm (12)
    $ bgfx ('bg01a')
    $ char ('tas124')

    voice as0098
    asumi "...Hmm, I see."
    "Asumi gets persistent when she gets curious."
    "Then, Asumi calls for an emergency meeting: 'A Complete Investigation of the Relationship between Moe-Moe and the Fat Cat.'"
    "...Asumi just wants to know what happened between two people...I mean Tomoe and the cat."
    "From what Tomoe told us, this is how they started their relationship:"

    $ char ('tts001')

    "The fat cat Toshibo (named by Tomoe) used to live near Tomoe's house."
    "One day, friendship started to grow between them, and they kept it up for five years."
    "But Toshibo wasn't her pet, by the way."
    "And when Tomoe decided to move into Harukaze dorm a year ago, they said their farewells."

    $ char ()

    yusuke "...Hey, how can you and Toshibo..."

    $ char ('tas105')

    voice as0099
    asumi "Okay! I understand. There's no need to ask her any more questions!"

    $ char ('tma102')

    voice ma0065a
    marumu "......(nod)"

    $ char ('tto225')

    voice to0023
    tomoe "Hey, guys..."
    "What the heck!?"
    "There are still tons of stuff we don't know at all!"
    "How can Tomoe have a conversation with Toshibo?"
    "Is it possible to grow a friendship between a human and a cat?"
    "Why? Why? Why? And...why!?"
    "And still, the girls are finishing this meeting. Are they out of their minds!?"
    yusuke "Hey, I have a question!"

    $ char ('tas107')

    voice as0100
    asumi "Overruled. Parasite One doesn't have a right to speak up!"
    yusuke "Noooo..."
    "Asumi ignores me and points at the fat cat."

    $ bgm (5)

    voice as0101
    asumi "Toshibo is just promoted to Parasite Two. Are there any objections?"

    $ char ('tto225')

    voice to0024
    tomoe "Asumi..."

    $ char ('tma102')

    voice ma0065a
    marumu "......(nod)"
    yusuke "...Is this for real?"
    "I have an apprentice all of a sudden."
    "Just like that."

    $ char ('tas105')

    voice as0102
    asumi "Parasite One, take good care of Parasite Two. If Two causes a problem, both of you will pay for it!"
    yusuke "That's not fair...sob-sob."

    $ char ('tts001')

    "This is how I started to take care of Toshibo, a.k.a. Parasite Two. I clean up his fallen hair, fix his scratches on the wall and floor, and also feed him."
    "No matter how you think about this, #1 is treated a lot more poorly than #2!"
    yusuke "Why is this happening to me... Am I that unlucky?"

    $ char ('tts002')

    voice ts0008
    toshibo "Meow!"

    $ bgfx ('sora01')

    "The curse doesn't end there."

    $ bgfx ('bg04a')
    $ char ('tas018')

    yusuke "Ohh, I'm starving...GRRR."

    voice as0103
    asumi "Same here...it's all Toshibo's fault...ohh."


    call ep_middle from _call_ep_middle_13

    $ bgm (12)
    $ cg ('e3_0201')
    $ unlock_gallery ('g4e12')

    "Our room becomes more cheerful by adding Toshibo as our new member."
    "Toshibo is close to Tomoe, but he also gets along with Marumu, too."
    "They play together as if they're old friends."
    "They sit next to each other when they eat."
    yusuke "They must be 'Birds of a feather flock together.'"
    yusuke "......!!"

    $ music_stop ()
    call effect ('SE12', ['red']) from _call_effect_30
    $ bgm (7)

    yusuke "Whoooaa!!"

    $ cg ('e3_0202')

    voice as0104
    asumi "Be quiet, Parasite One. We're still eating."
    "You can't stop screaming if you're struck with a fork in your hand."
    "Marutan...she's scary."

    $ cg ('e3_0203')

    voice to0025
    tomoe "Hmmmm...good morning, everyone."

    voice ts0009
    toshibo "Meow!"
    "Everyone follows Toshibo's lead and greets Tomoe."
    "She's not good at waking up in the morning. She always comes last to the table."

    $ cg ('e3_0212')

    "The sleepy eyed Tomoe sits at the table. Toshibo has her grab a fork."

    $ cg ('e3_0203')

    voice to0026
    tomoe "Thanks, Toshibo."

    voice ts0010
    toshibo "Mew mew!"

    voice as0105
    asumi "Toshibo is much more useful than Parasite One."

    voice ma0065a
    marumu "......(nod-nod)"
    yusuke "Don't be so cruel to me...I'm a human being, you know!? And I take care of you girls a lot! How dare you to say that I'm less than that freakin' cat!?"

    voice as0106
    asumi "Because you ARE more worthless than Toshibo. Ha ha ha!"
    yusuke "...Ohhh...ohh..."
    "I clench my fists tight."
    "That's it! I can't take their abuse anymore!"
    "I'm enraged. I stand up and yell...only I can't."
    "Because Marumu gets me from behind and gags me,"
    "...by shoving a boiled egg into my mouth."
    yusuke "Guhhhh... Mguhhh..."

    voice as0107
    asumi "...Somebody's here!"

    $ sfx ('SE10', loop=True)
    $ bgfx ('black', diss_long)

    "Asumi hurriedly stands up and holds Toshibo."
    "Then she opens up the closet and throws Toshibo into it."
    "Then Marumu...WHOOOOA!?"
    "ZRRR...DONG!"
    "Marumu powerfully throws me into the closet as well. How does she do that...!?"

    $ sfx (delay=0.5)

    yusuke "Ummm...it hurts."

    voice ts0011
    toshibo "Meow..."
    "Toshibo and I hug each other in the dark closet."
    "Then, I hear a familiar voice, which doesn't belong to any of our members."

    $ music_stop ()
    $ bgm (4)
    $ bgfx ('bg01a')
    $ char ('tyo101')

    voice yo0005
    yagami "...Good morning Asumi. May I ask you a question?"

    voice as0108
    asumi "Oh, it's you, Ms. Yagami. What's up?"

    $ char ('tyo113')

    voice yo0006
    yagami "......"
    "Indescribable silence follows."
    "I concentrate on listening to their conversation, knowing I'm the 'suspicious' male in the girls' dorm."
    "Ms. Yagami starts speaking after a while."

    $ char ('tyo102')

    voice yo0371
    yagami "Hey, girls...have you seen anything strange around here?"

    $ char ('tas133')

    voice as1280
    asumi "...Anything strange."

    $ char ('tto102')

    voice to0950
    tomoe "Could you be more specific, Ms. Yagami?"

    $ char ('tyo113')

    voice yo0372
    yagami "Something...round."

    $ char ('tas106')

    voice as1281
    asumi "...Huh?"

    $ char ('tyo102')

    "Ms. Yagami starts explaining."
    "A mysterious 'round' creature sometimes appears at Harukaze dorm recently."
    "Some girls reported that they saw a quick-moving, suspicious round object running around."
    "And their food is missing at the same time."
    "Ms. Yagami sighs."

    $ char ('tyo113')

    voice yo0373
    yagami "...So, I need to resolve this before it gets worse."

    $ char ('tyo101')

    voice yo0374
    yagami "Inform me if you see something suspicious, okay?"

    voice as1282
    asumi "S...sure."

    $ char ('tyo113')

    yusuke "......"

    $ music_stop ()
    $ char ()

    "Ms. Yagami quickly looks inside the room and leaves."
    "Everyone breathes a sigh of relief as she leaves."

    $ bgfx ('black')
    $ bgfx ('bg01a')
    $ char ('tas130')

    yusuke "...Whew. What a surprise!"

    voice as1283
    asumi "...This isn't good at all. Speaking of suspicious, round objects..."

    $ char ('tts001')

    voice ts0081
    toshibo "...Mew?"
    "Toshibo comes out of the closet after me. He and Asumi glance at one another."
    "But Tomoe cuts in between them."

    $ char ('tto113')

    voice to0951
    tomoe "...Asumi, listen to me! Toshibo isn't the kind to steal others' food! I'm telling you the truth...!"

    $ char ('tas137')

    asumi "......"

    $ char ('tma118')

    marumu "......"
    yusuke "...Oh?"
    "I don't know since when, but Asumi and Marumu are glaring at me now."

    $ char ('tas110')

    voice as1284
    asumi "You stole other people's food then."
    yusuke "How can you think like that...?"

    voice as1285
    asumi "You shameless thief! How could you do that to us!? You must be stealing our...panties as well!"
    yusuke "Which I didn't do... Waaaahhh!!"

    voice as1286
    asumi "I hate men's excuses!!"

    call effect ('SE10', ETYPE3, sound_loop=True) from _call_effect_31
    $ bgm (7)

    "Asumi starts throwing everything in the room at me."
    "Most of these items used to belong to me. They are crap."
    "Tomoe looks worried and tries to stop Asumi, but..."

    $ sfx (delay = 1.0)
    $ char ('tto113')

    voice to0952
    tomoe "H...hey, Asumi... YIKES!"

    call effect ('SE36', ETYPE1) from _call_effect_32

    "One of the items thrown by Asumi hits Tomoe."

    $ char ()

    "Seeing the friendly fire, Asumi finally stops throwing."

    $ music_stop ()
    $ char ('tas127')

    voice as1287
    asumi "Oops...sorry, Moe-Moe."
    yusuke "To...Tomoe."
    "Worried, we rush to her."
    "Tomoe rubs her head where she's been hit and slowly stands up."

    $ char ('tto107')

    voice to0953
    tomoe "Ohh, it hurts... You know what? I think Yusuke wouldn't do something like that."

    $ char ('tas133')

    voice as1288
    asumi "If you say so...but still..."
    "Then..."
    "Marumu suddenly shouts:"

    $ char ('tma101')

    voice ma0497
    marumu "...Oh."

    $ char ('tas105')

    voice as1289
    asumi "Marutan, what's wrong?"

    $ char ('tma101')

    voice ma0496
    marumu "Number two is missing."
    yusuke "Uh, you're right."

    $ char ('tto104')

    voice to0954
    tomoe "Toshibo..."

    $ bgfx ('black')

    "Parasite Two...we don't see Toshibo in the room any more."
    "He vanished all of a sudden."

    $ bgfx ('sora01')

    "A couple of days passed."
    "Toshibo hasn't come back here yet."
    "Everything is back to normal in the dorm since Toshibo left."
    "Nobody says anything...but still, I occasionally think that Toshibo was the one who caused all the trouble."
    "Tomoe must feel the same way."

    $ bgm (9)
    $ bgfx ('bg01a')
    $ char ('tto004')

    tomoe "......"
    "Does she feel responsible, or is she worrying about Toshibo..."
    "She hasn't spoken to anyone at all in the past few days. She looks so sad."

    $ char ('tas024')

    voice as1290
    asumi "...Yes, that's right!"
    yusuke "...? H...hey!!"

    $ bgfx ('black')

    "Asumi looks determined and grabs my arm."
    "Then she drags me to the door."
    "Asumi also calls for Marumu and goes out, taking the two of us with her."

    $ music_stop ()
    $ bgfx ('bg02a')
    $ bgm (5)
    $ char ('tas007')

    "Asumi declares the following outside the dorm:"

    voice as1291
    asumi "We must do something. We're going to search for Toshibo!"
    yusuke "You mean...!?"
    "She can't let Tomoe stay depressed, I guess."
    "Three of us will search for Toshibo now."
    "We might discover the truth behind all the incidents, if we find Toshibo."
    "But isn't that..."

    $ char ('tma010')

    voice ma0498
    marumu "...Asumin is a busybody."

    $ char ('tas010')

    voice as1292
    asumi "Don't tell me that! I can't let her stay like that."
    yusuke "Asumi..."
    "Yep, that's the Asumi I know."
    "She always pokes her nose into everything and messes it up."
    "In other words,"

    $ char ('tma017')

    voice ma0499
    marumu "...Troubleshooter."
    yusuke "No, it's troublemaker!"
    "I remember, she was trying to catch the panty thief when I came to this town."
    "Is she becoming more helpful...? Maybe she is."
    "But in this case..."

    menu:
        " "
        "Search for Toshibo with them.":


            yusuke "Yeah, sure. Let's go find Toshibo."
            "I think we're overreacting, but still...I want to help Tomoe in some way."

            $ char ('tas012')

            "Asumi looks at me and smiles as I think."

            voice as1294
            asumi "That's the spirit, Parasite One! You go search in the mountain. We'll search the town. Let's go, Marutan!"

            $ char ('tma011')

            voice ma0500a
            marumu "...Oh, yeah."

            $ char ('tas002')

            voice as1295
            asumi "Okay, let's go!"
            yusuke "......"

            $ char (fx=None)
            $ ev ('ea_1101')
            $ ev ()

            "She quickly assigns me and runs away."
            "Oh my. This is unfair. I feel uneasy as I see them off."

            $ F016 += 1
            $ F018 += 1
        "Make an excuse.":


            yusuke "I have something important to do..."
            "I don't need new troubles."
            "That's my honest feeling."
            "Because I'm already causing enough trouble staying in the girls' dorm."
            "I must stay subdued, you know."

            $ char ('tas001')

            "Asumi looks back at me and seems to understand my position."
            "She raises her hand high and shouts:"

            $ char ('tas002')

            voice as1293
            asumi "Marutan, Parasite One, Let's go!"

            $ char ('tma011')

            voice ma0500a
            marumu "...Yeah."
            yusuke "......"

            $ char (fx=None)
            $ ev ('ea_1101')

            "Asumi dashes away."

            $ ev ()

            "Marumu quickly follows Asumi."
            "...I'm left alone."
            yusuke "Okay, okay. You want me to go with you, right? *sob*..."
            "And so, once again, I give into the pressure and proceed. *sob*"

    call blackout from _call_blackout_75

    "I come to the mountain, which is located behind the dorm."
    "Man, this is far tougher than I thought."
    "It's steep, slippery, and filled with tons of weird vegetation and bugs..."
    "There's no doubt Asumi has malice towards me."
    "Oh, geez. This is tough."
    "I don't think the fatty Toshibo would ever come to a place like this."
    "That's right, he must be somewhere more... Ahh!?"
    "I can't believe my eyes."
    "This sight is extraordinary..."

    $ bgfx ('bg12a')
    $ char ('tts017')

    yusuke "To...Toshibo!"

    voice ts0082
    toshibo "m...mew..."
    "Toshibo just ended a furious battle and walks toward me."
    "He's scarred up everywhere and covered with dirt."
    "I see his opponent fall on the ground."
    "It's a big fat raccoon...Toshibo was fighting against this raccoon."
    "Toshibo vanished without saying anything because he wanted to catch this bad-ass raccoon."
    "This is something I concluded from my investigation: Guess what, this raccoon is the one who broke into the dorm and caused all the confusion!"
    "My, my... I find tons of panties and remains of food in this guy's nest."
    "We pack up the evidence and go back to the dorm."

    $ bgfx ('black')
    $ bgfx ('bg02b')
    $ char ('tas001')

    voice as1296
    asumi "Oh, there you are, Number One...and Toshibo!?"
    "I tell Asumi everything in front of the dorm."
    "This is how Toshibo's innocence was finally proven..."
    "And of course, I feel great."

    $ bgm (10)
    $ bgfx ('bg01b')
    $ char ('tas042')

    voice as1297
    asumi "I'm sorry, Moe-Moe. I shouldn't have suspected Toshibo even a bit."
    yusuke "Yeah...same here."
    "We sincerely apologize to Tomoe and Toshibo."
    "And they pardon us with smiles."

    $ char ('tto019')

    voice to0955
    tomoe "Thank you everyone and don't worry."

    $ char ('tts004')

    voice ts0083
    toshibo "Meow!"
    "Asumi strokes Toshibo's head."

    $ char ('tas001')

    voice as1298
    asumi "You can stay here as long as you want, Toshibo!"

    $ char ('tts004')

    voice ts0084
    toshibo "Meow meow."
    "Toshibo proved his innocence by himself."
    "And I'm a witness...am I not?"
    "We were able to settle this because Asumi forced us...AHEM...suggested us to help."
    "Helping and believing in your friends..."
    "I realize how wonderful it is to do so from this event."

    call blackout from _call_blackout_76
    $ bgfx ('sora01')

    "But the next morning..."
    "Once again, Toshibo left us without saying goodbye!"
    "There's a memo from Toshibo to Tomoe."
    "Tomoe translates the memo with a bunch of footprints."
    "\"Thank you for your hospitality.\""
    "So the memo says..."
    "I can't believe it... How can she read that!?"
    "Anyway, the bottom line is Toshibo is no longer staying with us."
    "It was too short... I thought we could become good friends."

    $ bgfx ('black')

    "Few days later,"
    "As usual, our room is very noisy in the morning."

    $ bgm (5)
    $ bgfx ('bg01a')
    $ char ('tas107')

    voice as1299
    asumi "Hey, Parasite One! Why is my sunny-side up crushed!?"
    yusuke "S...sorry, but mine is crushed too."

    $ char ('tas110')

    voice as1300
    asumi "Shut up! You messed up my beautiful morning. I'll make you pay!"
    yusuke "Oh...waaaahhh!"

    $ char ('tto128')

    voice to0956
    tomoe "Good morning...everybody."

    call effect ('SE36', ETYPE2) from _call_effect_33

    "Asumi throws a 'Super-hard French Bread' to me. However, it hits Tomoe on her face!"

    $ char ()

    "Tomoe falls on the floor as we worry about her."
    "Then, she stands up as if nothing happened."

    $ char ('tto128')

    voice to0957
    tomoe "Everyone, good morning... THUD!"

    $ char ()

    "She's knocked out cold."

    $ music_stop ()
    $ char ('tas130')

    voice as1301
    asumi "Moe-Moe!"
    "Asumi rushes to Tomoe, then a mysterious shadow suddenly appears in front of her."

    $ bgfx ('nt0304', diss_short)
    $ bgfx ('bg01a', diss_short)

    voice ts0085
    toshibo "Meow!!"

    $ char ('tts002')

    "The shadow jumps into our room from the balcony and it is... Toshibo!"
    "I don't know how it's possible for a cat, but Toshibo starts nursing Tomoe."
    yusuke "Toshibo!?"

    voice ts0086
    toshibo "Mew mew!"

    $ bgfx ('sora01')

    "With Toshibo's great care, Tomoe regains consciousness."
    "Then, we eat breakfast together again."

    $ bgm (3)
    $ bgfx ('bg01a')
    $ char ('tto016')

    voice to0958
    tomoe "See you later, Toshibo."

    $ char ('tts002')

    voice ts0087
    toshibo "Meow, mew mew!"

    $ char ('tto016')

    voice to0959
    tomoe "Yes, I know...heh heh."
    "Are they having a conversation?"
    "I'm very curious as to what they're talking about, so I ask her,"

    $ bgfx ('bg02a')
    $ char ('tto031')

    yusuke "Tomoe, what did he say?"

    voice to0960
    tomoe "He'll go wandering again, but he promised to come to my rescue whenever I'm in trouble."

    $ char ('tma008')

    voice ma0501
    marumu "...He's cool."
    "Did he...really say that?"
    "The lone wolf...no, the cat Toshibo leaves with a brisk step."
    "And so our new, indefinite roommate (cat) joined us."


    call ep_finish from _call_ep_finish_12

    $ renpy.end_replay()
    $ unlock_episode (3)
    jump episode04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

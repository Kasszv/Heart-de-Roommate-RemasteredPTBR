label episode09:

    $ Fnum = 9
    $ save_name = "Episode 9: A girl under the Moonlight"

    $ bgfx ('sora08')
    $ bgm (12)

    "The test season has come."
    "We have an achievement test once in a while, even though the Aiho School has its own educational standards."
    "So, in our room..."

    $ cg ('e3_0210')

    voice as1362
    asumi "OK! Let's start cramming for the examination!"

    voice to0999
    tomoe "I don't have to cram, I study regularly."

    $ cg ('e3_0211')

    voice as1363
    asumi "Are you kidding, Moe-Moe!? Don't you know that cramming for examinations is a big event for youth! Hey, give me the answer for number 5!"
    "We study together because of Asumi's selfish ways."
    yusuke "...Asumin, you just don't want to study alone."

    voice as1364
    asumi "Yusuke, why don't you make us some tea!"
    yusuke "Okay..."
    "I want to study for my test too... I should follow Tomoe's lead."

    voice as1365
    asumi "Marutan, are you studying? Stick to it!"

    voice ma0537
    marumu "...I don't need to study."

    voice as1366
    asumi "Why?"

    $ cg ('e3_0210')

    voice ma0538
    marumu "...I'm a genius."

    voice as1367
    asumi "OK. Moe-Moe, how about number 6?"
    "Asumi ignores Marumu."
    "Tomoe holds back a yawn and gives Asumi the answer."

    voice to1000
    tomoe "It's a... Whaaaa..."

    $ bgfx ('sora08')

    "The unfair night passes."
    "I can't go to sleep yet..."


    call ep_start from _call_ep_start_11

    $ sfx ('SE37', loop=True)

    yusuke "......?"
    "I was getting drowsy in the closet when I heard some strange noises."
    "The sounds began to move towards the front door."
    yusuke "If it's not a thief, what could it be?"
    "It must be one of my roommates."
    "I open the closet door a little, just enough to peep into the dark room."

    $ sfx (delay=0.5)
    $ bgfx ('bg01d')

    "I'm able to see images inside the dark room because I've been in a dark closet."
    "My eyes catch something."
    "I see the shadow of someone I know."
    yusuke "...It's late, where is she going?"
    "I thought about ignoring it altogether, but on second thought, it could be dangerous for a girl to be out walking in the middle of the night."
    "...Unless it's Namiki."

    $ bgfx ('bg02c')

    yusuke "Hm?"
    "Before realizing it, I'm outside the girls' dorm."
    "There's nobody around."
    "I thought I was doing well in terms of following her."
    "In an instant, the shadow turned a corner, and I lost track of her."
    "Then, I arrived here."

    $ bgfx ('sora10')

    "Dead silence... I look at the shining stars in the sky."
    "The white, full moon shines overhead."
    yusuke "Mmm... Where did Marutan go?"

    $ bgfx ('black')
    $ bgm (6)
    $ bgfx ('bg03a')
    $ char ('tna020')

    voice na0129
    namiki "Good morning, Tomo-Tomo!"

    $ char ('tto001')

    voice to0149
    tomoe "...What was that?"
    "Someone runs into us on our way to school. It's her, of course."
    "She calls herself, 'Your Shadow Leader.'"
    "Moe-Moe looks back and leans her head to the side."
    "Namiki starts to talk."

    $ char ('tna002')

    voice na0130
    namiki "I decided to call Tomoe 'Tomo-Tomo' and Marutan 'Maru-Maru.' I think they're better."
    yusuke "Huh?"

    voice na0131
    namiki "I made new nicknames for all of you. You're 'Yu-Yu,' OK!?'"
    yusuke "I don't think so!"

    $ char ('tas006')

    voice as0278
    asumi "Yeah, you can't make up nicknames for the sake of making them up!"
    "Asumi speaks up."
    "Namiki smiles at Asumi."

    $ char ('tna020')

    voice na0132
    namiki "Don't be jealous, I made a good nickname for you too!"

    $ char ('tas018')

    voice as0279
    asumi "If you call me 'Asu-Asu,' I'll kick your butt!"

    $ empat ('SE49')
    $ char ('tna019')

    voice na0133
    namiki "Oh! How did you know!?"

    $ empat ()
    $ char ('tas010')

    voice as0280
    asumi "Of course, everybody can tell! You're just repeating the beginning of the syllables!"

    $ empat ('j7')
    $ char ('tna023')

    voice na0134
    namiki "You're terrible... It took so long to come up with these nicknames... I didn't even get any sleep last night. I only wanted to make you guys happy."
    "I think she wants to do something befitting a 'Shadow Leader,' just a bit."

    $ empat ()
    $ bgm (7)
    $ vox ('na0135')

    "Namiki and Asumi start to argue again."
    "Tomoe and I decide to watch them from a few yards away."

    $ vox ('as0281')

    yusuke "Ah? Where's Marumu?"

    $ vox (delay=0.3)
    $ char ('tto001')

    voice to0150
    tomoe "Hm, where is she?"
    "We left our room together, but I don't see her now."
    "I look around trying to find her."

    $ char ('tto004')

    voice to0151
    tomoe "She goes to school ahead of us sometimes."
    yusuke "I see."

    $ music_stop ()

    "I think about last night."
    "She went somewhere last night."
    "Where did she go at that late hour?"
    "I call Namiki,"
    yusuke "Namiki!"

    $ char ('tna002')

    voice na0136
    namiki "W...what...huh...is it Yu-Yu?"
    yusuke "Please don't call me that. Anyway...did you notice anything strange last night? You were up all night, weren't you?"

    $ char ('tna001')

    voice na0137
    namiki "Hmm, I don't think so."
    yusuke "Did Marumu visit you?"

    voice na0138
    namiki "Maru-Maru? No. But of course, she's always welcome."
    "She waves to Tomoe and smiles."

    $ char ('tna002')

    voice na0139
    namiki "Tomo-Tomo! You're always welcome too, you know!? We can have a fun together."

    voice to0152
    tomoe "Ah, no thank you..."

    $ bgfx ('sora01')

    "Marumu is already in the classroom."
    "She acts as if nothing happened last night."
    "I can't stop thinking about her."

    $ sfx ('SE51')
    $ bgm (4)
    $ bgfx ('bg04a')
    $ char ('tyo001')

    voice yo0093
    yagami "...OK, everyone! Let's win the tournament next week!"
    everyone "YEEES!!!"
    yusuke "......"
    "Homeroom ends while I'm thinking about Marumu."

    $ sfx (delay=0.3)

    "Then, I notice someone standing next to me."

    $ char ('tyo015')

    voice yo0094
    yagami "Can I talk to you?"
    yusuke "Ms. Yagami."

    $ bgfx ('bg05a')
    $ char ('tyo002')

    voice yo0095
    yagami "Your mind was wandering during homeroom. What's wrong?"
    yusuke "I...ah..."

    voice yo0096
    yagami "Is something wrong? Did someone find out about you?"
    yusuke "N...no, nobody...I don't think."
    "She worries about me."
    "She's a good teacher."
    "She pats my shoulder lightly and smiles."

    $ char ('tyo007')

    voice yo0097
    yagami "Well, if you don't have any problems, that's good. Be ready for the tournament!"
    yusuke "Alright..."

    $ char ()

    "Ms. Yagami happily walks away."
    "But...what do I have to do for the tournament?"

    $ music_stop ()
    $ bgfx ('bg04a')
    $ char ('tko001')

    kosuke "It's a softball tournament!"
    yusuke "I see."
    "A softball tournament... I know many schools have athletic meets during the year."
    "But this school has a lot of tournaments like 'tug of war,' 'once-every-four-years soccer tournament,' 'cooking,' etc., etc..."
    "It's one of the trustees idea. All these tournaments are inter-class. He thinks that way, students will naturally learn to have cooperative spirits and friendship."
    "I think the way he thinks is old fashioned."
    "This school is different from others."
    "Especially the students."
    "They're much more energetic than students in Tokyo."
    yusuke "Maybe they're just slaphappy?"
    "But I think they're special."
    "And I know the most special one."
    "She's always on my mind."

    $ bgfx ('black')
    $ sfx ('SE44')

    "I knock on the door."

    $ sfx ()

    "I never thought it proper to visit a lady at this hour...but she invited me, so I didn't have a choice."
    "Ms. Yagami called me after class."


    $ bgm (4)
    $ bgfx ('bg10c')
    $ char ('tyo107')

    voice yo0376
    yagami "Hi, Yusuke!"
    "She welcomes me."
    "'A regular report meeting.'"
    "I promised her this."
    "With this condition, she keeps my secret that I'm living in Harukaze Dorm, even though I'm a male."

    $ char ('tyo101')

    "I tell her what's happened lately."
    "Well, most of them are stupid stories."
    "After I finish my story, she smiles at me and says,"

    $ char ('tyo107')

    voice yo0377
    yagami "I see. You enjoy living there."
    yusuke "Ah, maybe..."
    "She continues,"

    $ char ('tyo101')

    voice yo0378
    yagami "By the way, does anybody know about your secret yet?"
    yusuke "I don't think so."

    voice yo0379
    yagami "Hm, you are lucky...chuckle...chuckle."
    "I agree with her."
    "Maybe my life is just based on miracles."
    "Next, she curiously asks me,"

    $ char ('tyo102')

    voice yo0380
    yagami "Don't you have problems living with those pretty girls?"
    yusuke "No, I don't have any problems."

    $ char ('tyo119')

    voice yo0381
    yagami "You may fall in love with all the girls."
    yusuke "Ms. Yagami!!!"
    "I sense her teasing me."
    "Is she having fun with me?"
    "Is she the same as the other girls?"
    "Oh well, my life is okay as long as she keeps my secret."
    "She seems satisfied with my report."

    $ music_stop ()
    $ bgfx ('bg03c')
    $ char ('tyo101')

    voice yo0382
    yagami "See you later! You can talk to me whenever you have a problem, okay?"
    yusuke "Yes..."
    "I think she might make fun of me if I visit her again."
    "Whew, I'm tired. I'd better go to sleep."

    $ bgfx ('black')

    yusuke "Um...mm...what!?"
    "I'm awakened by noises."
    "It's a small sound, but it wakes me up."
    "My sense of hearing is really keen lately."
    "That's because I've gotten used to the idea of getting up in case Marumu goes out in the middle of the night again."
    yusuke "I may come closer to solving Marutan's riddle tonight!"
    "I quickly get ready."
    "I won't lose her this time!"

    $ bgm (2)
    $ bgfx ('bg13c')

    yusuke "Hmm...willpower doesn't work all the time."
    "I lose track of her again."
    "It's almost in the same place as the last time."
    "I feel stupid."
    yusuke "Idiot! I'm such an idiot!"

    voice hs0008
    unknown "Is someone there?"
    yusuke "Oops!"
    "A girl's voice."
    "It sounds familiar."
    "But I can't remember who it is."
    "Huh...what is she doing?"
    yusuke "Hmm...I guess I feel the same way."
    "Damn, I don't have time to think!"
    "I realize I'm wearing guys' clothes."
    "If she sees me close-up, she'll be able to tell that I'm not a girl."
    "I could be caught by the police, and they may think that I'm a pervert!"

    voice hs0009
    girl "...Is someone there? Please answer me."
    yusuke "......"
    "I'd like to answer her, but..."
    "I step back quietly."

    voice hs0010
    girl "I'm scared...sob, sob..."
    yusuke "Don't cry, please."
    "The girl starts to cry."
    "I'm so stupid."
    "Even though a girl is crying, I shouldn't... Heh!"

    voice hs0011
    girl "Someone is there, right?"
    "She walks towards me."
    "Oh no! She'll see me!"
    "I've been patient with my miserable life, but it'll all be for naught!"
    yusuke "I've got to do something... Ahhhh!"

    $ sfx ('SE01')
    $ bgm (7)

    "I'm in a panic."
    "I run away, and as I run, I bump into things I can't see."
    "I know it's impossible to run away in this small space, but... OH!?"

    $ sfx (delay=0.3)
    $ bgfx ('black')

    voice hs0012
    girl "Nobody... Was it a ghost or what? Oh no...I'm scared...sob!"
    "A girl cries."

    $ vox ('hs0013')

    yusuke "Is she...?"
    "Miss Hisame? The cool girl?"
    "I want to find out."
    "But I can't."
    "I continue to hide."
    "I'm just about 3 feet away from her."
    "There's a thick board between us."
    "I'm hiding behind it."

    $ vox (delay=0.3)
    $ music_stop ()

    yusuke "Ouch... What's this?"
    "Well, anyway. I can hide for now."
    "A revolving door under the steps? Is this a ninja house or something?"
    "Who made this and for what purpose?"
    "Is this the place to play hide-and-seek?"
    yusuke "Probably not..."
    "I find something important in the dark."
    "Steps which lead upward."
    "I've discovered a new path into the Harukaze Dorm."
    "It means... Yes! There's something new!"
    yusuke "When I go up the stairs, perhaps I'll find a secret room! ...No, this is not a game..."

    $ cg ('em_0101', pos=[ALIGN(0.0, 0.0)])

    "What was I thinking? There is no secret room."
    "Instead, I find a beautiful, night sky with a bright, full moon."

    call cg_slide (picture='em_0101', tm=3.0, kind='v', start=0.0, end=1.0, cls=diss_fast) from _call_cg_slide_15

    "And...the person I was looking for."
    yusuke "I seem to have lost her because of the secret door."
    "Did Marutan make this secret path?"
    "Or did she find it accidentally?"
    "I have no idea."
    "Why don't I ask her?"
    "She's looking at the full moon."

    menu:
        " "
        "Get close to her quietly.":


            "I cross the roof slowly."
            "I don't know why I'm walking on my tip-toes."
            "I'm not doing anything wrong... Oops, she notices me!"

            $ cg ('em_0102')

            yusuke "I...I'm sorry! I didn't follow you! ...WAAAAAAA!"

            $ bgfx ('black')
            call effect ('SE10', ETYPE3) from _call_effect_28

            "I slip and fall down, down, down..."
            "I hit the hard, cold ground."
        "Talk to her.":


            yusuke "...Marumu?"
            "I call her."
            "But she... Ah!?"

            $ cg ('em_0102')

            yusuke "H...heeee!!!"

            $ bgfx ('black')
            call effect ('SE10', ETYPE3) from _call_effect_29

            "Surprised, I slip and fall down, down, down..."
            "I hit the hard, cold ground."

            $ F018 += 1


    call ep_middle from _call_ep_middle_11

    $ bgfx ('bg01a')
    $ bgm (6)

    yusuke "Ouch...kuh..."

    $ char ('tts001')

    voice ts0021
    toshibo "MEOW!"
    "Toshibo takes good care of me."
    "What a good cat!"
    "Every family needs this kind of cat. Of course, it'd be better if he didn't eat so much..."
    "Painfully, I move around behind the bush."
    "But the dorm is in a panic already because I made too much noise."
    "Is it a thief or a pervert? The anxious mood in the air holds the Harukaze Dorm till morning..."
    "Toshibo went to get help, brought Moe-Moe, and I was rescued from the edge of death (exaggeration)."

    $ char ('tto031')

    voice to0153
    tomoe "You'd better rest today, Yusuke. Don't move around too much."

    $ char ('tas013')

    voice as0282
    asumi "She's right! If you move around, you may be mistaken for a thief or a pervert. Heh heh heh!"

    $ char ('tma001')

    marumu "......"

    $ char ()

    "I skipped class today. The three girls went off to school."
    "Even if someone told me to move, I couldn't."

    $ char ('tts002')

    voice ts0022
    toshibo "Meow, meow!"
    yusuke "Thanks Toshibo."

    call blackout from _call_blackout_64

    "Because of Toshibo or some miraculous power, I'm able to move by evening."
    "I can go to school tomorrow."

    $ bgfx ('bg01b')

    yusuke "I think I can take a walk."

    $ char ('tts002')

    voice ts0023
    toshibo "Meow, meow, meow!!"
    yusuke "OK, OK. I'll just rest today."

    $ char ()

    "I lie down and think."
    "Thinking about last night."

    $ bgfx ('black')
    $ cg ('em_0101', pos=[ALIGN(0.0, 1.0)])

    "Marutan... She was looking at the moon alone."

    $ cg ('em_0102', pos=[ALIGN(0.0, 1.0)])

    "I remember the expression on her face when she suddenly looked back."

    $ bgfx ('black')
    $ bgfx ('bg01b')

    yusuke "She looked sad."
    "I realize that I don't know anything about Marutan."
    "I kind of understand Asumin and Moe-Moe now."
    "But Marutan... I only know her as 'the mysterious girl.'"
    "It seems impossible to understand her."
    "But maybe Asumin and Moe-Moe know her better..."

    $ bgfx ('black')
    $ bgfx ('sora01')

    "A quiet holiday."
    "Marumu has been out since early morning."
    "I wonder where she went, but I'm even more curious about her."
    "Since she is out, today is the best day to ask them."

    $ bgm (5)
    $ bgfx ('bg01a')

    yusuke "Asumin, can I ask you something?"

    $ char ('tas144')

    voice as0283
    asumi "What is it? I'm busy!"
    "Asumi answers while holding a lot of thick books."
    "They're not magazines."
    "Does she read those kinds of books?"
    "'The Key to Becoming a Good Boss 101.'"
    "'Those Who Can Lead, Those Who May Lead, And Those Who Will Not.'"
    "'Leaders of the Last Century: The Legendary Leaders.'"
    yusuke "What are you reading, Asumin?"

    voice as0284
    asumi "These books are exactly what I need."
    yusuke "I think you'd better study your major... Well, but reading books is good anyway..."
    "Asumin puts the books on a table and notices that I'm exhausted."

    $ char ('tas105')

    voice as0285
    asumi "A leader should listen to followers, so tell me."
    yusuke "It's not a big deal..."
    "I ask Asumin."
    "She hears me out and then tells me,"

    call blackout from _call_blackout_65
    $ bgfx ('sora09')

    "It's a sad story."

    $ bgm (8)

    "The moon brings her memories back."
    "She longs for her home, somewhere faraway."
    "I don't know where she came from. I'm not sure, but I think she's from some very distant place."
    "Maybe her 'parents from the moon' abandoned her."
    "She was the result of an illicit love affair, or they abandoned her to save food..."
    "Or they sent her to Earth to learn about human life..."
    "Whatever the reason, she's homesick."
    "Whenever she feels sad, she goes up on the roof..."

    call blackout from _call_blackout_66
    $ bgm (5)
    $ bgfx ('bg01a')
    $ char ('tas115')

    voice as0286
    asumi "...In addition, her hair ornament proves she's the princess from the moon."
    yusuke "What a liar! You made that story up."

    voice as0287
    asumi "Don't you trust your leader?"
    yusuke "It has nothing to do with leadership! Who would believe that story, anyway!?"

    $ char ('tas105')

    voice as0288
    asumi "So you can't believe it?"
    yusuke "Of course not!"
    "I've wasted my time."
    "I walk away miffed. Then Asumi says,"

    $ char ('tas106')

    voice as0289
    asumi "Hey, Yusuke! Wait!"
    yusuke "Why, will you tell me something better?"

    $ char ('tas112')

    voice as0290
    asumi "No. Tell me where the secret door is. It sounds fun!"
    yusuke "...Yeah, yeah."
    "I'd better leave here as soon as possible."

    call blackout from _call_blackout_67
    $ bgfx ('bg02a')

    yusuke "Moe-Moe said she's going to visit her parents."
    "I know where it is. It's a Japanese-style hotel in a hot spring resort."
    "Even though I know where it is, I don't know if it's a good idea to visit her."

    $ bgm (3)
    $ bgfx ('bg16a')

    yusuke "I came anyway..."

    voice ta0007
    tomomi "Oh, welcome to our hotel!"
    "Suddenly, someone talks to me from behind."
    "It's Tomoe's lovely sister. She sounds as if she knew I was coming."

    $ char ('ttm001')

    voice ta0008
    tomomi "Tomoe is taking a bath right now. She loves the hot springs. Would you like to join her?"
    yusuke "Ah! N...no! But thanks."

    $ char ()

    "What a fascinating idea! I was almost going to join her."
    "But Moe-Moe would hate me if I did."
    yusuke "NO! I have to have a strong mind. Of course, it'd be wonderful if I could take a bath with her."

    voice to0154
    tomoe "...Take a bath with her?"
    yusuke "It would be heaven..."
    tomoe "......"
    yusuke "Tomoe?"

    $ char ('tto234')

    voice to0155
    tomoe "...Yes."

    $ empat ('j5')
    call blackout (True) from _call_blackout_68

    "This is bad."
    "Why didn't I stay in the girls' dorm and wait for Tomoe!"
    "That way, she wouldn't hate me!"

    $ empat ()
    $ bgm (9)
    $ bgfx ('bg03b')
    $ char ('tto202')

    yusuke "......"

    voice to0156
    tomoe "Yusuke."
    "I'm on my way back."
    "The kind Tomoe talks to me."
    "I'm so embarrassed, I don't know what to say."
    "Tomoe continues to talk to me,"

    voice to0157
    tomoe "Yusuke..."
    yusuke "Don't talk to me, I'm terrible..."

    $ char ('tto201')

    voice to0158
    tomoe "Maybe you are 'terrible,' but cheer up."
    yusuke "That's nice, Tomoe."

    $ music_stop ()

    "I laugh."
    "As she looks at me, she smiles."

    $ bgm (3)
    $ char ('tto210')

    voice to0159
    tomoe "Good. You smiled. I was worried about you."
    yusuke "I could get hurt from what you said, you know? Ha ha ha."
    "Tomoe's nice, even though she has a sharp tongue."
    "Her lovely smile... NO! Don't get aroused, Yusuke!"
    "If I give her that idea, she won't ever forgive me."
    "Besides, I came here to ask her something."
    yusuke "Tomoe."

    $ char ('tto201')

    voice to0160
    tomoe "Yes?"
    "Tomoe calmly responds to me."
    "She looks sad."

    call blackout from _call_blackout_69
    $ bgm (9)
    $ bgfx ('sora09')

    "The moon spurs her memories."
    "Her unforgettable, sad memories..."
    "She was always alone when she was a child."
    "She's no good at expressing herself."
    "She could only watch the other kids play from outside of the park."
    "One day, a boy talked to her."
    "She'd never seen him around before. He smiled and told her,"
    "'Let's play together, OK?'"
    "Since then, he came to her everyday."
    "They had a wonderful time."
    "She was so happy."
    "But one night, he visited her."
    "And he said, 'I'm sorry, I have to go.'"
    "Tears filled her eyes. When she wiped her tears away, he was gone."
    "It was as if he had disappeared into the moonlight."
    "It was a beautiful moon."
    "The friend of the lonely girl. He might be from the moon..."

    call blackout from _call_blackout_70
    $ bgfx ('bg03b', diss_long)
    $ char ('tto207')

    voice to0161
    tomoe "Ohh...sob!"
    yusuke "Are you crying, Tomoe?"
    "Tomoe's eyes are wet, but I don't know about that story."
    "I think it's 120%% fiction."
    yusuke "Tomoe, the story is..."

    voice to0162
    tomoe "When Asumi told me the story, I couldn't stop crying."
    "As she tells me, I clearly understand."
    "I think tenderly of Tomoe; she's so pure."
    "Now, I have no way of finding out the truth."
    "I'd better ask Marumu."

    $ bgfx ('sora05')
    $ vox ('to0163')

    "I become determined while I'm comforting the crying Tomoe."

    $ vox (delay=0.3)
    $ bgfx ('black')

    yusuke "You're here, Marutan."
    marumu "......"
    yusuke "Can I sit next to you?"

    voice ma0065a
    marumu "......(nod)"

    call cg_slide (picture='em_0101', tm=1.2, kind='v', start=0.0, end=1.0, cls=diss_fast) from _call_cg_slide_16

    "She nods without looking back."
    "I sit quietly as I look up with her."
    "The phosphorous globe is in the sky."
    "Looking at it, I feel lonely... Is it because of her sad expression?"

    menu:
        " "
        "Talk to her.":


            "The words come out of my mouth."
            yusuke "Marutan, are you sad?"
            marumu "......"
            yusuke "You've been acting weird."
            marumu "......"
            "Marumu doesn't say anything."
            "Maybe I shouldn't have asked her, but I can't take it back now."
            yusuke "You leave the room in the middle of the night to look at the moon alone... I'm kind of worried about you."

            voice ma0061
            marumu "Why do you worry about me?"
            yusuke "B...because I'm your roommate."
            marumu "......"
            yusuke "...Ohh!?"

            $ bgm (14)
            $ cg ('em_0102', pos=[ALIGN(0.0, 1.0)])

            "She gives me an answer without saying a word."
            "She flings herself into my arms."
            "Well, perhaps she's just tired."
            "I feel her body temperature."
            "Her defenseless act makes me feel like she trusts me."
            yusuke "M...Marumu..."

            voice ma0062
            marumu "Thank you for your concern."
            yusuke "Y...you're welcome."
            "We bow to each other."
            "I still don't understand her."
            "Even though I've spent time with her under the night sky,"
            "The mystery remains."
            "I can't deny the 'moon princess' story 100%% tonight."
            "But now, I think it's okay just the way that it is."
            "Because she is a special girl."
            yusuke "...Actually, I still want to know."

            $ F018 += 1
        "Remain silent.":


            "I don't know what to say to her."
            "I don't know what's on her mind."
            yusuke "......"
            marumu "......"
            "Only the stars illuminate the night sky."
            "We remain silent."
            "An interesting moment..."
            marumu "......"
            "After a while, Marumu quietly stands up,"
            "to return to our dorm room."
            "I'm alone on the roof."
            yusuke "I feel kind of lonely."

            $ bgm (13)

            "I didn't get any answers."
            "Why does she look at the moon alone?"
            "Why does she look so sad?"
            "But now, I think it's okay just the way that it is."
            "She's special, anyway."


    call ep_finish from _call_ep_finish_10

    $ renpy.end_replay()
    $ unlock_episode (9)
    $ unlock_gallery ('g2e8')
    jump episode10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

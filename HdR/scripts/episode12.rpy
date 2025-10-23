label episode12:

    $ Fnum = 12
    $ save_name = "Episode 12: Shaking Heart - Part 1"

    $ bgm (6)
    $ bgfx ('bg13a')
    $ char ('tfu001')

    voice fu0011
    midori "Umm..."
    yusuke "...Excuse me?"

    voice fu0012
    midori "Ummmm."
    yusuke "Can you move out of my way, please?"
    "I haven't slept too well lately."
    "I'm tired, I overslept this morning."
    "I have to go to school alone. On the way, I run into this girl."
    "She's staring at me for a while and tells me in a soft voice,"

    voice fu0013
    midori "I see that you're having trouble with women."
    yusuke "Excuse me?"

    voice fu0014
    midori "Your physiognomy indicates that you'll have trouble with women."
    yusuke "Huh!? Oh no... (I already have enough trouble with women!)"
    "I don't know how she can see that."
    "But I don't think she's just taking a guess."

    voice fu0015
    midori "But... Hmm."
    yusuke "What are you thinking?"

    voice fu0016
    midori "It's weird because you're a girl. Usually, this problem is for guys."
    yusuke "OHH! I'll be late!"

    $ bgm (5)
    $ bgfx ('black')
    $ sfx ('SE13', loop=True)

    "I quickly run away."
    "I think she has powers of observation."
    "She may find out my secret if she looks at me any longer."


    call ep_start from _call_ep_start_9

    $ bgfx ('bg04a')
    $ char ('tko001')
    $ bgm (5)

    kosuke "Oh, good morning!"
    yusuke "Hah, hah... Good morning."
    "...Phew, I made it."
    "But I don't see the math teacher, Mr. Ogata."
    "That's why the class is still noisy."

    $ music_stop ()

    "When I catch my breath, Kosuke asks me,"

    $ bgm (6)

    kosuke "What's your astrological sign?"
    yusuke "Are you looking at the horoscopes again? You're weird, Kosuke."
    "He likes to read the horoscopes in magazines."
    "And he always asks me the same question."
    "The horoscope's never right."
    "I tell him my astrological sign anyway. Kosuke starts to read."
    "He remains silent for a while, and then he suddenly looks up."

    $ char ('tko002')

    kosuke "Did you kiss someone this week?"
    yusuke "A kiss, hmm... A KISS!?"
    "All my classmates are looking at me because I said it louder."
    "Asumi, Tomoe, and Marumu look at me also."
    "I grab Kosuke's head and drag him out to the hallway."

    $ bgm (7)
    $ bgfx ('bg05a')
    $ char ('tko001')

    yusuke "Don't ask me such questions, Kosuke!"
    kosuke "Because! Look at this."
    "He shows me the horoscope."
    "And he points at it. It says,"
    "Your love energy this week: 122%%"
    "'Your love energy is high now!! You'll fall in love with the person you kissed during the week! Hit ratio: 98%%'"
    "A '122%%?' I don't know where the number came from. And how can you trust the 'hit ratio?'"
    "Besides, the horoscope says scary things."
    "I'll just ignore it as usual."
    "But..."

    $ char ('tko002')

    kosuke "If you kiss someone during the week, you can fall in love with the person! I envy you."
    yusuke "......"

    $ char ('tko001')

    kosuke "Why don't you say something? Like 'don't be so silly,' or 'it's ridiculous, I don't believe it.'"
    yusuke "Of course, I don't believe it..."
    "Namiki and Ms. Yagami."
    "If the horoscope is true, I have two people I could be in love with."
    "I think I'm quite out of character for love!"
    yusuke "I don't know, what should I do, Kosuke?"

    $ char ('tko003')

    kosuke "What should you do? Umm."
    "I think about it quite seriously, and so does Kosuke."
    "Aren't we even aware that class has begun? Mr. Ogata really gets mad at the two of us."

    call blackout from _call_blackout_46
    $ bgfx ('bg04a')
    $ char ('tko001')
    $ bgm (6)

    kosuke "Can you imagine if the things that horoscope says came true..."
    yusuke "I don't think so..."
    "I say it in a soft voice without much confidence."
    "Kosuke stares at me with envy."

    $ char ('tko002')

    kosuke "If I were you, I'd kiss Tomoe..."
    yusuke "...What?"
    "Did I hear him right or is there something wrong with my ears?"
    "I think Kosuke said..."

    menu:
        " "
        "Ask him.":


            $ music_stop ()

            yusuke "Did you say Tomoe?"
            kosuke "Oops, did you hear?"
            yusuke "Yes."
            "He turns red and looks down, and then he whispers,"
            kosuke "Tomoe's very good. Don't you think so?"
            yusuke "Yeah..."

            $ char ('tko001')

            kosuke "Aren't you interested in her?"
            yusuke "I...am not..."
            kosuke "But you did cheer her up at the softball game."
            yusuke "Only because she's my classmate. That's all."
            "I start thinking about Tomoe as I talk about her with Kosuke."
            "I cast a side glance at her."
            "Her face, and...her lips."

            $ char ('tko002')

            kosuke "You won't kiss her?"
            yusuke "Huh?"
            kosuke "You won't kiss Tomoe, will you?"
            yusuke "No! I won't do that. I don't care about...her."
            kosuke "Good, I already have enough rivals over her."
            yusuke "Is that right?"
            kosuke "Yeah! She's very popular among enthusiasts."
            yusuke "Among enthusiasts..."
            "I kind of understand."

            $ bgfx ('black')

            "I've got an idea!"

            $ bgm (6)
            $ bgfx ('bg03a')

            yusuke "I've been thinking about the fact that Marutan reminds me of something."

            $ char ('tas005')

            voice as1390
            asumi "You see? She looks like a stag beetle! Ha ha ha!"

            $ char ('tma007')

            voice ma0541
            marumu "Beetle, beetle!"
            yusuke "No, I think she looks like a Martian."

            $ char ('tma008')

            voice ma0542
            marumu "Quack, quack, quack."

            $ char ('tas018')

            voice as1391
            asumi "...What is it?"

            $ char ('tto001')

            voice to1006
            tomoe "I think she's more like a crawfish."
            yusuke "Hmm, you may be right about that."

            $ char ('tas011')

            voice as1392
            asumi "What are you guys talking about?"

            call blackout from _call_blackout_47
            $ bgfx ('bg04a')
            $ char ('tko002')

            "I don't know why, but I don't feel good about those enthusiasts."
            "How would they know about Tomoe? They're only observing her."
            "They look at her simply for entertainment. They can't love her!"

            $ char ('tko003')

            kosuke "Yusuke, you look mad."
            yusuke "Really? Ha ha ha!"

            call blackout from _call_blackout_48

            yusuke "Hmm."
            "I may be jealous."
            "Jealous of Kosuke and the others."

            $ F017 += 1
        "Don't ask him.":




            "Forget about it."
            "There're some things I shouldn't get involved in."
            "Especially relationships."
            "I don't know if Kosuke was telling me that he loves Tomoe or not."
            "Do I fight with him?"
            "Or do I give up Tomoe to Kosuke?"
            yusuke "What am I thinking about?"
            "Kosuke's talking about something else, but it doesn't even reach my ears."

            call blackout from _call_blackout_49

    $ bgm (13)
    $ bgfx ('bg07a')

    yusuke "Do I love her?"
    "I don't dislike her, that's true."
    "And I like her, that's true also."
    "But it's not always the case that 'Like = Love.'"
    yusuke "I feel like Namiki's controlling me."
    "'Don't you think you'd be happy if Moe-Moe were your girlfriend?'"
    yusuke "Perhaps I'd be happy."
    "Even if I do think so, I won't take any action."
    "But it's me. There's nothing I can do."
    yusuke "Well, there's no point in thinking about it. Lunch break will be over soon... Um?"

    $ music_stop ()

    "I hear a familiar voice."
    "It's not sudden."
    "I was thinking so deeply, I didn't even notice until now."
    yusuke "Is that Asumi? OH!"

    $ char ('tas001')

    "Yes. It's Asumi."
    "She's not alone."

    $ chars ('tas001', 'tmi001')

    yusuke "He's a student from the next class!"
    "Yugo Misaki."
    "Many girls often talk about him."
    "I remember my class lost to his class in the softball game. And he played an active part."
    "Girls would easily fall in love with him."
    "I can see his expressionless face."
    "But Asumi looks happy next to him."
    "A cool boy with a fine girlfriend."
    "Everybody would think so."
    yusuke "Why does she look so happy!? ...Ah!"
    "Am I jealous?"
    "Again, with Asumi, it's not 'Like = Love.'"
    yusuke "Or am I just fickle?"
    "Someone walks in front of me. It's Misaki."
    misaki "......"
    yusuke "......!"
    "I think he's nice looking. I'm a bit biased, though."
    "God is unfair!"

    $ chars ('tas001', 'tmi001')

    voice as0344
    asumi "Hey, Yusuke!"
    yusuke "(Damn, she found me.)"
    "This situation."
    "I was tailing her because I care about her. And then, I see Misaki and her having a secret meeting."
    "I already made up a story in my mind."
    "Does Asumi think so?"
    "She stares at me and smiles."

    $ char ('tas002')

    voice as0345
    asumi "Oh, Yusuke! Were you tailing me because you care about this pretty Asumi?"
    yusuke "Don't be silly! Which part of you is pretty!?"
    "...Her smiling face."
    "I can't tell her honestly. Asumi's usual self would knock my block off..."

    $ char ('tas012')

    voice as0346
    asumi "Oh, I'm lost. You're prettier than me when you change...heh heh heh."
    yusuke "You act weird."

    voice as0347
    asumi "Heh heh! It's okay. See you later, pretty Yusuke!"

    $ char ()

    "She leaves, but her laugh echoes in my ears."
    "I'm vexed."
    "Really vexed."

    $ bgfx ('black')

    "I can't get it out of my mind."
    "About the relationship between Asumi and him."

    $ bgfx ('bg11a')

    yusuke "I'm feeling kind of strange today...sob!"

    voice na0180
    namiki "Hi, Yusuke!"
    "I freeze as soon as I hear the voice."
    "Because she's the one who puts me in this situation."

    $ char ('tna001')

    voice na0181
    namiki "Yusuke, are you trying to avoid me?"
    yusuke "No, I'm not."

    voice na0182
    namiki "Okay. By the way, did you practice the lesson I gave you?"
    yusuke "Practice?"

    $ bgm (7)

    "It reminds me of the night she gave me 'THE Lesson.'"

    $ sfx ('SE13', loop=True)

    "I'm in a panic, so I just run away."

    $ char ('tna018')

    voice na0183
    namiki "Heh heh heh! You're so naive."

    $ sfx (delay=0.5)
    $ bgfx ('black')
    $ bgfx ('bg05a')

    yusuke "Whew, whew, whew... I've fled this far, so I should be safe now... WAAH!"

    $ char ('tyo004')

    voice yo0126
    yagami "Yikes! Don't run in the hallway...oh!"
    "It's Ms. Yagami."

    $ char ('tyo020')

    "When our gazes meet, she turns red."
    "Perhaps I do too."

    voice yo0127
    yagami "Yusuke, about the other day..."
    yusuke "I...I don't really care about that! It was just an accident!"

    $ char ('tyo019')

    voice yo0128
    yagami "Really...thank you."
    "We're both uncomfortable."
    "She smiles and tells me,"

    $ char ('tyo002')

    voice yo0129
    yagami "You can come talk to me anytime. Don't hesitate..."
    yusuke "Thank you. I have to go, so see you later."

    $ bgfx ('sora01')

    "I leave quickly."
    "Otherwise, I'll tell her everything."
    "Too many things are going on. I can't handle all of it anymore... I feel like I'm drowning in a bog."
    "I feel like I'll never find peace at this school."

    $ music_stop ()
    $ bgfx ('bg05b')

    yusuke "...Phew, I want to leave now."

    $ bgfx ('black')

    voice to0190
    unknown "...Who's that?" (voice_tag='v_tomoe')
    "It's a classic way to call when you blindfold someone."
    "But my mind was somewhere else. I didn't pay attention to the voice."
    yusuke "Hmm, Marutan's not this tall."

    voice to0191
    unknown "He he he! Can't you tell?" (voice_tag='v_tomoe')
    "The girl laughs and presses her body against me."
    "Instantly, I know who it is."

    menu:
        " "
        "It's Asumin!!":


            yusuke "Asumin?"

            $ bgfx ('bg05b')
            $ char ('tto004')

            tomoe "......"
            "I look back and find Tomoe instead of Asumi."
            "I notice that Asumi's breasts are one size smaller than Tomoe's."
            "Tomoe's breasts are bigger. They're nice and soft."

            $ F016 += 1
        "It's Moe-Moe!!":


            yusuke "Tomoe?"

            voice to0192
            tomoe "You got it!"

            $ bgfx ('bg05b')
            $ char ('tto019')

            "I look back and see Tomoe's bashful face."
            "She's pretty, but I feel she's even prettier than usual."
            "Her long, shiny black hair and her big breasts...everything about her makes me attracted to her."

            $ F017 += 1
        "It's Marutan!??":


            yusuke "Marutan?"

            $ bgfx ('bg05b')
            $ char ('tto004')

            tomoe "......"
            "I look back and find Tomoe instead of Marumu."
            "I notice that Marumu's breasts are much smaller than Tomoe's. How could I make that mistake!?"
            "I'm embarrassed at my inexperience."
            "Tomoe's breasts are big, nice, and soft..."

            $ F018 += 1

    $ bgm (3)

    yusuke "(It's not a good idea to be with her alone. I'd better leave before I get excited.)"

    $ char ('tto031')

    voice to0193
    tomoe "Heave-ho! OK, see you later, Yusuke."

    $ char ()

    "Tomoe takes a big pile of books from the floor and heads to the library."
    "She stopped to blindfold me, even though she had to put all the books down."
    "I think...she's cute, very cute!"
    yusuke "Do you need some help?"

    $ char ('tto025')

    voice to0194
    tomoe "...Thank you!"
    "She looks back and smiles."
    "A beautiful smile. Anyone would fall for that smile."


    call ep_middle from _call_ep_middle_8

    $ cg ('sde_0104')
    $ bgm (04)

    yusuke "Don't worry... I'm supporting the ladder, and I'm not looking up."

    $ cg ('sde_0102')

    voice to0195
    tomoe "Yes, I know. Thank you."
    "We both say unnecessary things, that's just us."
    "I think we are similar in a way."
    "I used to just imagine having a relationship with Tomoe, but now, it's slowly becoming real in my mind."
    yusuke "Yes, I'd be happy... OHH!"

    $ cg ('sde_0108')
    $ cg ('sde_0101')

    voice to0196
    tomoe "WOW! Yusuke, please hold it tight."
    yusuke "Sorry, I'm sorry!"
    "While I was thinking, I took my hands off the ladder."
    "I really feel sorry and put the happy images deep inside of me."
    "Later, when I calm down, I'll realize that it was just a fantasy."
    "We are good for each other, but only because we're roommates."

    voice to0197
    tomoe "Ah...Yusuke."
    yusuke "Yes? Don't worry, I'm holding it."

    voice to0198
    tomoe "No, I want to ask you something else."
    yusuke "I see. I'll answer anything I can."

    $ cg ('sde_0106')

    tomoe "......"
    "She seems to have trouble asking me."
    "Her hands stop also."
    "Finally, she asks me in a soft voice,"

    $ music_stop ()
    $ cg ('sde_0101')

    voice to0199
    tomoe "What do you think of Asumi?"
    yusuke "W...why do you ask me about her?"

    voice to0200
    tomoe "Why? I kind of...care about it."
    yusuke "What do I think of Asumi? Are you asking me if I like her?"

    $ cg ('sde_0106')

    voice to0201
    tomoe "I think you like her."
    "She sounds depressed."
    "And she has already made up her mind."
    "She's like me. We don't need to be this similar."

    menu:
        " "
        "Explain to her.":


            yusuke "Tomoe, you must be misunderstanding! Asumi and I are...!!"

            $ cg ('sde_0101')

            voice to0202
            tomoe "I've been assuming that you stay in our dorm because you like her."
            "I look up at Tomoe and accidentally see her panties again."
            "And then she notices it."

            $ cg ('sde_0107')

            "I'm in a panic. I unintentionally take my hands off the ladder."

            $ F017 += 1
        "Don't answer.":


            yusuke "......"
            tomoe "......"
            "I don't know what to say."

            $ cg ('sde_0101')

            "She looks at me while I remain silent."
            "Our eyes meet. An uncomfortable atmosphere surrounds us."
            "I move my eyes away."
            "Then, I see them again."
            yusuke "They're white again today..."

            $ cg ('sde_0104')

            tomoe "......!?"
            "Oops. I saw inside her skirt again."
            "I'm in a panic. I inadvertently shake the ladder."

    $ bgm (7)
    $ cg ('sde_0108')

    "Everything above me falls on me: some books and Tomoe with her bright, red cheeks."

    $ bgfx ('black', cls=True)
    call effect ('SE40', ETYPE3, sound_loop=True) from _call_effect_20

    yusuke "(Are you all right, Tomoe?)"
    "I want to say it right away."
    "But I can't."
    "Because my mouth is shut tight."

    $ sfx (delay=1.0)

    "History repeats itself."
    "I hope I'm not in trouble again."

    $ music_stop ()

    "I slowly open my eyes."
    "I don't see the white panties."
    "Just wide, open eyes."
    "I don't realize they're hers for a while because they're so close."
    "I feel her soft body on mine."
    "And the thing that holds my mouth is...!?"

    $ cg ('kt_01')
    $ unlock_gallery ('g5e2')

    yusuke "WAAAAH!!!"
    "I hurriedly push her away."
    "But I push the wrong spot, her soft rounded part."
    tomoe "......"

    $ bgfx ('black')

    "She rips my hand away and runs out in the hallway."
    "I get up and go after her."

    $ bgfx ('bg05b')

    yusuke "Tomoe! Wait! Wait for me!"

    $ char ('tto007')

    voice to0203
    tomoe "Hah, hah, hah... No!"
    "Finally, I grab her arm and stop her."
    "But she looks like she's ready to cry."
    yusuke "Ah, Tomoe."

    $ char ('tto013')

    tomoe "......!!"

    call effect ('SE56', ['white']) from _call_effect_21

    "I feel a sharp pain on my cheek."

    $ char ()

    "Tomoe leaves."
    "I freeze. I can't go after her."
    "I'm too shocked. She slapped me."
    "Then, something comes to mind."
    "The horoscope."
    "'You'll fall in love with the person you kiss during the week!'"
    yusuke "In love? No, she hates me!!!"
    "I don't believe in horoscopes. They never tell the truth."

    $ bgfx ('black')
    $ music_stop ()
    $ bgm (8)
    $ bgfx ('bg01a')
    $ char ('tas001')

    voice as0348
    asumi "Hey, Moe-Moe! I know it's hard to wake up in the morning, but this is too much!"

    voice to0204
    tomoe "I'm sorry. Just go ahead, please."

    $ char ('tas044')

    voice as0349
    asumi "Okay."

    $ char ('tma007')

    voice ma0075
    marumu "...We're leaving."
    yusuke "......"
    "I know she doesn't want to see me."
    "She really hates me."
    "She slapped me."
    "Nobody would believe me if I told them about that."
    yusuke "What should I do!?"
    asumi "......"

    $ bgfx ('black', diss_long)
    $ bgfx ('bg01b')

    yusuke "What should I do!? What should I do!?"

    $ char ('tas001')

    voice as0350
    asumi "What have you been thinking all day?"
    yusuke "Asumi."
    "I shrink back at her sudden appearance."
    "I shouldn't act like this, she'll get suspicious!"

    $ char ('tas037')

    voice as0351
    asumi "Moe-Moe hasn't come out from her room since she came back. Surely, you didn't...!"
    yusuke "No, I didn't do anything! I wouldn't do anything lecherous!"

    voice as0352
    asumi "I didn't say that."
    yusuke "Ah...no. You didn't."

    $ music_stop ()

    "I'm digging my own grave."

    $ char ('tas006')

    voice as0353
    asumi "What happened between you two!?"
    yusuke "N...no! Nothing."

    voice as0354
    asumi "You're lying! You guys are acting too weird."
    yusuke "We aren't acting weird at all..."
    "Asumi presses me for the truth."
    "I have nowhere to run."
    "Here, at school, nowhere. Like the day when I came to this town."
    "Suddenly, I get an idea."
    "But it's a really cowardly thing to do."
    yusuke "Don't come any closer to me! If you do..."

    voice as0355
    asumi "Huh? What will you do?"
    yusuke "I'll tell your secret to everybody!"

    $ char ('tas043')

    "I use 'Asumi's secret' as a shield, even though I don't remember what it is."
    "I stand at bay, well, at least I think I do."
    "Asumi gives me a scornful look."

    $ bgm (9)
    $ char ('tas010')

    voice as0356
    asumi "So what!? Tell people if you want!"
    yusuke "Are you sure? OK! I will!!!"

    $ char ('tas021')

    voice as0357
    asumi "What an idiot I am...sob!"
    "Asumi's eyes are brimming with tears."
    "Is she finally tired of me? Does she regret having me as her roommate?"
    "And...why did I say that?"
    "Asumi wipes her tears away and murmurs,"

    voice as0358
    asumi "Why? Why am I..."
    yusuke "...I'm sorry. I take back the words. Actually, I don't even..."

    $ char ('tas010')

    voice as0359
    asumi "Do you think that you can just take them back!?"

    $ bgfx ('black')
    $ music_stop ()

    "Asumi attacks me with her angry power."
    "Perhaps I've never been as scared of her."

    call cgeffect (sound_source='SE10', graphics=KENKA1, sound_loop=True) from _call_cgeffect_5
    $ bgm (7)

    "I run away fast! I just run away!"
    "But Asumi keeps attacking me mercilessly. She hits my back and the back of my head."
    "I'll die from the damage."
    "I have to put up some sort of last-resort resistance."
    "I decide..."
    "...to apologize to her from the bottom of my heart."
    "I stop and look back, then I..."

    $ bgfx ('black')
    call effect ('SE45', ETYPE3) from _call_effect_22

    "She doesn't give me the chance."
    "Asumi just dashes at me, and I collide with her."
    "Forehead to forehead."

    $ bgfx ('sora10')

    "My eyes are blurry from the shock."
    "And then, I'm out."

    call blackout from _call_blackout_50

    voice as0360
    asumi "Yusuke, Yusuke!"
    yusuke "Is someone...?"

    voice as0361
    asumi "Hey, are you all right!? Yusuke!"
    yusuke "...Calling me!?"
    "I open my eyes, and everything is still blurry."
    "I have a terrible headache."
    "But I can slightly move, anyway."
    "I start to get up... Um?"

    $ cg ('ka_01')

    yusuke "......"
    asumi "......"
    yusuke "...Eh?"

    voice as0362
    asumi "You...stupid!"

    $ bgfx ('black')
    call effect ('SE56', ['red']) from _call_effect_23

    "She lets fly with a slap."
    "The shock knocks me down again."

    $ bgfx ('bg01b')

    "My dim eyes see her running off."
    "Asumi was worried about me."
    "I jump up at her call."
    "Then our lips bump into each other."
    yusuke "I...kissed again."
    "Tomoe hit my left cheek."
    "And now Asumi hits my right cheek."
    "Both cheeks hurt as well as my head."
    "I lose consciousness with the pain."

    $ bgm (8)
    $ bgfx ('black')

    yusuke "What should I do...sob!"
    "Asumi doesn't show up for dinner."
    "Tomoe made dinner for me, but she doesn't even look at me."
    "I've never felt so uncomfortable in this room before."
    "I make a hasty retreat to the closet."
    "But I can't even sleep with all these problems weighing on my mind."
    yusuke "Ah, I have to see Asumi again tomorrow... Hmm?"

    $ music_stop ()
    $ sfx ('SE37', loop=True)

    "I hear rustling sounds."
    "I quietly open the closet door and look around."

    $ sfx (delay=0.5)
    call cg_slide (picture='em_0102', tm=1.5, kind='v', start=0.0, end=1.0, cls=diss_fast) from _call_cg_slide_11

    yusuke "Marutan, you're here again."

    voice ma0076
    marumu "I've been waiting for you."
    yusuke "Eh?"
    "Unexpected words. I'm surprised."
    "I followed Marumu because I was worried about her. I didn't know she came here for this."
    "When I sit next to her, she closes her eyes."
    "I don't understand why she does this."
    marumu "......"
    yusuke "Ah, Marutan."

    voice ma0077
    marumu "...You don't want to do it?"
    yusuke "Do what?"

    voice ma0078
    marumu "...Kiss."
    yusuke "...Huh?"
    "She opens her eyes wide and mutters,"

    voice ma0079
    marumu "You kissed Moe-Moe and Asumin."
    yusuke "How do you know that?"

    voice ma0080
    marumu "...I saw."
    yusuke "...Are you serious?"

    voice ma0081
    marumu "...Yes. Completely serious."
    "I almost say, 'Are you stalking me?' but I don't. I just look at Marumu."
    "She gives me a look of dissatisfaction."
    yusuke "Marutan, they were just accidents."

    voice ma0082
    marumu "I'm the only one who is not a part of all this."
    "She presses her body against mine."
    "It's hard to keep my balance on the roof."
    "She straddles me and brings her face close to mine."
    yusuke "H...hey! Marutan. Mmm!"

    $ cg ('km_01')

    voice ma0083
    marumu "SMOOCH..."
    yusuke "Oh..."

    voice ma0084
    marumu "...Now, I'm included."
    yusuke "UGAHH!"

    $ bgm (7)
    $ bgfx ('sora09')

    "I scream at the moon and lose all my energy."

    $ sfx ('SE40', loop=True)

    "I fall off the roof."

    $ bgfx ('black')

    "I made a lot of noise again, so I painfully hide in the bushes and cry."
    yusuke "I was kissed again... I don't know what to do...sob, sob!"


    call ep_finish from _call_ep_finish_8

    $ renpy.end_replay()
    $ unlock_episode (12)
    jump episode13
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

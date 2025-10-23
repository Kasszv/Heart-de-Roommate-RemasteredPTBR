label episode17_asumi:

    $ bgm (12)
    $ bgfx ('bg01a')
    $ char ('tto202')

    voice to0268
    tomoe "I won't be back tonight."
    yusuke "Okay. Have a nice one!"

    $ char ()

    "Tomoe leaves the dorm in the morning."
    "Her parents' hotel has a lot of customers today, so she's going home to help them."
    "Today is Saturday. There's no school."
    "After I see her off, I look around the room."
    yusuke "Asumi and Marumu are still in their bedrooms..."
    "Because we've been to Tomoe's house many times, we know her family."
    "But I don't know about the other two girls' families."
    "Where do their parents live? Do they have brothers or sisters?"
    yusuke "I think Asumi has a sister."

    $ char ('tas124')

    voice as0584
    asumi "What? Did you call me?"
    yusuke "Hi, Asumi. No, I didn't."
    "She comes out of her room and asks."

    $ char ('tas105')

    voice as0585
    asumi "What are your plans for today?"
    yusuke "Hmm, nothing special. How about you?"

    $ char ('tas133')

    voice as0586
    asumi "I'm going to..."
    "If she didn't have any plans, I'd ask her out. I'd say, 'Do you want to go out with me?'"
    "Thinking about that, I wait for her answer."
    "Then she goes back to her room, nodding."

    $ char ('tas105')

    voice as0587
    asumi "I'm going to school today."
    yusuke "Hey, that's rare. There's no school today but you're going."

    $ char ('tas127')

    voice as0588
    asumi "What's wrong with that? You can stay home with Marutan."
    yusuke "Okay."

    $ char ()

    "After a while, she leaves the dorm."
    "When she leaves, I feel something different from her profile."
    "She looks serious, as if she's going to meet someone important."
    yusuke "I feel uneasy..."


    call ep_start from _call_ep_start_26

    "I usually don't go out."
    "It's okay to go out, but as long as I live in the girls' dorm, it's hard to do, even on weekends."
    "I have to dress like a girl when I leave."
    yusuke "But I really want to know... All right!"
    "My fashion coordinator Tomoe is gone. I'll use the patio to leave like Toshibo."
    "I change my clothes as quickly as I can."
    "Otherwise, I'll miss Asumi."

    $ bgfx ('bg01a')

    yusuke "Okay, I'll take my shoes and..."

    $ char ('tma101')

    voice ma0121
    marumu "Are you going out, Yusuke?"
    yusuke "Hey, Marutan! Yeah, are you all right alone?"

    $ char ('tma108')

    voice ma0122
    marumu "No problem! Toshibo is with me."

    $ char ('tts002')

    voice ts0039
    toshibo "Meow!"

    $ bgm (2)

    "I was wondering where he was. He's with Marumu."

    $ char ('tma101')

    "These 2 people, I should say a person and a cat are like a perfect combination in a drawing."
    "Toshibo looks better with her than with Tomoe."
    yusuke "(They don't look like the owner and a cat. I can put them in the same category.)"

    $ char ('tma104')

    voice ma0123
    marumu "Yusuke, don't get too close!"
    yusuke "What?"

    voice ma0124
    marumu "People have things they don't want others to know."
    yusuke "Do you mean...?"

    $ char ('tma116')

    voice ma0125
    marumu "Just kidding. Go now."

    $ char ('tts002')

    voice ts0040
    toshibo "Meow!"
    "Is she advising me, knowing what I'm going to do?"
    "However, I don't know her real intention."
    "She's a mysterious girl."

    $ music_stop ()
    $ bgfx ('sora02')

    yusuke "...Yes! Nobody sees me! I'm safe now."

    voice yu0028
    unknown "Hey, you!"
    yusuke "Eek! Wh...what?"

    $ bgfx ('bg02a')
    $ bgm (16)

    "I look back in the direction where I heard the voice."

    $ char ('tyu002')

    "Ms. Yukimura, one of the 'Trio de Bitches.'"
    "I remember she loves Misaki."

    voice yu0029
    akane "What are you looking at? Did you..."
    yusuke "I...I didn't come out of the dorm."

    voice yu0030
    akane "Of course not, but you were trying to get into the building."
    yusuke "No, no! That's not it!!"
    "She's completely misunderstanding."
    "I have to leave here immediately."
    yusuke "I'm not interested in girls. I'm busy studying and doing other stuff."

    voice yu0031
    akane "Are you interested in guys, then?"
    yusuke "Huh?"
    "The subject is heading in an unexpected direction."
    "I quickly try to deny it, but she yells at me in an angry voice."

    voice yu0032
    akane "I know you, Sawada! You and Misaki are..."
    yusuke "You're misunderstanding."

    $ char ('tyu004')

    voice yu0033
    akane "I'll bring him back to the right way. Remember that!"

    $ char ()

    "Then, she dashes into the dorm."
    "It leaves me with a bad aftertaste."

    call blackout from _call_blackout_174
    $ bgfx ('bg04a')

    yusuke "Whew..."
    "I wasted my time."
    "I rush to school, but I can't find her."
    "The campus is big, so it's hard to find her."
    yusuke "It's impossible..."
    "I guess I've wasted my time."
    "I took the risk of not wearing girl's clothes when I left, but I couldn't find her."
    "I didn't need to leave the dorm then."
    yusuke "Damn it, what a waste. I don't want to go back empty handed."

    $ bgfx ('black')
    $ bgm (6)
    $ bgfx ('bg16a')

    yusuke "I should have gone back."
    "I regret coming to the hot spring resort."
    "It costs money to go anywhere."
    "My wallet is thin and light."
    "I can't do anything other than stroll aimlessly around in town."
    yusuke "I feel impudent visiting Tomoe's place..."
    "I envy Asumi's audacity."
    yusuke "Phew, I should have stayed home... Oh?"

    $ music_stop ()

    "A person is passing in front of me."
    "I scratch my eyes and look at the person again."

    $ bgm (5)
    $ bg ('bg16a')
    $ ev ('ea_1101')
    $ bgfx ('bg16a')

    yusuke "Asumi...why is she here?"
    "I appreciate this lucky coincidence."
    "She restlessly looks around as if she's looking for something."
    "She has a bouquet in her hand."
    "She enters one of the souvenir stores."
    "Before I move in closer, she comes out of the store."
    "She's carrying a small paper bag."
    "Then she runs up the hill."
    "She's really fast."

    call blackout from _call_blackout_175
    $ bgfx ('sora02')

    yusuke "She's really full of vigor... Cough."
    "If this were downtown Tokyo, I would lose her."
    "Fortunately, the road leads directly to the hill."
    "I'm not able to catch up to her but I don't lose track of her."
    "The place Asumi stops at is unexpected."
    yusuke "A cemetery...?"
    "There is only one thing to do here."
    yusuke "It's to test your courage.... Wait. It's daytime now."
    "I take a jab at myself and look at her."
    "She puts the flowers on a small grave."
    "She comes to the cemetery alone."

    $ bgm (9)
    $ cg ('ea_0101')

    "She cleans the tombstone, puts water on it and burns incense."
    "Then, she pulls something out from the small paper bag."
    "It's something she bought at the souvenir store."
    "I can't see clearly from here but it looks like candy or something."
    "She starts praying."
    "For a long, long time."
    "As she brings her hands down, she puts her hand in her pocket."
    "Something is in her hand...an accessory?"
    yusuke "Is that..."
    "The small yellow accessory. When she couldn't find it, she freaked out."
    "Holding it tight, she talks to the grave."

    $ cg ('ea_0103')

    "Smiling, she's reporting something to the person."
    "Her gentle, sweet smile."

    $ cg ('ea_0102')

    "Who is she talking to with the smile the other girls and I have never seen?"
    yusuke "Her ex-boyfriend...? I don't think so."
    "That accessory was a present from him."
    yusuke "I want to know who it is...ohh..."
    "If I get close to her and listen to what she's saying, I might find out who it is."
    "I can look at the name on the tombstone after she leaves."
    yusuke "But..."
    "'People have things they don't want others to know.'"
    "The words Marumu said before I left cross my mind."
    yusuke "I shouldn't do this."

    $ cg ('ea_0101')

    "Following and secretly watching her."
    "I already feel I'm doing something bad."
    "Though she doesn't notice me, I feel I'm interrupting a special time between them."
    yusuke "I'll go home."
    "The moment I look around,"
    "I see it."
    "The unexpected thing."

    $ cg ('ea_0104')

    "Asumi is crying."
    "With a sorrowful face."
    "Tears stream down her cheeks."
    "As if she were a little kid, frightened of the dark."
    "I've never seen her like this. She looks weak and despairing."


    call ep_middle from _call_ep_middle_26

    $ bgfx ('bg16a')

    yusuke "I have to leave now."
    "But I can't move my legs."
    "I'm wrapped up with mixed emotions."
    "I think again and again."
    "I wonder whether I should talk to her or not."
    "I don't know what I can do for her, but I'll do anything she wants."
    "I don't want to see her crying!"
    "Yet, my legs move in the opposite direction."
    "To walk away as quickly as possible."
    yusuke "If she sees me, she'll have doubts about me... Oh?"
    "From far away."
    "Someone is coming down."
    "She's like a wild boar, coming at full speed."
    yusuke "I don't look back..."
    "Feeling something bad, I step aside and try to enter a shop."
    "Suddenly, the person stops behind me."

    $ char ('tas036')

    voice as0589
    asumi "Is that you, Yusuke?"
    yusuke "......"
    "I almost say, 'No, you've got the wrong person.'"
    "If she realizes it's me, I'll be in big trouble."
    "She'll ask me why I'm here and why I'm lying."
    "I slowly look back and make a surprised face."

    $ bgm (5)

    yusuke "Asumi? What are you doing here?"

    $ char ('tas037')

    voice as0590
    asumi "That's what I want to ask you. I thought you were going to stay at the dorm all day."
    "She's sharp."
    "But I can't give up so easily."
    "Especially today."
    yusuke "I didn't say that. I was bored, so I went out for a walk. Besides, it's nice weather outside."

    voice as0591
    asumi "Is that so...?"
    "She still looks at me with suspicion."
    "However, she doesn't ask me any further."

    $ char ('tas044')

    "She's staring at my face."
    yusuke "Do I have something on my face?"

    voice as0592
    asumi "Yusuke, is your walk finished?"
    yusuke "Yeah. I was thinking about going back."

    $ char ('tas001')

    voice as0593
    asumi "All right, then. Come with me, please."
    yusuke "Where?"

    $ char ('tas012')

    voice as0594
    asumi "Let's go out on a date!"
    yusuke "Wait, Asumi..."
    "We 'run into' each other and have a 'date.'"
    "Oddly, this was my first plan."

    $ bgfx ('black')
    $ bgm (10)
    $ bgfx ('sora02')

    "Is this Asumi's hometown?"
    "She takes me to various places."
    "The restaurant with good steamed buns, big and small spas, and the hill with a wonderful view...I've never been to those places before."
    "I'm familiar with this town now."
    "We spend the rest of the day sightseeing, more than having a date."
    "It doesn't matter."
    "I'm really having a good time."
    "We hold hands and smile."

    $ bgfx ('bg14a')
    $ char ('tas002')
    $ bgm (14)

    voice as0595
    asumi "Yusuke?"
    yusuke "What...?"

    $ char ('tas045')

    voice as0596
    asumi "If we continue doing this everyday, we'd be happy forever, don't you think?"
    yusuke "......"

    $ bgfx ('sora02')

    "I hold her tight."
    "Impulsively and passionately."
    "She relaxes in my arms and smiles."
    "Her warmth gets into me and changes to love."
    "I wish I could hold her like this forever and ever."

    $ music_stop ()
    $ bgfx ('sora05')
    $ bgfx ('bg02b')

    "After Asumi goes inside the dorm first to make sure nobody is around, I rush inside."
    "And I run into our room."

    $ bgm (3)
    $ bgfx ('bg01b')
    $ char ('tas002')

    yusuke "Phew, we made it."

    voice as0597
    asumi "Why don't you wear girl's clothes when you go out? Moe-Moe would be more than happy to choose your clothes for you."
    yusuke "No thanks..."
    "Asumi calls out to the door."

    $ char ('tas001')

    voice as0598
    asumi "Marutan, thanks for staying. I bought some dumplings for you. I also bought flavored boiled eggs for Toshibo."
    "Nobody answers."
    "I notice a piece of paper on the table."
    yusuke "Asumi, nobody is here."
    "'I'm on an expedition with Toshibo. We'll be back tonight. Marumu.'"
    "As I hand it to her, she puts the food on the table."

    $ char ('tas024')

    voice as0599
    asumi "Moe-Moe won't be back tonight either. Let's eat them, just the two of us."
    yusuke "Yeah, the food will get cold."

    $ char ('tas044')

    voice as0600
    asumi "Yusuke..."
    yusuke "Yes...?"

    $ char ('tas005')

    voice as0601
    asumi "Give me a cup of tea."
    yusuke "Okay..."
    "I expected her to say something romantic but I was wrong."

    call blackout from _call_blackout_176
    $ bgm (13)
    $ bgfx ('bg01b')
    $ char ('tas105')

    voice as0602
    asumi "Hmm...it was good."
    "While I'm making tea, she eats a bunch of them."
    "The sky turns purple. It's time for dinner."
    yusuke "Moe-Moe won't be back until tomorrow. What do you want for dinner? How about Okonomiyaki?"

    $ char ('tas118')

    voice as0603
    asumi "They taste pretty similar to the dumplings we just ate."
    yusuke "Yeah, you're right. Then, let's get something at the grocery store."
    "She prevents me from leaving."

    $ char ('tas105')

    voice as0604
    asumi "We just ate a short while ago, so we can skip dinner, don't you think?"
    yusuke "Umm...okay."
    "Rubbing my belly, I sit down on the floor."

    $ bgfx ('sora05')

    "We don't talk for a while."
    "Soft orange lights shine on us through the window."
    "A peaceful time with the person I love."
    "It brings me happiness, but at the same time, it makes me feel a bit dissatisfied."
    "I slowly stretch my hand out to her."
    "A few more inches...I want to hold her hand."
    "Before my tiny wish comes true, Asumi suddenly looks back at me."
    "I hurriedly pull my hand back. It makes her smile."

    $ bgfx ('bg01b')
    $ char ('tas146')

    voice as0605
    asumi "He he. Just the two of us..."
    yusuke "Yeah, ha ha."

    $ char ('tas147')

    voice as0606
    asumi "Yusuke?"
    yusuke "Tea? Wait a second, I'll make it."
    "Before I expect something that won't happen, I head to the kitchen."
    "The conditioned reflex makes me move."
    "However, she prevents me from leaving."

    voice as0607
    asumi "I don't want tea..."
    yusuke "Okay..."
    asumi "......"
    yusuke "......"
    asumi "......"
    yusuke "How about coffee?"

    voice as0608
    asumi "Yusuke..."
    yusuke "Something different? I guess we have some black tea."

    voice as0609
    asumi "...Do you want to do it?"
    yusuke "Uh...ah..."
    "I understand what she's saying."
    "Though she doesn't tell me, I understand her true feelings."
    "I've always wanted her."
    "I sometimes wonder whether it's my pure feelings or whether it's just a dirty desire for her."
    "But..."
    "It doesn't matter."
    "At least for us now."
    "We both want each other so bad."
    "We both want to hold and accept each other."

    call blackout from _call_blackout_177
    $ bgm (14)
    $ cg ('ha_0601')
    $ unlock_gallery ('g1e8')

    "I reach my hand to her."

    voice as0610
    asumi "Ah...aaahhh...mmm."
    "I hold her tight to feel her warmth."
    "She wraps her arms around me as well."
    "Kissing her lightly, I bring my hand to her."

    voice as0611
    asumi "Umm...ahh...ah..."
    yusuke "Do you feel good?"

    voice as0612
    asumi "Yeah, I guess so."
    "The word 'guess' bothers me a little."
    "But she looks cute when she tells me."
    "I want her to feel really good."
    "I passionately fondle her with care."

    voice as0613
    asumi "Ahh! Hmm...uhh...mmm..."
    yusuke "Your voice is getting louder, Asumi."

    voice as0614
    asumi "Shut...up...mmm. Ahh...aahhh..."
    yusuke "It sounds so cute."
    "My hand is crawling down to her lower half."

    $ cg ('ha_0602')

    "Then I slide it between her legs."
    "I softly rub her womanhood."

    voice as0615
    asumi "Oh...mmm..."
    yusuke "You're already wet..."
    "She complains over what I say,"

    voice as0616
    asumi "Umm...mmm...don't say that...ahhh..."
    yusuke "You're hot, Asumi... Ahh..."

    voice as0617
    asumi "No, don't touch me like that...ahh...mmm... Ohh!"
    yusuke "You're so sensitive. Feel more and moan louder."

    voice as0618
    asumi "You're mean...ahh...mmm..."
    "Stimulating her harder, I continue giving her more pleasure."
    "I want her to show me the cuter, girlish side of herself."
    "Unexpectedly, she turns to retaliate."
    "She's not a girl who quietly bears the pleasure."

    $ bgfx ('black')

    yusuke "Huh!? Hey, hey..."

    voice as0619
    asumi "Ahh...he-he..."
    "She's touching my crotch."
    "And she caresses my dick over my underwear."
    "With her delicate fingers, I'm gradually becoming intoxicated."

    voice as0620
    asumi "What's wrong, Yusuke?"
    yusuke "Umm...nothing..."
    "Her soft hand is caressing me harder and harder."
    "Moreover, she whispers in my ear,"

    voice as0621
    asumi "Yusuke..."
    yusuke "Mmm...?"

    voice as0622
    asumi "Want more...?"
    yusuke "Ohh...mmm...uhh..."
    "I want her to do it...but I can't say it."
    "I obstinately refuse to answer her."

    voice as0623
    asumi "You don't answer me...okay, then."
    yusuke "Oh..."
    "She lets go of my shaft."
    "I involuntarily let out a cry."
    "Chuckling, she holds my dick again."

    voice as0624
    asumi "I'll do whatever I want because you don't say anything. SMACK!"
    yusuke "Hey, Asumi...oh!"

    $ cg ('ha_0303')

    "She abruptly takes my underwear off and kisses my shaft."
    "I'm surprised as she holds my cock in her mouth."

    $ cg ('ha_0301')
    $ unlock_gallery ('g1e9')

    voice as0625
    asumi "Hmm...mmm...uhh...mmm..."

    voice as0626
    asumi "Umm...hmmm...mmm."
    yusuke "Asumi, don't suck it so hard..."

    voice as0627
    asumi "Umm...ahh...mmm..."
    "She continues giving me a blowjob."
    "Affectionately and frantically."
    "I'm confused at her enthusiasm."
    "She uses her tongue hard to give me more pleasure."
    "Lying here without doing anything makes me feel embarrassed."
    "I can give her more pleasure!"
    "I stretch out to her."

    $ cg ('ha_0302')

    voice as0628
    asumi "Mmm...ahh... No, stop it..."
    yusuke "You're doing very well...I...mmm..."

    $ cg ('ha_0301')

    voice as0629
    asumi "Uhhh...mmm...umm..."
    yusuke "Ugh...mmm...aahhhh..."

    voice as0630
    asumi "Hmm...ohh...aaahhh...."
    "We intensely grope each other."

    $ cg ('ha_0304')

    "She unconsciously starts touching herself."
    "Both of us indulge in the pleasure."

    $ cg ('ha_0305')

    voice as0631
    asumi "Ohh...mmm...aahhh...yes...yes...aahhh."
    yusuke "Ummm...mmm.... Ohh! Ahh...ahhh."

    $ bgfx ('white')
    $ bgfx ('black')

    "Asumi and I both cum, just caressing each other."
    "Breathing heavily for a while, I lay alongside her."
    "We easily flare up."

    voice as0632
    asumi "Ahh...aahhhh...mmm..."
    yusuke "Hmm...mmm..."

    voice as0633
    asumi "Umm...SMOOCH."
    "She kisses me all of a sudden."
    "Fondling each other again, we start French kissing."
    "Our desires have risen again."
    "Our hands are now busily going at each other."
    "We furiously fondle each other."
    yusuke "Oh...Asumi..."

    voice as0634
    asumi "Yusuke...aahhhh...mmm..."

    $ sfx ('SE04', loop=True)

    "We're absorbed in making love."
    "As I pull my wet finger out of her slit, I whisper to her,"

    $ sfx (delay=0.5)

    yusuke "I want you, Asumi."
    "Holding my cock, she murmurs in a soft voice,"

    voice as0635
    asumi "Yes, I want you too..."
    "She kisses my dick again."
    "We're ready."
    "Looking at one another, I hold her to become one."
    "I want to feel her warmth, and so does she."
    "That's why we make love."

    $ cg ('ha_02')
    $ unlock_gallery ('g1e10')

    voice as0636
    asumi "Ahh...you're coming inside me...mmm."
    "I slowly thrust deep in her from behind."
    "She cries out with joy."
    "I help her to sit down on my lap."

    voice as0637
    asumi "Oooow, yes...mmm...aahhh...yes, yes..."
    yusuke "Open your legs more, Asumi..."

    voice as0638
    asumi "B...but...aahhh...I'm embarrassed."
    "She blushes at my request."
    "Pumping away at her from beneath, I ask her again,"
    yusuke "I want to feel you more, so please..."

    voice as0639
    asumi "Y...yeah...aaahh!!"
    "Hesitantly, she opens her legs wide."
    "My cock is swallowed even deeper...we connect tightly."
    "As I hold her legs up, I ram her hard."
    "Along with the movements, she yelps out."

    voice as0640
    asumi "Ohh...yes, Yusuke. Yes, yes...aaahhh...mmm..."
    yusuke "You're hot and tight...oohhh!!"
    "Her wet pussy walls are quivering."
    "Sometimes, they tighten up around my dick."
    "Stimulated, my dick twitches inside her."
    "The build-up of sexual tension inside us is reaching the limits."

    voice as0641
    asumi "Ahhh....you're scraping me inside...aaahhhh..."

    voice as0642
    asumi "Harder, Yusuke. Do me harder...ahh...mmm...aahhhh!!"

    $ sfx ('SE07', loop=True)

    "She's twisting around, rising to meet me."
    "With her hair disheveled and flying in all directions, she indulges herself in pleasure. She looks incredibly beautiful."
    "We're cumming together."

    voice as0643
    asumi "Ohh...I...I'm cumming...aahhh...aahh..."
    yusuke "Oooow, Asumi, I can't hold it any longer...Asumi!"

    voice as0644
    asumi "Ahh...aah..ah...mmm...ahh... AAAHHHH!!!"
    "She convulses again and again in my arms."

    $ sfx (delay=0.5)

    "I let myself explode, filling her with my hot cum."

    $ bgfx ('white')
    $ music_stop ()

    "Feeling my hot liquid, she slowly loosens up."
    "Then she falls down on me."
    "As I hold her, she wraps her arms around me."

    $ bgm (10)

    voice as0645
    asumi "Yusuke...you're warm."
    yusuke "Yeah...you too."

    voice as0646
    asumi "Let's stay like this for a while..."
    "I feel comfortable with her warmth."
    "As a reply to her, I hold her even tighter."
    "My heart beats slower and slower."
    "The rhythm sounds like a lullaby."
    "And then, I fall asleep."

    call blackout from _call_blackout_178

    voice as0647
    asumi "Yusuke, wake up."
    yusuke "Umm...uh...Asumi."

    $ bgm (14)
    $ cg ('ha_0703')
    $ unlock_gallery ('g1e11')

    "I wake up as I hear her voice."
    "We're sharing one sheet together."
    "Looking at my sleepy face, she smiles."

    voice as0648
    asumi "He he. Wake up, Yusuke."
    yusuke "Oh, I fell asleep..."

    $ cg ('ha_0701')

    "She woke up first and has been looking at me."
    "I feel a little embarrassed."
    "So, I look back at her."
    yusuke "......"
    asumi "......"
    "We're totally naked."
    yusuke "I feel...embarrassed."

    voice as0649
    asumi "Heh heh...you act like a girl."
    yusuke "I don't think so. It's because..."

    $ cg ('ha_0706')

    "I touch her breasts."
    "Her well-rounded breasts."

    voice as0650
    asumi "Yikes!"
    yusuke "I don't have such cute, sensitive breasts."
    "I softly fondle them."
    "She twists hesitantly and tells me,"

    $ cg ('ha_0701')

    voice as0651
    asumi "You'll get dumped if you want to have sex all the time."
    yusuke "By whom?"

    $ cg ('ha_0703')

    voice as0652
    asumi "I don't know...heh heh."

    $ cg ('ha_0706')

    "As I continue to caress her, I whisper,"
    yusuke "Do you want it?"

    voice as0653
    asumi "Yeah...I guess."
    yusuke "......"

    voice as0654
    asumi "Mmm..."
    "We kiss."
    "Kissing lightly again and again... I want her."
    "As I look at her, she looks back at me with pure eyes."
    "We move closer and hold each other... Oh!?"

    $ music_stop ()

    yusuke "Huh... Ohh!"

    voice ts0041
    toshibo "Meow!"

    $ bgfx ('black')
    $ bgm (7)

    "Under the sheet, it lies on my feet."
    "It's Toshibo."
    "He went out with Marumu."
    yusuke "Toshibo, you're back...?"

    voice ts0042
    toshibo "Meooow!"
    yusuke "That means... WHAAA!!"
    "Marumu will be back soon."
    "I can't let her see us on the floor naked...never!"
    "I'm agitated and confused."
    "I ask Asumi for help."
    yusuke "What should we do, Asumi?"

    voice as0655
    asumi "I don't know, actually..."
    yusuke "Oh, no! Marutan will be back soon. What should we do?"

    voice as0656
    asumi "Calm down! We can think... Ohh!"
    "We hear the door open."
    "Marumu comes back."
    "It's too late now."
    "We can't do anything!"
    "Asumi and I are wrapped up in the sheet."
    "Marumu's (maybe) footsteps are getting closer."
    "She stops next to us."

    $ cg ('ha_0704')

    asumi "......"
    yusuke "......"

    voice ma0126
    marumu "Tap-Tap..."
    "She pokes the sheet."
    "We're in the middle of the room."
    "She pokes Asumi, not me."

    $ cg ('ha_0705')

    asumi "(No, stop!)"
    yusuke "(Be patient!)"

    voice ma0126
    marumu "Tap-Tap..."
    yusuke "...Yikes."
    asumi "(Shhh...be quiet!)"
    yusuke "(S...sorry.)"
    "Marumu doesn't notice my voice and stops tapping us."
    "However, her curiosity is aroused, and she tries to do something different."

    voice ma0127
    marumu "What's this?"

    voice ts0043
    toshibo "Meow!"

    voice ma0128
    marumu "Toshibo..."
    "Toshibo is gone."
    "He's already out from under the sheet."
    "Her interest changes from the sheet to Toshibo."
    "Good job, Toshibo!"
    "Marumu starts asking him questions."

    voice ma0129
    marumu "Is this your house?"

    voice ts0044
    toshibo "Mew?"

    voice ma0130
    marumu "Or is this your egg?"

    voice ts0045
    toshibo "Meoww!"
    "I don't think she's able to communicate with cats. She's not Tomoe."
    "Yet, she gets an answer from Toshibo."

    $ music_stop ()

    voice ma0131
    marumu "Let's go out, Toshibo."

    voice ts0046
    toshibo "Meow!!"
    yusuke "(Good, she's leaving.)"

    $ cg ('ha_0702')

    voice as0657
    asumi "(I'm so relieved she didn't notice your voice.)"

    $ bgm (7)
    $ cg ('ha_0705')

    voice ma0126
    marumu "Tap-Tap..."

    voice as0658
    asumi "!!!"
    "Marumu makes a surprise final inspection."
    "The last poke hit Asumi's weakest part."
    asumi "(Ahh, I can't stand it any longer!)"
    yusuke "(Be patient. It'll be over soon, Asumi.)"
    "She's covering her mouth to subdue her voice."
    "Thanks to her efforts, the menace is leaving now."

    voice ma0132
    marumu "Bye..."

    voice ts0047
    toshibo "Meow, meow!"
    "Marumu and Toshibo go outside again."
    "The danger has finally left."

    $ music_stop ()
    $ cg ('ha_0701')

    "Asumi is relieved and suddenly pinches my nose."
    "She's upset at me because I peeped out a word."

    voice as0659
    asumi "Hey! What were you thinking!?"
    yusuke "S...sorry, but I couldn't help it."

    $ cg ('ha_0703')

    voice as0660
    asumi "That's okay...heh-heh."
    "We can smile now because we made it."
    "However, our romantic mood was ruined by Marumu's curiosity."
    yusuke "Whew. What do you want to do?"

    voice as0661
    asumi "Marutan took the romance away..."
    "Looking at her, I'm still thinking to ask her."
    yusuke "......"
    asumi "......"
    "She's pretty charming and cute in this situation."

    $ bgm (14)
    $ cg ('ha_0706')

    yusuke "Asumi..."

    voice as0662
    asumi "Ahh...hey, stop."
    "I can't control myself and grab her breast."
    "She doesn't refuse me and moves closer."
    "We start the second round."
    "We're young, after all."

    jump episode17_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

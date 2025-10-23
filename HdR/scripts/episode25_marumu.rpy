label episode25_marumu:

    $ bgm (16)

    "We divide into two groups."
    "Asumi pairs with Tomoe, and I and Marumu form the other team."
    "Since we don't know where Hikaru is, it's better to separate into two groups to find her."

    $ bgfx ('bg12a')

    "However hard we look for Hikaru, we still can't find a trace of her yet."
    yusuke "Just as I was afraid of, we won't be able to find her."

    $ char ('tma001')

    voice ma0421
    marumu "Yusuke, don't give up."
    yusuke "I know, I know. But...oh?"

    $ char ('tma004')

    marumu "......"
    "Suddenly, Marumu stops walking."
    "Then she closes her eyes as though she's praying for something."
    yusuke "...What are you doing, Marutan?"

    voice ma0422
    marumu "Praying."
    yusuke "For what?"

    voice ma0423
    marumu "...For finding Hikaru."
    "What a girl!"
    yusuke "If we can come across her by praying to God, we wouldn't have any trouble. Silly girl...ah!?"

    $ music_stop ()
    $ char ('tma025')
    $ char ('tma001')

    voice ma0424
    marumu "It came?"

    $ bgfx ('white')
    $ bgfx ('bg14a')
    $ sfx ('SE52')

    yusuke "Yeah. Somehow...it just came to me."

    $ bgfx ('bg12a')
    $ char ('tma017')
    $ bgm (5)
    $ sfx (delay=0.5)

    "Then my jaw drops down."
    "Usually, I don't believe in supernatural phenomena."
    "Yet a memory from the past abruptly pops into my mind."
    "...The clear vision of her standing alone at the observatory."
    "Marumu is, after all, a mysterious girl."
    "Anyhow, I explain to her about my flash."
    "But..."
    yusuke "Can we really find her there?"

    $ char ('tma001')

    voice ma0425
    marumu "Maybe."
    "For now, we don't have any other ideas where she might be."
    "We'd better believe in the flash."
    yusuke "Trust the vision, and let's go to the observatory!"

    $ char ('tma017')

    voice ma0426
    marumu "Marumu and Yusuke are a psychic couple!"
    yusuke "...Good try, Marutan."
    "I know she's joking, but I can't stop thinking that if I had supernatural power, how great my life would be."

    jump episode25_b

label episode25_marumu_c:

    $ bgfx ('black')

    "At last, the day of departure has arrived."
    "...The day to leave the Harukaze Dorm."

    $ bgfx ('bg09a')
    $ chars ('tna002', 'thi001')
    $ bgm (10)

    "Namiki and Hikaru already left yesterday."
    "I know Namiki plans on teaching her how to relax."
    "Namiki will probably take her to every single hot spring in Japan until Spring comes."

    $ bgfx ('black')
    $ bgfx ('bg02a')
    $ chars ('tas201', 'tto207')

    "This morning, Asumi and Tomoe left."
    "Asumi wanted to think about her future alone."
    "And Tomoe wanted to help with her parents' business."

    call blackout from _call_blackout_2

    "I know I have to leave the dorm soon too."
    "If I don't, the new students won't be able to move in."
    "That's why I have to move on and go out into the world."
    "There are only two of us left in the room."
    "Me and Marumu."
    "We can't stay here forever."
    "The night before departure,"

    $ cg ('em_0101', pos=[ALIGN(0.0, 0.0)])
    $ bgm (16)

    "I climb up on roof to look for Marumu."
    "I know that on nights like this, she usually bathes in the moonlight."

    call cg_slide (picture='em_0101', tm=3.0, kind='v', start=0.0, end=1.0, cls=diss_fast) from _call_cg_slide

    yusuke "Marutan?"

    voice ma0427
    marumu "...Yusuke."

    $ cg ('em_0102', pos=[ALIGN(0.0, 1.0)])

    "She turns around when I call her name."
    "Then as usual, I sit next to her."
    yusuke "What do you see?"

    voice ma0428
    marumu "The moon."
    yusuke "I know that..."
    "I thought she'd give me an odd answer, but it was pretty straight forward."

    $ cg ('em_0101', pos=[ALIGN(0.0, 1.0)])

    "As if reading my mind, she broods over it a while and gives me a different answer."

    $ cg ('em_0102', pos=[ALIGN(0.0, 1.0)])

    voice ma0429
    marumu "...My bright future."

    $ sfx ('SE59')

    "I like her positive attitude!"
    "I praise her in my own words."
    yusuke "Congratulations! You just won a million dollars!"

    $ sfx (delay=0.5)

    voice ma0430
    marumu "No thanks."
    yusuke "Ah...okay."
    "Well, she doesn't like my joke, so just forget it."

    call cg_slide (picture='em_0102', tm=3.0, kind='v', start=1.0, end=0.0, cls=diss_fast) from _call_cg_slide_1

    "I look up at the moon and remain silent."
    "Our surroundings are so quiet."
    "It's because only the two of us are left."
    yusuke "Tomorrow's the last day, isn't it!?"

    voice ma0431
    marumu "Yeah."
    "I feel so strange."
    "I'm having a hard time accepting we have to leave here forever."
    "It feels like I'll come back and meet all my friends after the spring break."
    "But in the bottom of my heart, I actually know the fun times are over."
    yusuke "......"

    voice ma0432
    marumu "...Yusuke."
    yusuke "What?"
    "All of sudden, Marumu takes her eyes off the moon."
    "Then she looks straight into my eyes."

    $ bgm (14)

    voice ma0433
    marumu "Teach me."
    yusuke "What do you want me to teach you?"
    "She clings to me and mutters,"

    voice ma0434
    marumu "...The feeling of true love."
    yusuke "......"
    "I hesitate to answer her."
    "Actually, I don't know how to answer her."
    "To tell you the truth, I'm too young to handle this kind of situation."
    "But I've got to think of what I can do for her!"
    "Then I give her a gentle kiss."
    "...Under the quiet moonlight."

    call blackout from _call_blackout_3

    "It's growing late."
    "Tomorrow, we have to leave early in the morning."
    "I know I can't, but I should try to go to bed early."

    $ bgfx ('bg01d')
    $ char ('tma101')
    $ bgm (9)

    yusuke "Good night, Marutan."
    "Before I can slip into bed, she grabs my hand."

    voice ma0435
    marumu "I want to sleep with you."
    yusuke "......"
    "It's our final night."
    "When the sun comes up, I have to say goodbye to her."
    "That's why this is her last favor."

    $ char ('tma103')

    voice ma0436
    marumu "Can I sleep with you?"
    yusuke "...Okay."
    "Without realizing it, I nod."
    "We should spend the last night together."
    "...To feel each other's warmth."
    "I don't know why, but I just think so."

    call blackout from _call_blackout_4

    "I'm having a hard time falling asleep."
    "Is it because I feel her warmth next to me?"
    "I notice an unknown feeling rising inside me."
    "It says, 'I want to be closer to her and feel more of her warmth.'"
    "Does it mean I love her?"
    "I gaze blankly at her sleeping face."
    "Without warning, she grabs my hand."
    "It seems she's been wake, just closing her eyes."

    voice ma0437
    marumu "...Yusuke."
    yusuke "What is it?"

    voice ma0438
    marumu "...Teach me the feeling of true love."
    "She asks for the same thing again."
    "But again, I can't answer."
    "Because I don't know what to do."
    "But I guess I don't need to brood over it."
    "I should simply follow my heart."
    "We've been seeing each other, anyway."
    yusuke "...Okay."
    "I frankly nod."
    "I hold her under the blanket."
    "I want to undress her and sense her warmth."
    "And touch and feel her."
    "Then I want to make love to her."

    $ bgm (10)
    $ cg ('hm_0401')
    $ unlock_gallery ('g3e9')

    "For the first time, we make love."
    "...During our final night."
    "It doesn't go smoothly, and we're rather clumsy."
    "I don't know how much time has passed."
    "I kept wanting her more than anything in the world."
    "I feel her with my fingers, my lips, and even with my whole body."
    "I'm occasionally puzzled over what to do."

    $ cg ('hm_0402')

    "But still, I make love to her."
    "Suddenly, she lets out a small sigh."

    voice ma0439
    marumu "...Ah."
    yusuke "Marutan?"
    "She holds me tight."
    "Then she whispers,"

    $ bgfx ('black')
    $ bgfx ('sora09')

    voice ma0440
    marumu "...Just a little."
    yusuke "......"

    voice ma0441
    marumu "I think I understand what true love is."
    "The moon shines in the darkness."
    "Under the moonlight, I see her cheeks redden a bit."
    "Then I hug her tighter than ever."
    "...My everlasting love."

    call blackout from _call_blackout_5

    "When I wake up, it's broad daylight."
    "This is the day I must say goodbye to her."

    $ bgfx ('sora02')
    $ bgm (14)

    "I keep talking to her until the last minute, as if reluctant to part from her."
    "From this point on, we'll take different paths."

    $ bgfx ('bg02a')
    $ char ('tma001')

    voice ma0442
    marumu "Hey, Yusuke."
    yusuke "What, Marutan?"

    voice ma0443
    marumu "...I'll study more."
    "I know she studies hard."
    "Still, she'll keep studying many things in her own way."
    "I should follow her example and continue learning too."
    "I can't let her beat me!"
    yusuke "We should always do our best, okay?"

    $ char ('tma004')

    voice ma0444
    marumu "I'll be a pretty woman someday!"
    yusuke "Huh?"
    "Oh, I get it! She was talking about a different kind of studying."
    "I unconsciously stare at her in round-eyed wonder."
    "There's a smile on her lips as she looks at my amazement."
    "It's very much like her."
    "Then she holds my hand tight."

    $ char ('tma001')

    "And we wish about meeting each other again someday."
    "This isn't the end."
    "We're just too immature."
    "That's why we'll start again from this point."

    voice ma0445
    marumu "Someday, if I could be your girlfriend again..."
    yusuke "......"

    $ char ('tma003')

    voice ma0446
    marumu "I'd be so happy!"
    yusuke "Ha ha."
    "I give her a gentle smile."
    "I love the times I can talk to her like this."
    "No matter how far we're apart, I believe that someday, we'll meet again."

    jump episode25_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

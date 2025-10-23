label episode15_asumi:

    $ bgfx ('bg02a')

    yusuke "Hmm...it's been a long time."
    "Summer is still lingering."
    "Finally, the new semester starts tomorrow!"
    "Before the summer vacation started, I thought I'd have terrible problems, but I got back here safe enough."

    $ bgfx ('white')
    $ bgm (14)
    $ bgfx ('sora02', diss_long)

    "Summer vacation started right after Asumi and I became a couple."
    "Honestly, I felt sorry."
    "Summer is supposed to be the season that lovers passionately love each other! (only in my dreams of course.)"
    "School orders (vacation) forced us apart."
    "On second thought, it was a good time to think about how I really feel about her."
    "I love Asumi, but I don't know why I love her or what attracts me to her."
    "I just feel it's because I fell in love with her."
    "Namiki would tell me, 'it's okay to do anything you want when you're young.'"
    "While I stayed at my parents' and thought about her...I wanted to see her so bad."
    "I wanted to see her smile and hear her voice!"
    "I impulsively called her."

    $ vox ('as0512')

    "She was surprised, but I felt better hearing her happy voice."

    $ vox (delay=0.3)

    "We talked a lot more than I thought we would."
    "And then I couldn't stop myself."
    "I called her everyday and the telephone bill nearly killed me. "
    "However, I felt like I was in Seventh Heaven."
    "I spent too much money going all the way over to see her."
    "Yet our first date was unforgettable for me."
    "A kiss before we said goodbye..."

    $ bgfx ('white', diss_long)
    $ bgfx ('bg02a')
    $ bgm (5)

    yusuke "And finally, I'm back!"
    "I longed for the end of summer vacation!"
    "From tomorrow, no, from tonight, I can be with Asumi again."
    "I look up at the dorm with different feelings than the first time I came here."
    yusuke "What should I say first? 'I'm home!'...that's not good. 'We can see each other again!'...that isn't good either."
    yusuke "How about, 'I'm so happy to see your smile again.' Umm, that's not me, heh-heh..."

    jump episode15_b

label episode15_asumi_b:

    $ bgfx ('black')

    "I hear her scream, and she suddenly throws herself at me."
    "My heart leap at the unexpected event."
    "Her soft boobs push against me."
    "I can't...I can't control myself any longer."

    $ bgfx ('bg01a')
    $ char ('tma201')

    voice ma0109
    marumu "I'm home."
    yusuke "Huh...?"

    voice to0249
    tomoe "Marutan...welcome back."

    $ bgm (2)

    "She shows up out of the blue."
    "Tomoe is astonished to see Marumu."
    "I can't blame Tomoe for mistaking Marumu as a big stag beetle. "
    "Marumu starts eating dinner, and I try to calm down."

    call blackout from _call_blackout_136
    $ bgfx ('bg01a')

    yusuke "Where's Asumi...?"

    $ char ('tma004')

    voice ma0110
    marumu "She's not here yet..."

    $ char ('tto004')

    voice to0250
    tomoe "What happened to Asumi...?"

    $ bgfx ('sora01')

    "Asumi hasn't returned, though we've finished Marutan's special breakfast."
    "Well, it's time to go to school."

    $ bgfx ('bg04a')
    $ char ('tko001')

    kosuke "Good morning, Yusuke."
    yusuke "Morning..."
    kosuke "Hey, how was your summer vacation? Yusuke...?"
    yusuke "......"
    "I don't see her in the classroom."
    "I even go to the hallway to look for her."
    "She's a mature girl, so I think she's all right, but..."
    kosuke "Are you listening? Hey, Yusuke!"
    yusuke "Sorry, I have to go!"

    $ char ('tko003')

    kosuke "Hey, Yusuke... Hey!"

    $ bgfx ('bg07a')

    yusuke "Whew-whew...she's not here."
    "I go to the rooftop, but I don't see anyone."
    "I don't think students would come up here this early in the morning."
    yusuke "Is there something wrong, Asumi...?"

    $ bgfx ('bg05a')

    yusuke "She's not here..."

    $ char ('tto013')

    voice to0251
    tomoe "What's wrong with you, running out of class so suddenly?"
    yusuke "I thought Asumi might be on the roof."

    $ char ('tto001')

    voice to0252
    tomoe "Hey, here comes Ms. Yagami!"
    yusuke "Yeah..."
    "Our conversation is interrupted."

    $ bgfx ('sora01')
    $ sfx ('SE51')

    "Asumi doesn't even show up for homeroom."

    $ bgfx ('bg04a')
    $ char ('tyo001')
    $ bgm (4)
    $ sfx (delay=0.3)

    voice yo0146
    yagami "Good morning, everybody. I hope you had a good summer vacation. I'll call roll then. Aizawa..."

    voice as0513
    asumi "G...good morning!"
    "The whole class looks back in the direction the voice comes from."
    "The first person late for the first class of the semester."

    $ bgm (5)
    $ char ('tas030')

    voice yo0147
    yagami "Ms. Hirota. You're out."

    $ char ('tas018')

    voice as0514
    asumi "Oh, please! Today is the first day, you know. Have mercy."

    voice yo0148
    yagami "No way!"

    voice as0515
    asumi "Oh boy..."
    "Asumi drops her head and walks to her desk."
    "When she passes by, she whispers,"

    $ char ('tas046')
    $ bgm (14)

    voice as0516
    asumi "Hi, good to see you again."
    yusuke "Yeah..."
    "My new 'semester' finally starts."


    call ep_middle from _call_ep_middle_22

    jump episode15_c

label episode15_asumi_c:

    call blackout from _call_blackout_137
    $ bgm (13)
    $ bgfx ('bg07a')
    $ char ('tas001')

    voice as0522
    asumi "Sorry, I'm late!"
    yusuke "That's okay; I just got here a few minutes ago, myself."
    "I sound like her boyfriend, out on a date."
    "But perhaps my feelings are now fairly close to that."
    "I was so excited, I actually got here 10 minutes early."
    "When Asumi told me, 'Come to the rooftop after school,' my heart started beating fast."
    "Not the dorm, the rooftop."
    "Not some place with other people; just the two of us."
    "What does Asumi want to tell me...?"

    $ bgfx ('black')
    $ music_stop ()
    $ bgfx ('bg07a')
    $ char ('tas001')

    yusuke "Eh?"

    voice as0523
    asumi "Didn't you hear me? Do you have a problem with your hearing?"
    yusuke "No, but..."

    $ char ('tas044')

    voice as0524
    asumi "OK, I'll tell you one more time. Don't tell Moe-Moe and Marutan about us!"
    yusuke "Why not?"
    "Of course, I don't plan on telling anyone about us."
    "I'm shy."
    "But I don't feel good hearing what Asumi is saying."
    "We aren't doing anything bad. There's not a problem if someone finds out about us."
    "But...Asumi doesn't want anyone to find out?"
    "She doesn't want them to because she's too embarrassed having a boyfriend like me?"

    $ char ('tas002')

    voice as0525
    asumi "Okay, Yusuke! I'm going back to the dorm ahead of you!"
    yusuke "H...hey!"

    $ char ()

    "After she tells me this, she quickly leaves the rooftop."
    "And I'm here alone and confused."

    $ bgfx ('black')
    $ bgm (9)
    $ bgfx ('bg05b')
    $ char ('tyo001')

    voice yo0156
    yagami "Oh, Yusuke! You haven't left yet."
    yusuke "You haven't either, Ms. Yagami."

    voice yo0157
    yagami "Well, I'm a teacher and I've got some club activities like the 'Baked Potato Club.'"
    yusuke "I...see... See you tomorrow then."
    "Telling her, I try to leave, but Ms. Yagami stops me."

    $ char ('tyo019')

    voice yo0158
    yagami "Wait, Yusuke! I'm a girl, you know. I'm curious about others' relationships."
    yusuke "And so?"

    $ char ('tyo007')

    voice yo0159
    yagami "Don't try fooling me. What's going on between Asumi and you?"
    yusuke "There's nothing between us."

    $ char ('tyo019')

    voice yo0160
    yagami "Liar! You were looking at her all during class."
    yusuke "It was just a coincidence. Besides, Asumi doesn't care about me..."

    $ char ('tyo002')

    voice yo0161
    yagami "You seem troubled. Why don't you tell me about it?"
    yusuke "But don't you have a club to go to?"

    $ char ('tyo007')

    voice yo0162
    yagami "Forget about it! I can't leave a lamb alone and in trouble!"
    yusuke "...Okay."
    "Okay, you're a good teacher..."

    $ bgfx ('black')
    $ bgm (4)
    $ bgfx ('bg04b')
    $ char ('tyo013')

    voice yo0163
    yagami "Hmm... I don't think you need to think about it that hard."
    yusuke "Really? But I don't think Asumi really cares about me..."

    $ char ('tyo004')

    voice yo0164
    yagami "Hey, you're a man. Don't be so weak! Don't care about such little things. Just be strong and hold her tight!"
    yusuke "Okay..."
    "I decide to follow Ms. Yagami's advice. But still, I'm nervous..."

    call blackout from _call_blackout_138
    $ bgfx ('bg02b')
    $ char ('tna001')

    voice na0193
    namiki "Oh, Yusuke. Welcome back! Come here!"
    yusuke "Ohh... It's Namiki."

    $ bgm (12)
    $ bgfx ('sora08')

    "She pulls me into her room and asks me many questions."
    "Especially about my long conversations on the phone. I know who told Namiki."
    "Talkative parents!"
    "Without caring about my feelings, Namiki jokes around and makes fun of me."
    "But suddenly, her expression changes. She looks so serious."

    $ bgfx ('bg09c')
    $ char ('tna016')

    voice na0194
    namiki "By the way, I wanted to ask you about that, Yusuke."
    yusuke "About what?"

    $ char ('tna025')

    voice na0195
    namiki "How long are you planning on staying here?"
    yusuke "Huh? You mean in your room?"

    $ char ('tna019')

    voice na0196
    namiki "No, I'm talking about this girls' dorm! Did you forget you don't actually belong here!?"
    yusuke "O...okay. Good question...ha ha ha..."
    "I don't want her to ask me anything more about the subject."
    "I think about it sometimes, but I usually forget about it."
    "Right now, I have a lot more to think about than that."
    yusuke "I'm going back to my room! Bye!"

    $ char ('tna020')

    voice na0197
    namiki "Hey! Say hello to Moe-Moe! And tell her I love her!"
    yusuke "Moe-Moe would pass out if I told her that."

    call blackout from _call_blackout_139

    "How long have I been with Ms. Yagami and Namiki?"
    "When I get back, everybody has already started eating dinner."

    $ bgfx ('bg01c')
    $ char ('tas106')

    voice as0526
    asumi "You're late, Yusuke! Going out on the town at night is the first step to bad habits!"

    $ char ('tma107')

    voice ma0112
    marumu "Bad, bad."

    $ char ('tto202')

    voice to0255
    tomoe "I was worried about you. Where have you been?"
    yusuke "I've been imprisoned in Namiki's room. She said to say hello to you, Moe-Moe."

    $ char ('tto204')

    voice to0256
    tomoe "...Okay."
    "Hmm? Was Moe-Moe depressed for a second...?"
    "Is Namiki doing something bad to Moe-Moe behind our backs?"
    "From the views of normal people, Namiki is a trouble maker."

    jump episode15_d

label episode15_asumi_d:

    yusuke "After graduation... Hmm, should I go to college? Huh?"

    $ sfx ('SE44')

    "I thought it was just outside noises to begin with, but,"
    "Someone's knocking on the closet door calling me."
    "I open the door."

    $ sfx (delay=0.1)
    $ bgfx ('bg01d')
    $ char ('tas105')

    yusuke "Ah, Asumi?"

    voice as0529
    asumi "Can I talk to you now?"

    $ bgm (14)
    $ bg ('bg02c')
    $ char ('tas105')

    yusuke "...It's already cold here. It's much different than Tokyo."

    voice as0530
    asumi "I see."
    "Before, I would've been mad and said, 'Don't bother me, it's so late!'"
    "But now, I'm happy to have her bother me like this."
    "It feels like this is a date, even though the atmosphere isn't very romantic."
    yusuke "I only want you beside me. I don't need anything else."

    $ char ('tas124')

    voice as0531
    asumi "Huh? What did you say?"
    yusuke "N...never mind."
    "It's good she didn't hear me. I'm embarrassed at my words."
    "I'll talk about something else."
    yusuke "After graduation, I think I should go to college. How about you, Asumi?"

    $ char ('tas121')

    voice as0532
    asumi "I haven't decided yet."
    yusuke "I see... Huh?"
    "I notice she's a bit different than usual."
    "But I can't tell what's different about her."
    "I stare at her for a while and then I get it."
    "She looks sad... At least that's what I think."
    "And then, she notices my gaze and stares at me."

    $ char ('tas137')

    voice as0533
    asumi "What?"
    yusuke "Ah, I was just thinking you're different than usual today, Asumi."

    $ char ('tas106')

    voice as0534
    asumi "I'm always like this! It's you! You've acted weird since coming back."
    yusuke "B...because you told me that..."

    $ char ('tas124')

    voice as0535
    asumi "That?"
    yusuke "Ah... (Oops!)"
    "I can't change the subject anymore."

    $ bgfx ('black')
    $ bgfx ('bg02c')
    $ char ('tas105')

    voice as0536
    asumi "I see. You've been worrying about that?"
    yusuke "Of course! This is a big deal for me!"

    $ char ('tas124')

    voice as0537
    asumi "Girls are complicated! Especially when someone has a boyfriend."

    voice as0538
    asumi "But what? Do you want to tell people, 'I'm going out with Asumi, who's pretty and smart!?'"
    yusuke "N...no... I don't mean that."
    "I can't talk back to her. Looking at me, Asumi chuckles,"

    $ char ('tas146')

    voice as0539
    asumi "I love you, Yusuke. Can't you trust me?"
    yusuke "Of course I trust you. I won't doubt your words anymore!"

    $ char ('tas112')

    voice as0540
    asumi "Okay, thanks. Heh heh!"
    "We both understand each other now (...I'm still a bit anxious)."

    $ bgfx ('sora10')

    "Asumi looks up at the fall night sky and happily runs around."
    "After a while, she comes back to me. She tells me with her head turned to the side,"

    $ bgfx ('bg03c')
    $ char ('tas105')

    voice as0541
    asumi "I think it's important to think about the future, but right now is also important!"
    yusuke "That's true..."

    voice as0542
    asumi "We should enjoy our youth just as much as we enjoy our future!"

    voice as0543
    asumi "I'll try as hard as I can! Join me, Yusuke!"
    "I tell her,"
    yusuke "Yes. I will. I'd be happy to do that with you!"

    $ char ('tas137')

    voice as0544
    asumi "Oh!? I thought you'd say, 'What a bother' or something else."
    "I proudly tell her,"
    yusuke "Of course I will. I'm your boyfriend, remember?"

    $ char ('tas145')

    voice as0545
    asumi "I see. I think you've changed. SMOOCH!"

    $ char ('tas412')

    yusuke "Um...h...hey..."

    $ char ('tas146')

    voice as0546
    asumi "The kiss was just a thank you."

    $ bgfx ('sora08')

    "The light kiss with her bright smile."
    "I'm so attracted to her. I want to stay with her for the rest of my life."
    "Our youth with love has just begun."

    jump episode15_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

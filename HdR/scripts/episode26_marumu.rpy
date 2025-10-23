label episode26_marumu:

    call blackout from _call_blackout_54
    $ bgfx ('bg03a')

    "I hear somebody walking towards me."
    "The footsteps suddenly stop beside me."
    "I slowly turn around."

    $ char ('tto601')
    $ bgm (3)

    voice to0796
    tomoe "Hello, Yusuke."
    yusuke "Hi, Tomoe. Oh, sorry...I'd better call you 'Ms. Katsuragi,' shouldn't I!?"

    voice to0878
    tomoe "Don't even bother. Besides, I'd feel so weird if you called me by my last name."
    yusuke "True."
    "Without realizing it, we smile at each other."
    "The reunion with my beloved roommates."
    "From the bottom of my heart, I'm happy to be meeting them again."

    call blackout from _call_blackout_55
    $ bgm (14)

    "Since Tomoe and I have so much we want to say to each other, we continue talking for a while."
    "Yet something bothers me during the conversation."
    "It's about Marumu."
    "I haven't seen her for a long time."
    "I wonder if Marumu has changed."

    $ bgfx ('bg03a')
    $ char ('tto601')
    $ music_stop ()

    voice to0879
    tomoe "Then Toshibo did...are you listening, Yusuke?"
    yusuke "Oh, sorry."
    "I quickly apologize to her."
    "Yet Tomoe doesn't seem angry."

    $ char ('tto619')

    voice to0880
    tomoe "You were thinking about your girlfriend, weren't you!?"
    yusuke "No, I was just..."

    $ char ('tma501')

    voice ma0447
    marumu "Just what?"
    yusuke "Nothing. Ah!?"

    $ char ('tma510')

    marumu "......"
    "I snap my mouth shut, but it's too late."
    "When I turn around, I see Marumu standing there."
    "It doesn't look like she's changed a bit."

    $ char ('tma501')
    $ bgm (13)

    voice ma0448
    marumu "Hi, Moe-Moe."

    $ char ('tto619')

    voice to0881
    tomoe "Marutan, it's been a long time. You look great!"
    "They start talking like old friends."
    "After a few seconds, I jump into their conversation as well."
    yusuke "How are you, Marutan?"

    $ char ('tma510')

    marumu "......"
    yusuke "......"
    "No answer."
    "I start wondering if I've said something wrong."

    voice ma0449
    marumu "Yusuke, you aren't thinking about me."
    yusuke "Well, it's..."

    voice ma0450
    marumu "You forgot me."
    yusuke "No, that's not true! I just..."
    "Tomoe happily stares at us."

    $ char ('tto601')

    voice to0882
    tomoe "Marutan, you should forgive him. He's just shy, that's all."

    $ char ('tma501')

    voice ma0451
    marumu "A popular girl, tough business."
    yusuke "Ha ha ha."
    "She's just like before, it's so like her!"
    "Then we all start smiling."
    "At our first reunion, I find Marumu hasn't changed a bit."

    jump episode26_b

label episode26_marumu_b:

    $ cg ('em_0102', pos=[ALIGN(0.0, 1.0)])

    "My thoughts turn to the old days with Marumu."
    "I've kept the memories tucked away, but little by little, I vividly recall them."
    "Memories of happiness, good old days."

    $ bgfx ('black')

    "We get tired from walking around so much."
    "We decide to take a break in the park."

    $ bgfx ('bg14a')

    "Tomoe lives close by, and she tactfully made us some lunch."
    "It tastes great, as always."

    jump episode26_c

label episode26_marumu_c:

    $ cg ('ea_0812')
    $ bgm (11)
    $ cg ('ea_0816')

    voice as1130
    asumi "How're you doing, Moe-Moe?"

    voice as1131
    asumi "You're so kind, so as always, I'm pretty sure you care about others more than yourself."

    $ cg ('ea_0803')

    voice as1132
    asumi "Or have you become more mature, showing your feelings to others? I haven't see you for a year, so you may look totally grown up now."

    $ vox ('to0993')
    $ cg ('ea_0813')

    voice as1133
    asumi "I like you like that, but remember, you also need to be stronger."

    $ cg ('ea_0814')
    $ vox (delay=0.3)

    voice as1134
    asumi "The next time I see you, I hope you're stronger than ever and can retort back at me sharply."

    $ vox ('to0990')
    $ cg ('ea_0805')

    voice as1135
    asumi "I suppose Marutan is doing well."

    voice as1136
    asumi "Have you changed at all? Anyway, I think you're lovely just as you are."

    $ vox ('ma0529')

    voice as1137
    asumi "Until the last moment, you were the most mysterious person I've ever known."

    $ cg ('ea_0816')
    $ vox (delay=0.3)

    voice as1138
    asumi "That's why I want to tell you this..."

    $ cg ('ea_0804')

    voice as1139
    asumi "You're great!"

    $ cg ('ea_0803')

    voice as1140
    asumi "Just keep being yourself, okay?"

    $ vox ('ma0530')
    $ cg ('ea_0811')

    voice as1141
    asumi "And...Yusuke."

    voice as1142
    asumi "I'd like to tell you one thing."

    $ cg ('ea_0814')
    $ vox (delay=0.3)

    voice as1143
    asumi "Be a tolerant person!"

    $ cg ('ea_0803')

    voice as1144
    asumi "Oh, and one more thing. If you want, you can dress like a girl again!"

    $ vox ('ma0531')
    $ cg ('ea_0810')

    voice as1145
    asumi "Anyway, I believe you guys will make a great couple."

    $ vox (delay=0.3)

    jump episode26_d

label episode26_marumu_e:

    $ cg ('ea_0816')

    voice as1146
    asumi "That's the end of my lovely video letter! And Yusuke, keep the tape as your family treasure, okay?"

    $ cg ('ea_0802')

    voice as1147
    asumi "I'm a little tired. Maybe I should take a nap."

    $ cg ('ea_0813')

    voice as1148
    asumi "Since I can't go to the reunion, I want to see you guys in my dreams. Honestly, I miss you so much."

    $ cg ('ea_0812')
    $ cg ('ea_0806')

    voice as1149
    asumi "I'd love to see you guys someday. Take care."

    $ say_hide ()
    $ music_stop ()
    $ cg ('ea_0827')
    $ sfx ('SE11', loop=True)
    $ cg ('ea_0826')
    $ set_vol ()

    "Then she shows us the brightest smile we've ever seen."
    "The only thing left is static and noise."
    "We all keep staring at the snow without saying a word."

    $ sfx (delay=1.0)
    $ bgfx ('black')

    "When I realize it, we're shedding tears."
    "Nobody knows why it happened."
    "Tears unconsciously rolled down our cheeks as we watched the video from Asumi."
    "And nobody could stop the tears."

    $ bgfx ('sora04')
    $ bgm (9)

    "After a while, we all leave the Harukaze Dorm."
    "We return the dorm key and say goodbye to Ms. Yagami."
    "On the way to the bus station, nobody says a word."
    "Perhaps we're all lost in reminiscing."
    "Everybody remains silent the whole time."

    $ bgfx ('bg03a')
    $ char ('tto604')

    voice to0883
    tomoe "Well, I have some shopping to do on the way back home."
    yusuke "Okay, take care."

    $ char ('tma501')

    voice ma0452
    marumu "See ya, Moe-Moe."
    "As Tomoe leaves, she sometimes looks back and waves at us."
    "All of sudden, she freezes and rushes back to us."
    "Then she takes a deep, long breath."

    $ char ('tto619')
    $ bgm (10)

    voice to0884
    tomoe "I just want to remind you one more time that we'll definitely meet again. That's a promise, okay?"
    "My heart bursts with joy."
    yusuke "Absolutely."

    $ char ('tma501')

    voice ma0453
    marumu "I'll definitely come too."

    $ char ('tto619')

    voice to0885
    tomoe "Good, good!"
    "We shake on it."
    "This isn't the end."
    "Through the video, Asumi taught us that our friendship will last forever."

    $ bgfx ('sora04')

    "This time Tomoe gradually disappears from sight."
    "Now, there's only the two of us left."
    "Abruptly, Marumu glances at me."
    "Then she mutters,"

    $ music_stop ()
    $ bgfx ('bg03a')
    $ char ('tma501')

    voice ma0454
    marumu "Yusuke, do you have a girlfriend?"
    yusuke "Nope."
    "I gently smile at her."
    "I'm neither popular nor a playboy."
    "Yet it doesn't matter because I do have somebody in mind."
    "Once, the feeling began to fade deep inside me, but Asumi reminded me of it today."
    "I really appreciate her sending the message to us."
    "Truly, from the bottom of my heart."

    $ char ('tma529')

    "Somehow, Marumu looks confused."

    voice ma0455
    marumu "I've studied a lot!"

    voice ma0456
    marumu "But I still don't know..."
    yusuke "About what?"
    "For a moment, she hesitates to answer the question."
    "Yet she doesn't stop talking."

    voice ma0457
    marumu "Have I become a real woman?"
    yusuke "Marumu..."

    voice ma0458
    marumu "...Yusuke."
    "I recall the last scene with Marumu vividly."
    "I know I love her more than a year ago."
    "Thus, I want to be with her."
    "I really think so."
    "In fact, I've been thinking about her for a year."
    "I'd like to tell her how I feel about her now."

    $ bgm (14)

    "Today, we've been reunited."
    "And we walked around places full of memories."
    "Through the video, Asumi reminded me about my feelings."
    "That's why I really want to be honest with myself."
    "I smile at her looking so anxious."
    yusuke "I know I have to keep studying too, so..."

    voice ma0459
    marumu "So?"
    yusuke "Let's study together."

    $ char ('tma501')

    "As I say this, she gazes at me."
    "I look back at her and continue my story."
    "Unlike before, I know exactly what I want."
    yusuke "Would you like to be my girlfriend again?"

    voice ma0460
    marumu "...Yusuke, Yusuke!"
    "She can't quite express her feelings in words."
    "Her face shows a little irritation."
    "Yet it seems as if she's looking for the right words."
    "hen she tries to calm down a little."
    "At last, she expresses her feelings in words."
    "Her true feelings."

    $ cg ('em_03')
    $ unlock_gallery ('g3e10')

    voice ma0461
    marumu "I'm happy!"
    "She jumps into my arms."
    "Then I hug her tight."
    "We both know we've just started our true relationship."
    "Our romance has just made a new start."
    "To learn about true, everlasting love together."

    $ unlock_ending ('Marumu')

    jump episode26_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

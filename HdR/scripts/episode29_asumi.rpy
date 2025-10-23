label episode29:

    $ Fnum = 27
    $ save_name = "Asumi Route: The place where the sun sets..."

    $ bgfx ('white', diss_long)
    $ bgm (9)
    $ bg ('sora04', tag=0)
    $ bg ('sora02', tag=1, pos=[HIDE(3.5, 0.5)])
    $ _fx (diss_long)
    $ sfx ('SE18')
    $ wait (2.0)

    yusuke "It feels like everything is moving so slow here."

    $ sfx (delay=0.3)

    "Until two hours ago, I was so busy."
    "But now I'm not."
    "Little by little, the memories of my high school days come back to me."
    "Stopped time once again quietly goes on."
    "The time I spent with them quietly continues."
    "The time with my best friends in the whole world became a part of my past."
    "But I know nothing has changed here."
    "The air is here."
    "And our wonderful memories."
    "It's almost time for our reunion."
    "Without realizing it, I continue recalling my faded memories."


    call ep_start from _call_ep_start_2

    $ bgfx ('sora04')
    $ bgm (10)

    yusuke "A year has passed from that day."
    "Actually, it's not quite a year, to be exact."
    "My college entrance exam is in the spring, and I haven't taken it yet."
    "It's four months shy of a year ago that we promised to meet again."
    "I wait for her in the cold."
    "I've been waiting for her."
    "She suddenly decided to come home and said she wanted to see me right away."
    "That's why I've been waiting for her in the cold."
    "Tomoe and Marumu won't come today."
    "It's a reunion for only the two of us."
    "I missed her so much. And at last, I can see her today."
    "Anyway, I guess I got here a bit too early."
    yusuke "The next bus won't be here for another hour..."
    "Unfortunately, I didn't bring anything to kill time."
    "I usually take a vocabulary book with me, even when I go out to eat."
    "But I didn't bring it today, so I have to spend an hour doing nothing."
    yusuke "Well, I guess it's okay to relax like this once in a while."
    "That's right."
    "I just need to wait an hour for her."
    "Then I can get my treat, which I've been waiting for a long time."

    call blackout from _call_blackout_13
    $ bgfx ('bg03a')
    $ char ('tas601')
    $ sfx ('SE18')

    yusuke "Ah!"

    voice as1150
    asumi "Why do you look so spaced out?"
    yusuke "......"

    $ sfx (delay=0.3)

    voice as1151
    asumi "By any chance, have you forgotten my face?"
    yusuke "No, but..."

    voice as1152
    asumi "Then what?"
    yusuke "I just think you look great, you know."

    $ char ('tas645')

    voice as1153
    asumi "It sounds like you've finally learned how to treat a lady."
    yusuke "No, I wasn't trying to compliment you..."

    $ char ('tas646')

    voice as1154
    asumi "No, I guess not."
    "I just want her to be happy with my words without being sarcastic."
    "I just told her how I really felt."

    $ char ('tas601')
    $ bgm (14)

    "Compared to eight months ago, Asumi looks a lot more mature."
    "On the other hand, I haven't changed much."
    "I don't think I've kept the promise, 'I'll be a real man before seeing her next time.'"
    "All of sudden, she grabs on to me."

    $ char ('tas646')

    voice as1155
    asumi "It looks like you've become a little more mature than before."
    yusuke "Do you think so? Well, maybe because I worried about the college entrance exam I'll be taking soon."

    $ char ('tas645')

    voice as1156
    asumi "It sounds like you've been having a tough time."
    yusuke "Yep! I'll bet you don't understand my anxiety."

    $ char ('tas621')

    voice as1157
    asumi "Perhaps not."
    "Somehow, she looks a little blue now."
    "I don't know why she looks at me like that, but when she shows me her big smile, I forget all my troubles."
    "Then she holds my hand."

    $ char ('tas645')

    voice as1158
    asumi "Well, let's forget about the exam for a while and have some fun together, okay?"
    yusuke "Okay, but what are we going to do?"

    $ char ('tas646')

    voice as1159
    asumi "We're going to have a real date. What do you think?"
    "It looks like she's enjoying herself."
    "Then she pulls on my hand and starts running."

    $ bgfx ('sora02', diss_long)
    $ bgm (13)

    "We follow a path to places we used to spend time together."

    $ bgfx ('bg02a')

    "Happy memories."

    $ bgfx ('bg06a')

    "Bitter memories."

    $ bgfx ('bg03a')

    "And memorable places."

    $ bgfx ('bg16a')

    "Everything in this town is nostalgic to us."
    "I'm so glad it hasn't changed much."

    $ bg ('bg16a')
    $ char ('tas645')

    "And I would like to thank God for giving me the chance to spend time with her here once again."

    $ bgfx ('sora07')

    "Eventually, we head towards our most memorable spot."
    "It's the beach where we had our first official date."

    $ music_stop ()
    $ cg ('ea_0601')
    $ unlock_gallery ('g2e2')
    $ sfx ('SE57', loop=True)

    "Not once did I come back to the beach after the date."
    "That's why I missed this place so much."
    "When I came here with her a year ago, it was Summer. Since it's Winter now, it looks a little different."
    "As I look at her face,"
    "I realize again that she's really grown up."

    $ sfx (delay=3.0)
    $ bgm (10)

    yusuke "I haven't been for a walk like this in a long time!"

    voice as1160
    asumi "That's right. You've stayed at home studying for the exam."
    yusuke "Actually, I've been taking an exam preparation class. But still, I haven't had fun going out like this in a while."

    voice as1161
    asumi "Well, I'm glad to be a change for you."

    $ cg ('ea_0602')

    yusuke "Thanks to you, I feel relaxed now."
    "She's right. This really is a good opportunity to release my tension."
    "But more than that, I'm glad to see her."
    "I've been waiting to meet her again since she left."
    "Since my wish came true, I think I'll be able to concentrate on my studies better starting tomorrow."

    voice as1162
    asumi "Well, you really should thank me, you know."
    yusuke "I know, I know. Anyway, I'm so glad to see you, Asumi."

    $ cg ('ea_0604')

    voice as1163
    asumi "Actually, I'd like to thank you."
    yusuke "Huh?"
    "As I stare at her, she looks straight into my eyes."
    "And she says something unexpected."
    "Listening to her serious voice, I can tell she's not making fun of me."

    voice as1164
    asumi "Although you complain, you always listen to my self-centeredness to the end. Like today, I knew you had to study for the exam, but you still came to see me."
    yusuke "Oh, don't even worry about it. I wanted to see you too, you know."

    $ cg ('ea_0602')

    voice as1165
    asumi "I was always selfish, but anyway, thank you for bearing with me."
    yusuke "Asumi..."
    "Somehow, I feel strange hearing her thank me."
    "Honestly, I'm pleased to hear it."
    "But I think I expected her to say something different."
    "I wonder if something happened and forced her to change."
    "However, she's still the same person I used to know."
    "At least her voice and face are the same. I've really missed her."

    $ cg ('ea_0603')

    voice as1166
    asumi "I was really lucky to have met Moe-Moe and Marutan."

    voice as1167
    asumi "Yet the best thing was meeting you, Yusuke. I think I'm glad you knew about my weaknesses."

    $ cg ('ea_0604')

    yusuke "Same here. If I hadn't seen you that day, I might have..."

    voice as1168
    asumi "What?"
    yusuke "I might have died with hunger and cold."

    voice as1169
    asumi "I think we were destined to meet, anyway."
    "Again and so unlike her, she says something wonderful."
    "Nevertheless, I'd still like to agree with her."

    voice as1170
    asumi "Because of you and the others, I had a wonderful time."
    yusuke "You took the words right out of my mouth. You made my days a lot of fun too, you know."
    yusuke "I'll bet Moe-Moe and Marutan feel the same way."

    voice as1171
    asumi "If that were true, I'd really be happy!"
    "She gently smiles."
    "Somehow her smile looks more mature than before."
    "And it seems full of happiness."

    $ cg ('ea_0605', diss_long)

    voice as1172
    asumi "I'm so happy to see you again and talk about our good old days. I'm really glad I came back, you know."

    $ cg ('ea_0606')

    yusuke "Then stay here, don't go back to Greenland."
    "I say this jokingly."
    "Then she calmly smiles back at me."

    $ cg ('ea_0608')

    voice as1173
    asumi "I'm not going anywhere."
    yusuke "Really?"

    voice as1174
    asumi "Yeah. I want to be with you, so I came back."
    yusuke "Asumi..."
    "I'm really surprised."
    "I'm so surprised, I could probably fly."
    "I've been waiting to be with her for a long time."
    "If it were possible, I'd like to be with her forever."
    "And she just told me she feels the same."
    "She really came back to be with me!"
    "Suddenly, I'm filled with emotion."
    "My heart begins to beat so loud, I'm sure anyone a mile away could hear it."
    "My love is right next me, and I can touch her anytime I want."

    $ cg ('ea_0613', diss_long)

    "Her head softly touches my shoulder."
    "It feels so good to have her lean on me."
    "As I wonder if she might have lost some weight, she whispers in my ear,"

    voice as1175
    asumi "Because I..."
    yusuke "......"

    voice as1176
    asumi "I'm totally in love with you."
    yusuke "Having you tell me so bluntly, I'm a little embarrassed."
    asumi "......"
    yusuke "......"
    asumi "......"
    yusuke "...Asumi?"
    asumi "......"
    yusuke "Hey, are you sleeping?"
    asumi "......"
    yusuke "...Ha ha."

    $ music_stop ()
    $ sfx ('SE57', loop=True)

    "She puts her head on my shoulder and closes her eyes."
    "She looks so peaceful."
    "The soft ocean breeze surrounds us."
    "When was I ever this happy?"
    "It seems like Asumi always makes me happy."
    "And she gives me peace."
    "I know she's the one for me."
    "She's beside me, with her eyes closed."
    "It's such a peaceful moment."
    "It gives me some comfort, like the lull before a storm."
    "Asumi isn't the same person I used to know."
    "The incident in the car a few minutes later makes me realize it."
    "On the way to the emergency hospital..."

    $ bgfx ('black')
    $ sfx ('SE60', loop=True)

    "Asumi doesn't wake up."
    "The cold ocean wind blows at us."
    "I tried to wake her up, but she wouldn't."
    "Her forehead was burning hot."
    "I didn't know what to do."
    "So I called 911."
    "To get help from paramedics."
    "Then..."
    "I'm in the ambulance,"
    "Sitting right next to Asumi."
    "The sounds of the siren echo along the beach."
    "At last, she comes around."
    "Then she starts talking to me in a weak voice."

    $ sfx (delay=1.0)
    $ bgm (9)

    voice as1177
    asumi "Good. I finally found you."
    yusuke "Asumi!"
    "Can she hear me?"
    "She keeps staring at me and continues talking."
    "She looks in pain, and she uses all her energy to speak to me."

    voice as1178
    asumi "I wondered where you were. I just didn't want it to end without seeing you one last time."
    yusuke "What do you mean?"

    voice as1179
    asumi "Every night, I was so afraid to go to sleep. I was scared that I wouldn't wake up."

    voice as1180
    asumi "That's why I was so happy to see you and the others' faces in the morning."
    yusuke "Why do you say that? You're always full of pep and smile so much, remember?"

    voice as1181
    asumi "I couldn't waste even a day because I promised Asuka I'd do my best."
    yusuke "Asuka?"
    "Her name sounds so familiar."
    "I don't have any time to think about it."
    "I listen as I continue looking at her."
    "Because I know that's all I can do for her now."
    asumi "......"
    "I realize her hand is searching for something."
    "The hand eventually creeps around her waist and takes out something from her pocket."
    "With no more strength, she drops it on the floor."
    "I pick it up and give it to Asumi."
    "I'm sure I've seen it before."
    "She lost it once, and she was upset for a long time."
    "Even visiting the cemetery, she used to take it with her."
    "She holds it tightly so she won't lose it."

    $ cg ('ea_10', Dissolve(3.0))
    $ unlock_gallery ('g2e3')

    voice as1182
    asumi "That's why I've been doing my best for Asuka."

    voice as1183
    asumi "She wanted to study in Greenland, so I went there too."
    yusuke "......"
    "I don't get her story."
    "I'm totally confused."
    "Yet I keep listening to her."
    "Although she's only half conscious, she's trying to tell me something."
    "Something that is very important to her."
    "But little by little, she starts looking at me with vacant eyes."
    "Her voice sounds weaker too."

    voice as1184
    asumi "My parents knew this would happen to me."

    voice as1185
    asumi "So they suffered, but my mom still decided to bring me into this world."

    voice as1186
    asumi "They named me 'Asumi,' wishing my future would be bright and beautiful."

    voice as1187
    asumi "I love them so much."
    yusuke "......"
    "Not the words, I feel something else pouring into me."
    "The story of her life."
    "If her condition weren't like this, she'd probably take forever to tell me the story."
    "Suddenly, she seeks something in the air."
    "It looks as if she's trying to hug me."
    "I quickly hold her hand."
    "As she heaves a sigh of relief,"
    "she holds my hand back."
    "As if it will all suddenly disappear."

    voice as1188
    asumi "And..."

    voice as1189
    asumi "Moe-Moe, Marutan, and you gave me the greatest treasure I've ever had. I love you guys so much."

    voice as1190
    asumi "I love you...Yusuke..."
    yusuke "Asumi, Asumi...ASUMI!!"
    "She peacefully closes her eyes."
    "When the ambulance arrives at the hospital,"
    "Her white arm slips down."
    "And I silently scream."

    call blackout from _call_blackout_14
    $ bgfx ('sora07')

    "Asumi is hospitalized, and her parents come."
    "They look sad, but they don't seem really shocked."
    "Her parents knew this day would come someday."
    "Her parents let me stay with them as her doctor explains her condition."
    "They also tell me a lot of memories of her."
    "Even the things she did when she was a kid."
    "She was never afraid of her life ending at anytime, and she decided to do her best. They're really proud of her."
    "She knew she wouldn't live long. But instead of feeling sorry for herself, she felt blessed to be in this world."
    "You've been an inspiration to her everyday."
    "Tears well up in their eyes."
    "But I don't know anything."
    "It feels like the anxiety will crush my heart to pieces."
    "The fear makes my eyes and ears close tighter."
    "Otherwise, I'm sure I'll scream as loud as I can."
    "I shudder at the thought of losing her."
    "I don't think I can keep standing."
    "As her doctor whispers to her parents,"
    "The dreaded words pierce my ears."
    "The reality that even his medical team doesn't know how long she can last."

    $ sfx ('SE58', loop=True)
    $ bgfx ('black')

    "I think I just felt the tip of her finger move."
    "I've been holding her hand for a long time."
    "I grip her hand, so she'll know I'm here with her."
    "I feel her hand hold mine back a little."
    "It's weak, but it seems as if she's trying not to let go."
    "After a short while, she slowly opens her eyes."

    $ sfx (delay=3.0)
    $ cg ('ea_0701')
    $ unlock_gallery ('g2e4')

    voice as1191
    asumi "Mmm..."
    yusuke "......"

    voice as1192
    asumi "...Yusuke?"
    yusuke "Yeah?"
    "She gazes at me a while and squeezes my hand."
    "But she's so weak."
    "Then she looks straight into my eyes and starts talking."

    voice as1193
    asumi "I..."
    yusuke "......"
    asumi "......"
    "She wants to tell me something."
    "But somehow, she can't say the words."
    "I can feel it from her eyes."
    "Her parents said Asumi knows herself better than anybody else."
    "Of course, about her illness and condition as well."
    "She's also aware that even she doesn't know how long she can last."
    "Under the present circumstances, I assume it must be very hard to talk about."
    "If I were her, I'd probably lie there crying."
    "That's why I have to speak, not her."
    "To let her know what's on my mind."

    $ bgm (11)

    yusuke "It's my turn to talk, okay?"

    voice as1194
    asumi "Yusuke?"
    yusuke "You were really a pampered girl."

    voice as1195
    asumi "I know."
    "She calmly nods."
    "Then I burst out."
    yusuke "So it's my turn to be a little selfish, alright?"
    "I squeeze her hand."
    "I thought about this so many times, and finally, I've decided to tell her what's on my mind."
    yusuke "From now on, we will do everything that I want to do. Until I'm satisfied, you can't get away from me, okay?"

    $ cg ('ea_0702')

    voice as1196
    asumi "But I..."
    "She's totally perplexed."
    "Because she knows she won't be able to keep the promise."
    "But I scold her for her faintheartedness."
    yusuke "I'll never forgive you if you simply disappear."
    yusuke "Until now, I'm pretty sure you've had everything your own way."
    yusuke "If so, live for me from now on!"

    voice as1197
    asumi "Live?"
    "She's startled momentarily."
    "Probably from the moment she found out about her illness,"
    "She kept telling herself to live as long as she could."
    "That's why she's always tried to do her best."
    "However, when the terror of death crept up on her, it made her blind."
    "I can't let her be like that, not yet."
    "Without noticing it, tears well up in my eyes. I try hard to hold them back."
    yusuke "I won't forgive you if you go somewhere I can't go. I'll never let you do that."

    voice as1198
    asumi "But I...can't..."
    yusuke "Whatever happens, I'll always be with you."
    "I hold her hand tighter than ever."
    "I won't let her go. Although Asumi says she has to go somewhere, I won't leave her."
    "I swear to God, I'll be with her, no matter what happens."
    yusuke "Promise me, Asumi. You'll try to live and stay with me as long as you can."

    voice as1199
    asumi "You're so selfish, you know that?"
    "Tears trickle down her face."
    "As she half cries and half smiles, I tell her a joke,"
    yusuke "I guess I caught your egotism."
    asumi "......"
    "She holds my hand back."
    "I can feel something change inside her."
    "I definitely see a note of resolution in her eyes."
    "The resolution to live."
    "This is not the end."
    "We'll keep living together until a natural death parts us."
    "I can feel her strong determination in her warm hand."

    voice as1200
    asumi "I'd love to be with you, forever."
    yusuke "Sounds good."

    $ bgfx ('white')
    $ cg ('ea_0703', Dissolve(2.0))

    "We stare at each other and smile."
    "In fact, we don't know how long we can be together like this."
    "But until then, I'll make her keep smiling."
    "No matter what happens, I swear I won't leave my love."

    call breakskip from _call_breakskip_1
    $ music_stop ()
    $ say_hide ()
    $ cg ('ea_1102', Dissolve(5.0))
    $ unlock_gallery ('g2e5')
    $ vox ('as1372')
    $ cg ('ea_1103', Dissolve(5.0))
    $ wait (2.0)
    $ vox (delay=0.3)
    $ bgfx ('white')

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

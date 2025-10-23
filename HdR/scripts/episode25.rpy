label episode25:

    $ Fnum = 25
    $ save_name = "Episode 25: Our Bright Youth"

    $ bgfx ('sora02')
    $ bgm (14)

    "I don't know how long it's been since Hikaru moved into the Harukaze Dorm."
    "It feels like starting all over again."
    "That's because Asumi drags us and Hikaru around."
    "It's Asumi's plan to get back our lost blossoming time."
    "Everyday, we're busy doing many 'friend' things."
    "I think we all have a fruitful, happy time together."
    "Especially with our new friend, Hikaru."
    "Namiki used to hate Hikaru, but now she really seems to like her."
    "I know Moe-Moe is Namiki's favorite girl, so I asked her if she had 'a change of heart.' She told me, 'I still like her, but I think I can have another darling, can't I!?'"
    "However, Hikaru thinks Namiki is a bit hard to deal with. Thus, poor Hikaru sometimes runs to our room and hides until Namiki leaves."
    "We somehow get along with the Trio de Bitches, and the important thing is they've forgotten about 'the mysterious roommate.' Phew, I'm safe!"
    "Hikaru is definitely our dorm mate, though she doggedly keeps saying she doesn't belong to us."

    call blackout from _call_blackout_123
    $ bgfx ('bg13a')
    $ chars ('tas015', 'thi001')
    $ bgm (12)

    voice as0837
    asumi "It's fun living in this dorm, isn't it!?"

    voice hi0060
    hikaru "...You think."

    $ char1 ('tas005')

    voice as0838
    asumi "Since we all hang out together, it's so fun!"

    voice hi0061
    hikaru "Fun? I think it's just annoying."

    $ char2 ('thi002')

    voice hi0062
    hikaru "But it may be better than just being alone."

    $ char1 ('tas037')

    voice as0839
    asumi "Don't act like a cool, mature girl! Come on, smile!"

    $ cg ('sde_0801')
    $ unlock_gallery ('g5e12')
    $ cg ('sde_0802')

    "Asumi tickles Hikaru."
    "Yet Hikaru keeps her poker face."
    hikaru "......"

    $ cg ('sde_0803')

    voice as0840
    asumi "Aren't you ticklish?"

    voice hi0063
    hikaru "Of course I am."

    $ bgfx ('black')

    voice as0841
    asumi "Ha ha ha ha!"

    voice as0842
    asumi "Hey, look everybody! I'm tickling Hikaru, but her expression doesn't change!"

    voice hi0064
    hikaru "Stop it!"

    $ bgfx ('sora01')

    "The air fills with happiness and smiles."
    "I wonder if such peaceful days have helped Hikaru..."
    "...to defrost her frozen heart, little by little."
    "At least Hikaru doesn't stare at us with sharp, icy looks anymore."
    "No matter what, she's one of us, and we'll make great memories together."
    "We all accept her as our buddy."
    "Our life is full of fun everyday."
    "Thus, there's no such words like 'waste of time' in our dictionary."

    call blackout from _call_blackout_124

    "We've finally reached a turning point in our happy, endless school life."
    "Today is the start of a new phase for all of us."
    "It's our graduation."


    call ep_start from _call_ep_start_19

    $ bgfx ('sora02')
    $ sfx ('SE41')
    $ bgm (13)

    "Familiar faces begin gathering in the classroom."
    "Of course, I see Asumi and the rest of the crew as well."
    "However, I don't spot Hikaru among them."

    $ sfx (delay=0.3)
    $ bgfx ('bg04a')
    $ char ('tto002')

    voice to0382
    tomoe "...I wonder where Hikaru is."

    $ char ('tas005')

    voice as0843
    asumi "She's probably planning 'a big entrance' to the ceremony. She looks cool whatever she does, remember?"
    yusuke "...In your dreams, girl!"

    $ char ('tas037')

    voice as0844
    asumi "Huh? What did you say, Yusuke?"
    yusuke "No, I didn't say anything, your highness."
    "All of sudden, I start looking back upon bygone days with my friends."
    "From the beginning to the end, Asumi always acted bossy."

    if F015 != 0:

        "If I could have remembered her weak points, the situation might have changed a little. But I guess it's too late now."

    $ bgfx ('black')
    $ bgfx ('sora01')

    "And time has passed since my first day."

    voice ma0203
    marumu "...Chimes."

    $ sfx ('SE51')

    "Although the bell has chimed, I don't see Hikaru anywhere."

    $ bgfx ('bg04a')
    $ char ('tyo014')

    "Ms. Yagami and all of us stare at her empty seat with worried looks."
    "Anyway, we have to start the last homeroom class."
    "Even by the end of the class, Hikaru hasn't showed up."
    "Ms. Yagami starts leading us to the gym where our graduation ceremony will be held."

    $ sfx (delay=0.3)
    $ char ('tyo010')

    voice yo0184
    yagami "Everybody, please head towards the gym. Oh, don't cry yet. You can cry as much as you want later, okay?"
    yusuke "But it seems like you're crying more than anybody else here, Ms. Yagami."

    call blackout from _call_blackout_125
    $ bgfx ('bg04a')

    "We all start to worry about Hikaru since she hasn't shown up yet."
    yusuke "I wonder what happened to Hikaru."

    $ char ('tma017')

    voice ma0204
    marumu "Overslept."

    voice as0845
    everyone "I don't think so!"
    "Marutan is always Marutan."

    $ char ('tna001')

    "I don't know why, but Namiki suddenly comes to our classroom."
    "Did she come here to check on us?"
    "Namiki notices Hikaru isn't in the room."

    voice na0212
    namiki "Hey, you guys! Oh my...Hikaru isn't here, is she!?"

    voice to0385
    tomoe "No, she's not."

    $ char ('tna007')

    voice na0213
    namiki "She acted a little weird last night and wouldn't talk to me much either."
    asumi "......"

    $ char ('tna016')

    voice na0214
    namiki "Oh, but it's her usual behavior..."
    "That's Namiki's poor stand-up comedy."
    "We all stand blankly with our mouths wide open."
    "Anyway...where's Hikaru?"
    "Everybody looks so blue worrying about her."
    "Then Ms. Yagami walks toward us."

    $ char ('tyo002')

    voice yo0185
    yagami "Come on guys, please go to the gym! I'll look for Hikaru, so don't worry about her."

    $ char ('tas044')

    asumi "......"
    "Asumi abruptly stands up."
    "We all know what she's thinking now."

    $ char ('tas006')
    $ bgm (5)

    voice as0846
    asumi "I'm going to look for her!"

    $ char ('tyo023')

    voice yo0186
    yagami "Hey, Asumi! Somebody, please stop her!"
    yusuke "......"
    "Yet nobody stops her."
    "Because we all know no one can stop her now."
    "Asumi rushes out of the room."
    "Soon, Tomoe, Marumu, and I stand up."

    $ char ('tto013')

    voice to0386
    tomoe "We'll go look for Hikaru as well. Sorry, Ms. Yagami."

    $ char ('tma001')

    voice ma0205
    marumu "Graduate together."
    yusuke "We're all worried, so let's..."

    $ char ('tyo023')

    voice yo0187
    yagami "Hey guys, wait!"
    "She tries to stop us."
    "Then Namiki stands blocking her."

    $ char ('tna002')
    $ bgm (10)

    voice na0215
    namiki "Go look for her! I'll take care of the rest!"
    yusuke "Thanks, Namiki!"

    voice to0387
    tomoe "Thank you so much, Namiki."

    voice ma0206
    marumu "Thank yooooou!"
    "But still, Ms. Yagami continues trying to stop us."

    $ char ('tyo023')

    voice yo0188
    yagami "Hey guys, wait! Your important ceremony will start..."

    $ char ('tna025')

    voice na0216
    namiki "Ms. Yagami, I'll take all the blame, so please let them go."

    $ char ('tyo015')

    voice yo0189
    yagami "Namiki..."
    "After all, Ms. Yagami couldn't stop us ditching the ceremony."

    $ music_stop ()
    $ char ('tyo022')
    $ bgm (14)

    voice yo0190
    yagami "Ah, they're really gone..."

    $ char ('tna025')

    voice na0217
    namiki "It doesn't mean anything if Hikaru doesn't attend the graduation ceremony with them."

    $ char ('tyo001')

    voice yo0191
    yagami "The most valuable thing you can find here is 'friendship.' Don't you agree, Namiki?"

    $ char ('tna002')

    voice na0218
    namiki "Yes, I think so too."

    $ char ('tyo002')

    voice yo0192
    yagami "Were you serious?"

    $ char ('tna013')

    voice na0219
    namiki "Excuse me?"

    $ char ('tyo002')

    voice yo0193
    yagami "About...you're going to take all the blame for letting them go..."

    $ char ('tna020')

    voice na0220
    namiki "Oh, it's time to go to the gym!"

    $ music_stop ()
    $ char ('tyo023')

    "Ms. Yagami stands there blankly with her mouth wide open."
    "After all, one fourth of her students won't be at the ceremony."

    $ bgfx ('black')

    if F015 == 0:
        jump episode25_asumi

    elif F015 == 1:
        jump episode25_tomoe

    elif F015 == 2:
        jump episode25_marumu

label episode25_b:

    call blackout from _call_blackout_126
    $ bgfx ('sora01')

    "On the way to the observatory, the others join us."
    "We all keep running, hoping to find Hikaru there."
    "Without her, we won't be able to graduate with smiles."


    call ep_middle from _call_ep_middle_20

    if F015 == 0:
        jump episode25_asumi_b
    else:

        jump episode25_tomoe_marumu_b

label episode25_c:

    $ chars ('tas006', 'thi002')
    $ bgm (9)

    voice hi0070
    hikaru "I became so weak after I met you guys."

    voice hi0071
    hikaru "You smashed my shell to pieces, so I had to reveal my true nature."

    voice hi0072
    hikaru "I can't hide it. Actually, I don't know how anymore!"

    voice as0866
    asumi "Why? Why do you have to cover yourself? You're you, and that's something that will never change!"

    voice hi0073
    hikaru "I know what I am! I'm the person who always hurts others' feelings. I'm not considerate, and I can't respond well to kindness. That's who I am!"

    voice hi0074
    hikaru "When that kind of person goes out in the real world, I'm very sure she'll be thrown into despair. Then, she may lose faith in life and rebuild her shell. That means the chain of sequences will never end."

    $ char1 ('tas042')

    voice as0867
    asumi "...Hikaru."

    $ music_stop ()
    $ char1 ('tas002')

    voice as0868
    asumi "You still don't get it, do you!? What an ass! Do you think you're a tragedy heroine or something?"

    $ char2 ('thi004')

    voice hi0075
    hikaru "What!?"

    $ char1 ('tas007')

    voice as0869
    asumi "Why do you think you're so different from others? I know everybody has their own personalities, but you're not an oddball at all."

    $ char1 ('tas042')

    voice as0870
    asumi "Even me, I'm also scared of starting a new life without my friends around."

    voice as0871
    asumi "Sometimes, I'm afraid to greet a new day because it may not be the same as yesterday, and I don't know what'll happen to me. But I assume everybody has to live with some kind of worry."

    $ char2 ('thi002')

    hikaru "......"

    $ char1 ('tas005')

    voice as0872
    asumi "But I'm okay! I won't ever give up, and I believe you'll be fine too!"

    $ char2 ('thi001')

    voice hi0076
    hikaru "You think...I'll be fine?"

    $ char1 ('tas001')

    voice as0873
    asumi "You just forgot something very important. That's why you got frightened. But if you went to school with us, I don't think you'd be scared at all!"

    $ char2 ('thi002')

    voice hi0077
    hikaru "Why do you say that?"

    $ char1 ('tas045')

    voice as0874
    asumi "Because...then you will know you've already found the most important treasure."

    voice hi0078
    hikaru "The most important treasure?"

    $ char1 ('tas002')

    voice as0875
    asumi "Yep, that's our friendship. Just look around you, then you'll see we have so many friends who care about us. That means we're not alone at all!"

    $ bgm (10)

    "Asumi points at us."

    $ chars ('tto025', 'tma001')

    "We all smile at Hikaru."

    $ chars ('tas001', 'thi002')

    voice as0876
    asumi "Do you think you're alone in this universe? That's bullshit! You have Moe-Moe, Marutan, and Toshibo. Oh, and...you have Yusuke too, remember?"
    yusuke "Did she almost forget about me? That's not fair."

    voice ma0207
    marumu "Don't cry."

    voice as0877
    asumi "You also have Namiki, Ms. Yagami, and even the Trio de Bitches. Maybe you forgot, but you have your classmates and dorm mates as well."

    $ char2 ('thi001')

    hikaru "......"

    $ char1 ('tas007')

    voice as0878
    asumi "One last and important thing is..."
    "Asumi takes a short pause and continues in an assured manner,"

    $ char1 ('tas015')

    voice as0879
    asumi "Don't forget you have me, the leader of the group!"
    hikaru "......"

    $ char1 ('tas024')

    voice as0880
    asumi "Hikaru?"

    voice hi0079
    hikaru "From when?"

    $ char1 ('tas001')

    voice as0881
    asumi "What?"

    voice hi0080
    hikaru "From exactly when did you become the leader, Asumin?"

    $ char1 ('tas005')

    voice as0882
    asumi "Of course, from the beginning!"

    $ char2 ('thi005')

    voice hi0081
    hikaru "Ha ha ha...hic."

    $ char2 ('thi008')

    "Amazed, Hikaru slowly begins to smile, and her countenance changes as well."

    $ char1 ('tas045')

    "Asumi quietly snuggles up to Hikaru."
    "We all gather around them."
    "I want to grow up with these friends."
    "And head towards our bright future."
    "That's why we never gave up on Hikaru."

    $ bgfx ('sora02')

    voice as0883
    asumi "Let's graduate together!"

    voice to0388
    tomoe "Let's go, Hikaru!"

    voice ma0208
    marumu "...Should auld acquaintance be forgot, and never brought to mind..."

    voice ts0058
    toshibo "Meoow!"

    voice hi0081a
    hikaru "Hic, hic."
    "Hikaru nods and continues crying."
    "Asumi holds her hand and says,"

    voice as0884
    asumi "We'll be friends forever!"

    call blackout from _call_blackout_127
    $ bgfx ('bg06b')

    "We return to our school."
    "Of course, we don't see any of our classmates in the classroom."
    "Only Ms. Yagami with a sneer is waiting for us."

    $ bgfx ('bg04b')
    $ char ('tyo001')
    $ bgm (4)

    voice yo0194
    yagami "Hello, guys."

    $ char ('tas030')

    voice as0885
    asumi "You don't look as mad as I thought you would be."

    $ char ('tyo007')

    voice yo0195
    yagami "Do you really think so?"

    $ char ('tas012')

    voice as0886
    asumi "You look like an angel, Ms. Yagami!"

    $ char ('tma007')

    voice ma0209
    marumu "...An angel smile."

    $ char ('tyo007')

    voice yo0196
    yagami "Do I look like an Angel? Then you guys need to check your eyes!"

    $ music_stop ()
    $ char ('tyo005')

    "All of sudden, she stares at us with an icy look."
    "She looks so scary."
    "Somehow, I calmly imagine such things."
    "Of course, it's to run away from the severity of reality."
    "We didn't mean it, but we still ruined something very important for Ms. Yagami."
    "Her commencement..."

    $ char ('tyo023')
    $ bgm (16)

    voice yo0197
    yagami "The commencement finished a long time ago. You guys wrecked my once a year event!"

    $ char ('tto004')

    voice to0389
    tomoe "Ah, well..."

    $ char ('tas042')

    voice as0887
    asumi "Sorry."

    $ char ('tyo004')

    voice yo0198
    yagami "If you think you can get off just by apologizing, you've got another thing coming! Anyway, have you learned your lesson yet? If you haven't, you'll end up learning it for the next year."
    yusuke "You mean...!?"
    "Then somebody else mentions the cruel words."

    $ char ('tma016')

    voice ma0210
    marumu "...Failing."

    $ char ('tyo004')

    voice yo0199
    yagami "You guys deserve it! Since you've ditched the ceremony, you're not expecting to receive your diplomas, right guys?"

    $ char ('tas042')

    voice as0888
    everyone "That's not fair!!"
    "We all turn blue at the finality of her words."
    "It's not fair telling us to repeat our senior year on our graduation day!"
    "Just then..."
    "Hikaru was standing a step behind, but she suddenly walks up to her."

    $ char ('thi001')
    $ bgm (9)

    voice hi0082
    hikaru "Ms. Yagami, please. Please let everybody graduate. I..."
    "Ms. Yagami calmly asks her,"

    $ char ('tyo014')

    voice yo0200
    yagami "Don't you want to graduate with them?"

    $ char ('thi002')

    voice hi0083
    hikaru "...Yes, I do."

    $ char ('tas042')

    voice as0889
    asumi "...Hikaru."

    $ char ('thi002')

    "It sounds like she's trying to take all the responsibility."
    "But if she does that, she can't keep her promise to graduate with us!"
    "Of course, Ms. Yagami doesn't accept such an offer."
    "Yet it's her way of showing her kindness."

    $ char ('tyo002')
    $ bgm (13)

    voice yo0201
    yagami "I can't accept your offer, Hikaru. If you don't graduate, I'm sure the other silly four will keep you company."

    $ char ('thi004')

    voice hi0084
    hikaru "...Ms. Yagami."

    $ char ('tyo007')

    voice yo0202
    yagami "There are only five of you in here, but I'm going to pass out your diplomas. When I call your names, step forward, okay?"

    $ char ('tas002')

    voice as0890
    everyone "All right!"
    "Without realizing it, we all cheer at the same time."

    $ char ('thi009')

    "Even Hikaru looks happy, and tears of joy come to her eyes."

    $ bgfx ('black')
    $ bgfx ('sora05')

    "We couldn't attend the commencement with the other classmates."
    "But now, we receive our diplomas from Ms. Yagami, one by one."
    "And each of us recall our happy school memories."

    $ bgfx ('bg04b')
    $ bgm (10)
    $ char ('tas045')

    "After all, Asumi kept going as fast as she could from beginning to end."
    "I don't think the words, 'once in a while, let's relax and have a break,' can be found in her dictionary."

    if F015 == 0:

        "Yet, that's why I fell in love with her."
    else:


        "Yet, that's why we followed her lead, although we sometimes complained."

    if F015 == 1:
        $ char ('tto025')
    else:
        $ char ('tto001')

    "Asumi and Tomoe are like 'plus and minus.'"
    "But I think Asumi could act like she did because of Tomoe."

    if F015 == 1:

        "I really appreciate Asumi being her roommate."
        "That's how I met such a wonderful girl."
    else:


        "I really appreciate her being our roommate."
        "Little by little, her mind grew stronger than ever. And I don't believe she'll ever stop developing."

    $ char ('tma001')

    "Marutan, or I could call her, Marumu. She's really a mysterious girl."

    if F015 == 2:

        "But I believe she's the purest girl in our group."
        "I was lucky to have met her."
        "I hope she never changes. Because I strongly believe she's all right, just as she is."
    else:


        "However, I assume she's the purest girl I've ever known."
        "That's why she enjoyed school like she did."
        "I don't think she'll ever stop being a wonder girl."

    $ char ('thi009')

    "Hikaru also received her diploma."
    "She couldn't graduate a year ago, but I think this will help release her loneliness at last."
    "Anyway, I wonder why Hikaru doesn't have any nicknames?"
    "I notice I don't have any either. Silly me!"

    $ char ()

    "Finally, it's my turn to step forward."

    $ char ('tyo001')

    voice yo0203
    yagami "Yusuke Sawada."
    yusuke "Yes, ma'am!"
    "I was only here for a year, but I really enjoyed it."
    "Just for the moment, I'd like to appreciate my dumb parents."
    "I receive the proof of my hard work from Ms. Yagami."
    "As she hands me my diploma, she says in an undertone,"

    $ char ('tyo007')

    voice yo0204
    yagami "Wow! You lived in that room for a whole year, after all!"
    yusuke "...You're right. I guess I survived."
    "She reminds me what an outrageous thing I did."

    call blackout from _call_blackout_128

    "And so, we all safely graduate."
    "Now we should go back to our dormitory and..."

    $ bgfx ('bg04b')
    $ char ('tyo002')

    voice yo0205
    yagami "Alright, let's go to the schoolyard!"

    $ char ('tto001')

    voice to0392
    tomoe "But why, Ms. Yagami?"

    $ char ('tyo002')

    voice yo0206
    yagami "We shouldn't let the others wait too long for us, right?"
    yusuke "The others?"

    $ bgfx ('black')

    "When we find who's waiting, we're speechless."
    "All of our classmates have been waiting for us!"

    $ bgfx ('bg11b')
    $ char ('tas044')
    $ bgm (14)

    voice as0891
    asumi "How come...?"

    $ char ('tyo002')

    voice yo0207
    yagami "Everyone has been waiting for you guys. They all agreed that it wouldn't mean anything if some of their classmates were missing from the graduation picture."

    $ char ('tto025')

    voice to0393
    tomoe "You guys..."

    $ char ('tma003')

    voice ma0213
    marumu "...Thank you."

    $ char ('tyo010')

    "Ms. Yagami's eyes are wet with tears."

    voice yo0208
    yagami "Even I'd be sad if you guys weren't in the picture. This will be our last group picture, right?"

    $ char ('tas042')

    voice as0892
    asumi "Ms. Yagami..."

    $ char ('tyo001')

    voice yo0209
    yagami "What is it, Asumi?"

    $ char ('tas012')

    voice as0893
    asumi "Your speech was a little old fashioned, you know."

    $ char ('tyo007')

    voice yo0210
    yagami "...I guess you don't want to be in our picture, do you!?"

    $ char ('tas039')

    voice as0894
    asumi "Noooooooo!"

    $ cg ('e3_04')
    $ unlock_gallery ('g5e5')

    "Asumi isn't able to be in the picture because she displeased Ms. Yagami. Alright, no more joking! Of course, we took the last class picture with her as well."
    "All of our classmates are in the picture."
    "I'll never forget about them, ever..."
    "Our graduation ceremony comes to an end."

    $ music_stop ()
    $ bgfx ('white')
    $ bgfx ('black')

    "However, some people are so strange."
    "I see three shadows heading toward us to disturb us!"

    $ bgfx ('bg11b')
    $ char ('tik999')

    "It's the 'Trio de Bitches.'"
    "I'm pretty sure they've already taken their class picture. What are they doing here?"
    "As usual, they stand blocking us."
    "Why does the last day at school have to be the worst? What do they want? Do they want to settle this, once and for all?"
    "Yet their faces look a bit milder."

    $ bgm (10)

    voice yu0054
    akane "We had a lot of fights, so I wanted to tell you..."

    voice as1345
    asumi "...What?"

    voice yu0055
    akane "Because of you, the last three years were never boring."

    voice hs0031
    kaoru "If I hadn't had anyone to tease, I probably wouldn't have realized just how great I am."

    voice fu0028
    midori "Thanks to you, I collected a lot of interesting data. After all, I guess I could say it was fun."

    $ char ('tas015')

    voice as1346
    asumi "Huh, good for you. I guess you'll never forget our names."

    $ char ('tyu002')

    voice yu0056
    akane "I probably couldn't forget your names, even if I wanted to. You too, the class president and the strange beetle-like girl!"

    $ char ('tto007')

    voice to0994
    tomoe "Akane, I..."

    $ char ('tma001')

    voice ma0536
    marumu "I've saved your name on my brain, too."

    $ char ('ths001')

    voice hs0032
    kaoru "And you! The wanna be leader, who looks after everybody like a big sister...and of course, the cold bitch!"

    $ char ('tna019')

    voice na0381
    namiki "What the hell!? Did you just say I'm 'the wanna be leader?'"

    $ char ('thi005')

    voice hi0115
    hikaru "He he."

    $ char ('tfu001')

    voice fu0029
    midori "Yusuke, you were the most interesting of all."
    yusuke "Should I say thanks?"
    "As she mentions it, I suddenly realize something."
    "Perhaps, the Trio de Bitches knew about my second identity."
    "But they didn't rat me out."
    "If my guess is right, I should thank them from the bottom of my heart."
    "It seems like they've said everything they wanted to tell us."
    "The last battle is moving towards its finale."

    $ char ('tik999')

    voice yu0057
    akane "Well, it's time to say goodbye. I'll bet we won't see each other ever again."

    $ char ('tas045')

    voice as1347
    asumi "But still, I'll never forget you."

    $ music_stop ()
    $ char ('tas005')

    voice as1348
    asumi "Yeah, just remember me as one of your silly school memories!"

    $ bgm (16)
    $ char ('tyu002')

    voice yu0058
    akane "Hey! Those are my words, idiot!"

    $ bgfx ('sora05')

    "Ah, that's exactly what I thought! Like this, our last battle seems to carry over to our dorm."

    $ bgfx ('black')
    $ music_stop ()
    $ bgfx ('sora09')

    "It's time for our graduation party!"
    "After we return to the dorm, we start whooping it up right away."
    "Naturally enough, Asumi and Namiki are hyper, and somehow, I see the Trio de bitches having fun as well."
    "Tomoe and Marumu seem unusually high-spirited and talkative."
    "It looks like Hikaru is also enjoying herself and smiling happily at her friends."
    "And as expected, I become the girls' toy."
    "Poor Yusuke..."

    $ bg ()

    if F015 == 0:
        jump episode25_asumi_c

    elif F015 == 1:
        jump episode25_tomoe_c

    elif F015 == 2:
        jump episode25_marumu_c

label episode25_end:


    call ep_finish from _call_ep_finish_16

    $ renpy.end_replay()
    $ unlock_episode (25)

    jump episode26
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

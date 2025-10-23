label episode07:

    $ Fnum = 7
    $ save_name = "Episode 7: U-SUKE Exposed!"

    $ bgfx ('sora01')

    "This room is always filled with tons of surprises."

    $ bgfx ('bg01a')
    $ chars ('tas105', 'tma101')
    $ bgm (3)

    voice as1393
    asumi "Marutan. You're cute, but you always look so subdued."

    voice ma0543
    marumu "...Subdued?"

    $ char1 ('tto225')

    voice to1007
    tomoe "Hey...I've been wondering if I could coordinate Marutan's fashion every once in a while."

    $ char2 ('tma108')

    voice ma0544
    marumu "...You could."

    $ bgfx ('sora01')

    "Tomoe does her best to coordinate 'beauty' on Marumu."

    $ bgfx ('bg01a')
    $ chars ('tas145', 'tto220')

    voice as1394
    asumi "Oh my...she's so cute!"

    voice to1008
    tomoe "See? I thought these things would suit Marumu, and I was right!"

    $ empat ('j6')
    $ char ('tma201')

    voice ma0545
    marumu "...A rabbit?"

    $ char ('tma222')

    voice ma0546
    marumu "...SLURP-SLURP."

    $ empat ()
    call blackout from _call_blackout_193

    "We find unexpected skill and prettiness this way."
    "I guess everybody has an unexpected side or two."
    "Like that person..."


    call ep_start from _call_ep_start_30

    $ bgfx ('bg04b')
    $ char ('tyo001')

    voice yo0014
    yagami "Hey, Yusuke."
    yusuke "Oh, Ms. Yagami. What can I do for you?"
    "I stammer as Ms. Yagami hails me."
    "I'm about to get ready to go home in the ladies' room."
    "She looks straight into my eyes and says,"

    $ char ('tyo013')

    voice yo0015
    yagami "I have a question. Recently, students have seen an unfamiliar girl in the Harukaze dorm."
    yusuke "R...really!?"
    "I have a bad feeling about this."

    voice yo0016
    yagami "The girl wears glasses just like yours. She's slim but tall for a girl...just about your height."
    yusuke "Oh...yeah? (Oh my.)"
    "Is she trying to trick me? Does she already know everything!?"
    "Do I think this way because I'm feeling guilty about what I'm doing?"

    voice yo0017
    yagami "No one knows about this girl. I wonder which room she lives in or which class she attends."
    yusuke "Err...is that so?"

    $ char ('tyo007')

    voice yo0018
    yagami "By the way, you live in an apartment, don't you? I want to visit your place to see how you're doing. He he."
    "...Is she intentionally hunting me down?"
    "It sounds like it."
    "However, Ms. Yagami doesn't ask me anything else about this 'mysterious girl.'"

    $ char ('tyo001')

    voice yo0019
    yagami "Okay, then. I've got to go take care of club activities. You want to join one? I have a list of recommendations."
    yusuke "N...no thanks. See you."
    "I run away from her."

    $ bgfx ('black')
    $ bgfx ('bg05b')

    yusuke "A list of clubs. She must be in charge of all of them."
    "She's so kind, and that's why she couldn't refuse when people asked her to become a coach in more than ten club activities!"
    "...Is she kind or does she just like people?"

    voice to0089
    tomoe "...Yusuke?"

    $ char ('tto001')

    yusuke "Oh hey, Moe-Moe...I mean Tomoe."

    $ bgm (3)

    "Even though I've officially become a temporary roommate, I should call her by her name when we're alone."
    "Tomoe and I pass each other in the hallway. She's heading out somewhere."
    yusuke "Are you doing the student union stuff?"

    voice to0090
    tomoe "...Uh-huh. I'm returning these books."
    yusuke "I see."
    "Tomoe still looks stiff in front of me."
    "I wonder if she feels uncomfortable because she doesn't like boys or maybe it's just me."
    yusuke "Well, no wonder. I accidentally peeped at her without a shred of clothing on."

    voice to0091
    tomoe "...Did you say something?"
    yusuke "No...it's nothing."
    "I want to make a better impression of myself to her."
    "Because we are roommates now."

    menu:
        " "
        "Help Tomoe.":


            $ F017 += 1
        "Leave her alone.":


            "However, she's still cautious of me."
            "She'll hate me if I become persistent."
            yusuke "......"
            tomoe "......"

            $ char ()

            "Tomoe tries to hold all the books that are piled up next to me."
            "And I'm about to leave her alone."

            voice to0961
            tomoe "Heave-ho... Yaa!"
            "I see the books have scattered all over the floor when I turn around."
            "Tomoe dropped them."
            "She picks them up in a flurry. Well, I can't leave her alone now."

    yusuke "Let me help you, Tomoe."

    $ char ('tto022')

    voice to0092
    tomoe "Oh?"
    "I forcibly take some of the books in her hands."
    "Then, I start walking towards the library."
    yusuke "Let's finish this up quickly and go home, all right?"

    $ char ('tto034')

    voice to0093
    tomoe "Yeah...sure."
    "Tomoe shyly (cautiously maybe?) follows me."
    "Her bashful manner is somewhat attractive."
    yusuke "What am I thinking!? Focus, Yusuke!"

    $ cg ('sde_0101', diss_long)
    $ unlock_gallery ('g5e6')
    $ bgm (2)

    yusuke "I'll take care of the higher shelves."

    voice to0094
    tomoe "D...don't worry. This is my job. Besides, you don't know where to put back these books."
    yusuke "Well, that's true, but..."
    "She returns all the books to where they're supposed to be. Wow, she's like a librarian."
    "She said it's her job. Yep, she's serious about her task."
    "Then, I hear a small, familiar scream."

    $ cg ('sde_0108')

    voice to0095
    tomoe "Yaah!"
    yusuke "Tomoe, are you alright?"

    $ cg ('sde_0101')

    voice to0096
    tomoe "I'm fine. I just lost my balance, that's all."
    "She's standing on a ladder and placing the books back on the shelf."
    "She doesn't look like a person with reflexes. She looks scary on the ladder."
    yusuke "Here, let me do that."

    voice to0097
    tomoe "No, let me finish this. But..."
    yusuke "But?"

    voice to0098
    tomoe "I'd appreciate it if you would hold the ladder for me."
    yusuke "Sure. No problem!"
    "I firmly hold down on the ladder."
    "It won't move now, even if Tomoe loses her balance again."
    "I'm not doing this to impress her, but I hope she is."
    "I look up at her as I expect this."
    "And I realize I've failed her again."
    "Because I see what I'm not supposed to see now."
    yusuke "...Oh my."

    voice to0099
    tomoe "I'll be done in a minute. Yusuke?"
    "O...okay, take your time."

    voice to0100
    tomoe "Why are you looking away from...ah!?"
    "Tomoe realizes it."
    "I can clearly see her panties from here."

    $ cg ('sde_0107')

    voice to0101
    tomoe "Oh no! I...I...!"
    "She pulls the hem of her skirt down with her hands."
    "And quite naturally, the books that were in her hands obey the law of gravity."
    "A couple of big, fat hardcover books hit me on the head."
    "I release the ladder and cover my head in pain."

    $ cg ('sde_0108')
    $ bgm (7)

    voice to0102
    tomoe "Ahh!? Yaaaaahhh!!"
    "Tomoe completely loses her balance."
    "Now, she falls on me."

    call effect ('SE40', ETYPE3) from _call_effect_48

    voice to0103
    tomoe "Ohh...ouch."

    $ bgfx ('black')

    yusuke "Umm...Romoe, fer phew haulait?"
    "I bear the pain and ask her 'Are you alright,' but I don't sound right."
    "Something is covering my face."
    "I can't see a thing."
    "Something soft is wrapped around my face."
    "Anyway, I have to sit up. Then, I hear a sorrowful moan as I rise up."

    $ music_stop ()

    voice to0104
    tomoe "Ahh...no..."
    yusuke "What do you mean, 'no?'"

    voice to0105
    tomoe "Yusuke, please don't move...ohh."

    $ cg ('ht_0201', diss_short)
    $ unlock_gallery ('g2e6')

    $ bgfx ('black', diss_short)

    "I'm such a man of vivid imagination, but I've never dreamed of this somewhat unique position with Tomoe."

    $ bgfx ('bg12b')
    $ char ('tto034')

    yusuke "...Excuse me."
    tomoe "......"
    yusuke "I'm sorry."

    $ char ('tto011')

    voice to0106
    tomoe "You don't need to apologize. I'm the one who lost my balance."
    yusuke "Still, if I hadn't see your...err..."

    voice to0107
    tomoe "I asked you to hold the ladder. Don't worry."
    yusuke "......"
    "The way she behaves is totally different from Asumi."
    "We both try to take full responsibility for this."

    $ cg ('ht_0201')

    "Anyway, Tomoe was on me in such an erotic..."

    $ bgfx ('bg12b')
    $ char ('tto031')

    yusuke "No! Stop it, Yusuke!"

    $ char ('tto001')

    tomoe "???"
    "I'd better stop remembering about the incident."
    "Her white panties and everything inside were clinging to my face..."
    yusuke "If Asumi discovers what happened...it'll be a mess."

    $ char ()
    $ char ('tto013')

    voice to0108
    tomoe "Don't ever, ever tell anybody. Please, Yusuke."
    yusuke "O...of course not."

    $ bgm (14)
    $ bgfx ('sora05')

    "Tomoe seriously looks into my eyes."
    "She has nothing to worry about."
    "I won't say a thing about today."
    "Now, Tomoe and I have a secret to share."
    yusuke "I don't feel bad, though."

    voice to0109
    tomoe "...Hey, Yusuke!"
    "Tomoe yells my name and stops me."
    "But it's too late."

    $ music_stop ()
    $ bgfx ('bg02b')
    $ char ('tyo007')

    voice yo0020
    yagami "Good evening, Tomoe. And you are...?"

    $ char ('tto036')

    voice to0110
    tomoe "Ex...excuse us, Ms. Yagami!"

    $ char ('tyo013')

    "Tomoe tells her and grabs my arm. She violently leads me inside the dorm."
    "True, I should never let Ms. Yagami see me in this costume, but if I run away from her like this, I'll draw attention as well."
    "For now though, I care more about Tomoe's warm hand."

    $ bgfx ('black')
    $ bgm (7)
    $ bgfx ('bg01c')
    $ char ('tas403')

    voice as0217
    asumi "What were you thinking!?"

    $ char ('tto007')

    voice to0111
    tomoe "I'm sorry."
    yusuke "You don't need to apologize. It's actually my fault."

    $ char ('tto013')

    voice to0112
    tomoe "No, that's not true. Only if I haven't done it..."

    $ char ('tas006')

    voice as0218
    asumi "It's your fault. Both of you!"

    $ char ('tto007')

    voice to0113
    yusuke_tomoe "Sorry."
    "We can't talk back to Asumi."
    "There's no use trying to protect each other here."
    "Still, what Asumi says is right. The situation doesn't look good."

    $ char ('tas007')

    voice as0219
    asumi "People are already talking about 'the mysterious girl' enough around here. Now, Ms. Yagami saw her with Moe-Moe, right?"
    yusuke "Ye...yeah."

    voice as0220
    asumi "Moe-Moe, Ms. Yagami will summon you and ask you about Yusuke."
    yusuke "......"

    $ char ('tto007')

    voice to0114
    tomoe "Hic hic."

    $ music_stop ()

    "Tomoe is so diffident and honest."
    "If she's called in by Ms. Yagami and asked about me..."
    "It's unusual, but the air in here feels heavy."

    $ bgfx ('black')

    "During the night."
    "Toshibo visits me."
    "I see a letter tied to his back."
    "'It's really my fault. Yusuke, I'm sorry.'"
    "But it's really not her fault."
    "Alright then. If she's called in by Ms. Yagami, I'll show up instead."
    "I make up my mind. However,"

    $ bgfx ('bg01a')
    $ char ('tas033')

    voice as0221
    asumi "She didn't call."
    yusuke "Yeah...right."

    $ char ('tto004')

    voice to0115
    tomoe "I couldn't sleep."

    $ char ('tma007')

    marumu "......"
    "The next morning..."
    "Nothing has happened since the incident."
    "Maybe we just worried too much?"
    "Or perhaps Ms. Yagami didn't see me?"
    "Either way, it's good to see that nothing has happened."

    $ bgm (16)
    $ bg ('bg02a')
    $ char ('tik999')

    voice yu0006
    akane "Hey, good morning to the people from the suspicious room."

    voice hs0006
    kaoru "We heard a rumor that you have a mysterious girl, a huge cat, and a beastly boy in your room. Is that true?"

    voice fu0006
    midori "Be careful. Somebody might catch you and have you all expelled."

    $ char ()

    "The Trio de Bitches. They're as spiteful as always."
    "However, what they just said isn't that far from the truth."

    $ char ('tas033')

    voice as0222
    asumi "Someone will find out about our secret sooner or later."

    $ char ('tto007')

    voice to0116
    tomoe "What are we going to do...?"

    $ char ('tas007')

    voice as0223
    asumi "Don't cry, Moe-Moe! We have to fight!"

    $ char ('tma016')

    voice ma0054a
    marumu "...Let's fight for the love we share."
    yusuke "......"

    call blackout from _call_blackout_194

    "I appreciate their kindness."
    "However, I can't have my roommates risk themselves anymore."
    "I'm the one who's responsible for all this trouble (well, except for Toshibo)."
    "I have to resolve this by myself!"
    "I hide behind my roommates on our way to the school and make up my mind."


    call ep_middle from _call_ep_middle_31

    $ bgfx ('bg05b')

    yusuke "Good!"
    "I put on a girls' uniform and spring out of the men's bathroom."
    "A male student nearby looks astounded to see me. I don't care right now."
    "Because I'm going to fight a duel with Ms. Yagami."
    "I can't think of anything now."

    $ bgfx ('black')

    "I walk around the huge school building and finally find her."
    "She's coaching the calligraphy club."
    "She sees me through the half opened door."

    $ vox ('yo0021')

    "She tells her students to wait inside and comes out of the room."

    $ vox (delay=0.3)
    $ bgm (4)
    $ bgfx ('bg05b')
    $ char ('tyo013')

    voice yo0022
    yagami "You...I remember you."
    yusuke "Can I have a word with you, Ms. Yagami?"

    voice yo0023
    yagami "Good. I've wanted to talk to you, too. But not now."
    yusuke "I'll wait outside until you finish."

    $ char ('tyo001')

    voice yo0024
    yagami "I also have a Gardening club and a Capsule Toy club after this."
    yusuke "Then...I'll wait."

    $ bgfx ('sora05')

    "What the hell is a Capsule Toy club!? Anyway, I decide to wait for her to finish everything."

    $ bgfx ('bg05b')
    $ char ('tyo002')

    voice yo0025
    yagami "Sorry to make you wait. It's kind of late, isn't it?"
    yusuke "No, I'm...sorry to bother you. I know you're busy, but..."

    $ char ('tyo007')

    voice yo0026
    yagami "Hey. You talk like a boy. You sound cute."
    yusuke "Oh."
    "ell, it's easier for me."

    $ char ('tyo002')

    voice yo0027
    yagami "Anyway, it's late. Why don't you come to my house?"
    yusuke "May I?"

    $ char ('tyo007')

    voice yo0028
    yagami "Of course. Let's eat something good!"
    "All of a sudden, I'm invited to her house."
    "With girl's clothes on."

    $ bgfx ('black')
    $ bgm (12)
    $ bgfx ('bg03b')
    $ char ('tyo116')

    yusuke "......"
    yagami "......"
    "I can't bear this silence."
    "My sole purpose in being here is to tell Ms. Yagami that I'm not a friend of Tomoe's."
    "Then she won't bother Tomoe about me."
    "Ms. Yagami might find out who I actually am."
    "Heck, I'll worry about that later!"
    "Again, I'll take sole responsibility for this. Those girls shouldn't have been involved in this to begin with."
    "...So I think, but I'm so tense now."
    "I want to clear this heavy atmosphere, but I can't come up with a good icebreaker so far."
    "She must be testing this 'mysterious girl.'"
    "Am I thinking too much?"
    "I have to relax before I say something I shouldn't."
    yusuke "Excuse me, Ms. Yagami?"
    yagami "......"
    yusuke "Ms. Yagami...Ms. Yagami?"

    $ char ('tyo117')

    voice yo0029
    yagami "...Huh?"
    "She's looking down at the floor, when she suddenly jumps."
    "Then she slowly turns to me and murmurs,"

    $ char ('tyo101')

    voice yo0030
    yagami "Oh, I'm sorry. I fell asleep."
    yusuke "Ah!?"

    $ char ('tyo107')

    voice yo0031
    yagami "Oops. Fuhhh! I'm kind of tired. Whew."

    $ char ('tyo116')

    "She's always so busy. She must be exhausted."
    "But still,"
    yusuke "Is it possible to fall asleep while you're walking!?"

    $ char ('tyo102')

    voice yo0032
    yagami "Yes, you can. Superstars sleep like this to save time, you know."
    yusuke "That's a lie!"
    "She looks around the dimly lit surroundings and gently smiles at me."

    $ char ('tyo107')

    voice yo0033
    yagami "It's still going to take a while to get to my place. Good night."

    $ char ('tyo116')

    yusuke "She's amazing."
    "She looks down again and closes eyes."
    "But she keeps walking at the same pace."
    "I've never seen anything like this...oh?"

    $ music_stop ()
    $ bgfx ('sora07')
    $ sfx ('SE46', loop=True)

    "I hear the thunderous sound of horns coming from the other side of the road."
    "One, two...more than ten of them?"
    "They're highly modified tractors."
    yusuke "Are they the ones Asumi once told me about?"

    $ sfx (delay=1.0)
    $ bgm (7)

    "They're the team called 'Tractors at Sunset.'"
    "They're local farmers and car racer wannabes. They've modified their tractors and started a racing team."
    "Those old men cruise around town before it gets too dark outside."
    "They follow the traffic rules, so they're quite harmless."
    "The only thing they do wrong is spread cold mud around and...what the!?"
    yusuke "Ms. Yagami! Ms. Yagami! The mud! Waaaaaahhh!!"

    menu:
        " "
        "Protect Ms. Yagami.":


            call blackout from _call_blackout_195
            $ bgfx ('sora08')

            yusuke "What should I do?"
            "I'm in the bathroom now."
            "The bathroom in Ms. Yagami's apartment, to be exact."
            "She kept walking in her sleep."
            "I tried to protect her and got covered with cold mud."
            "Ms. Yagami herself got a little mud in her hair and on her glasses."
            "Then she woke up alright."

            $ F01A += 1
        "Wake her up.":


            call blackout from _call_blackout_196
            $ bgfx ('sora08')

            yusuke "Oh my..."
            "I'm in the bathroom now."
            "The bathroom in Ms. Yagami's apartment, to be exact."
            "I tried to wake her up."
            "She woke up alright, but only after the tractors passed us."
            "Ms. Yagami and I were completely covered with cold mud."

    "She led me to the bathroom as soon as we got to her apartment."
    "I don't think she's peeping at me. I hurriedly take my clothes off and jump into the bathroom."
    yusuke "I won't get out of this mess if she sees me like this."
    "The hot shower washes everything away. Now, how can I get out of here?"
    "Ms. Yagami told me she would wash my clothes and dry them right away."
    "But I can't stay here naked until they're done."
    yusuke "What am I going to do...oh?"
    "What I'm seeing right now is..."
    "It's a person on the other side of the glass door."
    "The person is taking her clothes off...taking her clothes off!?"

    voice yo0034
    yagami "I'm joining you. My hair is messed up, you know. Maybe I shouldn't sleep while I'm walking, huh? Heh heh."
    yusuke "Ms. Yagami! I'm coming out, so please wait for me to..."

    voice yo0035
    yagami "Hey, are you embarrassed? Don't worry. It's kind of rare to see a shy girl like you nowadays."
    yusuke "No, that's not what I'm saying...ahh!!"

    $ cg ('ey_0101')
    $ unlock_gallery ('g4e3')

    "She's coming in."
    "There's no way out."
    "This is it. Everything is over now!"

    $ bgm (7)

    "I quickly turn away from her, but she'll find out any second."
    "No matter how thin I am or how well I hide my package, she'll find out."

    voice yo0036
    yagami "Hey, you don't need to stand in the corner. You're really a shy girl, aren't you?"
    yusuke "No, I told you to... WOW!"
    "She's bare naked."
    "She comes closer to me, step by step."
    "She IS naked. My privates vividly reflect the sight."
    "Don't come any closer...you're too close to me..."
    yusuke "Ms. Yagami, I..."

    $ cg ('ey_0103')

    voice yo0037
    yagami "Oh?"
    "She touches my back without warning."
    "Her hand slides down my back as if she's searching for something. Then she says,"

    $ cg ('ey_0102')

    voice yo0038
    yagami "You have a nice build for a girl."
    yusuke "You think?"

    voice yo0039
    yagami "I can't see you clearly without glasses, but you look like an athlete. Are you a member of a sports club?"
    "I don't answer her."
    "Instead, I ask her a question."
    yusuke "Ms. Yagami, are your eyes that bad?"

    voice yo0040
    yagami "Uh-huh. I'm almost blind without glasses. It's very inconvenient in the bathroom, you know."
    yusuke "That's very...unfortunate."
    "This must be providential help!"
    "Miracles do happen!"
    "I'm saved by a wonderful coincidence."

    $ bgm (4)

    yusuke "Okay, Ms. Yagami. I'm done."

    $ cg ('ey_0101')

    voice yo0041
    yagami "Hey, let me wash your back. Hold on."

    voice yo0042
    yagami "You really have a nice build. Why don't you join my Breast Stroke club?"
    yusuke "No thanks. What's the difference between the swimming club and the breast stroke club anyway?"

    $ cg ('ey_0102')

    voice yo0043
    yagami "You only need to learn one style, so you'll quickly improve. And you won't get as tired."
    "What a strange subject. She starts washing my back."
    "I can't evade her anymore."
    "I can't stop praying that she won't find out my secret."
    "Ms. Yagami obviously doesn't care about my feelings and continues asking me."

    $ cg ('ey_0101')

    voice yo0044
    yagami "Can I ask you a question?"
    yusuke "Sure...you can."

    voice yo0045
    yagami "What's your name?"

    $ cg ('ey_0104')

    yusuke "My name!?"
    "I quickly think."
    "A girlish name. A fake name. Anything...ANYTHING NOW!"

    $ cg ('ey_0107')

    "But I almost panic and can't come up with one."
    yusuke "I can't tell you that."

    voice yo0046
    yagami "You can't. How come?"
    yusuke "Because of my...personal reasons."

    voice yo0047
    yagami "...I see."
    "Uncomfortable silence."

    $ cg ('ey_0101')

    "She doesn't ask me any further about my name."
    "But that doesn't mean that she stops asking me questions."

    voice yo0048
    yagami "I haven't seen you around. Did you transfer here recently?"

    $ cg ('ey_0104')

    yusuke "......"

    voice yo0049
    yagami "I know how you feel. Sometimes, it's hard to adjust to a new environment."
    yusuke "...Yes."
    "She's misunderstanding, but what she says is very kind."

    $ cg ('ey_0101')

    "Good, she thinks I'm a newcomer at the school. There's less chance of my identity being exposed, I think. However..."

    $ music_stop ()
    $ cg ('ey_0102')

    voice yo0050
    yagami "I have a transfer student in my class. His name is Mr. Sawada."

    $ empat ('SE49')
    call cgeffect (graphics=['ey_0110', 'ey_0105'], fx=dissolve) from _call_cgeffect_12

    yusuke "......(POUND!)"

    $ empat ()

    voice yo0051
    yagami "Speaking of Mr. Sawada...you resemble him."

    $ empat ('SE49')

    call cgeffect (graphics=['ey_0110', 'ey_0105']*2, fx=dissolve) from _call_cgeffect_13

    yusuke "......(POUND! POUND!)"
    "My heartbeat is skyrocketing."
    "What am I doing here!? I'm losing it!"

    voice yo0052
    yagami "I get it! You are Mr. Sawada..."

    $ empat ()
    $ cg ('ey_0107')

    yusuke "Ohhh..."

    voice yo0053
    yagami "...Mr. Sawada's sister, aren't you?"

    $ cg ('ey_0104')

    yusuke "No...I'm not."

    voice yo0054
    yagami "Really? I just thought that the two of you look a lot alike."
    yusuke "Ohhh."

    $ cg ('ey_0101')

    "I sigh."
    "I try to relax now."
    "This situation isn't good for my heart. I must get away from here, IMMEDIATELY!"

    $ empat ('SE49')
    call cgeffect (graphics=['ey_0110', 'ey_0105'], fx=dissolve) from _call_cgeffect_14

    yusuke "Ahhh!?"
    "She sticks to me."
    "It feels so good."
    "Her two bulges are warm and soft. Again, my heartbeat skyrockets."
    "Something else raises its head again as well."

    $ empat ()
    $ cg ('ey_0106')

    voice yo0055
    yagami "Excuse me, but..."
    yusuke "Yes?"

    voice yo0056
    yagami "What's this?"
    yusuke "Which is?"

    $ cg ('ey_0104')

    voice yo0057
    yagami "...This."
    "Ms. Yagami sticks her arm out to my groin."
    "To my swelling dick."

    $ empat ('j5')
    call cgeffect (graphics=['ey_0110', 'ey_0107'], fx=dissolve) from _call_cgeffect_15

    "I can't move or say a thing."
    "I don't know how to react."
    "I'm completely flustered."

    voice yo0058
    yagami "Hey..."
    yusuke "I'm terribly sorry!!"

    $ empat ()
    $ bgm (7)
    $ bgfx ('black')

    "I must run away right NOW!"
    "I quickly head for the door."
    "However, the floor is slippery with liquid soap."
    "I slip on the tile floor,"
    yusuke "Waaaaah!!"
    "I see everything go upside-down as I float in the air."
    "Time stops for a moment."
    "But my fate won't change a bit."

    call effect ('SE45', ETYPE2) from _call_effect_49

    "The floor is so smooth. I can't get a grip on it."
    "I fall on my back and feel a sharp pain."
    "I'm slowly losing my sight."
    "My mind ceases to function. What have I done?"
    "Am I that stupid? Yep, I guess I am."
    "I hear something."
    "It's Ms. Yagami's shout of surprise."

    voice yo0059
    yagami "Hey, are you alright? Is this really...!?"
    "Her slim, white fingers are grabbing my dick."
    "Ms. Yagami realizes what she's holding and...screams."

    $ music_stop ()

    $ vox ('yo0060')
    $ pause (2.0)
    $ bgm (12)
    $ bgfx ('bg10c')
    $ char ('tyo114')
    $ vox (delay=0.3)

    voice yo0061
    yagami "Does it still hurt?"
    "The voice wakes me up."
    "Actually, I've been awake for a while."
    "But I lost my sense of reality for a while and couldn't understand what she had said."
    yusuke "Ohhh...it hurts!"

    voice yo0062
    yagami "Don't try to get up now. You hit your back pretty hard."
    yusuke "But..."

    $ char ('tyo104')

    voice yo0063
    yagami "Listen to your teacher, Yusuke."
    yusuke "Yes, ma'am...wait a minute!"
    "I'm a bit surprised."
    "But it's no wonder."
    "Even though she's nearsighted, she must've found out my true identity by now."
    "What do I do now?"
    "What do I tell Asumi, Tomoe, and Marumu?"
    "I came here to see Ms. Yagami by myself and blew it by myself."
    "There's only one choice left for me."
    "Tell her it's all my fault that I've lived in the girls' dorm."
    "Using my arms, not to hurt my back again, I slowly sit up."
    "I open my mouth as she gazes at my face."
    yusuke "Ms. Yagami, there's something I need to tell you."

    voice yo0064
    yagami "I can't believe that I couldn't tell it was you. Your clothes were different, but your voices sounded the same."
    yusuke "Tha...that's true."
    "I show her my taut smile."
    "Still, I have to tell her."
    "Before I can open my mouth again, Ms. Yagami points at the table and says,"

    $ char ('tyo107')

    voice yo0065
    yagami "Okay, let's eat something. We can talk later."
    yusuke "Oh...okay."
    "I feel a little saved."
    "Her usual, warm and tender smile."
    "Her smile purifies my guilty conscience a little bit."

    $ bgfx ('black', diss_long)
    $ bgm (4)
    $ bgfx ('bg10c')
    $ char ('tyo101')

    yusuke "Ms. Yagami?"

    voice yo0066
    yagami "Yes, what's up? Doesn't it taste good?"
    yusuke "Yes, it tastes great, but...you bought all of this at a convenience store?"
    "I was thinking she'd serve me her own home cooking."
    "But I only see ready-made TV dinners in front of me."

    voice yo0067
    yagami "You know what? This 'Half-cooked Sukiyaki Bowl' is good. I thought it was a joke, but it's not."
    yusuke "Is that so?"
    "Can't she cook? Or isn't she good at it?"
    "I wonder."
    "Doesn't her boyfriend say something about it? Wait, perhaps she doesn't have a boyfriend at all."
    "Then, I realize."
    "The clothes I'm wearing right now,"
    "They're men's clothes."
    "Do they belong to her boyfriend? However, this room doesn't show any signs of 'his' presence."
    "Did she buy these for me while I was passed out? But all the stores are closed by now."
    "I have a lot of things to think about. I eat without tasting any of it."

    call blackout from _call_blackout_197

    "Dinner is finished."
    "It's my confession time."
    "I'll tell her everything... and at the same time, I'll try not to say too much about Asumi and her roommates."

    $ bgfx ('bg10c')
    $ char ('tyo115')

    yusuke "Excuse me, Ms. Yagami?"

    voice yo0068
    yagami "Yes, tell me your story. Why you had to wear a girl's costume and go in the girls' dorm."
    yusuke "That's because,"

    voice yo0069
    yagami "Did you do that to see your favorite girl? Like Tomoe?"
    yusuke "No, that's not true! Tomoe is more like...she avoids me when we're in the same room."

    $ char ('tyo113')

    voice yo0070
    yagami "...The same room?"
    yusuke "Oh, I did it again!"
    "I curse my stupidity."
    "I have no way out now."

    $ bgfx ('black')
    $ bgm (12)
    $ bgfx ('sora08')

    voice yo0071
    yagami "POOF."
    yusuke "Ms. Yagami?"

    voice yo0072
    yagami "Ha ha ha!! You're funny! I never dreamed of you doing that!!"
    yusuke "Don't laugh at me so much."
    "I tell her the whole truth."
    "She just keeps laughing at me while I speak."

    $ bgfx ('bg10c')
    $ char ('tyo107')

    voice yo0073
    yagami "Sorry, but I can't stop laughing. I didn't know a boy lives in the Harukaze Dorm."
    yusuke "I guess it's time for me to leave. But please, don't force the girls out of there, too!"

    $ char ('tyo104')

    voice yo0074
    yagami "But I have to. No matter who they are, those who break the rules must be punished."
    yusuke "No...noooo!"

    $ char ('tyo107')

    "She tells me in a cold tone, then she starts chuckling."
    "How can she smile like that? I feel bad."
    "As she sees my taut face, she returns to her usual self and continues,"

    $ char ('tyo101')

    voice yo0075
    yagami "Well, no one broke the rules in this case. I can't punish anyone if there's no one to punish."
    yusuke "Oh?"
    "I must look pretty stupid with my mouth wide open."
    "I'm at a complete loss about what she's talking about."
    "She puts on a mischievous smile and tells me,"

    $ char ('tyo102')

    voice yo0076
    yagami "Harukaze Dorm regulations clearly state that you may not take any male student inside."
    yusuke "I know that. And the fact is those girls broke those regulations."

    $ char ('tyo101')

    voice yo0077
    yagami "But you just told me that you live in the dorm."
    yusuke "Yeah, so?"

    voice yo0078
    yagami "Then they didn't take a boy in. Hence, it's not against the regulations."
    "I lean forward and tell her,"
    yusuke "That's it!? I don't think your logic works in this case, though..."

    $ char ('tyo102')

    voice yo0079
    yagami "You want me to punish you then?"
    yusuke "Of course not...which means!?"
    "She smiles and says,"

    $ char ('tyo107')

    voice yo0080
    yagami "I'll inform the faculty that the mysterious girl is just a transfer student, and there's no problem at Harukaze Dorm."

    voice yo0081
    yagami "She just visits there to see her friends. That's all."
    yusuke "Th...thank you. Thank you very much!"
    "I'm glad. I'm relieved. She saved me."
    "But I still don't understand why Ms. Yagami helps me this much."
    "I appreciate her, but I don't get it."

    $ char ('tyo115')

    "Ms. Yagami stares at me with serious eyes while I feel these mixed emotions."

    voice yo0082
    yagami "If something goes wrong, not only you guys, but I will be punished as well."
    yusuke "Ms. Yagami..."

    $ char ('tyo101')

    voice yo0083
    yagami "Well, if that's the case, I'll take sole responsibility for this. He he."
    yusuke "......"
    "Another innocent person becomes involved."
    "She'll become our strong ally, but in a sense, she's victimized because of my mistakes."
    yusuke "I'll try to get out of there as soon as possible."

    voice yo0084
    yagami "By the way, Yusuke. I need to tell you something."
    yusuke "Yes, ma'am?"

    $ char ('tyo107')

    "She passes me the cleaned-up uniform and smiles."

    $ bgm (7)

    voice yo0085
    yagami "You saw, didn't you?"
    yusuke "Saw what?"

    voice yo0086
    yagami "Me...naked."
    yusuke "What!? I...err... in fact, I can't see a thing without glasses, just like you, so..."

    voice yo0087
    yagami "You saw me."

    menu:
        " "
        "Sorry, I did.":


            yusuke "...Yes."
            "I can't lie, you know."

            $ F01A += 1
        "No, I didn't.":


            yusuke "I mean..."
            yagami "......"
            yusuke "Well..."
            yagami "......"
            "I can't evade her any longer."
            "I feel like a criminal being interrogated."
            "If I were a criminal, I'd confess everything before the police actually got me in the interrogation room."
            "I shut up and nod."

    $ char ('tyo104')

    voice yo0088
    yagami "Then, I must punish you, even though you're my student."
    yusuke "Are you sure!?"

    voice yo0089
    yagami "Yes, I'm sure!"

    $ char ('tyo115')

    "Ms. Yagami looks dead serious. Then she returns to normal and tells me like a teacher,"

    $ bgm (4)
    $ char ('tyo101')

    voice yo0090
    yagami "I want you to come here occasionally and tell me the latest about you guys."
    yusuke "How come?"

    voice yo0091
    yagami "I want to be updated, just in case."

    $ bgfx ('black')

    "Again, I have to thank her."
    "Ms. Yagami is now officially involved in this situation."

    $ bgfx ('sora08')

    "I see stars."
    "The sea of stars here is quite different from Tokyo's."
    "I look up at the night sky and feel as if it's trying to suck me up. Then, I murmur,"
    yusuke "Ms. Yagami, you're TOO generous."


    call ep_finish from _call_ep_finish_24

    $ renpy.end_replay()
    $ unlock_gallery ('g5e7')
    $ unlock_gallery ('g5e8')
    $ unlock_episode (7)
    jump episode08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label episode10:

    $ Fnum = 10
    $ save_name = "Episode 10: The Baseball Fanatics"

    $ bgfx ('sora01')

    "In the afternoon, we have a class meeting."
    "The meeting will be presided by Tomoe!"
    "Well, she's the class president, anyway."
    "But I'm kind of worried about her."

    $ sfx ('SE51')
    $ bgfx ('bg04a')
    $ char ('tto001')

    voice to0995
    tomoe "We are going to talk about the class presentations for next week."
    "Tomoe tells her classmates."
    "But the class is still abuzz."
    "She tries to carry on with the meeting."

    $ sfx (delay=0.5)
    $ char ('tto013')

    voice to0996
    tomoe "Does anybody have an opinion?"
    "The presentation of the results of our chemistry research with another class."
    "We have to choose a representative for it."
    "However, no one has been recommended or volunteered. The time just passes by."
    "Then suddenly,"
    "One of students, who looks bored, raises his hand and says,"
    man "Tomoe should be the representative. She's an excellent student and the class president."

    voice et0008
    girl "I agree!!!"

    $ char ('tto004')

    "Everybody agrees."
    "It looks like they just want to push the responsibility off on her."

    voice to0997
    tomoe "O...kay. Any other opinions?"

    $ sfx ('SE41')

    "Tomoe admirably continues the meeting."
    "But her voice becomes hoarse and small."
    "In the buzz, a girl stands up and says in a loud voice,"

    $ char ('tas011')

    voice as1349
    asumi "Why don't you listen to her!!!"

    $ char ('tto007')

    voice to0998
    tomoe "Asumi."

    $ sfx ()
    $ bgfx ('black')

    "The class becomes quiet. Tomoe continues the meeting."
    "In the end, Tomoe becomes the representative."
    "Asumi looks at Tomoe, who's accepted the post."
    "Asumi wants Tomoe to better express her opinions."
    "As her roommate."


    call ep_start from _call_ep_start_15

    $ bgm (5)
    $ bgfx ('bg11a')
    $ char ('tas501')

    voice as0291
    asumi "Let's do our best today too!!!"
    marumu "......"
    "I hear the girls' energetic voices."
    "We boys are energetic too, but we don't have a mood-maker like Asumi."

    voice as0292
    asumi "Why don't you cheer them up? You can do it because you are my pupil."
    yusuke "When did I become your pupil?"

    $ char ('tas512')

    voice as0293
    asumi "Since you were born!"
    yusuke "......"
    "I'm at a loss for words as Asumi smiles at me."

    $ char ('tas501')

    voice as0294
    asumi "Oh, I have a good idea!"
    yusuke "What is it?"
    "Asumi whispers,"

    voice as0295
    asumi "You dress like a girl and say 'Do your best! I love you guys!' I think you're very cute when you dress like a girl."
    yusuke "You aren't serious, are you?"
    "I'm hurt."
    "Well, I'm used to it."
    "Girls started practice earlier than boys."
    "Looking at them, I've noticed something."
    yusuke "Where's Moe-Moe?"

    $ char ('tas543')

    voice as0296
    asumi "She's gone already."
    yusuke "Why?"

    voice as0297
    asumi "She doesn't feel well. She has a fever."
    "Asumi looks like she's in trouble."
    "I couldn't help but to be concerned about Tomoe."

    call blackout from _call_blackout_87
    $ bgfx ('bg02b')

    yusuke "Umm. I'm tired."

    $ char ('tas007')

    voice as0298
    asumi "If you're already tired, you can't win the game!"

    $ char ('tma001')

    voice ma0063
    marumu "She's right."
    "After the hard practice, I dressed up like a girl and headed back to the dorm."
    "Sometimes, I don't know what I'm doing."

    $ char ('tik999')

    voice yu0010
    akane "Oh, are you back now? You must train hard. Well, a loser needs to work harder."

    voice as0299
    asumi "......!"

    $ bgm (16)

    "The Trio de Bitches appear."
    "They're really good at making Asumi mad."
    yusuke "I should learn something from them..."

    $ char ('tas036')

    voice as0300
    asumi "You got a yellow card!"
    "She forces me to shut up."
    "The 3 vs. 1 fight starts."

    $ char ('tas006')

    voice as0301
    asumi "We'll make it up for last year! We won't lose this time!"

    $ char ('tfu001')

    voice fu0008
    midori "Do you think so? From my data, our team has an advantage over you guys."

    $ char ('ths001')

    voice hs0014
    kaoru "Yeah, our team already has good members. And we got a new member this year."

    $ char ('tas044')

    voice as0302
    asumi "A new member?"
    "I can't blame Asumi for being surprised."
    "Because at this school, the class members don't change after the conclusion of a school year."
    "The homeroom teacher is the same as well."
    "That way, each class can draw up its own curriculum."
    "But then, why do they have a new member...? Ah!"

    $ char ('tyu001')

    voice yu0011
    akane "The transfer student usually causes trouble, but I notice that she has quick reflexes."
    yusuke "Namiki..."
    "That's true."
    "Her motor skills are much better than the others, even most boys."
    "She's never played softball, but I'm sure she'll be great at it."

    $ char ('tas042')

    voice as0303
    asumi "Ugh...it's a problem."
    "Even Asumi recognizes Namiki's abilities."
    "The leader of the Trio de Bitches says,"

    $ char ('tik999')

    voice yu0012
    akane "Anyway, your class has dead wood."

    voice hs0015
    kaoru "But I haven't seen her today. Did she run away because she's slow?"

    voice fu0009
    midori "Great! She made the right decision. I'll give her praise."

    $ char ('tas006')

    voice as0304
    asumi "...You'd better shut up."

    $ music_stop ()

    "A small, sharp, cold voice reaches everybody's ears."
    "It doesn't sound familiar."
    "But it was the angry voice of the girl who's standing next to me."

    voice as0305
    asumi "If you say one more word, I'll kill you."

    $ char ('tyu002')

    voice yu0013
    akane "W...what? AEEE!"

    call effect ('SE36', ETYPE1) from _call_effect_34

    "The leader of the enemy moans in agony."
    "The two followers are too."
    "Asumi didn't do anything yet. Does she have telekinetic power!?"

    $ bgm (5)
    $ char ('ths002')

    voice hs0016
    kaoru "What are you doing, you stubby!? Don't kick me!"

    $ char ('tas013')

    voice as0306
    asumi "Good job! Marutan!"

    $ char ('tma008')

    voice ma0064
    marumu "...Gooood."
    "After we defeated the enemy with Marutan's attack, we went back to the dorm with mixed feelings."

    call blackout from _call_blackout_88
    $ bgfx ('bg01c')
    $ char ('tas001')

    voice as0307
    asumi "The fever's gone, Moe-Moe."

    $ char ('tto104')

    voice to0164
    tomoe "Yeah... I'm sorry."
    "Actually, Tomoe left school early, but it wasn't because of a fever."
    "I knew it."
    "The Trio de Bitches were talking about Tomoe."

    $ bgm (8)
    $ bgfx ('black', diss_long)

    "Asumi told me,"
    "Tomoe gets a fever when she's stressed."
    "She doesn't pretend to be sick."
    "Asumi says that it's because she's so pure and far too serious."
    "I've never heard of that kind of sickness, but I can understand."
    "Because it's Tomoe."

    $ bg ('bg01c')
    $ char ('tas043')

    "But Asumi doesn't move away from Tomoe."
    "She tells her,"

    voice as0308
    asumi "Moe-Moe, I understand how you feel, but...why don't you just join us and do your best. The school's motto is that all students should participate."

    $ char ('tma001')

    voice ma0065
    marumu "...Participation is the most important thing."
    "Marumu tells Tomoe her opinion. That's unusual."
    "I understand why they tell her that."
    "I know them because I've spent a lot of time with them."
    "They try to tell her, 'Let's work together, no matter what happens.'"
    "I agree. The result is just a bonus."
    "The most important thing is motivation."

    $ bgm (9)
    $ char ('tto104')

    voice to0165
    tomoe "...I'm sorry, Asumi, Marumu. I caused you some trouble."

    $ char ('tas006')

    voice as0309
    asumi "You caused us trouble? I've never thought so!"

    $ char ('tto104')

    voice to0166
    tomoe "You can tell me the truth. I know it."

    $ char ('tas001')

    voice as0310
    asumi "You're misunderstanding. Right, Marutan?"

    $ char ('tma001')

    voice ma0065a
    marumu "......(nod)"
    "Tomoe wipes her tears."
    "But she turns around and runs toward the door."

    $ char ('tto107')

    voice to0167
    tomoe "But... Still, you don't understand."

    voice as0311
    asumi "Moe-Moe!?"

    $ char ('tto113')

    voice to0168
    tomoe "I don't think either one of you can understand how I feel!"
    yusuke "Tomoe..."

    $ char ()

    "I stretched out my arm, but I couldn't reach her."
    "Her tears and the uncomfortable atmosphere subsided."

    call blackout from _call_blackout_89

    "...A minute later,"

    $ bgm (6)
    $ bgfx ('bg01c')
    $ char ('tna002')

    voice na0140
    namiki "Hey! Your class plays a game with my class, right?"
    yusuke "Namiki..."

    voice na0141
    namiki "Let's bet! If my class wins, let me decide your nicknames. What do you say?"

    $ char ('tas036')

    voice as0312
    asumi "...Twitch, twitch..."
    yusuke "Namiki... What bad timing."

    call cgeffect ('SE10', KENKA3) from _call_cgeffect_8
    $ bgm (7)

    "Namiki and Asumi start a battle again."
    "I quietly escape from the room."
    "It's not only that I don't want to get involved in their fight, but also because I care about something else."

    $ bgfx ('black', diss_long)
    $ music_stop ()
    $ bgfx ('bg02c')
    $ char ('tto104')

    yusuke "...So you were here after all."

    voice to0169
    tomoe "I...uh..."
    "Tomoe holds her tongue."
    "I think we're similar in a way."
    "That's why I can understand her better than Asumi and Marumu."
    "Even if it seems like I'm being conceited, I still think I'm the only one who can give her some advice at this very moment."

    menu:
        " "
        "Push her.":


            $ bgm (9)

            yusuke "I don't like you, Tomoe."

            voice to0170
            tomoe "Oh... I don't blame you...I only cause everyone trouble."
            yusuke "That's not true. I don't like the fact you give up so easily and run away."

            $ char ('tto113')

            voice to0171
            tomoe "B...but I...think that's better than if I participate..."
            "I feel like I'm looking at myself."
            "I give up on things easily and thought I was doing good."
            "But I've changed since I came to this small town."
            "Since I met Asumi, Marumu...and Tomoe."
            "That's why I want to help Tomoe now."
            yusuke "If you think you bother them, then don't do it."

            $ char ('tto104')

            voice to0172
            tomoe "Yusuke..."
            yusuke "Tomoe, did you try? Did you do anything to not bother them?"
            yusuke "It's no good to give up before you try."

            $ char ('tto107')

            voice to0173
            tomoe "...Sob...sob!"
            "Tears drop from her big eyes."
            "But the tears are not from being sad."
            "They are tears of vexation."
            "Tomoe tells me in tears,"

            voice to0174
            tomoe "I...I'm going to...join practice...tomorrow."

            $ F017 += 1
        "Comfort her.":


            $ bgm (9)

            yusuke "Tomoe... I understand how you feel, but..."
            tomoe "......"
            yusuke "Asumi and Marumu want to play with you."

            $ char ('tto113')

            voice to0171
            tomoe "B...but I'm definitely a burden on them..."
            "She looks hurt."
            "She thinks that she causes others trouble."
            "A serious girl like her can't take it."
            "But that's why I want to push her a little."
            "Even though it pains her."
            yusuke "Don't give up before you do anything, Tomoe."

            $ char ('tto107')

            voice to0173
            tomoe "...Sob!"
            "Tears overflow from her big eyes."
            "But it looks like she sheds tears of vexation."
            "Tears stream incessantly down her cheeks."
            "I can only silently stay beside her."
            "Finally, she starts to wipe her tears."
            "So as to not give up and step ahead."

            $ char ('tto102')

            voice to0174
            tomoe "I...I'll participate... in practice tomorrow..."


    call ep_middle from _call_ep_middle_14

    $ bgfx ('bg11a')
    $ bgm (16)
    $ char ('tyu001')

    voice yu0014
    akane "Oh! Our victory is as good as sealed."

    $ char ('tto404')

    "Tomoe drops the bat down after she swings and misses."
    "She still has a fever."
    "They continually say terrible things to her."
    "Hearing them, Tomoe's roommates run into them."
    "It's rare to see Marumu ready to fight."
    "The relations between them become tense. Tomoe tells them,"

    $ char ('tto413')

    voice to0175
    tomoe "Don't fight. We shouldn't bother others."

    $ char ('tas543')

    voice as0313
    asumi "But..."

    $ char ('ths001')

    voice hs0017
    kaoru "She's right. We don't need to waste our time. We don't even need to practice."

    $ char ('tas536')

    voice as0314
    asumi "Watch your mouth!"

    $ char ('tyu001')

    voice yu0015
    akane "Well, unlike us, you guys have a person who doesn't need training. She shouldn't waste her time... HEEEEH!"

    $ char ('tyu003')
    $ bgfx ('black')
    call effect ('SE39', ETYPE3) from _call_effect_35

    "THUMP! THUMP! THUMP!"
    "The sounds made by a bat."

    $ bgfx ('bg11a')
    $ char ('tyu002')

    voice yu0016
    akane "W...what are you doing!"

    $ char ('tna019')

    voice na0142
    namiki "Don't be mean to Tomo-Tomo! Why don't you listen to your leader!?"

    $ char ('tfu002')

    voice fu0010
    midori "We don't think of you as our leader!"

    $ char ('tna024')

    voice na0143
    namiki "Shut up! Come here!"

    $ char ()
    $ music_stop ()

    "Namiki drags them to their practice area."
    "And gives Tomoe a big smile."

    $ char ('tna020')

    voice na0144
    namiki "You look good when you're trying something, Tomo-Tomo."

    voice to0176
    tomoe "But...that nickname..."

    $ char ('tna001')

    voice na0145
    namiki "But it's a game! I won't lose! When you lose the game, you're 'Tomo-Tomo.' DOO YOO UNDAASUTANDO?"

    voice as0315
    asumi "Don't use some other language with a terrible accent! Only Mister can use it!"

    voice na0146
    namiki "Who's this 'Mister' you're talking about? Anyway, do your best! I'll cheer you guys on, despite being an opponent!"
    yusuke "Noo..."
    "Namiki's living in her egocentric world."

    $ char ()

    "But maybe because of Namiki, the Trio de Bitches stopped being mean to Moe-Moe."
    "Tomoe practices hard everyday, even though she has a fever."
    "Like Namiki says, Tomoe looks good when she's trying."
    "Tomoe works so hard at practice."
    "Looking at her, I feel happy."

    $ bgfx ('black')
    $ bgfx ('sora09')
    $ bgfx ('black', diss_long)

    yusuke "Hmm...?"
    "Since Marumu's incident, I wake up easily at any small sound."
    "I quietly open the closet door."

    $ bgfx ('bg01d')

    yusuke "Is it Marutan again?"
    "But all I see is a shadow. It's bigger than Marutan's."
    "And another shadow of something round shaped around the other's feet."
    "They leave the room with stealthy steps, so I decide to follow them."

    $ bgfx ('bg02c')
    $ char ('tto440')

    voice to0177
    tomoe "Huh, huh... YAHH!"

    $ char ('tts019')

    voice ts0024
    toshibo "MEEOW!!"
    "I see something that I would never have imagined."
    "Tomoe's practicing to hit the ball in the middle of the night."
    "But what I'm actually surprised by is..."
    "Toshibo. He's helping her train."
    "He's just a cat, but he's throwing the ball to Tomoe."
    yusuke "...I've never seen that kind of cat."

    $ char ('tto440')

    "I stop paying attention to Toshibo and look at Tomoe."
    "She swings the bat to hit the ball again and again."
    "She looks like an example of how not to swing a bat, due to her being a greenhorn."
    "Why does she work so hard?"

    $ char ('tto407')

    voice to0178
    tomoe "Ouch! Ugh..."
    "She drops the bat."
    "She's holding her right hand. She looks like she's in pain."
    "I can't see her hand, but the bat is stained with some kind of liquid."
    "Is it her blood?"
    "Is her hand skinned?"

    $ char ('tto440')

    "But after a while, Tomoe takes the bat again."
    "She positions the bat and looks at Toshibo."

    $ bgm (9)

    voice to0179
    tomoe "Okay, Toshibo...throw it!"

    $ char ('tts019')

    voice ts0025
    toshibo "Mee, meeow!"

    $ char ('tto440')

    voice to0180
    tomoe "Thank you, Toshibo. But I have to do this."
    "She holds the bat tight."

    voice to0181
    tomoe "Asumi, Marumu, and Yusuke told me to just participate in the game, even if I play terribly."

    voice to0182
    tomoe "But I don't think so."

    voice to0183
    tomoe "I want to win if I play. I'm the same as the others. I don't want to drag their feet. Toshibo, please..."

    $ char ('tts019')

    voice ts0026
    toshibo "MEOW!"
    "Toshibo looks at Tomoe and throws the ball."

    $ char ('tto440')

    "Tomoe swings."
    "I can't look at her anymore."
    "I directed some harsh words at her to cheer her up."
    "And she didn't take it the wrong way."
    "She doesn't run away anymore and works hard at it."
    "Tomoe cried."
    "But the tears were merely her determination."

    $ char ('tto407')

    yusuke "She's doing this because of me... Huh!?"
    "As soon as I decided to tell her stop,"
    "Someone holds my arm."
    yusuke "Asumi...and..."
    "Marumu."
    "They knew this?"

    voice as0316
    asumi "...She was doing that yesterday and the day before yesterday as well."
    yusuke "R...really..."
    "I didn't know!"
    "I really think that I should stop Tomoe now."
    "But Asumi won't let me."
    yusuke "Asumin, let me stop her. She doesn't have to do that..."

    voice as0317
    asumi "...We'd better let her do it."
    yusuke "B...but!!"

    $ char ('tto440')

    "I don't know what to say."
    "Yes. Asumi has known Tomoe longer than me."
    "And Asumi is stopping me."
    "She's trying to say, 'Let Tomoe do that until she's satisfied.'"
    "Tears drop down Asumi's cheeks..."

    call blackout from _call_blackout_90

    "We remain silent."
    "Tomoe continues swinging the bat under the bright moonlight."
    "The day of tournament arrived."

    $ bgfx ('white')
    $ bgm (5)
    $ bgfx ('sora02', diss_long)

    "Tomoe participates in the game without a fever."
    "With Asumi and Marutan, of course."
    "I care about their games."
    "But as the girls have their games, the boys have them too."
    "I can't concentrate on my game."

    $ bgfx ('bg11a')

    kosuke "...Ohh. We lost this year again."
    yusuke "I couldn't concentrate because I care about the girls' game."
    kosuke "...I don't think it really matters, even if you could concentrate on the game."
    yusuke "You're right..."
    "I don't care about that. The game's over, anyway."
    "I have to hurry to go see the girls."
    "I run towards the other playground where they're playing."
    yusuke "Hmm, already in the bottom of the ninth... OHH!?"
    "I look at the score. It's 5-4. Namiki's team leads by one run."
    "There's no great difference between the two teams."
    "There's a big difference between my team and theirs."

    $ char ('tas506')

    voice as0318
    asumi "The boys' team lost already..."
    yusuke "Sorry. By the way, how are you girls doing?"

    $ char ('tas544')

    voice as0319
    asumi "We're doing pretty well, as you can see. Our practice paid off, but..."
    "But Namiki plays better than anybody."
    "She's the pitcher and bats fourth. She plays a significant part in the game."
    "And the Trio de Bitches, they don't really play well. They haven't had much practice."
    "Asumi has two hits in three at bats, and Marumu has one hit in three at bats. Very good."
    "But Tomoe... She struck out on a forkball and has one error on defense."
    "But her teammates have been playing well as they watched Tomoe's efforts."

    $ char ('tas543')

    voice as0320
    asumi "...Ah, two outs... Moe-Moe's turn to bat won't come up again."
    "Tomoe is on deck. She's swinging a bat to practice."
    "I don't think she can hit Namiki's ball."
    "I think the game's over."
    judge "Ball! Ball four!"

    $ char ('tas506')

    "The umpire called the pitch a ball. Asumi and I are surprised."
    "The next batter is Tomoe."

    $ cg ('et_0201')

    yusuke "...Namiki, you did that on purpose!"

    voice as0321
    asumi "Will you let Moe-Moe take the credit for the game?"

    voice na0147
    namiki "Life isn't as easy as you think. I'll knock her off and give her a new nickname."
    "But those words don't reach Tomoe's ears."
    "Nervously, yet seriously, Tomoe stands in the batter box."

    voice na0148
    namiki "OK, this is it! I'll let you know how good I am!"

    voice to0184
    tomoe "Okay, Namiki!"

    voice na0149
    namiki "Aaah, say that again!"
    "That might be a good idea..."
    "While Tomoe doesn't do it on purpose, Namiki is weak against Tomoe calling her name."
    "Namiki may throw the ball softly..."

    $ cg ('et_0203')

    judge "Strike!"
    yusuke "She doesn't..."
    "Tomoe swings! She misses the ball."
    "Her swing looks much nicer than before. I think her night training worked."
    "But there's a big difference between Toshibo's ball and Namiki's."

    $ cg ('et_0201')

    voice as0322
    asumi "Moe-Moe, swing the bat a little faster!"

    voice ma0066
    marumu "...Do your best."
    "I don't think Tomoe can hear us."
    "She stares straight at Namiki."

    voice as0323
    asumi "MOE-MOE!!!"

    voice ma0066
    marumu "...Moe-Moe."
    "Next ball..."
    "That's fast. How can she throw the ball like that?"

    $ cg ('et_0203')

    "Tomoe misses again."
    "But her timing's getting better."

    $ cg ('et_0201')

    yusuke "Tomoe, try! ...Huh?"

    voice ts0027
    toshibo "MEEOW!"
    "I find Toshibo around my feet."
    "He must be worried about Tomoe."
    "He came here from the girls' dorm. It's not that close."
    "He's really a good cat."
    yusuke "Toshibo, you came! Let's cheer Tomoe together!"

    voice ts0028
    toshibo "Meeeow!"
    "I pick him up...and gosh, he's heavy (at least 20 pounds...)."
    "And then, we shout words of encouragement to Tomoe."
    yusuke "TOMOE! YOU CAN DO IT!"

    voice ts0029
    toshibo "Meow! Meo, meo, meeooow!"

    voice as0324
    asumi "You worked hard on it. You can... Moe-Moe!!"

    voice ma0067
    marumu "...MOE-MOEEEE."
    "Namiki gets ready to throw the ball."
    "And Tomoe stares at the ball."
    "She shows a spirited look."

    $ music_stop ()

    voice na0150
    namiki "Sorry, Tomo-Tomo... You're finished!"
    "Namiki throws the ball..."
    "Just then, Toshibo screams,"

    $ cg ('et_0202')

    voice ts0030
    toshibo "MEEOWWW!!"
    yusuke "Toshibo..."
    "He sounds like he's saying, 'NOW!'"
    "But it's not just me that hears it."
    "The girl who's standing in the batter box does as well."
    "She swings the bat with all her might."

    $ cg ('et_0204')
    $ sfx ('SE17')
    $ bgfx ('sora02', diss_long)

    "And...the bat hits the ball. It makes a big sound!"

    $ say_hide ()
    $ sfx ()
    $ bgfx ('black', blinds_long)
    $ bgm (12)
    $ cg ('e3_0113')

    yusuke "Whew...I'm tired."

    voice as0325
    asumi "Do you think you played hard? The boys' team needs more practice!"

    voice ma0068
    marumu "It'll be ready soon."

    $ sfx ('SE14')

    "I flip the Okonomiyaki."
    "But Tomoe isn't paying much attention to anything right now."
    "Her mind is elsewhere."
    "She's been like this since the end of the game."
    yusuke "Moe-Moe! You'd better turn the Okonomiyaki."
    tomoe "......"
    yusuke "Okay, I'll do it."
    tomoe "......"
    "No reaction."
    "She doesn't show any emotion."
    "Is she that disappointed?"

    $ sfx ()
    $ music_stop ()

    "Tomoe hit Namiki's fast ball."
    "The ball went flying far."
    "Not many people can hit a ball that far."
    "The ball passed over the fence."
    "It was a great hit."
    "But there's one pity."
    "The ball passed through foul territory."
    "So, it was a foul ball."
    "Tomoe fell down on her knees."
    "When she stood up, she had no energy left."
    tomoe "......"

    voice as0326
    asumi "Hey, Moe-Moe!"
    "Asumi yells at Tomoe."
    "Tomoe sighs and looks at the one-quarter Okonomiyaki Asumi gave her."

    voice to0185
    tomoe "Asumi, what's this?"

    voice as0327
    asumi "Buta Tama, my favorite."

    voice to0186
    tomoe "For me? Why?"

    voice as0328
    asumi "It's a special prize for you. You played the hardest today!"
    "Asumi says it loud. It echoes in the restaurant."

    $ cg ('e3_0114')
    $ bgm (5)

    voice as0329
    asumi "I've decided today's Asumin prize goes to Moe-Moe!!!"

    voice to0187
    tomoe "Asumi."

    "Marumu puts her one-quarter Ika Tama (Squid & Egg Japanese pancake) on Tomoe's dish without our noticing it."

    $ cg ('e3_0115')

    voice ma0069
    marumu "...Marutan prize too."

    menu:
        " "
        "Quickly cut them for her.":


            "I give my mixed Okonomiyaki to Tomoe."
            yusuke "Of course, Moe-Moe gets the Yusuke prize too! You did great!"

            voice as0330
            asumi "Yes, you did great!"

            voice ma0069a
            marumu "...Great."

            voice ts0031
            toshibo "Meeow, meeooow!"
            "The four of us (including Toshibo) all clap our hands."

            $ sfx ('SE59')

            "The customers around us applause too, even though they don't know what it's for."
            "We all give Tomoe a big hand."

            $ sfx (delay=0.3)
            $ F017 += 1
        "Watch over the beautiful sight.":


            "I'm watching over the beautiful sight."
            "Friendship is beautiful."
            "Asumi and Marumu applause Tomoe."
            "So does Toshibo. He claps his cute, plump palms."
            "I follow them."
            "We all praise her. She didn't give up to the end."

    $ bgfx ('sora06')
    $ bgm (10)

    "Tomoe murmurs as she looks at the heaps of Okonomiyaki."

    voice to0188
    tomoe "If I eat all of this, I'll gain weight...heh heh."
    "Tears drop from Tomoe's eyes."
    "But the tears are different than before."
    "Tears of joy."

    voice as0331
    asumi "Good job, Moe-Moe!"

    voice ma0070
    marumu "Good job. Moe-Moe."
    yusuke "Good job, Moe-Moe!"

    voice ts0032
    toshibo "Meeow, meeow!"


    call ep_finish from _call_ep_finish_14

    $ renpy.end_replay()
    $ unlock_episode (10)
    jump episode11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

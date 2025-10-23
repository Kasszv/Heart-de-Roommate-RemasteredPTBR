label episode27:

    $ Fnum = 28
    $ save_name = "Namiki Route: Don't call me Sis"


    $ bgfx ('sora02')

    "The days go by peacefully."
    "Summer vacation is over, and the fall semester starts."
    "There's no vacancy in the men's dorm yet, so I still live with the girls."
    "We spend fun days together."
    "However, someone's proposal breaks our peace."
    "The person is Namiki, who just ran into our room."

    $ bgfx ('bg01a')
    $ char ('tna002')
    $ bgm (6)

    voice na0248
    namiki "I have something I want to discuss with you girls."

    $ char ('tas001')

    voice as1228
    asumi "What? We might not help you, but you can say it anyway."

    $ char ('tto002')

    voice to0896
    tomoe "Be nice, Asumi. Sorry, Namiki."

    $ char ('tna020')

    voice na0249
    namiki "Thank you Moe-Moe! I like you anyway."
    yusuke "What are you talking about?"
    "Feeling uneasy, I ask her."

    $ char ('tna010')

    voice na0250
    namiki "Recently, I realize I'm lonely. I want a roommate!"

    $ char ('tas006')

    voice as1229
    asumi "You're selfish! How can you say such a thing?"

    $ char ('tto001')

    voice to0897
    tomoe "I don't think this is right. Four people live in the same size room as Namiki's, but she lives alone..."

    $ char ('tts007')

    voice ts0076
    toshibo "Meow!"

    $ char ('tto011')

    voice to0898
    tomoe "Oh, sorry, Toshibo. Four people and a cat."

    $ char ('tna002')

    voice na0251
    namiki "Yeah, you get the point! So give me Moe-Moe."

    $ char ('tto002')

    voice to0899
    tomoe "Ah...but..."

    $ char ('tas007')

    voice as1230
    asumi "No way! I know you'll do something nasty to her. I'll never let her go!"

    $ char ('tma016')

    voice ma0468
    marumu "How about Marumu?"

    $ char ('tna001')

    voice na0252
    namiki "You're cute, but I want someone to communicate with."
    yusuke "Then, Asumi would be perfect."

    $ char ('tas036')

    voice as1231
    asumi "Hey, what kind of underling gives the leader to another room?"
    yusuke "Well, if it were to happen, we could live peacefully... Whaaaa!!"

    $ music_stop ()
    $ say_hide (diss_flash)
    call cgeffect ('SE10', KENKA1) from _call_cgeffect_9
    $ bgfx ('black')

    "After Asumi beats me up, we talk about this for more than 3 hours."
    "The person who goes to Namiki's room is..."

    $ bgfx ('bg01a')
    $ char ('tna016')
    $ bgm (9)

    voice na0253
    namiki "So, you're the one..."
    yusuke "Yeeks...don't send me to Siberia."

    $ char ('tna001')

    voice na0254
    namiki "He's perfect for miscellaneous things. I'll take him."

    $ char ('tas045')

    voice as1232
    asumi "Good luck, Yusuke. I won't forget our time together."

    $ char ('tto001')

    voice to0900
    tomoe "We can meet again...at school."

    $ char ('tma008')

    voice ma0469
    marumu "Farewell, friend."

    $ char ('tts010')

    voice ts0077
    toshibo "Meow, meoow!"
    yusuke "Ugh...hic..."

    $ bgfx ('black')

    "I say goodbye to my wonderful life."
    "And the hard days as Namiki's slave begin."


    call ep_start from _call_ep_start_17

    $ bgfx ('bg09a')
    $ char ('tna002')
    $ bgm (5)

    voice na0255
    namiki "Let's do our best again today!"
    yusuke "...Yeah..."

    $ char ('tna019')

    voice na0256
    namiki "Say it louder! Be a man!"
    yusuke "Okay..."

    $ char ('tna001')

    voice na0257
    namiki "Anyway, clean the table and take care of my backpack, too."
    yusuke "All right."

    $ music_stop ()
    $ bgfx ('sora01')

    "Namiki goes to school carrying nothing."
    "After I clean the table, I have to take two backpacks to school."
    "This isn't right!"
    "I'm not happy about this at all!"
    yusuke "Ugh...she's a slave driver...but she's always been like that since we were kids."
    "A girl calls out to me as I leave the dorm."
    "The girl is my ex-roommate, Tomoe, with two other girls."

    $ bgfx ('bg03a')
    $ char ('tto013')
    $ bgm (3)

    voice to0901
    tomoe "Morning, Yusuke. Oh, look at you! Girls have to take care of their appearances!"
    yusuke "I'm a man...in fact."

    $ char ('tto020')

    voice to0902
    tomoe "Starting tomorrow, I'll go to your room and check before you leave."
    yusuke "I don't know whether to be sad or happy..."
    "Looking around, she asks,"

    $ char ('tto001')

    voice to0903
    tomoe "Where's Namiki?"
    yusuke "She's already gone...she left her backpack and took off."

    $ char ('tma001')

    voice ma0470
    marumu "Selfish..."

    $ char ('tas015')

    voice as1233
    asumi "Yeah, that's right. I hate selfish people."
    yusuke "YOU can't say that!"
    "Asumi, the one who gave me to Namiki, ignores me and continues,"

    $ char ('tas001')

    voice as1234
    asumi "Actually, Namiki looks pretty busy lately."
    yusuke "You don't listen to me at all... Well, it's better than having you hit me."

    $ char ('tas036')

    voice as1235
    asumi "Yusuke, did you say something?"
    yusuke "Nothiiiing! But why is she so busy? She doesn't belong to any clubs, and we don't have an exam yet...?"

    $ char ('tto031')

    voice to0904
    tomoe "Didn't you know? She became the head cheerleader."

    $ char ('tma017')

    voice ma0471
    marumu "The leader..."
    yusuke "What!?"
    "Everybody knows about it but me."
    "I didn't know that. I find out she was already the leader before I moved into her room."

    call blackout from _call_blackout_99

    "There are only eight people on the cheerleader squad."
    "They begged her to be their leader."
    "She accepted the offer because it's a leader role."
    "Now, she's busy practicing for the fall competition."
    "That's why she leaves early in the morning and comes back late at night."

    $ bgfx ('sora01')

    "One day, I watch her practicing from the roof top."

    $ bgfx ('bg07a')

    yusuke "Wow, she's working hard."
    "Sure, she's practicing hard."
    "Then I notice something."
    "The cheerleader squad. That's an ideal place for a party girl like her."

    $ bgfx ('bg11a')
    $ char ('tna530')

    "She looks good in the cheerleading uniform."
    "Some guys might fall in love with her."
    "I guess the squad knew it. That's why they asked her to join their club."

    $ bgfx ('bg07a')
    $ char ('tto025')

    voice to0905
    tomoe "Namiki looks good in that uniform."
    yusuke "Oh, Tomoe..."
    "She calls out and comes to stand next to me."
    "As we watch their practice, she murmurs,"

    voice to0906
    tomoe "I have a question I've always wanted to ask."
    yusuke "Yeah? What?"

    $ char ('tto001')

    voice to0907
    tomoe "Why do you call Namiki 'Sis?' You guys are in the same grade..."
    yusuke "I was expecting you'd ask about it someday."
    "Actually, she asked me before."
    "Many people have asked the same question in the past."
    "She'll be disgusted when she finds out the reason."
    "I'm sure she will be, but I tell her the truth."

    $ bgfx ('sora01')
    $ bgm (6)

    "Namiki is my cousin. We grew up together."
    "She and I are in the same grade."
    "However, our birthdays are almost a year apart."
    "She was born in October."
    "I was born in September."
    "We're in the same grade...it bothers her a lot."
    "When she found out, she insisted I call her 'Sis.'"
    "'I'm older than you though we're in the same grade! Do you understand?'"
    "She made me call her 'Sis' since then."
    "And I got in the habit of calling her 'Sis.'"
    "I'd feel embarrassed to call her 'Namiki.'"
    "It also symbolizes our relationship."
    "I guess our current relationship won't change very easily..."

    $ music_stop ()

    "As I finish explaining, Tomoe opens her mouths in astonishment."

    $ bgfx ('bg07a')
    $ char ('tto013')

    voice to0908
    tomoe "I had no idea..."
    yusuke "Are you disgusted or what?"

    $ char ('tto016')

    voice to0909
    tomoe "No, I'm kind of moved!"
    yusuke "Oh please..."
    "She's a little bit strange after all."
    "Then she asks me another question."

    $ char ('tto001')

    voice to0910
    tomoe "Are you okay with it?"
    yusuke "What do you mean?"

    voice to0911
    tomoe "To be treated as Namiki's brother..."
    yusuke "Umm...I've never thought about it before."
    "I think about our relationship in the past."
    "Sure, she's selfish and a busybody, but she's a good sister."
    "That's why I've never thought about it before."
    "I really have never thought about it."

    $ bgfx ('black')

    "However, she forces me to work hard everyday."
    "I'm fed up with it and complain to her."

    $ bgfx ('bg09c')
    $ bgm (16)

    yusuke "I know you're busy with club activities, but you don't do anything. Do something! You're a woman, right!?"

    $ char ('tna118')

    voice na0258
    namiki "Hey, that's discrimination! Besides, you don't look like a man anyway."
    "I'm pissed off with her irrational excuse."
    yusuke "What's that supposed to mean? I don't understand at all! How come doing everything is related to being a man?"

    $ char ('tna104')

    voice na0259
    namiki "Because you're good at housework! You could be a housekeeper..."
    yusuke "Mmm..."
    "I unwillingly put on women's clothes everyday, so I'm a bit particular about my manhood."
    "Recently, I've really started to feel that way."
    "Especially because she doesn't treat me as a man. I want her to know I'm a man!"
    "So I ask her,"
    yusuke "If that's the case, how can I be treated as a man?"

    $ char ('tna118')

    voice na0260
    namiki "I know you're sexually a male...so don't sneak into my room at night. He he."
    yusuke "......"
    "I'm upset because she won't take me seriously."
    "Just for a moment, I think about sneaking into her room."
    "But I know I don't have the courage to do that..."

    call blackout from _call_blackout_100

    "Several months ago, she taught me about women's bodies."
    "I couldn't see very well because she turned the light off."
    "But I remember the touch on my lips and hands..."
    "As I recall the event, I blush."

    $ bgfx ('bg09c')
    $ char ('tna102')

    "I immediately put the thought away and ask her again."
    yusuke "That's not what I'm asking! What should I do to be treated as a man by you?"

    voice na0261
    namiki "Hmm...I don't think you can do it."
    yusuke "I can do anything! I'm a man!!"

    $ char ('tna120')

    voice na0262
    namiki "Okay then...if you say so. Heh heh."
    "She smirks."
    "When she smiles like that, she's up to no good."
    "I have a bad feeling about this..."

    $ bgfx ('black')

    "Looking at her evil smile, I feel uneasy."
    "My prediction comes true the next day."

    $ bgfx ('bg09a')
    $ char ('tna501')
    $ bgm (6)

    yusuke "What's this?"

    voice na0263
    namiki "A cheerleading uniform."
    yusuke "Why do I have to wear this?"

    voice na0264
    namiki "Because you've become a member of the cheerleading squad."
    yusuke "No, I haven't!"

    $ char ('tna504')

    voice na0265
    namiki "I signed you up. Well, prove it to me."
    yusuke "Prove what?"

    voice na0266
    namiki "You said you're a man, right? Let's go!"
    yusuke "W...why does this always happen to me...?"

    $ bgfx ('sora02')

    "I shout it out to the heavens."
    "I fell into her trap."
    "Doing housework in the dorm and practicing with the cheerleaders at school, I'm busier than ever."
    "I still have to take her backpack to school."
    "This is living hell... Help me, please..."

    $ music_stop ()
    $ bgfx ('bg11a')
    $ char ('tna531')

    "Cheerleading is tough."
    "It looked easy from the rooftop, but it isn't."
    "It's as hard as any other field sport."
    "However, she enjoys the practicing... She's a party girl!"
    "I watch her with fascination."

    $ char ('tna519')

    voice na0267
    namiki "What are you looking at?"
    yusuke "Ah...I think..."

    voice na0268
    namiki "What?"
    yusuke "You're practicing hard...and you look kind of beautiful."

    $ char ('tna525')

    voice na0269
    namiki "Yusuke..."
    "She instantly blushes."
    "This is a surprise. Is it really happening?"
    "I guess it is."
    "She's a woman, after all...oh?"
    "Her face turns beet-red."

    $ char ('tna519')

    "There's no embarrassment there, it's anger."
    "She isn't embarrassed."
    "She's mad at what I said."

    $ bgm (7)

    voice na0270
    namiki "Kind of? Did you say kind of? How can you say that to me?"
    yusuke "What's wrong with you? It was a compliment!!"

    voice na0271
    namiki "Shut up! Don't waste your breath!!"

    $ bgfx ('black')
    call effect ('SE10', ETYPE3, sound_loop=True) from _call_effect_36

    "She beats me up."
    "Moreover, I have to stay there practicing until the sun sets."
    "I'm exhausted mentally and physically."

    $ audio_stop ()
    $ bgfx ('bg09c')

    yusuke "I...I'm dead."
    "As soon as I return to the dorm, I fall down on my bed."
    "Namiki calls out to me."

    $ char ('tna001')

    voice na0272
    namiki "Yusuke..."
    yusuke "I know...I'll cook dinner. Wait a minute...ouch!"
    "I can't move... I have muscle pains."
    "The hard exercise caused this."
    "Just so you know, it's not because she beat me up."

    $ char ()

    "I don't know how long I've been lying here."
    "Feeling pain all over, I try to get up to cook dinner."
    "If I fall asleep, I'll be in big trouble."
    "But her next words surprise me."

    $ char ('tna102')

    voice na0273
    namiki "Dinner is ready..."
    yusuke "Seriously!?"
    "It's unbelievable."
    "She made dinner for me!"

    $ bgfx ('black')
    $ bgfx ('bg09c')
    $ char ('tna102')
    $ bgm (13)

    "It's been a long time since I had her cooking... It's good, no it's great."
    "She's a good cook, though she doesn't look like it."
    "P.E. and cooking are her favorite subjects."
    "What really surprises me is what she cooked."

    $ char ('tna116')

    voice na0274
    namiki "I didn't think you were in any shape to cook."
    yusuke "You're responsible for part of this!"

    $ bgfx ('black')

    "I talk back to her."
    "Out of the mouth comes evil..."

    $ bgfx ('bg09c')
    $ char ('tna125')

    "Rubbing the lump on my head, I groan in pain."

    voice na0275
    namiki "Yusuke...don't you remember?"
    yusuke "Huh...what?"

    voice na0276
    namiki "What you said a long time ago..."
    yusuke "???"
    "She tells me, recalling it from her memory."

    $ char ('tna102')

    voice na0277
    namiki "You always said, 'I'll marry you when I grow up. You're the most beautiful girl in the world.'"
    yusuke "That's a lie..."

    $ char ('tna118')

    voice na0278
    namiki "It's not a lie! You said that!"
    "I don't think I remember..."
    "I might have said it once."
    "We've been together since we were babies."
    "If I really said that to her...I was a dare-devil when I said it."
    "Smiling, she looks at me."

    $ char ('tna102')

    voice na0279
    namiki "Now, I'm kind of beautiful!? My ratings have went down...heh heh."
    yusuke "Sis..."
    "She suddenly points at the wall and says,"

    $ char ('tna110')

    voice na0280
    namiki "You should hit on the girl next door!"
    yusuke "Who...?"

    $ char ('tna120')

    voice na0281
    namiki "Any girl except Moe-Moe."
    yusuke "Okay, okay..."
    "I forget she likes pretty girls..."

    $ music_stop ()
    $ bgfx ('sora09')

    "Later, I think about her in my bed."
    "I remember a lot of things about her, and I think I really said that."
    "Perhaps I wanted to marry her with my pure, innocent heart."
    "What do I think about her now?"
    "Still...I like her."
    "But she's difficult to deal with."
    "But we did do something intimate..."
    yusuke "Oops...I'm thinking too much."
    "Thinking about her, I become wide-awake."

    $ bgfx ('black')

    "Time goes by."
    "I finally get used to cheerleading exercises."

    $ bgfx ('bg11a')
    $ char ('tna530')
    $ bgm (5)

    "However, the exercises are becoming increasingly more difficult."
    "We'll give a performance soon."
    "Namiki and the other members are practicing hard."

    voice na0282
    namiki "Come on, guys! Say it louder! Show some spirit!"
    "Everybody's really serious."
    "So is Namiki."
    "Her sweat shines in the sun, and she looks more charming than ever."
    yusuke "I'll do my best too!"
    "Yup, I'm a man!"
    "I'll do my best to have Namiki treat me as a man."
    "I continue practicing hard with the others."

    $ music_stop ()
    $ bgfx ('sora05')

    "A week later..."
    "Tomorrow is our first performance."
    "After the last practice, Namiki calls out to me."

    $ bgfx ('bg11b')
    $ char ('tna501')

    voice na0283
    namiki "Well, you're doing better."
    yusuke "Thanks."
    "I'm glad to hear her compliment."
    "However, her next words break me down."

    $ char ('tna504')

    voice na0284
    namiki "But you're still a 'He-She.' Oh, you dress like a girl everyday, it doesn't matter. Ha ha ha!"
    yusuke "Ugh...mmm!!"
    "She keeps laughing."
    "I can't talk back to her now."
    "I'll show you tomorrow!"
    "I inwardly resolve to myself."
    "Tomorrow is the day!"

    $ bgfx ('black')

    "I couldn't sleep very well because I was so excited."
    "With a big yawn, I resolve to do my best."
    "Some people come to cheer me on."
    "My ex-roommates."

    $ bgfx ('bg06a')
    $ char ('tas002')
    $ bgm (3)

    voice as1236
    asumi "I still can't believe you're a cheerleader. Don't screw up for their sakes."

    $ char ('tto001')

    voice to0912
    tomoe "I think you look better in the girl's school uniform than the cheerleader uniform..."
    yusuke "Did you say something, Tomoe?"

    $ char ('tto011')

    voice to0913
    tomoe "Oh...nothing. Do your best, Yusuke!"

    $ char ('tma008')

    voice ma0472
    marumu "Go Yusuke, go!"
    yusuke "(I don't understand what they're trying to say.)"

    $ char ()

    "I appreciate their kindness."
    "A cheerleader is cheered. That sounds strange, but I'm happy."

    call blackout from _call_blackout_101
    $ bgfx ('bg11a')
    $ sfx ('SE41', loop=True)
    $ char ('tna530')
    $ bgm (16)

    voice na0285
    namiki "Are you ready? Let's do it!!"
    yusuke "Yeah!!"

    $ sfx (delay=1.0)
    $ char ('tna531')

    "The cheerleading competition starts with shouts."
    "Both sides perform equally well."
    "I still can't believe I'm a cheerleader."
    "The person who gets the most attention is the head cheerleader."
    "Namiki has really become popular at our school."
    "When she yells, everyone looks at her."
    "Inevitably, our performance attracts a great deal of attention."
    "I can't be defeated as a man. I cheer at the top of my voice."
    "Actually, it's not really me to be so enthused."
    "I guess I look funny."
    "But there's an eye on me."
    "Namiki's eye."
    "I guess she's looking at me happily."

    call blackout from _call_blackout_102
    $ bgfx ('sora05')
    $ bgfx ('bg11b')
    $ char ('tna501')
    $ bgm (9)

    voice na0286
    namiki "Good job, everybody."
    yusuke "......"

    voice na0287
    namiki "What's wrong?"
    yusuke "We lost..."
    "All the students and cheerleaders look depressed."
    "Because they did their best and still lost."
    "Namiki pats my shoulder."

    $ char ('tna504')

    voice na0288
    namiki "Victory or defeat is all a matter of chance. But I think we cheered better than the others."
    yusuke "Sis..."
    "I didn't expect such words from her."
    "But..."

    $ bgm (5)

    voice na0289
    namiki "Of course, I'm the best! Ahem!"
    yusuke "......"
    "It's so Namiki..."
    "Then she smiles at me."

    $ char ('tna501')

    voice na0290
    namiki "But you did well. I'll give you a couple of points for your performance."
    yusuke "What? Just a couple?"

    voice na0291
    namiki "Of course. Do you think you'd become a real man?"
    yusuke "Well..."
    "I know it's hard for her to concede to."
    "But I think I deserve more..."

    call blackout from _call_blackout_103

    "After we put things away, everyone goes home."
    "Only Namiki and I are left."
    "Before I suggest we go home, she asks me,"

    $ bgfx ('bg11b')
    $ char ('tna501')

    voice na0292
    namiki "By the way, why do you care about 'manhood' so much?"
    yusuke "Needless to say...because I'm a man!"

    voice na0293
    namiki "You shouldn't aim so high."
    "She sounds like she's teasing me, so I talk back with my true feelings."
    yusuke "It just bothers me...that you don't treat me as a man."

    voice na0294
    namiki "Umm...is that so?"

    $ char ('tna525')

    "Namiki's thinking."
    "After a short while, she stares at me."
    "She seems to be checking me out."
    "Finally, as if coming to a conclusion, she nods."

    $ char ('tna501')

    voice na0295
    namiki "But Yusuke, there's a lot left before you become a man."
    yusuke "What!? What do you mean?"

    voice na0296
    namiki "Do you know how to give pleasure to a girl?"
    yusuke "I...it..."
    "I swallow the words, 'That has nothing to do with whether I'm a man or not!'"
    "I know she doesn't care about what I say."
    "But I can't let her get away with it!"
    "I'm looking for something to say back to her."
    "But Namiki speaks up before I can say anything."

    voice na0297
    namiki "If you want to say, 'I'm a man!' Why don't you prove it!"
    yusuke "P...prove..."

    voice na0298
    namiki "Yes. Show me the proof."
    yusuke "...Huh?"
    "My mind goes blank."
    "Proof...?"
    "To her?"
    "Show?"
    "That means..."
    "Some dirty ideas fill my head."
    "Namiki drags me to..."
    "The gym storage."

    $ bgfx ('black')

    voice na0299
    namiki "...Okay, Yusuke."
    yusuke "......"
    "I stand there motionless without words."
    "I don't know what to do, but my heart beats fast."
    "She smirks."

    voice na0300
    namiki "Don't worry, I won't hit you."
    yusuke "B...but..."
    "I'm still not sure what to do..."
    "Namiki starts laughing as if she knew how I'd react."

    voice na0301
    namiki "Huh? Are you frightened? See? You're far from becoming a man."
    yusuke "!!"

    $ sfx ('SE45')

    voice na0302
    namiki "YIKES!"
    "I suddenly grab her shoulder."
    "And I push her down on the mattress."
    "What...am I doing!?"
    "That's what I think, but I can't stop myself."
    "My hand rolls up her gym suit."
    "And then, her big boobs jump out! Why isn't she wearing a bra!?"
    "But still, I don't stop."
    "Her words really made me mad, so a part of me has taken over."
    "I'm afraid of myself."

    $ cg ('hn_0101', diss_long)
    $ unlock_gallery ('g3e11')
    $ bgm (12)

    "But I'm not afraid of her at all."
    "She doesn't seem embarrassed at all, even though I stare at her breasts."
    "She's not even afraid of me."

    voice na0303
    namiki "I see. You're more aggressive than I thought."
    yusuke "B...because..."
    "I can't tell her that my body won't listen to me."

    voice na0304
    namiki "It's a little late to be scared now! If I scream, the police will catch you."
    yusuke "Eh!? If you do that..."
    "This is a big problem!"
    "I'm frightened."
    "Namiki throws piercing words at me."

    voice na0305
    namiki "Don't you have the guts? If you're a man, why don't you attack me!"

    voice na0306
    namiki "I don't think you could give me pleasure, anyway."
    yusuke "Damn! You'll see..."
    "Can I forget what she said?"
    "No, I can't!"
    "Still scared shitless, I reach out for her."
    "My shaking hands move closer to her big breasts."
    "I've seen them before, but they look different now."
    "I'm excited just looking at the round shaped things."
    "As soon as I touch them, the feelings from that night come rushing back."

    $ cg ('hn_0102')

    "My hands move around on her breasts."

    voice na0307
    namiki "Don't rush. I won't scream...ah!"
    "I can't remain calm."
    "Then I'll just go with the flow!"
    "I start to caress her breasts with my desire."
    "Her softness feels really good."
    "I move my hand faster and faster."
    "But she calmly looks at me with cold eyes."

    voice na0308
    namiki "You move so awkwardly. I can't say you're a man."
    yusuke "Mmm!"

    voice na0309
    namiki "Don't be so rough! Real men don't violent women. You're far from what a man should be!"
    yusuke "S...sorry. Um..."

    voice na0310
    namiki "Yes, like that... You're getting better."
    yusuke "Then...do you feel good?"

    voice na0311
    namiki "Ha ha ha! Nooo! That's out of the question!"
    yusuke "Shit!"
    "I try whatever I can."
    "This feels more like a combative sport than sex."
    "I push her breasts hard."

    voice na0312
    namiki "They're sensitive, so be kind. Okay?"
    yusuke "They hardened up a bit."
    "I touch her nipple."
    "Hearing me, she tells me in a soft voice,"

    voice na0313
    namiki "No, they didn't... You're imagining things."
    "Does she feel pleasure?"
    "I massage her breasts, hardly listening to her."
    "I think her breathing is becoming ragged, but she still doesn't look like she feels good."
    "My breaths are shorter than hers."
    "I can't stand losing. I'm really pissed."
    "I should do something different!"
    "Thinking about it, I stop moving."

    $ cg ('hn_0103')

    "I softly squeeze her breast and kiss her nipple."
    yusuke "Smooch...mmm."
    namiki "......"
    yusuke "Smack...lick! Mm..."

    $ cg ('hn_0104')

    voice na0314
    namiki "Ahh...no..."
    yusuke "Eh!?"
    "I bring my face up."
    "And I look at her face."
    "She's finally moaning!"
    "Her sweet moan!"
    "However...she has a different expression than what I expected."

    $ cg ('hn_0105')

    voice na0315
    namiki "He he he! How's my moan?"
    yusuke "Heh?"

    voice na0316
    namiki "You worked so hard, so I wanted to lead you on. He he!"
    "I'm mad. I've never been so frustrated!"
    "I can't give up now. If I do, I'll look so stupid!"
    yusuke "How about this!?"

    voice na0317
    namiki "Yikes! You're so wild, Yusuke!"
    "She makes fun of me."
    "I get out of control."
    "Only my will-power pushes me on."

    $ music_stop ()
    $ cg ('hn_0201', diss_long)
    $ unlock_gallery ('g3e12')

    "I don't hesitate anymore. I roughly take off her clothes and panties."
    "And I move in close, where a girl is most sensitive."
    "But it's not easy to reach."
    "I try to open her legs."

    voice na0318
    namiki "H...hey, that hurts."
    "She twitches as she escapes from me."
    "And she murmurs in a soft voice with red cheeks."

    voice na0319
    namiki "You don't need to be so rough. You can just tell me to open them..."
    yusuke "If I tell you to?"

    voice na0320
    namiki "I'll...open them."
    yusuke "T...then open them."
    "She nods at my order with a bit of expectation."
    "Slowly, really slowly, she opens her legs."
    "Before she opens them completely, I jump between them and sink my face in."

    voice na0321
    namiki "Haah, aah, ah..."
    yusuke "Mmm, lick, lick..."

    $ cg ('hn_0202')

    voice na0322
    namiki "You can't just lick it...haahhh..."
    "I violently suck on her womanhood with passion."
    "I'm not afraid of anything now."
    "Namiki talks to me."
    "But I can't respond because my tongue and lips are too busy caressing her pussy."

    voice na0323
    namiki "T...that doesn't work... Not...at all..."

    voice na0324
    namiki "Haaah. You're still inexperienced..."

    $ cg ('hn_0203')

    voice na0325
    namiki "N...no. You can't put your finger in yet... Yikes!"

    voice na0326
    namiki "Ahh! Don't lick me like that... The sounds are...so dirty."

    voice na0327
    namiki "Nooo... Stupid! You should...aah...your tongue...aaahh!"

    voice na0328
    namiki "Ahh, caress my breasts too... Y...you're getting better..."

    $ sfx ('SE06', loop=True)
    $ cg ('hn_0204')

    voice na0329
    namiki "Haaah, haa, haahhh!"

    voice na0330
    namiki "Y...Yusuke...haah, ah..."
    "The dirty sounds echo around in the gym storage room."
    "I'm so excited, I completely forget about myself."
    "I hear Namiki's voice in my ear."
    "I pull my finger out of her and raise my head."

    $ sfx (delay=0.2)

    "I look into her blushed face."

    $ bgm (14)

    yusuke "Namiki..."

    $ cg ('hn_0203')

    voice na0331
    namiki "I don't feel...haah, anything...haa haa..."
    "Her sticky honey covers my finger."
    "I show her, and I'm surprised as well."
    yusuke "Look, you're so wet."

    voice na0332
    namiki "It's...not that..."
    "Her face is completely red."
    "And she's sighing."
    "This is my first time to see her as a woman, a real woman."
    "And the excitement spreads through me."
    yusuke "I...can't control myself anymore, Sis!"

    $ cg ('hn_0204')

    voice na0333
    namiki "N...noooo! Not yet...aah!"
    "She tries not to show that she feels good, even though she moans with pleasure."
    "But it has the opposite affect on me."
    "Her reaction makes me more excited."
    "Her flushed cheeks and wet pussy... I totally lose control."
    "I move without trying to."
    "She can't stop me anymore."
    "I roughly insert my swollen dick into her."

    $ cg ('hn_0301')
    $ unlock_gallery ('g4e1')

    voice na0334
    namiki "Y...you're too rough... Idiot!"
    yusuke "N...Namiki...mmm..."

    voice na0335
    namiki "D...don't...aaah!"

    voice na0336
    namiki "Haah, ah, aah, Yusuke...aahhh!"
    "Her wet softness swallows my member."
    "It makes a really dirty noise."
    "I'm caught up in the excitement."
    yusuke "W...wow... It's hot...inside...mmm..."

    voice na0337
    namiki "Don't push so hard... Haa, haahhh!"
    "Being inexperienced, I don't know what's hard or what's soft."
    "Anyway, I can't control myself anymore."
    "This is her fault!"
    "I see her face through my squinting eyes."
    "I see her breathe heavily with pleasure."
    "Just looking at her, my eagerness explodes."
    "I move my hips harder."

    $ sfx ('SE07', loop=True)

    "Her pussy tightens around me."
    yusuke "Ohhh, tight...it's tight... Mmmm..."

    voice na0338
    namiki "Ahh, yours...is moving around inside me...haa, haahh...!"

    $ cg ('hn_0302')

    voice na0339
    namiki "Oh no! I'm going crazy...haahhh..."
    "Before I realize it, not only am I moving my hips, but she is as well."
    "We're moving rhythmically."
    "She lecherously shifts her body and joins my movement."
    "The more she moves the tighter she gets."
    "And finally...I near the end."
    yusuke "Mmm, ummm...I...I...aah, uhh!!"

    voice na0340
    namiki "I'm cumming! I'm cumminnnnng! AHHHH!"

    $ sfx (delay=0.5)
    call effect (graphics=['white']) from _call_effect_37

    "Suddenly, my eyes and head go blank."

    $ cg ('hn_0303')

    "Immense pleasure runs through my body. I've never felt this good."
    "My dick slowly loses its stamina."
    "Namiki clings to me like a child."

    $ cg ('hn_0304')

    voice na0341
    namiki "Haa, haa, haahhh..."
    yusuke "Ohh...hahhh..."
    "We hold each other tight."
    "While holding her, I fall down."
    "When I open my eyes, the gym storage room is quiet."
    "Only our breaths echo inside..."
    "My excitement ebbs, and I calm down."
    "I'm back to the usual me."
    "Suddenly, I feel so embarrassed."

    $ bgfx ('sora05', diss_long)
    $ music_stop ()

    "I look at her sideways."
    "She's lying down on a mattress, all covered in sweat."
    "I don't know what to tell her."
    "But we can't stay like this forever."
    "I decide to ask her a question."
    yusuke "H...how was it?"

    voice na0342
    namiki "Haah haa... BAD."

    $ empat ('SE49')

    "SHOCK!"
    "The shock noisily rings in my head."
    yusuke "N...no..."
    voice na0343
    namiki "Yusuke, you were too rough and selfish."
    "Her words weigh me down."
    "But maybe she's right."
    "I'm completely depressed."
    "Namiki looks at me and softly hugs me."
    "And she gives me a soft kiss."

    $ empat ()
    $ bgm (10)

    voice na0344
    namiki "A man should think about aftercare."
    yusuke "Namiki..."

    voice na0345
    namiki "Well, it was your first time. I expect more from you in the future. He he!"
    yusuke "You mean...?"

    voice na0346
    namiki "You still need a lot of work, but...I'll concede that you're a man, yet MAYBE a man."
    yusuke "What's that!? Remember, you came too!"

    voice na0347
    namiki "That wasn't enough!"
    yusuke "Hmm... You always have to win, Namiki!"

    $ music_stop ()

    voice na0348
    namiki "WHAT!?"
    "I thought she looked cute, but it was only for a second."
    "The usual Namiki is back."

    $ sfx ('SE10', loop=True)
    $ bgm (7)

    "She jumps on me and attacks me."
    "She'll never change, but I feel happier than usual."

    call blackout from _call_blackout_104
    $ bgm (14)

    "And that's how she accepts me as a man, anyway."

    $ vox ('na0349')

    "Actually, I think it'll take more than that to make her know I'm a man."

    $ vox (delay=0.3)

    "Because basically, our relationship hasn't changed at all, even though we had sex."

    $ vox ('na0350')

    "She still makes fun of me everyday."

    $ vox (delay=0.3)

    "But sometimes, she treats me sweet."
    "Only then, do I feel we're cohabitants."

    $ vox ('na0351')

    "I forget this is a girls' dorm."

    $ vox (delay=0.3)

    "I don't see her just as a cousin anymore."
    "Of course, she's still like my older sister."

    $ vox ('na0352')

    "I already love her so much."

    $ vox (delay=0.3)

    "Sometimes, the pain when she hits me even makes me happy."
    "We're the same as usual."

    $ vox ('na0353')

    "But sometimes, we're different."

    $ vox (delay=0.3)

    "But this is just the way we are."
    "When we make love, we feel love for each other."

    $ music_stop ()
    $ bgfx ('sora09')

    "One night, together in bed, Namiki murmurs,"

    voice na0354
    namiki "Yusuke."
    yusuke "Yes?"

    voice na0355
    namiki "If you find someone better, you don't have to feel any obligation to me. I'll understand."
    yusuke "Why?"

    voice na0356
    namiki "Because when it comes down to it, I'm your older sister."
    "She tries to keep a certain distance from me."
    "Sometimes, I distance myself from her as well."
    "We grew up together, like brother and sister."
    "Perhaps we're both afraid of ruining the relationship."
    "But isn't it time to get over that?"
    "I start to think so."
    yusuke "You know, I realize I like someone older than me."

    voice na0357
    namiki "I understand that you're in love with me because I'm so attractive as I'm an adult."
    yusuke "I don't think you're an adult. I think you're more childish and a lot cuter than me."

    voice na0358
    namiki "I don't feel good when you say that."
    "She's mad and tries to change the subject."
    "I add,"
    yusuke "There's one more thing I realized."

    voice na0359
    namiki "What?"
    yusuke "That I really love you."

    voice na0360
    namiki "I...idiot!"
    "I'm happy to see this Namiki."
    "She's cute when she's embarrassed."
    "Whenever I see this Namiki, I feel I love her more and more."
    yusuke "Why are you blushing so much? Well, I think you look cute when your face is red."

    voice na0361
    namiki "I can zip up your mouth, Yusuke."
    yusuke "WAAAAAH!!!"

    $ bgfx ('black')
    call effect ('SE43', ETYPE1) from _call_effect_38

    "We need more time to become real lovers."
    "I rub my head after she hits me."
    "Namiki and me. We're not like normal couples."
    "We continue to keep a distance between us, even though we love each other."
    "But it won't last forever."
    "There's a beginning and also an end."
    "Yes."
    "The end of our living together has come."
    "Graduation. An important moment of youth."

    $ bgfx ('bg05a')
    $ char ('tas045')
    $ bgm (10)

    "After the ceremony, I tell Asumi and other girls goodbye."
    "To a conclusion of our shared life."
    "Looking back, the day I met Asumi and started living in the Harukaze Dorm was just the beginning."
    "Looking back on it, my heart fills with deep emotion."
    "We promise each other that one day, the 'Roommates' shall meet again."
    "We don't know when, but..."

    $ chars ('tto025', 'tma003')
    $ char ()

    "I see them off. I'm so glad I met Asumi, Tomoe, and Marumu."
    "I'm kind of thankful to my damn parents now."
    "After I say goodbye to the girls, someone walks up to me."

    $ char ('tna001')

    "The one who's spent the most time with me since transferring to this school."
    "She comes in front of me and smiles."

    voice na0362
    namiki "Congratulations, Yusuke!"
    yusuke "You too!"
    "I point at her diploma and tell her."

    $ char ('tna010')

    "But she shakes her head."
    "Like I'm misunderstanding."
    "What does she mean?"
    "Namiki says,"

    $ char ('tna001')

    voice na0363
    namiki "No, Yusuke. I meant that you've finally become a real man."
    yusuke "Oh, you finally concede to it!"

    $ bgm (14)

    "I'm happily surprised."
    "Then I jump!"
    "I've been wondering."
    "But Namiki hasn't said anything since the last time we talked about it."
    "But finally, she tells me today, on graduation day."
    "She looks at me sideways."
    "Something between us feels uncomfortable."
    "After a while, she shyly tells me,"

    $ char ('tna027')

    voice na0364
    namiki "I think we can become a real couple from today as a memento of our graduation."
    yusuke "Eh!?"
    "I can't believe what I just heard."
    "She's never even touched on the subject before now."
    "She kept telling me that she's my older sister."
    "I'm really surprised."
    "She looks away and tells me in a soft voice,"

    $ char ('tna010')

    voice na0365
    namiki "Of course, that's if you want to."
    yusuke "Yes."
    "I nod."
    "I continue looking at her beet-red face."

    $ char ('tna027')

    "She looks at me again."
    "Her eyes are wet."
    "We just stare at each other."
    "She calls my name with her red cherry-colored lips."

    voice na0366
    namiki "Yusuke."
    yusuke "...Namiki."
    "She's not my older sister anymore."
    "The girl in front of me now,"
    "She's my girl."
    "She's a childhood friend and my girlfriend... Namiki Honjo."
    "My wish has finally come true!"
    "I shake with happiness, and I notice Namiki shaking too."

    $ music_stop ()
    $ bgfx ('sora07')

    yusuke "What's wrong, Namiki?"

    voice na0367
    namiki "You're over-reacting, idiot!!"
    yusuke "Oh no... WAAAAH!!!"

    $ cg ('en_02')
    $ unlock_gallery ('g4e2')
    $ sfx ('SE10', loop=True)
    $ bgm (7)

    "Namiki, my love..."
    "She attacks me again."
    "And this is how my youth at Aiho School ends."

    $ sfx (delay=1.0)
    $ bgm (10)

    "I still can't beat Namiki."
    "Especially when she's in her 'older sister mode.'"
    "But some of my friends envy me."
    "Our relationship is like a brother and sister."
    "But since we graduated, it's slowly changing."
    "From the imitation brother and sister to lovers."
    "When can we become a normal couple? Will the day really come?"
    "I'm kind of nervous when I think about it."
    "But I'm satisfied with this relationship for now."
    "I don't need to rush things."
    "The time will come one day naturally."
    "Our love will never change..."

    call blackout (True) from _call_blackout_105

    jump credits
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

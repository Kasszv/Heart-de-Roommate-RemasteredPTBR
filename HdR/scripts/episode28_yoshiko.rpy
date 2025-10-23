label episode28:

    $ Fnum = 29
    $ save_name = "Yoshiko Route: Ms. Yagami, please!"


    $ bgfx ('bg04a')
    $ char ('tyo014')

    yusuke "What!?"

    voice yo0222
    yagami "That's right... Will you come to the teachers' office after class with me?"
    "It happens so suddenly."
    "I don't know why it happened."
    "But I know one thing for sure:"
    "My secret has been revealed."
    "Teachers know I've been living in the girls' dorm!"

    $ bgfx ('black')
    $ bgm (9)

    "This is the biggest problem Aiho School has ever faced."
    "In the teachers' office, all the teachers question me."
    "I guess I can't keep lying anymore."
    "I've been driven into a corner and caught at last."
    "However, I'm still a guy."
    "Even though I had to wear a girl's uniform to survive, I'm still a man!"
    "I'll tell all sorts of lies to keep the girls out of this mess."
    "I'll take all the responsibility."
    "Therefore, the girls get off with only a warning."
    "On the other hand, I'm cornered into the worst possibility, the possibility of being expelled."
    "Yet there's nothing I can do about it."
    "If I don't get expelled, I may put Asumi and the others through a lot of trouble."
    "I'm prepared for the worst, but Ms. Yagami makes a suggestion to the other teachers."

    voice yo0223
    yagami "This is also my fault, so please let me handle the matter."

    $ bgfx ('sora05')

    "Surprisingly, they accept her suggestion."
    "I guess the school would rather settle the matter peacefully."
    "Thanks to Ms. Yagami, I'm saved from being kicked out of school."
    "Instead, she gives me easy detention: writing an apology letter."
    "But if I do something bad again, she has to take all the responsibility, the worst, getting fired."
    "I can never thank her enough."
    "Then she even offers me a place to live."

    call blackout from _call_blackout_155
    $ bgfx ('bg10c')
    $ char ('tyo102')
    $ bgm (4)

    voice yo0224
    yagami "Well, this will be your room."
    yusuke "You mean...here?"

    voice yo0225
    yagami "After a while, I'm sure there will be a room available in the guys' dorm. So be patient until then, okay?"
    yusuke "......"
    "She took me to an apartment."
    "I'm totally speechless."
    "Because she volunteered to let me stay in her apartment."
    "That means I'm going to shack up with her."
    "It's hard to believe, but another phase of life has started."

    $ char ('tyo107')

    "I'm living with my homeroom teacher."


    call ep_start from _call_ep_start_25

    $ bgfx ('black')
    $ bgfx ('sora02')

    "At school, she looks so neat."
    "But at home, she's rather a slob."
    "To tell you the truth, she doesn't clean her room, and she even buys her meals (TV dinners) at a convenience store."
    "It seems she has an eye for picking yummy foods, so whatever she buys, it usually tastes good."
    "However, I can't let her continue this kind of life."
    "Since I'm living with her, I can't just ignore it."
    "Besides, she's helped me a lot."
    "I should do something to show my gratitude."
    "I'm lost in thought for a while."
    "I feel like I'm back in the Harukaze Dorm, taking care of my masters."
    yusuke "I'll bet I can be a great servant."
    "It seems as if I'm taking a step back from being a macho guy again."

    $ bgfx ('bg10a')
    $ char ('tyo101')
    $ bgm (13)

    yusuke "Good morning, Ms. Yagami!"

    voice yo0226
    yagami "Good morning, Yusuke. It smells like you made my breakfast again."
    yusuke "Don't you like me cooking for you?"

    $ char ('tyo123')

    voice yo0227
    yagami "No, but I feel a little embarrassed."
    yusuke "You really shouldn't be. Besides, your talent lies elsewhere."

    voice yo0228
    yagami "True. Well, then...mmm, this omelet is yummy!"

    $ char ('tyo107')

    "She looks so happy."
    yusuke "It's actually Tomoe's recipe, and I learned how to marinate fish from Marumu when I was in the dorm."

    $ char ('tyo102')

    voice yo0229
    yagami "I'm sure you'll be a wonderful housewife!"
    yusuke "I know, I know. Hey, stop teasing me!"
    "Although she's laughing, I feel she's a bit serious about it."

    voice yo0230
    yagami "And this Miso soup..."

    $ char ('tyo113')

    "As she sips it, she tilts her head in wonder."
    "I briefly explain to her,"
    yusuke "It's Asumi's recipe, using Chikuwa and Konnyaku."
    yusuke "She calls it something else, but I just used what was in the fridge."

    $ char ('tyo114')

    yagami "......"
    "Her smile suddenly disappears."
    "I regret making the soup."
    yusuke "I guess I shouldn't have made such weird soup."
    yagami "......"
    yusuke "Ms. Yagami?"

    $ char ('tyo117')

    voice yo0231
    yagami "W...what?"
    "She looks up as if she just woke up."
    "I'm not sure if she's been listening to my strange soup story or not."
    yusuke "Ah...well, finish up. Otherwise, you'll be late for work."

    $ char ('tyo119')

    voice yo0232
    yagami "Yeah, you're right."
    "She bolts down her food."
    "Sensing the strange atmosphere in the air, I start feeling somewhat nervous."
    "I wonder what she was thinking?"
    "But I know I shouldn't pry."
    "Because I'm not in the position to question her."
    "I silently finish my breakfast and head to school."

    call blackout from _call_blackout_156
    $ bgfx ('bg05a')

    "During a short break, I glance out at the peaceful fall scenery outside the window."
    "And I wonder about Ms. Yagami."
    "All of sudden, my lovely ex-roommate taps me on the shoulder."

    $ char ('tas002')
    $ bgm (5)

    voice as1201
    asumi "Hey, how's life with your forbidden love?"
    yusuke "Shut up, Asumi!"

    $ char ('tas005')

    voice as1202
    asumi "You can call me, 'Asumin.' Anyway, you're still my honorable roommate, though you're not there anymore."
    yusuke "Oh, thanks. Hey, that's not what I'm talking about!"
    "I grab her arm."
    "Then I pull her to the rooftop."

    $ bgfx ('black')
    $ bgfx ('bg07a')
    $ char ('tas001')

    yusuke "Don't you remember? I told you not to say a word about me living with Ms. Yagami."

    $ char ('tas007')

    voice as1203
    asumi "Hey, watch your mouth. I haven't told anyone."
    yusuke "But if you talk so loud, somebody may hear."

    $ char ('tas015')

    voice as1204
    asumi "Oh, really? Anyway, your secret is safe with me!"
    yusuke "I shouldn't have told you."
    "In fact, I regret unveiling my secret to her."
    "If I could go back in time, I'd reveal it to Tomoe and Marumu, but not Asumi."
    "I know she used to worry about me."
    "But now, she's somehow transformed herself into someone blackmailing me for fun."

    $ char ('tas037')
    $ bgm (16)

    voice as1205
    asumi "If you don't want me to disclose your secret, don't let mine out either."
    yusuke "What are you talking about?"

    $ char ('tas036')

    voice as1206
    asumi "Don't be a fool. Of course, I'm talking about THAT!"
    yusuke "So what is THAT?"

    $ char ('tas010')

    voice as1207
    asumi "You have something on me, remember?"
    yusuke "Oh, THAT."
    "Actually, I still don't know what she's talking about."
    "But I don't think it's necessary to tell her."
    "Otherwise, she may treat me like her servant for rest of my life."
    "I pretend to be keeping her secret, and we agree not to let each other's secret out."

    call blackout from _call_blackout_157

    "After school..."
    "For the first time in ages, I leave school with Asumi, Tomoe, and Marumu."
    "Because I just happen to meet them in front of the school gate."
    "Ms. Yagami has been very busy with a lot of extra work after school."
    "I was thinking of going home alone, so this was very good timing."

    $ bgfx ('bg03b')
    $ bgm (3)

    "Now, I don't need to pretend to be a female student anymore."
    "That's right! I can walk around as a guy!"
    "It's so refreshing going home with my friends, especially without wearing a girl's uniform."
    "Tomoe suddenly looks at me."

    $ char ('tto001')

    voice to0886
    tomoe "How have you been, Yusuke?"
    yusuke "It's kind of sad not being around you guys all the time, but in contrast, I'm happy I don't have to wear girls' clothes."

    $ char ('tma004')

    voice ma0462
    marumu "What a waste, Yusuke."

    $ char ('tto002')

    voice to0887
    tomoe "Yeah, you looked really nice in those clothes."
    yusuke "Not at all!"
    "It looks as if Tomoe's really disappointed."
    "However, I don't care about her feelings."
    "I don't want to do that ever again!"
    "Anyway, Tomoe must really be out in left field."
    "After Tomoe leaves, another nuisance comes along."

    $ char ('tas012')

    voice as1208
    asumi "I guess you're doing fine. How's everything with Ms. Yagami?"
    yusuke "Hey, what do you mean by that?"

    $ char ('tma004')

    voice ma0463
    marumu "Night life."
    yusuke "!!!"

    $ bgm (7)

    "Even Asumi is at a loss for words at Marumu's straightforward remark."
    "Tomoe starts walking around flustered."

    voice to0888
    tomoe "Marutan!"

    voice ma0464
    marumu "Do you guys fight about which adult programs to watch at night?"
    yusuke "Huh?"
    "I wonder how she knows about such things."
    yusuke "Don't worry, I don't watch such programs."
    "Tomoe heaves a sigh of relief."

    $ char ('tto020')

    voice to0889
    tomoe "Yusuke, come visit us sometimes! Of course, you have to wear a girl's uniform to sneak into the dorm, though."
    yusuke "No thanks!"

    $ char ('tas002')

    voice as1209
    asumi "Then we'll go visit you!"

    $ char ('tto025')

    voice to0890
    tomoe "Sounds good! I'd love to see Ms. Yagami's apartment at least once."

    $ char ('tma017')

    voice ma0465
    marumu "Me too."
    yusuke "Hey, guys!"
    "They haven't changed a bit."
    "Anyhow, it was really fun living with them."
    "My thoughts unconsciously turn to the good old memories."
    "At least I can still hang around with my friends like this."
    "If I'd been expelled, I couldn't do this anymore."
    "We keep chatting and slowly walk back home."

    $ music_stop ()
    $ bgfx ('sora05')

    "Even after leaving the Harukaze Dorm, everybody still cares about me."
    "I'm so pleased."

    $ bgfx ('black')

    "Many days have passed."
    "I'm getting used to living with Ms. Yagami."
    "One night..."
    "It's a little different from usual nights."

    $ bgfx ('sora09')

    "After finishing dinner, I wait for Ms. Yagami to return."
    "If someone were to see me now, I'd probably look like a wife waiting for her husband."
    "However, she hasn't returned yet, and it's after ten."
    "Usually, she calls me if she's planning to be late."
    "Is she in some kind of trouble?"
    yusuke "I hope she's all right."
    "I can't help worrying."
    "I go outside to check if she's there."

    $ bgfx ('bg03c')
    $ bgm (8)

    yusuke "Maybe I should have waited for her in the apartment."
    "It's awfully cold tonight."
    "I think it's because we're up in the mountains."
    "I walk at a quick pace to my school."
    "I haven't met anybody yet."
    "I decide to turn back."
    "Since I was gone for a while, she might have come home."
    yusuke "Ah?"
    "Something bothers me a little."
    "As I strain my eyes in the dark, I see someone staggering a little ahead of me."
    "I feel uneasy, so I hurry to the figure of a woman."
    yusuke "Ms. Yagami?"

    $ char ('tyo124')

    voice yo0233
    yagami "Hic, hic."
    "I'm sure it's her."
    "Yet she's walking with faltering steps."
    "Then I realize I smell alcohol on her breath."
    "On top of that, she looks really angry and even shouts once in a while."

    $ music_stop ()
    $ bgfx ('sora09')

    "I manage to get her home."
    "To tell you the truth, I had to coax her a million times on the way back."
    "I wonder why she drank so much?"
    "What happened to her?"
    "For an instant, an ominous premonition flits across my mind."

    $ bgfx ('black')

    "Without any further trouble, we arrive at her apartment."
    "I slowly take her to her bedroom."

    $ bgfx ('bg10c')

    "Even after lying her on her bed, she blabbers away drunkenly."
    "Little by little, she gets a hold of herself."
    "I hand her a glass of water to help sober her up."
    yusuke "Here you go, Ms. Yagami. By the way, what happened?"

    $ char ('tyo124')

    yagami "......"
    yusuke "Well, I understand you sometimes need to get drunk."
    yagami "......"
    "She doesn't answer, though she doesn't look quite so drunk anymore."
    "I keep talking to her."
    yusuke "You can tell me whatever's on your mind. Would you like to gripe?"

    voice yo0234
    yagami "No."
    yusuke "You don't have to hold it in; even you have one or two things you'd like to say, right?"
    yagami "......"
    "She gazes at me in silence."
    "For some reason, she looks grumpy."
    "Then she moves closer to me as though sticking her face out."
    yusuke "What's wrong, Ms. Yagami?"

    $ char ('tyo202')
    $ bgm (14)

    voice yo0235
    yagami "...Mmmm."
    yusuke "Umm, mmmmmm."
    "It suddenly happens..."
    "Honestly, I wasn't expecting this."
    "She abruptly embraces me."
    "I'm shocked and barely catch her."
    "Then she kisses me."
    "I'm ready to panic,"

    $ char ('tyo124')

    "And I push her away."
    "But she's still staring at me with dull eyes."
    "Then she mutters,"

    voice yo0236
    yagami "...Naoto."
    yusuke "Who?"

    voice yo0237
    yagami "Naoto."
    yusuke "Who's Naoto?"

    $ char ()

    voice yo0238
    yagami "Zzzzz..."
    "The next moment, she falls down on the bed."
    "I hear her let out a small sigh."
    "It looks like she fell asleep."
    yusuke "Who the hell is Naoto?"
    "For sure, I'm not going to find out who he is right now."
    "Because I don't want to wake her up now."
    "I quietly study her face."
    "If I ignore her red face, she's sleeping like a baby."
    "Suddenly, I feel a transparent string pulling my lips toward hers."
    "As I think about her kiss, I feel dizzy."
    "But why did she kiss me?"
    "Anyway, it wasn't the first time."
    "In fact, she's kissed me twice so far."
    "Without realizing it, my face draws closer to hers."
    "She's in a deep sleep, so even if I kissed her, I don't think she'd notice..."
    yusuke "Silly me! What was I thinking?"
    "I hurriedly move away from her."
    "And I try to clear the mist from my head."
    "Then I put a blanket over her."

    call blackout from _call_blackout_158
    $ bgfx ('sora09')

    "When I was distressed about who I was in love with, Ms. Yagami gave me a gentle kiss."
    "But for sure, the second kiss wasn't like that."
    "It definitely wasn't a light kiss."
    "It was more like a rich kiss between lovers."
    "I'm sure I won't forget the feeling for a long time."
    "She was pretty drunk, so she might have thought I was Naoto and kissed me."
    "That means Naoto is...her boyfriend?"
    "Once again, I recall a few memories after moving in here."
    "I don't think she has a boyfriend."
    "Has she been seeing somebody outside?"
    "Or did she go to a bar with Naoto?"
    "The more I think, the more questions I have."
    "Unconsciously, I start feeling jealous of this mysterious guy."
    "I wonder about her secret boyfriend and feel restless all night long."

    $ bgfx ('black')
    $ bgfx ('sora01')
    $ bgm (6)

    "The next morning, she wakes up with a hangover."
    "I ask her what happened last night."

    $ bgfx ('bg10a')

    "Of course, I don't ask her about Naoto nor about the second kiss."
    "Actually, I don't have the courage to hear her answer."

    $ char ('tyo101')

    "But somehow, she doesn't remember about last night at all."
    "It's as if her memory has been wiped out."
    "I'm a bit disappointed."
    "Because the second kiss was very shocking, even though she might have thought I was somebody else."
    "After all, the incident happened for no reason."
    "Maybe it was as simple as that."
    "If she remembered anything, I'll bet she could forget about it, just like that."
    "But for me, it wasn't just a happening."

    call blackout from _call_blackout_159

    "Because of that deep kiss,"
    "I unconsciously start looking for her all the time."
    "It seems as if she's the lady of my dreams."
    "I don't know when it may turn into love."
    "Silently, the feeling starts welling up inside me."

    $ bgfx ('sora08')

    "One day..."
    "It's a usual, quiet night."
    "Ms. Yagami and I are having a fun conversation."
    "She simply fascinates me."

    $ bgfx ('bg10c')
    $ char ('tyo102')
    $ bgm (13)

    voice yo0239
    yagami "...What do you think about that, Yusuke?"
    yusuke "......"

    voice yo0240
    yagami "Yusuke?"
    yusuke "......"

    $ char ('tyo105')

    voice yo0241
    yagami "Hey, wake up!"
    "As she calls out loud, I return from my day dreaming."
    "My mind was somewhere else, so I don't know how to answer."
    yusuke "Oh, yes! I'll get you more."

    $ char ('tyo104')

    voice yo0242
    yagami "Wrong."
    yusuke "Okay, then you miss TV dinners, right?"

    $ char ('tyo115')

    voice yo0243
    yagami "I wasn't talking about that either. Anyway, are you okay? You spaced out there for a while, you know."
    yusuke "Oh, I'm fine."
    "I'm embarrassed to tell her the truth."
    "Let alone, I don't think it's very good timing to mention it now."
    "The incident the other night made me begin having feelings toward her."
    "My attitude is odd, and she gives me a suspicious look."

    $ char ('tyo114')

    voice yo0244
    yagami "Why have you been staring at me? Do I have something on my face?"
    yusuke "Nope."

    voice yo0245
    yagami "Then, have you become infatuated with me?"
    yusuke "What?"
    "How? How does she know that!?"
    "I'm struck dumb with astonishment."
    "She looks at my stunned face and starts chuckling."

    $ char ('tyo107')

    voice yo0246
    yagami "I'm just kidding! I know you like one of the three girls."
    "I used to think I was interested in a girl from the group."
    "Without thinking, I say back to her,"
    yusuke "Why do you think that? If I lived with a girl and fell in love with her, I'd probably love..."

    $ char ('tyo119')

    voice yo0247
    yagami "True, you'd love me by now."
    yusuke "......"

    $ music_stop ()

    "She's right."
    "That's why I don't know what to do."
    "Because I can't tell what's real and what's not."
    "Do I really love Ms. Yagami?"
    "Or do I like her as my teacher?"
    "Who knows, she might be like the woman of my dreams."
    "Where is my heart?"
    "Since I don't know my true feelings, I sometimes act odd like this."
    "All of sudden, I realize her face is getting closer to me."
    "This isn't good!"

    $ char ('tyo201')

    voice yo0248
    yagami "Spill it out, Yusuke!"
    yusuke "What are you talking about?"

    voice yo0249
    yagami "You can't fool me. So just be a man and tell me who you love!"
    "Her face gets closer and closer."
    "If I were to stick out my lips, I could probably kiss her now."
    "I can't take my eyes off her charming lips and wet eyes."
    "I try not to remember the last kiss, but I don't know how long I can resist."
    "My heart starts beating fast."
    "Oh, gosh! I don't think she'll let me go until I tell her."
    "That's it! I can't do this anymore..."
    "After thinking for a while, I whisper to her,"
    yusuke "I kind of like..."

    voice yo0250
    yagami "Asumi?"
    yusuke "The person in front of me."

    voice yo0251
    yagami "In front...?"
    yusuke "I'm really interested in her."

    voice yo0252
    yagami "You mean..."
    yusuke "......"

    $ char ('tyo123')
    $ bgm (14)

    voice yo0253
    yagami "Whaaaaat!?"
    "She raises her voice in surprise."
    "Then she quickly moves away from me."

    $ char ('tyo119')

    voice yo0254
    yagami "Hey, don't try to trick an adult!"
    yusuke "I'm not tricking you! Because you asked me, I told you what's on my mind."

    $ char ('tyo115')

    yagami "......"
    "Silence falls between us."
    "Because neither of us know what to say now."
    "Soon, I start feeling sorry for her."
    "...I should say something."
    "Just as I make up my mind, she suddenly opens her mouth."
    "And she tells me in a gentle voice,"

    $ char ('tyo107')

    voice yo0255
    yagami "If it's true, I should say thank you."
    yusuke "Ms. Yagami?"
    "I wasn't expecting those words."
    "Does that mean she likes me too?"
    "But her next words break my heart to pieces."

    $ char ('tyo110')
    $ bgm (9)

    voice yo0256
    yagami "But I can't be with you."
    yusuke "Why?"

    voice yo0257
    yagami "Because you're my student."
    "She gives me a modeled answer as though it's from a textbook."
    "It makes me feel there's a thick wall between us."
    "Is it possible to break the wall?"
    yusuke "Ms. Yagami..."

    $ char ('tyo115')

    voice yo0258
    yagami "Let's change the subject, Yusuke."
    yusuke "......"

    $ char ('tyo110')

    voice yo0259
    yagami "...Sorry."
    "She apologizes to me."
    "That's not fair!"
    "There's nothing I can say if she apologizes to me like this!"
    "Until today, her flexible thoughts have helped me and have even cheered me up."
    "I didn't think she was like the other straitlaced teachers."
    "Nevertheless, she suddenly tells me to face up to reality."

    call blackout from _call_blackout_160

    "I know she's right."
    "Therefore, I should follow her decision."
    "But it's not that easy to do."
    "I become gloomy."
    "However, she hasn't changed a bit. Ms. Yagami is still Ms. Yagami."
    "I'm sitting there depressed, and she doesn't want to let things be as they are."

    $ bgfx ('sora05')

    "The next day..."

    voice yo0260
    yagami "Yusuke, can I see you for a moment?"
    yusuke "Yes, sure."

    $ bgfx ('bg07b')

    "She leads me to the rooftop."
    "There's nobody around but the two of us."
    "She calmly starts talking as if controlling her emotions."

    $ char ('tyo015')

    voice yo0261
    yagami "Once I fell in love with..."
    yusuke "Who?"
    "The name Naoto pops up in my mind."
    "At last, the name comes out of her mouth."

    $ char ('tyo020')

    voice yo0262
    yagami "Naoto...he was my student."

    voice yo0263
    yagami "He was a very hard worker. Sometimes I even invited him to my house as well."
    "After drawing a deep breath, she continues her story."

    $ char ('tyo010')

    voice yo0264
    yagami "All of sudden, he told me he was in love with me."

    voice yo0265
    yagami "Of course, I told him I wasn't willing to have such a relationship with him. At the same time, I thought his feelings for me were probably just admiration toward mature women."

    $ char ('tyo001')

    voice yo0266
    yagami "But every time I met him, he kept telling me how much he loved me."

    voice yo0267
    yagami "I could hardly resist his single-minded passion for me. After a while, I started falling in love with him."

    $ bgfx ('sora05')
    $ bgm (10)

    "'Soon, we started to make love.'"
    "'I wanted to follow my heart, being happy.'"
    "'Everyday, he'd stop at my place for a while before going home.'"
    "'Until late at night.'"
    "'Sometimes, he even spent the night at my apartment.'"
    "'By then, it was too late to stop loving him.'"
    "'And the same for him...'"
    "'Also, he was a very good cook.'"
    "'I was so amazed he could make me anything.'"
    "'I can cook, but it isn't my favorite part of housework.'"
    "'Anyway, there was a dish he couldn't cook very well.'"
    "'It was Miso soup.'"
    "'So he tried many different ways.'"
    "'Sometimes, he ended up making very weird Miso soup.'"
    "'One day, he put Chikuwa and Konnyaku in the soup. Another day, there were noodles in it.'"
    "'I couldn't help laughing everyday.'"
    "'I almost forgot he was my student.'"
    "'We became a couple, more like a brother and sister.'"
    "'Therefore, I hoped it would never end.'"

    call blackout from _call_blackout_161
    $ bgfx ('bg07b')
    $ char ('tyo001')

    "Just listening to her story, I feel so jealous of the guy."

    $ char ('tyo014')

    "Yet little by little, she becomes gloomy."
    "Soon, she starts talking about the painful ending of their relationship."

    $ bgm (9)

    voice yo0268
    yagami "One day, the teachers found out about our relationship."
    yusuke "And?"

    voice yo0269
    yagami "The school was famous for getting students into higher level universities. He was smart, so his parents expected him to go to one of the best. They ordered us not to see each other anymore."
    yusuke "......"
    "She looks miserable, as if it happened to her yesterday."
    "However, she can't stop talking about it."

    $ char ('tyo010')

    voice yo0270
    yagami "So I gave up on him. I thought it best for him, you know."

    voice yo0271
    yagami "But he didn't want to give up on our relationship, so he kept loving me."

    voice yo0272
    yagami "Finally, his parents had him transferred to a different school in order to get him away from me."

    voice yo0273
    yagami "I didn't have the nerve to speak up to either the school or his parents."

    voice yo0274
    yagami "I couldn't do anything for my love."
    yusuke "......"
    "Tears well up in her eyes."
    "I shouldn't make her recall the piercing memories."

    voice yo0275
    yagami "The worst thing of all, he failed his college entrance exam and ran away from home."

    voice yo0276
    yagami "For a while, I thought he might come back to me, but he didn't."

    voice yo0277
    yagami "He was probably mad at me for not rescuing him from the situation."
    yusuke "I don't think so. Absolutely not!"
    yagami "......"

    $ bgfx ('black')

    "Did I relieve her suffering a bit?"
    "She falls into silence."
    "And she starts crying quietly."
    "I feel so helpless...and I don't know how to console her."

    $ music_stop ()
    $ bgfx ('bg03c')
    $ char ('tyo110')

    "We don't say a word until we get back to her apartment."
    "I still feel heavy air around us."

    $ bgfx ('bg10c')
    $ char ('tyo110')

    "For quite a while, she hasn't looked at me straight in the eye."
    "Worst of all, I don't know what to say to her."
    "It seems as if there's a thick wall between us."
    "Unlike the fear, I feel her warmth right next to me."

    $ bgfx ('sora08')

    "That's because I start holding her before I even realize it."
    "I'm hugging her from behind."
    "Then she whispers to me in a sorrowful voice,"

    $ bgm (9)

    voice yo0278
    yagami "I think it's time for you to move out."
    yusuke "Ms. Yagami?"

    voice yo0279
    yagami "If you don't, I may fall in love with you someday."
    "I nearly weep for joy."
    "But at the same time, I feel so sad."
    "I recall the words."
    "And I clearly understand what she means."
    "She wants to wipe out the possibility of her falling in love with me."
    "I should tell her how I feel."
    yusuke "You mean...I can't love you because you're my teacher?"

    voice yo0280
    yagami "Ah!"
    "I shake off her grasp."
    "Then, I hold her tight."
    "She stiffens and lets out a small sigh."
    "Instead of letting her go,"
    "I keep hugging her tighter than ever."
    yusuke "I don't know how to explain this, but I can't stop thinking about you."

    voice yo0281
    yagami "Okay, but you can't..."
    "Little by little, she loosens up."
    "Then I forcefully kiss her."
    "The situation is reversed from the last kiss."
    "She freezes in shock."
    "After a while, she starts struggling to get away from me."

    voice yo0282
    yagami "Please, let me go."
    yusuke "Why?"

    voice yo0283
    yagami "Just because...please."
    "As my lips leave hers,"
    "I hear a small sigh."
    "I see tears roll down her face, and I quickly let her go."
    "But still, she won't stop shedding tears."
    "I don't know what to do, so I keep staring at her in silence."

    call blackout from _call_blackout_162
    $ bgfx ('bg07a')

    "After a couple of days,"
    "I find out Ms. Yagami has been trying to find an apartment for me."
    "She's been telling her realtor that it's urgent."
    "By accident, I heard the news from another teacher."
    "I try to conceal how upset I am, but I can't."
    "Am I just a burden for her?"
    "I contemplate such things alone on the rooftop."
    "What should I do?"
    "I'm sitting there pitying my predicament, and someone comes to the rooftop."

    $ char ('tas006')
    $ bgm (13)

    voice as1210
    asumi "Hey, why are you so blue?"
    yusuke "...I'm not."

    voice as1211
    asumi "Yes, you are. See?"
    "She looks into my eyes."
    "Then she straightens her back."

    $ char ('tas015')

    voice as1212
    asumi "I'll be your counselor, so tell me anything!"
    yusuke "Now, you're acting like Namiki."
    "When I say this, she knits her brows."

    $ char ('tas007')

    voice as1213
    asumi "Your secret will be safe with me, so just spell it out!"
    yusuke "......"
    "I can't stand her persistence."
    "Besides, I can't get an answer alone."
    "Without a second thought, I tell her what's on my mind."
    "Of course, I skip a few things."

    $ bgfx ('black')
    $ bgfx ('bg07a')
    $ char ('tas021')

    asumi "......"
    yusuke "I thought you'd tease me."

    voice as1214
    asumi "Well, do you want me to tease you?"
    yusuke "Not really."
    asumi "......"
    "I didn't expect this reaction from her."
    "She's seriously thinking, almost as if it's happened to herself."
    "What's wrong with her!?"
    "I don't know what to say, so I just stare at her."
    "After a while, she gives me one of her usual smiles."

    $ char ('tas044')

    voice as1215
    asumi "I guess I can't give you much advise. Sorry, Yusuke."
    "I can't complain at all."
    "Because she thought about it seriously."
    yusuke "Don't worry about it. In fact, I feel much better after talking to you, you know."

    $ char ('tas005')

    voice as1216
    asumi "Anyway, I can give you some basic advise."
    yusuke "......??"
    "I wonder what she's going to tell me."
    "Then she proudly tells me,"

    $ char ('tas007')

    voice as1217
    asumi "You only have one life to live, so follow your heart! Just don't regret anything, okay?"
    yusuke "Who said that?"

    $ char ('tas012')

    voice as1218
    asumi "Of course, me!"
    yusuke "Yeah, yeah, right."
    "I smirk at her."
    "After all, she hasn't changed a bit since the first time I met her."
    "Besides, she's absolutely right."
    "I deeply engrave the words on my mind."
    "Never regret."

    $ music_stop ()

    "All of a sudden, Tomoe shows up on the rooftop."
    "She's breathing so hard."

    $ char ('tto013')

    voice to0891
    tomoe "Yusuke, listen to me carefully. Ms. Yagami just collapsed on the floor!"

    $ empat ('SE49')

    yusuke "What?"

    $ bgfx ('sora01')

    "For a second, the news gives me cold shivers."
    "Then I race down the stairs as fast as I can."
    "To look for her."

    $ empat ()
    $ bgfx ('black')
    $ bgm (8)

    "At last, I find her in the nurse's office."
    "She's peacefully sleeping in bed."
    "According to the doctor, she had a break down from overworking."
    "Not just working as my homeroom teacher, she also coaches a bunch of clubs after school."
    "Then I caused a problem and started living with her. Additionally, I created another worry by telling her I loved her."
    "She must be tired in both mind and body."
    "It might be my fault."
    "As I think about it, I can't stand it."
    "Later, Asumi and Tomoe join me."
    "Even after everybody leaves, I remain in the room watching over her."
    "I don't remember how long I've been here."
    "Suddenly, Ms. Yagami wakes up."
    "When she sees me, she gives me a weak smile."
    "Then I pull her to me."

    $ bgm (10)

    yusuke "Ms. Yagami..."

    voice yo0284
    yagami "I guess I fainted. You must have been worried about me, sorry."
    "She apologizes to me."
    "But it hurts me even more."
    "She's been suffering because of me."
    "I should simply accept her decision and live somewhere else."
    "Suddenly, Asumi's words come to mind."
    "...Follow your heart."
    "I don't know what will happen to us, but I should do my best!"
    "I don't want to deceive myself anymore."
    yusuke "Ms. Yagami, I..."

    voice yo0285
    yagami "I'm feeling okay, so..."
    yusuke "Ms. Yagami!"
    "Looking at her beauty..."
    "Listening to her voice..."
    "Feeling her warmth..."
    "I can't restrain my passion towards her."
    "Without thinking,"
    "I hold her tight."

    voice yo0286
    yagami "Hey, Yusuke!?"

    $ cg ('hy_0101', diss_long)
    $ unlock_gallery ('g4e4')
    $ bgm (14)

    voice yo0287
    yagami "Stop it, please!"
    yusuke "No! I don't want to hold back my feelings anymore because I..."

    voice yo0288
    yagami "No, stop it. Ah!"
    "I violently push her down on the bed."
    "I grab her breasts over her clothes."
    "A sensual sigh abruptly escapes her lips."
    "As I hear it, I get more excited."
    "Then I continue going at her breasts."
    yusuke "Your breasts are so soft and warm."

    voice yo0289
    yagami "Stop it! No, noooooo!"
    "When she refuses, I lose my momentum."
    "But I desperately kiss her, wiping the thought away."
    yusuke "Mmmm..."

    voice yo0290
    yagami "Ah, don't do that. No..."
    yusuke "I can't help it. I love you, Yoshiko."

    voice yo0291
    yagami "Ah, hah, aaah. Yusuke!"

    $ cg ('hy_0102')

    "Before I realize it, I have her blouse and even her bra off."

    $ cg ('hy_0103')

    "I continue massaging her charming breasts."
    "At the same time, I kiss her neck and her ears."
    "I caress her as much as I can."
    "I slowly move my hand toward her skirt."
    "As I touch the inside of her thigh, she twitches."

    $ cg ('hy_0104')

    voice yo0292
    yagami "No, don't touch me there! Ah, haah, aaah."
    "She tries to stop my hand."
    "However, she can't easily stop me."

    $ cg ('hy_0105')

    "I slide my fingers inside her panties. Then I open her slit and play with it."

    $ sfx ('SE04', loop=True)

    "As I move my finger, I hear nasty sounds in the room."

    voice yo0293
    yagami "Ah, aaah, ummm. No..,"

    voice yo0294
    yagami "Haaaah, I can't help it."

    $ sfx (delay=1.0)
    $ cg ('hy_0104')

    yusuke "Yoshiko...umm, mmm."
    "I kiss her again when she moans hopelessly."
    "I even entwine my tongue with hers."
    "Suddenly, I realize she's staring at me with wet eyes."
    "Then she whispers as if pleading with me."

    $ cg ('hy_0103')

    voice yo0295
    yagami "Please, Yusuke..."
    yusuke "Yoshiko?"
    "I wonder if she'll beg me to stop."
    "Instead, she turns red."

    voice yo0296
    yagami "I don't want to do it here. I'm too embarrassed."
    yusuke "But..."
    "I can't stop anymore."
    "Actually, I don't want to stop!"
    "Because I'm sure I won't have a second chance."
    "I falter."
    "Then she tells me in a sweet voice,"

    voice yo0297
    yagami "Let's go home."
    "It doesn't sound like she's refusing me."
    "At least I don't think so."
    "Because she gives me a dispelled, refreshing smile."
    "A slave to her smile, I move my head like a puppet."

    call blackout from _call_blackout_163

    "When we arrive back at her apartment, we start hugging passionately."
    "We don't care where we are anymore."
    "We look at each other."
    "And we intensely kiss."

    $ bgfx ('bg10c')
    $ char ('tyo202')
    $ bgm (13)

    voice yo0298
    yagami "Umm, mmmm."
    yusuke "Mmmm...haah, haah."

    $ char ('tyo114')

    "She moves away from my lips."
    "She gazes at me, as though she's mad at me."

    $ char ('tyo110')

    voice yo0299
    yagami "You got me, Yusuke. You tricked me."
    yusuke "...Sorry."

    voice yo0300
    yagami "It's too late to apologize, you know."

    $ char ('tyo202')

    "Again, we passionately kiss."
    "My tongue entwines with hers."

    $ char ('tyo120')

    "Then she suddenly starts snuggling closer."

    voice yo0301
    yagami "I knew I had feelings toward you, so I wanted to stop before it was too late."
    yusuke "But I've already..."
    "This time, she doesn't turn away."
    "Instead, she opens her eyes wide and stares at me."

    voice yo0302
    yagami "I don't want to deceive myself anymore. I want you to love me and in return, I want to love you too."

    $ bgfx ('black')

    "After holding each other and kissing for a while,"
    "We start undressing each other."
    "Then my hands crawl over her beautiful body."
    "And I slide towards her bush."
    "When I slide my finger in her pussy, I realize it's already wet."
    yusuke "Yoshiko, you're so wet down there."

    voice yo0303
    yagami "Don't tease me like that, Yusuke."
    yusuke "Mmm,mmmmm."
    "All of sudden, she kneels down,"
    "And she touches my dick."
    "Her sudden movement surprises me."
    yusuke "Ah, Yoshiko..."

    voice yo0304
    yagami "Don't you like it?"
    yusuke "Yeah, but..."
    "Of course I like it."
    "Yet I feel a little embarrassed."
    "She simply ignores me and starts touching it."
    "Unconsciously, I moan."
    "When she hears it, she gives me a wicked smile."
    "For a while, she continues touching my dick."
    "Suddenly, she puts it in her mouth."

    $ cg ('hy_0201', diss_long)
    $ unlock_gallery ('g4e5')
    $ bgm (14)

    voice yo0305
    yagami "Mmm, ummmm, mmmm."
    "My first blowjob."
    "I feel so good, I can't even say a word."
    "She looks at me with upturned eyes and caresses it with her tongue."
    "Then she sandwiches it with her big, soft breasts and starts playing with it with her hands."
    "Her mature technique is great, and I can't stop moaning."

    voice yo0306
    yagami "Haah, mmmm, aaaah."
    yusuke "Mmm, mmmm, aaah."

    voice yo0307
    yagami "Your penis is twitching in my mouth. It's so cute, isn't it!?"
    yusuke "......"
    "My face is so hot."
    "It probably looks like a red balloon."
    "I'm totally embarrassed."
    "Ignoring me, she accelerates her blowjob."
    "Using her fingers, lips, tongue, and her breasts."

    voice yo0308
    yagami "SLURP, SLURP, SLURP."
    yusuke "Hah, I feel so good."

    voice yo0309
    yagami "You're really getting big."
    "It feels as if several small thunder bolts zip through me."
    "My dick is twitching between her breasts."

    $ cg ('hy_0202')

    yusuke "Aaaah, I'm cumming."

    voice yo0310
    yagami "Ahhh, aah, aaah."
    "I can't hold it anymore."
    "As I shoot my hot cum at her face, she lets out a scream."
    yusuke "Haah, aaaaaah."

    voice yo0311
    yagami "You made a mess on my glasses, he he."
    "She smiles and wipes them off."
    "Yet I can't help apologizing to her."
    yusuke "I'm so sorry...mmmm, Yoshiko?"

    voice yo0312
    yagami "SLURP, SLURP."
    "Suddenly, she holds my hard dick in her mouth again."
    "As she caresses it, it swells even more than last time."
    "I can hear only her rough breathing."

    voice yo0313
    yagami "Yusuke, I..."
    yusuke "Aaah, haah...haaaah."

    voice yo0314
    yagami "Your..."
    "She strokes my rod."
    "And she looks at me."

    voice yo0315
    yagami "...I want you."
    yusuke "......"
    "I nod without saying a word."
    "Because I feel the same way she feels."
    "She hugs me tight."
    "I hold her tighter than ever."
    "Then we both fall down on the bed."
    "Before I realize it, she's climbing on top of me."
    "She looks a little embarrassed."

    $ cg ('hy_0301')
    $ unlock_gallery ('g4e6')

    voice yo0316
    yagami "Yusuke..."
    yusuke "Yoshiko..."

    voice yo0317
    yagami "Don't stare at me like that, okay?"
    yusuke "......"
    "She tells me not to stare at her, but..."
    "She's so beautiful."
    "I can't take my eyes off of her."
    "She pushes her wet pussy against my dick."
    "The view makes me more excited."
    "When she notices my piercing glance, she shyly twists around."
    "Every time she moves, her big boobs shake like Jello."
    "Her movements really arouse me."
    "With a bit of embarrassment, she grabs my rod."
    "She slowly slides it in her pussy."
    "A wonderful sense surrounds my rod."

    voice yo0318
    yagami "Mmm, mmmmm, haaaaah."
    yusuke "You're so hot and it feels great."

    voice yo0319
    yagami "Don't say such a thing...aaaah."
    "When I gaze at her,"
    "She looks away."
    "After a while, she gets red and finally looks at me."
    "We're staring at each other, rubbing our bodies together."

    $ sfx ('SE07', loop=True)

    "She begins moving her hips up and down."
    "I hear only wet sounds in the room."

    voice yo0320
    yagami "Mmm, mmmm, aaaah."
    yusuke "When you squeeze on me, it feels great! Mmmmm..."

    voice yo0321
    yagami "Aah, aaaah, mmmmmm, haah."
    "She keeps looking at me."
    "When she moves, her pussy really makes me feel good."
    "To counterattack,"
    "I stretch out my hands and grab her breasts."

    voice yo0322
    yagami "Aaah, don't touch my nipple."

    voice yo0323
    yagami "But it feels good."
    "As I caress her nipple, she shakes her long hair up and down."
    "I awkwardly start moving my hips."
    "Little by little, we both accelerate."

    $ cg ('hy_0302')

    voice yo0324
    yagami "Aaaah, yes!"
    yusuke "Haah, mmmm, ummm!"

    voice yo0325
    yagami "Don't move so hard. Otherwise, I...aaah."
    "It looks like she's having a hard time supporting herself."
    "All of sudden, she falls on me."
    "She holds me tight and kisses around my nipples."
    "However, she keeps moving her hips up and down."
    "I also move my hips harder than ever."

    voice yo0326
    yagami "Whew, Y...Yusuke...I..."
    yusuke "I'm cumming, Yoshiko. Mmm, mmm, ummmm."

    voice yo0327
    yagami "I can't hold it anymore, I'm cumming too. Ahh, mmmm, aaaaaaaah!!"
    yusuke "Ouch! Mmmmm, aaaaaaah!!"

    $ sfx (delay=0.5)
    $ cg ('hy_0303')

    "We cum at the same time."
    "She buries her fingernails in my chest."

    voice yo0328
    yagami "...Aaaaaah, haaah."
    "She slowly relaxes."

    $ music_stop ()
    $ cg ('hy_0304')

    "Even after cumming, she stays on top of me."
    "She's still breathing hard."

    $ bgm (10)

    voice yo0329
    yagami "Aah, haah, Yusuke..."
    yusuke "Yes?"

    voice yo0330
    yagami "You're such a trouble maker."
    yusuke "I'm surprised at myself too."

    voice yo0331
    yagami "You're so silly!"
    "I still can't believe what has happened."
    "A timid person like me made love with her!"
    "And it was unbelievably passionate."
    "I don't know what to do but laugh now."
    "However, I don't regret it at all."
    "As she looks at me, she chuckles and pokes my cheek."
    "Then she asks me,"

    voice yo0332
    yagami "I may love you more and more everyday. What should we do?"
    yusuke "I'm going to love you more too. I guess that makes us equal."

    voice yo0333
    yagami "Alright, then."
    "We kiss and lose ourselves in happiness."
    "Then we hold each other tight."

    $ bgfx ('black')

    "This isn't my goal."
    "I want to love her more."
    "I know there will be a certain wall between us."
    "But we'll still be able to communicate our feelings."
    "In fact, I'm so happy I've made love to her."

    $ music_stop ()
    $ bgfx ('sora05')

    "Keep our secret at school!"
    "It's the prerequisite condition for continuing our secret relationship."
    "As a matter of fact, we don't even discuss it."
    "It's just natural."
    "Because if I cause any more problems, I'm sure that not only me, but Yoshiko will be punished as well."
    "I understand it very well."
    "I know what I have to do, but when I see her face at school, my smile slips."

    $ bgfx ('bg05b')
    $ bgm (4)

    yusuke "Ms. Yagami, aren't you going home yet?"

    $ char ('tyo001')

    voice yo0334
    yagami "Not yet. Since the American Cracker Club will be in the national competition, I have to stay and watch them practice until very late."
    yusuke "I didn't know there was such a club at this school."
    "I'm flabbergasted."
    "Even worse, I'm really sad."
    yusuke "I thought I could have one of your home-cooked meals. What a pity!"

    $ char ('tyo014')

    voice yo0335

    yagami "I know I promised to cook your favorite, Mabo Harusame (pan fried minced pork with gelatin noodles in chili oil)."
    "We're much closer than before."
    "And recently, I've been teaching her how to cook."
    "She's keen on learning how to cook."
    "I guess she was just too lazy to cook for herself."
    "She's learned a lot from books and now knows more recipes than I do."
    "I'll bet she's changed because of my love!"
    "Every time I eat her home-made cooking, I think about such silly things."
    "That's why I'm sad that I can't eat my favorite dish tonight, made with her love."
    yusuke "Well, I guess I don't have any choice."

    $ char ('tyo019')
    $ bgm (14)

    voice yo0336
    yagami "Maybe I should coach fewer clubs."
    "When she whines, I object,"
    yusuke "Don't be silly! I really like you because you hang in there, you know."

    $ char ('tyo007')

    "When I tell her this, she smiles at me."
    "She suddenly grabs my hand and pulls me to a corner in the hallway."
    "She thanks me and..."

    $ char ('tyo019')

    voice yo0337
    yagami "Really? Thanks; here's your treat!"

    $ char ('tyo202')

    yusuke "Mmmm."
    "Are we okay kissing here?"
    "I'm a little embarrassed."
    "It seems as if I have a girlfriend from the same generation."

    $ char ('tyo201')

    "Then her lips move away."

    $ char ('tyo019')

    voice yo0338
    yagami "I'll give you more when I get home."
    yusuke "Sounds great! Your dinner will be ready by then, okay?"

    $ char ('tyo007')

    voice yo0339
    yagami "Thanks! I love you!!"
    yusuke "Even though you're buttering me up, it's still your turn to cook tomorrow."

    voice yo0340
    yagami "I know, I know."
    "We're like a couple on a honeymoon."
    "Even silly conversations like this make us happy."
    "We're really happy."

    call blackout from _call_blackout_164

    "Perhaps it's just my imagination."
    "Because we were careless,"
    "A teacher saw us kissing in the hallway."
    "We get caught and end up being punished."

    $ bgfx ('bg04b')

    "I wait for her to go home together."
    "She calls out to me with a lifeless voice."

    $ char ('tyo014')

    yusuke "Something wrong?"

    voice yo0341
    yagami "Yusuke..."
    yusuke "You look pale. Are you okay? Should we go to the nurse's office?"

    voice yo0342
    yagami "I'm fine. Why don't you go home and wait for me?"
    yusuke "O...okay."

    $ char ()

    "Then she goes to the teacher's office for a meeting."
    "I have no idea something bad is about to happen."
    yusuke "I wonder what's wrong with her?"
    "Of course, I care about her."
    "But I decide to go home alone."
    "Because I want to make her something yummy to cheer her up."

    $ bgfx ('black')
    $ bgfx ('sora08')
    $ bgm (8)


    "When she gets back, the Sukiyaki (thinly sliced beef and vegetables cooked in a skillet with sweet sauce) is already cold."
    "She really looks sick now."

    $ bgfx ('bg10c')
    $ char ('tyo110')

    "When I rush towards her, she gives me a severe look."
    "After hesitating for a moment, she starts talking."
    "The urgent faculty meeting:"

    $ char ('tyo115')

    "Somebody saw us kissing."
    "That's why the principal called all the teachers to talk about it."
    "Sobbing, she gives me the bitter reality."

    $ char ('tyo123')
    $ bgm (9)

    voice yo0343
    yagami "We were so stupid to be so careless."
    yusuke "That means...this time, I'm going to be expelled from school?"
    "I think I'm ready for just about anything."
    "Surprisingly, I'm calm."
    "I don't want to cause problems for her anymore, so if the school has decided to expel me, I'll accept it."
    "Somehow, I've made up my mind, just like that."
    "But her answer is different than what I expected."
    "It's a reasonable answer."
    "However, it's more painful than being expelled."

    $ char ('tyo114')

    voice yo0344
    yagami "No, you're safe, but I can't be with you anymore."
    yusuke "No, noooooooooo!"
    "I'm shocked at her words."
    "I can't stop raising my voice."
    "If I were expelled, I probably wouldn't be this shocked."
    "I won't be able to be with her anymore..."
    "Her words force me down into hell."

    call blackout from _call_blackout_165

    "The whole world is just a cloudy haze."
    "I neither say anything or even touch my food."
    "I'm burrowed in sorrow as time slowly goes on."
    "But..."
    "I remember her sad, depressed eyes."
    "I don't want to think about anything."
    "When I realize it, I'm lying on the floor."
    "And there's a blanket over me."
    "Somehow, I fell asleep."
    "I check the time and find I'm already late for school."

    $ bgfx ('bg10a')

    yusuke "Shit, I'm late!"
    "I rub my sleepy eyes and look around the room."
    "But I don't see her anywhere."
    "Because she's already left."
    "I don't think she'd ever ditch her work."
    "I hurriedly change my clothes and rush to school."

    $ bgfx ('black')
    $ bgfx ('sora01')

    "I'm really late."
    "But I can't do anything about it."
    "In fact, there's nothing I can do."
    "If I see Yoshiko, what should I say?"
    "If I talk to her at school, I'll probably cause her more problems."
    "She looked so sad last night."
    "I wonder if she'll start crying again if she sees me now."
    "The severity of reality presses upon me."
    "I don't get the chance to talk to her."
    "Even though I saw her, I couldn't go up to her."

    $ bgfx ('black')
    $ bgfx ('bg05a')
    $ bgm (9)

    yusuke "...Phew."
    "I don't care about anything anymore."
    "I slowly become irresponsible with an apathetic attitude."
    "Asumi, who probably doesn't know anything about what's going on, comes up to me."

    $ char ('tas001')

    voice as1219
    asumi "Can I have a minute?"
    yusuke "Okay."

    $ bgfx ('black')

    "She takes me to the rooftop."
    "Then she gives me the shocking news,"
    "'Ms. Yagami is going to quit.'"

    $ music_stop ()
    $ bgfx ('bg07a')
    $ char ('tas030')

    yusuke "Is that true, Asumi?"

    voice as1220
    asumi "Hey, calm down."
    yusuke "Oh, sorry."
    "I almost grab her."
    "She barely manages to pull away."

    $ char ('tas021')

    voice as1221
    asumi "I didn't hear everything, but the principal called her in and raked her over the coals."
    yusuke "......"

    voice as1222
    asumi "She's made up her mind to take responsibility. Hey, Yusuke!"

    $ char ('tas006')

    "I stop her."
    "And I run towards the teacher's office."
    "This time, I should have been expelled."
    "Instead, Yoshiko has decided to take all the blame."
    "She told the other teachers it was all her fault. That's why I wasn't dragged out and summoned."
    "I can't let her quit like this!"
    "That's all I can think about now."
    "Asumi smiles at my fleeting departure and wishes me luck."

    $ char ('tas045')

    voice as1223
    asumi "He's really unstoppable, he he."

    $ bgfx ('black')

    "Without thinking, I'm doing an unbelievable thing again."
    "I'm negotiating with the teachers."
    "I tell them,"
    "'I promise not to cause anymore problems, and I won't be involved with Ms. Yagami anymore.'"
    "Ms. Yagami is a great teacher, and I don't want her to give up her career."
    "It was all my fault, not hers."
    "If I hadn't forcefully asked her to love me, this kind of problem would never have happened."
    "I spill out everything I've been thinking about."
    "I'm neither joking nor making light of the situation."
    "I'm truly in love with her."
    "After all the ruckus, the principal decides to hold another faculty meeting."
    "It's a serious problem, and in most cases, shouldn't have to be brought up again."
    "Is it because of the soft school traditions?"
    "Or is it because most of the teachers here care more about people's feelings than traditions?"
    "Have any of the teachers understood my true feelings?"

    $ bgfx ('sora05')
    $ bgm (14)

    "I wait for Yoshiko alone in the apartment."
    "There's nothing else I can do."
    "I impatiently wait for her."

    $ bgfx ('sora08')

    "She comes back really late."
    "She gives me a confused glance,"
    "And then she starts telling me what happened in the meeting."
    "I didn't get expelled."
    "And she doesn't need to quit, either."
    "At last, she tells me they've found a room for me."
    "That means...all the teachers have agreed to forgive us."
    "Under the condition of not breaking any more school regulations."
    "There are probably a few who may wonder if it was a mistake."
    "But for now, the reality of being her student won't change until I graduate."
    "Until the moment comes, we have to define our relationship in a different manner."

    $ bgfx ('black')

    "Tonight is the last night we can spend together."
    "Tomorrow, I have to leave."
    "Thinking about the separation, I really feel depressed."

    $ bgfx ('bg10c')
    $ char ('tyo114')

    "It's late, so I guess nothing is open now."
    "After heating up the leftover Sukiyaki,"
    "We eat together in silence."
    yagami "......"
    yusuke "......"

    $ char ('tyo107')

    voice yo0345
    yagami "It feels as if someone close to us has died."
    yusuke "Yeah, you're right."
    "She forces herself to smile."

    $ char ('tyo101')

    voice yo0346
    yagami "I heard you marched into the faculty office."

    voice yo0347
    yagami "And you were ready to be expelled. That's unbelievable, Yusuke."
    yusuke "So you found out about it."
    "I knew someone would tell her about the incident."
    "Actually, it'd be natural for any friend of hers to tell her what her ex-boyfriend had done."

    $ char ('tyo105')

    "She tells me in a sharp voice,"

    voice yo0348
    yagami "You're so selfish...idiot."
    yusuke "Idiot? You too, Yoshiko."

    $ char ('tyo110')
    $ bgm (9)

    voice yo0349
    yagami "You're a super-duper idiot, you know that?"

    voice yo0350
    yagami "Don't get expelled, okay? I don't want to regret falling in love with you."

    voice yo0351
    yagami "I don't want to have the same miserable ending again."
    yusuke "Yoshiko..."
    "I knew what had happened to her."
    "However, I pushed her bitter memories of Naoto out of my mind."
    "The happiness of being with her made me forget all about her pain."
    "I caused her the same kind of suffering."
    "As she cries, I hold her tenderly."
    "But that's all I do. I'm not going to make her suffer anymore."
    "I know that's the only thing I can do for her now."

    call blackout from _call_blackout_166

    "Like this, the last night with her passes."
    "Early in the morning, she sees off me."
    "I carve her peaceful smile and even her puffed, red eyes in my heart."

    $ bgfx ('bg03a')
    $ char ('tyo101')

    voice yo0352
    yagami "This is it, isn't it!?"
    yusuke "Yeah, but I'll still see you in the classroom. Right, Yoshiko?"

    voice yo0353
    yagami "That's right."
    "Although I say it jokingly, it really hurts."
    "We both know that meeting everyday at school as teacher and student will hurt more than not seeing each other at all."
    "Our happy past can never return."
    "I make up my mind and tell her goodbye."
    yusuke "Goodbye, my love."

    $ char ('tyo115')

    voice yo0354
    yagami "...Goodbye."
    "Like this, our honeymoon comes to an abrupt end."
    "Our relationship returns to student and teacher."

    $ bgfx ('white', diss_long)
    $ bgfx ('sora01', diss_long)
    $ bgm (13)

    "My ordinary days have returned."
    "I'm right back where I started."
    "...Life without her."
    "After experiencing the joy of love, it's so painful when it's gone."
    "But I must lock this feeling away, somewhere deep inside me."
    "I don't want Yoshiko to sense my negative feelings."
    "I really need to force myself to forget her."
    "And if I have to, I'll completely erase my memories with her."
    "Because that's the only way I can repay her love and kindness."

    $ bgfx ('black')

    "Day after day, time drudges ahead."
    "...My dismal youth."

    $ bgfx ('bg04a')
    $ char ('tyo015')

    "I eventually accept the situation."
    "I mean meeting Yoshiko in the classroom or in the hallways doesn't hurt me anymore."
    "Actually, I don't feel anything."
    "I guess that's how people move on."
    "Forgetting even the greatest pain you've ever felt."

    $ music_stop ()
    $ bgfx ('sora02', diss_long)

    "Now, It's time to end the dismal days."
    "At last, I'm going to graduate."
    "...The day has come to say goodbye to my friends and the school."
    "This means it's time to say farewell to Yoshiko as well."

    $ bgfx ('bg05a')
    $ char ('tyo015')

    "I arrive at school earlier than usual, and I meet Yoshiko in the hallway."
    "Something that has become a mindless ritual,"
    "I say hello to her."
    yusuke "Good morning, Ms. Yagami."

    $ char ('tyo001')

    voice yo0355
    yagami "Yusuke, congratulations on your graduation."
    yusuke "Thank you."
    "Silence falls on us."
    "And I start moving my stationary feet."

    $ char ()

    "As one of her students, I say hello and thank her."
    "It looks as if it's natural that nothing more will happen between us."

    $ bgfx ('sora02')

    "At last, our graduation ends."
    "After the ceremony, my friends and I get together."

    $ bgfx ('bg11a')
    $ char ('tas001')
    $ bgm (10)

    voice as1224
    asumi "We finally made it. Anyway, our real lives will start from here on, right?"

    $ char ('tma001')

    voice ma0466
    marumu "It just started!"
    "We all look sad, even though we're happy to graduate."
    "Tomoe suddenly opens her mouth,"

    $ char ('tto013')

    voice to0892
    tomoe "Someday, let's meet again. How about looking forward to a 'special meeting?'"

    $ char ('tas005')

    voice as1225
    asumi "Sounds good! Then how about having our first special meeting right this minute?"

    $ char ('tma008')

    voice ma0467
    marumu "Agreed!"
    "In a flash, everybody agrees with Asumi."

    $ char ('tto011')

    "Tomoe's amazed, but at the same time, she looks happy."

    voice to0893
    tomoe "You guys are so sudden. Anyway, are you going to join us, Yusuke?"
    "However, I pass on the delightful invitation."
    "Because I have something on my mind."
    yusuke "Sorry, Tomoe. Unfortunately, I have something I have to do before leaving school."

    $ char ('tto013')

    voice to0894
    tomoe "Why? Does it have to be today? We won't see each other for a long time, so let's go..."

    $ char ('tas044')

    voice as1226
    asumi "...Moe-Moe."
    "Asumi puts her hand on Tomoe's shoulder and interrupts her."

    $ char ('tto004')

    voice to0895
    tomoe "Asumin?"
    "Tomoe stares at her."
    "Before opening her mouth, she realizes what Asumi is trying to tell her."
    "Tomoe snaps her mouth shut."
    "I say farewell to my wonderful roommates."
    yusuke "Sorry, Tomoe. Well, see you guys around, okay?"
    "I jerk around and run back towards the building."

    $ char ('tas045')

    "Asumi whispers,"

    voice as1227
    asumi "Good luck, Yusuke."

    call blackout from _call_blackout_167
    $ bgfx ('bg05b')

    yusuke "Phew!"
    "I take a deep breath and enter the classroom."
    "The room where I and my friends spent a year."

    $ bgfx ('black')

    "I didn't ask her to meet me."
    "In other words, we haven't promised each other anything."
    "But I'm sure she'll be here."
    "That's why I needed to come here one last time."
    "She's standing there alone in the empty room."
    "My homeroom teacher, who cares more about her students than herself."
    "She looks at me in surprise and mutters as she sees me rush into the room."
    "...My name."

    $ bgfx ('bg04b')
    $ char ('tyo010')

    voice yo0356
    yagami "Yusuke..."
    yusuke "It hurt so much, you know."

    voice yo0357
    yagami "What?"
    "I've been keeping it inside, not saying anything."
    "But since I don't need to hold it in anymore, I've come to the classroom for the last time."
    "I just want to clear up my muddy feelings before I leave."
    yusuke "Although we're in the same room, I'm not allowed to touch you anymore."
    yusuke "But still, I can't completely erase my feelings toward you. It's impossible to forget you."
    yusuke "Even after we broke up, I kept loving you. And now, I love you more than ever!"
    yusuke "I can't stop loving you."

    $ char ('tyo014')

    yagami "......"
    "I throw out all I want to say."
    "I want to tell her this before leaving her forever."
    "Though I know we can't go back in time,"
    "I just can't graduate without telling her my true feelings."
    "At the same time, I wish a miracle would happen once more."
    "Finding her in the big universe was the first miracle."
    "Then we fell in love."
    "Please God, let me have one more miracle."
    yusuke "You don't need me anymore? Don't you feel like you used to?"
    yagami "......"
    yusuke "Even if you've already forgotten about our love, I wanted to tell you that I'm still in love with you."
    yusuke "I just wanted to say this before I leave."
    "She stares at me in silence."
    "She's calm, but somehow, her eyes look sad."
    "I gaze back at her."
    "I've told her everything on my mind."
    "Thus, I don't have any regrets."
    "And I'm proud of myself for being brave and honest."
    "She remains silent, though I've finished talking."
    "The heavy air surrounds us in the empty room."
    "I can't stand the silence anymore, so I tell her goodbye."
    "This time, it's a real farewell."
    yusuke "Goodbye, my love."
    "After saying this, I turn around, facing the other direction."
    "I don't have any regrets at all."
    "Because I don't need to pretend to be somebody else or lie about my feelings anymore."

    $ bgfx ('black')
    $ bgm (9)

    "For the last time, I glance around my classroom."
    "Then I leave without looking back."
    "I look straight ahead and keep moving my legs."
    "But as I'm about to leave the building, someone calls to me from behind."
    "The voice of my love."
    "I hastily jerk my head backwards."

    $ bgfx ('bg11b')
    $ char ('tyo015')

    "Yoshiko rushes toward me with downcast eyes."

    voice yo0358
    yagami "...Me too."
    yusuke "Excuse me?"

    voice yo0359
    yagami "I'm still in love with you. It's not that easy to forget my love, you know."

    voice yo0360
    yagami "Even after the incident, my feelings for you have never changed."
    yusuke "Yoshiko!!"

    $ cg ('ey_02', diss_long)
    $ unlock_gallery ('g4e7')

    "Even though she was beside me, I couldn't touch her for a long time."
    "Until today, I had to control the urge to hug and kiss her."
    "It was so bitter."
    "But now, I know she's been having as hard a time as I have."
    "She kept her true feelings hidden deep inside her."
    "So no one could read her mind."
    "Anyone would do the same."
    "Since people aren't that strong, it's hard to bear the pain."
    "However, even through the harsh days, our love has never changed."
    "We didn't have to force ourselves to forget each other."
    "Now we both understand it's from the bottom of our hearts."
    "As she gives me a bright smile,"
    "We both run up and hug each other tightly."
    "To make up for lost time."
    "And to remember what we almost lost."
    yusuke "I'll never leave you."

    voice yo0361
    yagami "Of course, stay with me forever, and promise not to go anywhere without me!"
    yusuke "I promise I won't make you worried, ever."

    voice yo0362
    yagami "Yes, yes!"
    "At last, I graduate."
    "I know I'm not mature enough to be called an adult."
    "But I believe I've grown up a little."
    "So I will keep learning."
    "To become strong enough to support her."
    "And to be with my love forever."
    "To confirm my resolution,"
    "I keep hugging her tighter than ever on the empty school grounds."
    "Nothing can obstruct us anymore."
    "Then we pledge to believe in each other and to be happy ever after."

    call blackout (True) from _call_blackout_168

    jump credits
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

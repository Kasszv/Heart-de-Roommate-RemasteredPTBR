label episode17_marumu:

    $ bgm (12)
    $ bgfx ('bg01a')
    $ char ('tto201')

    voice to0268
    tomoe "I won't be back tonight."
    yusuke "Okay! Have a nice one, Moe-Moe."
    "As I see her off, Asumi goes to the door."
    "She's wearing her school uniform on a weekend."

    $ char ('tas001')

    voice as1110
    asumi "Wait, Moe-Moe! I'll go some of the way with you. Bye, Yusuke!"
    yusuke "You're going out too. Bye."

    $ char ('tas037')

    voice as1111
    asumi "You treat me differently... I'll let the matter pass this once."
    "That's rare."
    "I don't like to be attacked, but it's really rare..."
    "They're leaving."
    "I don't see the other girl in here."

    $ char ('tto225')

    voice to0859
    tomoe "Stay with Marutan today."

    $ char ('tas012')

    voice as1112
    asumi "Yeah, you guys are lovers...he he."
    "They're smiling."
    "I don't think they believe we're really lovers."
    "Somehow, I feel like that."
    "But I understand why they think that."
    "In fact, even I don't think it's real."


    call ep_start from _call_ep_start_18

    "After they leave, I knock on Marumu's door."
    "I wonder what she's doing."
    "Marumu comes out of her room with Toshibo."

    $ bgm (2)
    $ bgfx ('bg01a')
    $ char ('tma101')

    voice ma0341
    marumu "What happened?"
    yusuke "Well, we're to stay at home today."
    "It's an exciting opportunity."
    "Our other roommates are gone, and just the two of us are here."
    "However, she coldly tells me,"

    $ char ('tma104')

    voice ma0342
    marumu "Yusuke, why don't you go out?"
    yusuke "Huh? Why?"

    voice ma0343
    marumu "I'll stay here with Toshibo."

    $ char ('tts004')

    voice ts0073
    toshibo "Meow!"
    "Marumu and her buddy suggest that I go out."
    "That's nice, but I don't understand."
    yusuke "Thank you...but would I bother you if I stayed?"

    $ char ('tma104')

    voice ma0065a
    marumu "......(nod)"

    $ music_stop ()

    "She doesn't mince her words."
    "I feel sad and miserable."
    "I'm also shocked at her cold attitude."
    "Are we really lovers?"

    $ char ()

    "She clearly indicated I'm not wanted here."
    "I don't have any particular place I want to go, but I go out alone anyway."
    "Though I say goodbye to her, she answers with no interest."
    "Is she doing something in her room?"

    $ vox ('ts0074')

    "I think I heard a noise or an animal's scream...maybe it's only my imagination."

    $ vox (delay=0.3)
    call blackout from _call_blackout_114
    $ bgfx ('sora01')
    $ bgm (6)

    yusuke "Umm...I feel something..."
    "Since leaving the dorm, I feel something on my back."
    "Someone's following me or something...?"
    "But I'm not that sharp."
    "I find out the reason right away."
    "I'm not sharp."
    "The person who's following me is conspicuous."
    "But...who? And for what?"
    yusuke "He looks like a child..."
    "I can't ignore him."
    "I decide to find out who he is."


    call ep_middle from _call_ep_middle_19

    $ bgfx ('bg03a')
    $ char ('tki001')

    boy "......!!"
    yusuke "Hey, what can I do for you?"
    "I ask the kid who's trying to tail me."
    "But..."
    boy "......"
    yusuke "Please tell me why you're following me."
    boy "......"
    yusuke "Ugh! Please, please tell me!"
    boy "......"
    "He doesn't reply at all."
    "I've seen a very similar face and attitude before...I remember seeing them somewhere. Ohh...I just can't ignore it."
    yusuke "Tell me please! If you don't tell me, I'll..."

    $ char ('tki002')

    boy "...h...hic..."
    yusuke "I won't be able to sleep tonight... Oh?"

    $ bgfx ('sora01')
    $ bgm (7)

    "He almost cries...no, he's already crying."
    "Does he think I'm mad at him?"
    "I can't leave him alone...phew."

    call blackout from _call_blackout_115
    $ bgfx ('bg03a')
    $ char ('tki003')
    $ bgm (6)

    boy "A good man..."
    yusuke "Well, thanks."
    "I try to comfort him but don't succeed."
    "He was looking at the candy in a store, so I bought some for him."
    "Then...look at him."
    "I'm thoroughly disgusted."
    "I think he understands I'm not upset at him."
    "I ask him again,"
    yusuke "Would you tell me why you followed me?"
    "The kid tells me in a soft voice,"
    boy "You pass the test with the lowest score."
    yusuke "Pass...?"
    boy "As my sister's boyfriend."
    yusuke "Your sister... What?"
    "Sister...his sister?"
    "I'm his sister's boyfriend...that means he's..."

    $ char ('tki001')

    boy "How do you do? My name is Kirimaru Ogumayama."
    yusuke "How do you do...?"
    "He looks like her...exactly."
    "I didn't know Marumu has a brother."
    "He explains why he was following me."

    call blackout from _call_blackout_116
    $ bgfx ('bg14a')
    $ char ('tki001')

    kirimaru "She needs a really good man, not an ordinary man."
    yusuke "Is that so...?"
    "I'm not sure but something happened to her in the past."
    "She's sure a mysterious girl. I don't think an ordinary man is good enough for her."
    "Yet, there is more in her past."
    kirimaru "Ah...do you have some time?"
    yusuke "Y...yeah."
    "He asks me politely, but it sounds funny."
    "And I nod at him."
    "Kirimaru starts talking about Marumu."
    "The secret of the mysterious girl will be exposed...I'm excited!"
    "However, my excitement is blown away as he tells me about her."

    $ bgfx ('black')

    "He proudly tells me,"
    "His IQ is more than 160."
    "I don't know the details, but he's quite a smart kid."
    "Everyone in the Ogumayama family is smart."
    "Of course, Marumu isn't an exception."
    "But Kirimaru tells me,"
    "'She's special...'"

    $ cg ('em_0101', pos=[ALIGN(0.0, 0.0)])
    $ bgm (9)

    "She lost something important."
    "It was the balance between her emotions and knowledge."

    $ bgfx ('black')
    $ cg ('raf_2801')
    $ unlock_gallery ('g6e10')

    "When they were little kids,"
    "They went hiking with their parents."
    "The joyful weekend turned into a nightmare."

    $ cg ('raf_2802')

    "Kirimaru was lost in the mountains."
    "Marumu was worried about him so much that she kept looking for him, though her parents tried to stop her."
    "Then she slipped..."
    "Two days later, the search party finally found her."
    "Kirimaru walked down the mountain alone. He blamed himself."

    $ bgfx ('black')

    "Marumu was in critical condition."
    "She hit her head hard and lost a lot of blood."
    "Fortunately, she escaped death."
    "Until she was rescued, she dimly looked up at the sky."

    $ bgfx ('sora02')

    "All she could do was look at the blue sky in the daytime and the moon at night."

    $ cg ('em_0101', pos=[ALIGN(0.0, 0.0)])

    "Blood streamed out of her head as if taking precious things from her."
    "Still, she looked up at the sky."

    $ bgfx ('black')

    "She gradually recovered."
    "However, an after-effect is left from the injury to her head."
    "Fragmentary knowledge and emotions were lost."

    $ cg ('raf_29')

    "Similar to amnesia, she became like a pure, innocent baby."
    "She went through rehab training and rapidly recovered with her family's support."
    "But the difference between her knowledge and her emotions has risen."
    "The part of her brain that manages knowledge fully recovered and works fine."
    "On the other hand, the part of her brain that manages emotions has not fully recovered."
    "She remains unbalanced."
    "Because of this, a unique and pure sensibility has taken over."

    call cg_slide (picture='em_0101', tm=2.0, kind='v', start=1.0, end=0.0, cls=diss_fast) from _call_cg_slide_17

    "Soon, she noticed what was going on inside her."
    "Yet, she wasn't sorry or sad."
    "She lost something...something precious."
    "She recalls it when she sees the bright moonlight."
    "While she was losing everything, she looked at the light."
    "She lost a lot of things..."
    "Then she thought,"
    "If she continues to look at the light,"
    "Someday, she'll remember what she lost."
    "Her family has watched over her affectionately."
    "She hasn't changed at all."
    "However, other people reacted differently."
    "They compared her to before the accident."
    "They treated her in different ways."
    "That's why she transferred to Aiho School two years ago."
    "To start a new life."

    call blackout from _call_blackout_117
    $ bgfx ('bg14a')
    $ char ('tki001')

    kirimaru "I love my sister...so please..."
    yusuke "......"
    kirimaru "Please accept who she is...please."
    yusuke "O...okay."
    "I nod."
    "That's all I can do."
    "Though I still don't understand what she's been through."
    "I nod at him."

    $ bgfx ('black')
    $ bgm (8)
    $ bgfx ('sora07')

    "I return to the dorm in the evening."
    "What a day...a shocking, agitating day."
    "I had no idea she had such a terrible past."
    "How should I act towards her?"
    "Will I be able to keep my promise to Kirimaru?"
    "He asked me to treat her the same as usual."

    $ bgfx ('bg02b')

    yusuke "It's hard to do..."
    "But I can't stand outside any longer."
    "I'm not wearing girls' clothes today. I have to return in secrecy."
    "I'm reluctant to go back..."

    $ music_stop ()
    $ bgfx ('bg01c')

    "As I open the door, a girl welcomes me."
    "It's not Asumi or Tomoe."

    $ char ('tma101')

    "It's Marumu."

    voice ma0344
    marumu "Welcome back, Yusuke."
    yusuke "H...hello."

    $ char ('tts010')

    voice ts0075
    toshibo "Meow..."
    "Toshibo looks tired next to her."
    "What did they do today?"

    $ char ()
    $ bgm (14)

    "I enter the room with Marumu."
    "Well, what should I say...? I'm nervous."
    "I can't help thinking about her past."
    "Act naturally, act naturally..."

    $ char ('tma101')

    yusuke "Uh...what did you do today?"

    voice ma0345
    marumu "I studied."
    yusuke "Oh...you're a good student."
    "I want to believe her, but I don't know what she studied."
    "As I sink into silence, she tells me,"

    voice ma0346
    marumu "Yusuke, close your eyes."
    yusuke "Huh? Okay..."

    $ bgfx ('black')

    "Is she going to give me a present? Or did she cook something for me?"
    "I close my eyes with expectation and mixed feelings."
    "And I wait for her to say, 'Open your eyes.'"

    voice ma0347
    marumu "...Rustle-Rustle."
    "I feel ticklish all over."
    "Feeling uneasy, I ask her,"
    yusuke "Marutan...?"

    voice ma0348
    marumu "Huh...?"
    yusuke "What...are you doing?"

    voice ma0349
    marumu "I'm taking off your clothes."
    yusuke "What...? WHAAA!"

    $ bgfx ('bg01c')
    $ char ('tma103')
    $ bgm (7)

    "I'm slow."
    "I didn't know my clothes were being taken off!!"
    "With startled eyes, I try to stop her."
    "But she jumps on me and pushes me down in the closet (my bedroom)."

    $ bgfx ('black')

    "I'm totally naked."
    "Marumu starts taking off her clothes too."
    "I'm completely flabbergasted."
    "What's going to happen? What will happen to me?"
    "Someone...tell me, please."

    $ music_stop ()
    $ cg ('hm_0201')
    $ unlock_gallery ('g3e7')

    yusuke "What are you doing...?"

    voice ma0350
    marumu "We're going to sleep together."
    yusuke "I see..."
    "She takes all her clothes off."
    "She lies down next to me, naked."
    "But she doesn't do anything more; she just stays with me."
    "This futon is too small for two people."
    "I was worried, but this is the way Marumu acts."
    "She's an extraordinary character."
    "I love her, including her unique personality."
    "As long as she's happy, I'm okay."

    $ bgm (14)

    "Thinking about her, I look at her."
    "She's staring at me naked, and I get aroused."
    "This is a man's nature to get excited."
    "She doesn't want to do anything with me, I guess."

    voice ma0351
    marumu "Yusuke."
    yusuke "Huh? What?"

    voice ma0352
    marumu "Yes, you can."
    yusuke "What?"

    $ cg ('hm_0203')

    voice ma0353
    marumu "You can touch me."
    yusuke "I see... What!?"
    "I can't control myself any longer."
    "She moves closer to me."
    "She seems to see right through me... I yelp involuntarily..."
    "But...still..."

    $ cg ('hm_0204')

    "After hesitating a minute, I touch her thigh with a shaking hand."
    "Her skin is soft, warm, and smooth."
    "It tells me she's a girl."
    "I caress her body, enjoying the feeling."
    "Occasionally, I look at her."
    "But she doesn't show any response."
    "Nor does she say a word."
    "I'm confused."
    "Doesn't she feel good? Am I awful?"
    "Or is she a frigid woman?"
    "The unpleasant thought is spinning around in my head."
    "On the contrary, my dick is getting harder."

    $ cg ('hm_0202')

    "She's watching it."

    voice ma0354
    marumu "Are you...?"
    yusuke "What?"

    voice ma0355
    marumu "Are you ready?"

    $ music_stop ()

    "Pointing at my dick, she asks me,"
    "I get even more excited."
    "Ready for...well...ahh..."
    "I furiously shake my head side to side."
    yusuke "Actually, I'm not ready..."

    voice ma0356
    marumu "I'll do my best."
    yusuke "Do...what?"

    voice ma0357
    marumu "I'll try what I learned today."

    $ bgfx ('black')

    "She gets up."
    "Then she stretches out her hand to my cock."
    "Holding it, she starts jerking me off."

    $ bgm (6)
    $ cg ('hm_0301')
    $ unlock_gallery ('g3e8')

    yusuke "H...hey...mmm."
    marumu "......"

    $ cg ('hm_0302')
    $ cg ('hm_0301')

    "Her small hands are polishing my rocket."
    "How can I say it... It tickles more than it feels good."
    "I twist my hips with the strange sensation."

    $ cg ('hm_0303')
    $ cg ('hm_0302')

    "She continues to move her hands as if she's trying to do different things."
    "Soon..."

    voice ma0358
    marumu "Kiss..."
    yusuke "M...Marumu?"
    "She kisses the tip of my dick."

    voice ma0359
    marumu "Snap..."
    yusuke "Ugh...uh..."
    "She tries to hold my cock in her mouth."

    voice ma0360
    marumu "Chomp..."
    yusuke "Ouch! Don't bite it..."
    "She bites my dick."
    "She sadly murmurs,"

    $ music_stop ()
    $ cg ('hm_0301')

    voice ma0361
    marumu "It's too big to fit in my mouth."
    yusuke "......"
    "She looks at me."

    voice ma0362
    marumu "What should I do, Yusuke?"
    yusuke "I...I don't know."
    "She's seriously worried about it."

    $ bgm (9)

    voice ma0363
    marumu "I studied, but I can't..."
    yusuke "Marumu..."
    "She doesn't cry, but she looks so sad."

    voice ma0364
    marumu "I'm not able to give you pleasure."
    yusuke "Give me pleasure... Well..."

    voice ma0365
    marumu "I'm not qualified to be your girlfriend."
    "She's depressed."
    "Though she studied hard, she can't do it very well."
    "What a pure, charming girl she is..."
    "I remember what Kirimaru told me."
    "And I chuckle."
    yusuke "Heh heh."

    call blackout from _call_blackout_118
    $ bgm (14)
    $ cg ('hm_0201')

    "I smile and draw her closer to me."
    "We lie down together and I tell her,"
    yusuke "I'm glad you studied a lot, but don't push yourself too hard."

    voice ma0366
    marumu "Yusuke..."
    "She looks relieved at my words."
    "I honestly tell her my true feelings,"
    yusuke "I haven't studied at all."
    yusuke "Besides, there are many ways to make love; they aren't like studying and finding one answer for an exam."

    voice ma0367
    marumu "Really?"
    yusuke "Yeah, I guess..."
    "I nod my head."
    "Holding her tight, I comfort her."

    voice ma0368
    marumu "Ah..."
    "She blushes for a moment...I'm not sure it really happened."
    "I'm satisfied with it."
    yusuke "I'm happy being with you like this."

    voice ma0369
    marumu "Yusuke..."

    $ cg ('hm_0203')

    "She clings to me."
    "Feeling her warmth, I tell her again."
    yusuke "We can do this at our own pace."

    voice ma0370
    marumu "Our own pace?"
    yusuke "Yup, our own pace!"
    "Our love looks strange to other people."
    "Our love is different from those seen in books or movies."
    "But I don't care...I truthfully feel like that."
    "It doesn't matter. Love is love."
    "We don't need to copy someone's love or manual books."

    $ bgfx ('sora09')

    "I softly stroke her head."
    "Trying to know more about each other is much more important."
    "Holding me tight, she whispers,"

    voice ma0371
    marumu "I love you, Yusuke."

    jump episode17_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

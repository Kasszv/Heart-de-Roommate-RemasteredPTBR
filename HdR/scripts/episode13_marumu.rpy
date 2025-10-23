label episode13_marumu:

    $ F018 += 1
    $ music_stop ()
    $ cg ('em_0101', pos=[ALIGN(0, 0)])

    "I'm not used to facing girls one on one."
    "Especially Marumu."
    "But I can't lose my resolve."
    "I decided to declare my love to her, so I called her here."

    if F018 >= 5:
        jump episode13_marumu_route

    $ bgfx ('black')

    "But she doesn't come."
    "I've been waiting a long time, but she still hasn't shown up."
    "I've become more and more interested in her."
    "But I have no idea what she thinks."
    "What was that kiss?"

    $ bgfx ('bg01a')
    $ char ('tma107')

    yusuke "Good morning, Marumu."
    marumu "......"
    "She's always at her own pace."
    "I'm okay with it."
    "I'm expecting to have a relationship with her."
    "But I realize this is a bit one-sided since I haven't done anything to expect a romantic relationship with her."

    $ bgfx ('black')

    jump game_over



label episode13_marumu_route:

    $ F015 = 2
    $ bgm (2)
    call cg_slide (picture='em_0101', tm=1.5, kind='v', start=0.0, end=1.0, cls=diss_fast) from _call_cg_slide_6

    yusuke "Marumu..."

    voice ma0259
    marumu "Marutan."
    yusuke "Oh, that's right."
    "She sounds like Asumi. That's not good."
    "I secretly think about it."
    "I continue,"
    yusuke "Marutan..."

    $ cg ('em_0102', pos=[ALIGN(0.0, 1.0)])

    voice ma0260
    marumu "Clearly."
    yusuke "Y...yes."
    "I'm swallowed up in her pace."
    "I feel scared now."
    "But I have to tell her..."
    yusuke "I've been thinking, Marumu."

    voice ma0261
    marumu "Your answer?"
    yusuke "Huh? My answer?"
    "I don't know what she's talking about."
    "But Marumu reminds me,"

    voice ma0262
    marumu "Marutan loves Yusuke."
    yusuke "Th...thank you."
    marumu "......"

    $ music_stop ()

    "Yes, I remember. She told me that when we kissed."
    "Perhaps I should give her my answer before I tell her how I feel about her."
    "Respond to Marumu."
    "Tell her honestly."
    "As soon as I think this, I decide to give her my answer first."
    yusuke "I love you too, Marutan."

    voice ma0263
    marumu "Do you want to go out with me?"
    yusuke "......"
    "I came here to ask her about it, so I'd better just nod."
    "But I hesitate for a second."
    "She looks anxious at my hesitation."
    "I see her sad expression and quickly nod."
    yusuke "Y...yes! I want to!"

    voice ma0065a
    marumu "......(nod)"
    "She nods."
    "We both want to have a relationship...don't we?"

    call cg_slide (picture='em_0102', tm=1.5, kind='v', start=1.0, end=0.0, cls=diss_fast) from _call_cg_slide_7

    "Marumu and I begin our relationship."
    "...Right?"


    call ep_middle from _call_ep_middle_2

    $ bgm (12)
    $ bgfx ('bg01a')
    $ char ('tma001')

    voice ma0264
    marumu "Good morning, Yusuke."
    yusuke "Good morning, Marutan."
    marumu "......"
    "I couldn't sleep after that last night."
    "Marumu and I easily started something."
    "But what should I do next?"
    "While thinking about it, morning came."
    "It's Marumu's turn to cook breakfast."
    "Marumu hasn't changed at all."
    "How should I react?"

    $ char ('tas105')

    voice as1078
    asumi "What's wrong, Yusuke?"
    yusuke "N...never mind."

    voice as1079
    asumi "You look out of it this morning."

    $ char ('tto128')

    voice to0816
    tomoe "...Good morning."

    voice as1080
    asumi "Well, you're better than Moe-Moe in the morning, anyway."

    $ char ('tma003')

    marumu "......"
    "Marumu continues preparing breakfast."
    "Before school and even at school, Marumu doesn't act any different than usual."

    $ music_stop ()
    $ bgfx ('sora09')

    "I become anxious."
    "When we get back, and even before we go to sleep, she acts the same."
    "Does she understand what becoming lovers means?"
    "No, I shouldn't think about it. Otherwise, I won't be able to sleep tonight either."
    "While I'm thinking about it, I hear the sounds of someone's footsteps."
    "I look out of the closet and see Marumu getting ready to leave."
    "Perhaps she's going to her usual place."
    "I decide to follow her."

    $ bgm (2)
    $ cg ('em_0101', pos=[ALIGN(0.0, 1.0)])

    "When I get to the roof, Marumu's looking at the moon."
    "She looks sad whenever I see her here."
    "I just watch her without saying anything."

    $ cg ('em_0102', pos=[ALIGN(0.0, 1.0)])

    "She turns back as she notices me."

    voice ma0265
    marumu "...Hi, Yusuke."
    yusuke "W...well, I just..."
    marumu "......"

    $ cg ('em_0101', pos=[ALIGN(0.0, 1.0)])

    "She looks up at the moon again."
    "I watch her for a while, and then I ask,"
    yusuke "Marutan, can I ask you something?"

    voice ma0065a
    marumu "......(nod)"
    yusuke "We decided to become lovers, right?"

    voice ma0065a
    marumu "......(nod)"
    yusuke "Do you think it's good just the way it is?"

    $ cg ('em_0102', pos=[ALIGN(0.0, 1.0)])

    voice ma0266
    marumu "Yusuke, do you want to do it?"
    yusuke "Eh?"
    "I freeze at her words."
    "I never dreamed Marumu would say such a thing."
    "My heartbeat quickens."
    "I calm down and tell her,"
    yusuke "No, no. But..."

    voice ma0267
    marumu "Do you want to kiss?"
    yusuke "Heh?"

    $ music_stop ()

    "OH! She meant a kiss... Whew, I'm kind of relieved."
    yusuke "A...kiss. Yeah...why not? We're lovers."

    $ cg ('km_01')

    voice ma0268
    marumu "Smooch!"

    $ bgm (13)

    "A sudden kiss."
    "Such a light kiss, but our lips touch for a second."
    "I'm really surprised."

    $ cg ('em_0102', pos=[ALIGN(0.0, 1.0)])

    "When her lips leave mine, I look at her with amazement."
    "Marumu goes back to looking at the moon again and remains silent."
    "I look at the moon also."
    "Even if I copy what she's doing, I have no idea what she's thinking."
    "We watch the moon for a while."
    yusuke "I don't feel like we're lovers at all."

    voice ma0269
    marumu "...Why is that?"
    yusuke "Well, I think we need to learn about our relationship more."

    voice ma0270
    marumu "Learn."

    call blackout from _call_blackout_21

    "As soon as she hears me, she suddenly stands up."
    "And she gets down from the roof."
    "I hurriedly follow her."

    $ bgfx ('bg01d')

    "Just before she enters her room, she turns back."

    $ char ('tma101')

    voice ma0271
    marumu "...I'll learn."
    yusuke "Learn...about what?"

    voice ma0272
    marumu "About lovers."
    yusuke "H...hey! Marumu!"

    $ char ('tma118')

    voice ma0273
    marumu "Marutan..."

    $ char ()

    "She sounds like Asumi."
    "After she says this, she goes in her room."
    "I'm kind of nervous."
    yusuke "Learn about what?"
    "I hope she doesn't misunderstand."

    $ bgfx ('black')

    "A few days later..."
    "When I return, Marumu calls to me."

    $ bgfx ('bg01a')
    $ char ('tma101')

    yusuke "Huh, Marutan?"

    voice ma0274
    marumu "Yusuke, come with me."
    yusuke "Okay."

    $ bgfx ('black')

    "She takes me to her room."
    "And as soon as we're inside, she suddenly..."
    "...rolls up her T-shirt."

    $ bgm (7)
    $ cg ('em_0201')
    $ unlock_gallery ('g3e5')

    "She's not wearing a bra underneath her T-shirt."
    "Her cute little breasts appear."
    "I'm at a loss for words with the view."
    yusuke "Marutan?"
    marumu "......"
    yusuke "What are you doing?"

    voice ma0276
    marumu "Showing you my breasts."
    yusuke "I know, but..."

    voice ma0277
    marumu "I've learned."
    yusuke "What did you learn...? (POUND! POUND!)"
    "I don't know how I should react."
    "Should I praise her, be mad at her or stop her? What should I do?"
    "While I'm thinking, she asks me,"

    voice ma0278
    marumu "Yusuke, are you satisfied?"
    yusuke "I don't know..."

    voice ma0279
    marumu "...Touch them."
    yusuke "Touch them...but..."
    "I can't answer."
    "But it's not good to do nothing."
    "People say, 'Don't make girls embarrassed.'"
    "She's staring at me."
    "I have to do something... (POUND! POUND!)"
    "Finally, I stick out my hands."

    $ cg ('em_0202')

    marumu "......"
    yusuke "......"
    "I touch her breasts."
    "But she doesn't show any reaction."
    "I just did it, but was it okay?"
    "I feel like she's coldly looking at me... No, she's the same as always."
    "I go stiff touching her breasts."
    "But Marumu tells me something unbelievable next."

    voice ma0280
    marumu "Rub them."
    yusuke "B...but...huh, huh..."
    "She tells me this without any passion, but I'm excited anyhow."
    "I deeply breathe once and then slowly press against her breasts."
    "Marumu's breasts... They're soft but not very elastic."
    "After I slowly rub them, I look at her."
    "She doesn't show any reaction at all."
    "My body starts to shake at her cool eyes."
    "I'm so nervous. Next, I rub them harder."

    $ music_stop ()
    $ cg ('em_0203')

    voice ma0281
    marumu "...Aah."
    "(POUND! POUND!)"
    "Was that a m...moan?"
    "Did she moan?"

    $ cg ('em_0202')

    voice ma0282
    marumu "Do you like to hear me moan?"
    yusuke "......"
    "I hold my head at her words."
    "What are we doing!?"
    "Suddenly, we hear the sound of the front door opening."
    "Asumi and Tomoe are back."

    $ bgm (7)

    voice as1081
    asumi "We're back! ...Hmm? Someone's back already?"

    voice to0817
    tomoe "Marutan, Yusuke?"
    yusuke "Oh no!"

    voice ma0283
    marumu "...What's wrong, Yusuke?"

    $ bgfx ('black')

    "I hurriedly roll down Marumu's T-shirt."
    "And I run out of the room."
    "As soon as I enter the living room, I see the two of them."

    $ bgfx ('bg01a')

    yusuke "H...hey, you guys are late today."

    $ char ('tas006')

    voice as1082
    asumi "You're just fast! I went grocery shopping with Moe-Moe."
    "They're holding shopping bags."
    "Completely out of character, Asumi went grocery shopping with Tomoe."
    "Tomoe puts her bags down and looks around."

    $ char ('tto001')

    voice to0818
    tomoe "Hmm, where's Marutan? Isn't she home yet?"
    yusuke "Oh, I think she's in her room."

    $ char ('tto016')

    voice to0819
    tomoe "Good. I'm going to make 'Omelet Rice' tonight; that's her favorite."
    yusuke "I see. She'll be thrilled. Ha ha ha!"
    "Just then, Marumu comes out of her room."

    $ char ('tma101')

    "With the same attitude as usual."
    "I don't know what she thinks. Marumu."

    call blackout from _call_blackout_22
    $ bgfx ('sora09')

    "At the Omelet Rice dinner."

    voice as1083
    asumi "Let's eat!"

    voice to0820
    tomoe "Yes."

    voice ma0284
    marumu "...An important announcement."
    "Everybody stops eating."
    "And we all look at Marumu."
    "In the silence, she says,"

    $ bgfx ('bg01c')
    $ char ('tma103')

    voice ma0285
    marumu "Yusuke and Marumu."

    $ char ('tas124')

    voice as1084
    asumi "What's that?"

    $ char ('tto201')

    voice to0821
    tomoe "What about Yusuke, Marutan?"
    yusuke "(Will she!?)"
    "I have a bad feeling about this..."

    $ char ('tma103')

    voice ma0286
    marumu "Yusuke is my boyfriend."

    $ empat ('j4')

    "Asumi and Tomoe drop their spoons."
    "...So do I."

    $ bgm (5)
    $ char ('tas130')

    voice as1085
    asumi "Wh...what did you say?"

    $ empat ()
    $ char ('tma103')

    voice ma0287
    marumu "Yusuke and I are going out."

    $ char ('tto222')

    voice to0822
    tomoe "Y...you must be kidding, Marutan?"

    $ char ('tma103')

    voice ma0288
    marumu "It's true."
    "Marumu doesn't deny it."
    "Of course not; she's the one who told them."
    "Asumi and Tomoe look at me next."
    "I'm kind of scared at their sharp eyes."

    $ chars ('tas106', 'tto202')

    voice as1086
    asumi "Is it true what Marutan said, Yusuke?"

    voice to0823
    tomoe "Answer us, Yusuke."
    yusuke "It's...ah..."

    $ char ('tma107')

    voice ma0289
    marumu "We're lovers."
    "Confused, Asumi and Tomoe stare at me."
    "I'm so scared that I can't even meet their stares."
    "I didn't think Marumu would tell them this way."
    "Usually, a girl confers before announcing something like that."
    "Can I continue a relationship with Marumu?"
    "How should I explain?"
    "I'm nervous about my future..."

    jump episode13_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

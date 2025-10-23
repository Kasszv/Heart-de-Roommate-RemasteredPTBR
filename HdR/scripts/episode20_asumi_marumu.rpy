label episode20_asumi_marumu:

    voice as0694
    everyone "An arranged marriage meeting?"

    $ bgfx ('bg01c')
    $ char ('tto204')

    voice to0281
    tomoe "Y...yes. I have to...meet the guy...next week."
    "All of us are surprised and at a loss at the shocking news... Well, not everybody."

    $ bgm (7)
    $ char ('tas105')

    voice as0695
    asumi "Really? I want to have an arranged marriage meeting too! You can eat good food and put on a nice dress, right?"

    $ char ('tma108')

    voice ma0141
    marumu "It sounds interesting."
    "They envy Tomoe so bad."
    "Girls... I kind of expected their reactions."
    "However, Tomoe yells at them with a sad, angry voice,"

    $ music_stop ()
    $ char ('tto204')

    voice to0282
    tomoe "It's not fun. I...I..."

    $ char ('tto207')
    $ char ()

    "She runs back to her room crying."
    "Dead silence reigns the room."
    "We realize she doesn't want to have the arranged marriage meeting."

    $ bgfx ('black')
    $ bgfx ('sora01')
    $ bgm (12)

    yusuke "Hey, Asumi. I don't think it's a good idea to interfere in someone's affairs."

    voice as0696
    asumi "How could you say that? Moe-Moe and we are..."

    voice ma0142
    marumu "Room maids."

    voice as0697
    asumi "NO! Not 'maids,' we're roommates and close friends!"
    "The next day."
    "Asumi, Marutan, and I go to the Hotel Katsuragi."
    "I'm worried about Tomoe, but visiting her house and asking why is going too far."
    "But no one can stop Asumi..."

    jump episode20_b

label episode20_asumi_marumu_b:

    $ bgfx ('bg03a')

    "We feel her anger in her tone of voice."

    $ bgm (5)
    $ chars ('tas210', 'tma201')

    voice as0700
    asumi "How could he say that!? I'll never ever forgive him!!"

    voice ma0143
    marumu "Liquidation..."
    "I'm surrounded by severe rage."

    $ char ('tas206')

    voice as0701
    asumi "He's a typical devil!"
    yusuke "I agree with you. He's a bad person, but..."

    $ char ('tas224')

    voice as0702
    asumi "But what?"
    yusuke "Tomoe is determined to accept the offer. She wants to protect the hotel her father and sister manage."

    $ char ('tas206')

    voice as0703
    asumi "No way! You're so naive!"
    "Holding her fist up to the sky, she declares,"

    voice as0704
    asumi "To sacrifice herself for her family...that's not right!"

    $ char ('tma201')

    voice ma0144
    marumu "Liquidation..."
    "Asumi and Marumu hold hands."
    "They grab my hands and form a circle."

    $ bgfx ('sora01')

    voice as0705
    asumi "We'll ruin Moe-Moe's arranged marriage meeting!"

    voice ma0145
    marumu "Yeah."
    yusuke "Is this really the right thing to do...?"

    jump episode20_c

label episode20_asumi_marumu_c:

    "All our plans have failed so far."
    "I don't think those were really plans."
    "The 'Obstruct the meeting - Code V' plan is in its last phase."
    "I really didn't want to go this far."

    $ bgfx ('bg16a')
    $ char ('tas206')
    $ bgm (16)

    voice as0713
    asumi "This is our last chance. Go, Yusuke!"
    yusuke "O...okay."
    "110 yards to the Hotel Katsuragi."
    "I block his way to the hotel."

    $ char ('tta001')

    takuto "Oh, I remember you... May I help you?"
    yusuke "I want you to cancel the arranged marriage meeting."
    takuto "Did you fall in love with me? Oh my!"

    $ char ('tta002')

    "I take my wig off and throw it on the ground."
    "Then I fiercely glare at him."
    "I yell at the guy who's totally at a loss."
    yusuke "I won't let you go inside! Never!"

    voice as0714
    asumi "Go, Yusuke go! Show him you've got some cojones!"

    voice ma0152
    marumu "Go! Go!"
    takuto "Who the hell are you...?"
    "I jump on him with their cheering."
    "Two men are fighting...one is wearing a dress, though (sob)."

    $ bg ('black', diss_fast)
    call effect ('SE39', ETYPE3) from _call_effect

    "The fight is over all too soon."

    $ bgfx ('bg16a')
    $ char ('tta002')
    $ bgm (6)

    yusuke "Asumi, you're a liar...you said a supporting character like him would be weak."

    voice as0715
    asumi "Oh well...there are exceptions, you know."

    voice ma0153
    marumu "Yusuke, you got the shit kicked out of you..."
    "I did my best."
    "He was much stronger than me."
    "I guess he's into some kind of combative sport."
    "As I sit down on the ground with scratches and bruises, I see a shadow."
    "It's Asumi. She was booing and complaining during the fight."

    $ bgm (5)
    $ char ('tas215')

    voice as0716
    asumi "I saw your skill. If I were you, I wouldn't be so proud of beating Yusuke."

    $ char ('tta001')

    takuto "Beating a wuss like him doesn't make me feel like that."
    yusuke "Uh...hic..."

    $ char ('tma201')

    voice ma0154
    marumu "Oh, you're crying. This is an opportunity for you to be stronger."
    yusuke "Oh, Marutan..."

    voice ma0155
    marumu "I know, I know."
    "Asumi and Takuto ignore us and stare at each other."

    $ chars ('tas236', 'tta001')

    takuto "I hesitate to fight you..."

    voice as0717
    asumi "Why? Are you afraid of me?"
    takuto "I don't like fighting girls. I wouldn't go out with a barbarous girl like you either."

    $ char1 ('tas210')

    voice as0718
    asumi "D...did you just call me barbarous!?"
    "She screams like a wild monkey."
    "I guess he's right. She's barbarous."
    takuto "If there's a man who'd date you, I'd like to meet the guy."

    if F015 == 0:

        yusuke "Ohhh....sob, sob."

        voice ma0156
        marumu "Yusuke. Why are you crying?"

    $ char1 ('tas236')

    voice as0719
    asumi "You're a dead man!"

    $ bgm (7)

    "Screaming, Asumi strikes out at him."
    "However, her fist stops in front of him."
    "We hear someone's scream."

    $ music_stop ()
    $ char ('tto213')

    voice to0284
    tomoe "What are you doing here? Oh, Takuto."
    takuto "Hey, Tomoe. Nice timing. They're getting in the way of me coming to your place."

    $ char ('tto251')

    "Her eyes get sharper."
    "She looks at us, not at Takuto."

    $ bgm (9)
    $ char ('tto213')

    voice to0285
    tomoe "How dare you...do this to me!"

    voice as0720
    asumi "Moe-Moe..."
    "We can't find the words to say to her."
    "Tomoe agreed to have the meeting to save the hotel."
    "But she's sacrificing herself."
    "We know her true feelings; that's why we came to ruin it."
    "Though we're wrong, we just can't let it happen."
    "However, she refuses us."
    "She clearly refuses what we're trying to do."

    $ char ('tto207')

    voice to0286
    tomoe "I...I..."

    $ char ('tta001')

    takuto "See? This is her decision. You guys misunderstood and bothered me."

    $ char ('tas210')

    voice as0721
    asumi "Wha...what did you say!? Gah...mmm!"
    "I cover Asumi's mouth and hold her firmly."
    "To continue the argument will just make Tomoe sad."
    "However, he continues to talk without knowing our feelings."

    $ char ('tta001')

    takuto "Tomoe and I used to be a couple. She didn't forget about me, even after we broke up."
    tomoe "......"
    takuto "She needs me. That's why she's agreed to have this meeting. You guys are misunderstanding her feelings and..."

    $ char ('tto204')

    tomoe "......"
    "Tomoe looks down quietly."
    "Asumi talks to her,"

    $ char ('tas206')

    voice as0722
    asumi "Moe-Moe! Tell us your true feelings! Do you really want to do this? You're going to sacrifice yourself to save the hotel, right?"

    $ char ('tta001')

    takuto "I said that's not true! She can't forget about me. Am I right, Tomoe?"

    $ char ('tto204')

    tomoe "......"
    takuto "Tomoe...?"

    $ music_stop ()

    "She remains clammed up."
    "Tomoe's sister speaks up in her place."

    $ char ('ttm004')

    voice ta0015
    tomomi "They're right. Tomoe doesn't want to have this arranged meeting!"
    takuto "But...but..."

    voice ta0016
    tomomi "Tomoe, tell him the truth."

    $ char ('tto204')

    "Tomoe's small lips are shaking."
    "As if she's trying to say something little by little."

    voice to0287
    tomoe "Sis...I...I..."

    $ char ('tas206')

    voice as0723
    asumi "Moe-Moe!"

    $ char ('tma201')

    voice ma0157
    marumu "Moe-Moe, be honest."
    yusuke "Tomoe..."
    "Finally, she tells us."
    "She finally releases her true feelings from her heart,"

    $ char ('tto213')

    voice to0288
    tomoe "I...don't want to do this!"

    $ char ('tta002')

    takuto "How come? You can't forget about me, right?"

    $ char ('tto213')

    voice to0289
    tomoe "I can't forget about you...though I want to! You hurt me so much!"

    $ char ('tta002')

    takuto "Tomoe..."
    "He turns pale."
    "She yells painfully. We don't know what happened between them in the past."
    "But she decides to put her bitter past away."
    "Calling forth all her courage, she tells us,"
    "Tomoe's sister coldly tells him,"

    $ char ('ttm004')
    $ bgm (13)

    voice ta0017
    tomomi "Leave...please leave now!"

    $ char ('tta002')

    takuto "Fine! But forget about the funds we talked about the other day!"

    $ char ('ttm004')

    voice ta0018
    tomomi "That's fine..."

    $ char ('tta002')

    takuto "Humph!!"

    $ char ()

    "Staring at her, us, and Tomoe, he leaves."
    "His back looks miserable."

    $ char ('tto207')

    "Tomoe's tension slowly leaves."
    "Tears spill down her cheeks."

    voice to0290
    tomoe "I'm sorry, Sis..."

    $ char ('ttm001')

    voice ta0019
    tomomi "Don't be. I couldn't stand you being his. We can find another way to save our hotel."

    $ char ('tto225')

    voice to0291
    tomoe "Sis, thank you."
    "She doesn't look sad anymore."
    "Then she looks back at us smiling."

    voice to0292
    tomoe "I'm sorry, everybody. And thank you, thank you so much."

    $ char ('tas215')

    voice as0724
    asumi "You're welcome. We did what we had to do."

    $ char ('tma201')

    voice ma0158
    marumu "Yup."
    yusuke "Yeah, Moe-Moe. We're roommates."

    $ music_stop ()
    $ bgfx ('sora05')

    "She doesn't cry anymore."
    "She smiles all over."
    "We're so glad to see her happy smile."

    $ bgfx ('black')

    "We return to our normal, everyday lives."

    $ bgm (16)
    $ bgfx ('bg13a')
    $ char ('tik999')

    voice yu0034
    akane "An idiot is an idiot forever! Your idiot virus is contagious to others."

    voice hs0020
    kaoru "An idiot makes a 'weird idiot' and a 'timid idiot.'"

    voice fu0019
    midori "Poor Ms. Glasses. I wish I could be your close friend."

    $ char ('tas006')

    voice as0725
    asumi "I'll kill you!"

    $ char ('tma014')

    voice ma0159
    marumu "Liquidation."

    $ char ('tto013')

    voice to0293
    tomoe "Even I get pissed off on occasion!"

    $ bgm (7)
    $ bgfx ('sora01')
    $ sfx ('SE10', loop=True)

    "I, Ms. Glasses, look at Tomoe vacantly from the side to avoid the cat fight."
    "She looks refreshed."
    "After struggling to protect something important to her, she's changed a lot."
    "The change hasn't clearly appeared yet, but others will notice the difference soon."
    "One problem is left..."

    $ bgm (6)
    $ bgfx ('bg03a')
    $ char ('tas036')
    call effect ('SE43', ETYPE1) from _call_effect_1

    yusuke "Ouch! Why did you hit me, Asumi?"

    $ char ('tas007')

    voice as0726
    asumi "Because you ran away from the fight, though you're a man."
    yusuke "Because I'm a man, I ran away! Would you have had my wig fall off?"

    $ char ('tas001')

    voice as0727
    asumi "Yeah, I get the point. How about gluing it on your head?"

    $ char ('tma002')

    voice ma0160
    marumu "Crazy glue..."
    yusuke "No, no way!"

    $ char ('tto010')

    voice to0294
    tomoe "Heh heh..."
    "I ask Tomoe as she smiles,"
    "About the problem I'm concerned about."

    $ music_stop ()

    yusuke "Ah, I know it's none of my business, but what happened to the hotel?"

    $ char ('tto004')

    voice to0295
    tomoe "Oh, that's..."

    $ char ('tas005')

    voice as0728
    asumi "Don't worry, Moe-Moe! We'll carry out plan, 'Reconstruct the hotel - Code P!'"

    $ char ('tma008')

    voice ma0161
    marumu "Perfect Plan."
    yusuke "You haven't even thought of anything yet..."

    $ char ('tas036')

    voice as0729
    asumi "What? Did you say something?"
    yusuke "N...no."

    $ char ('tto002')

    voice to0296
    tomoe "Uh...I haven't finished yet."

    voice as0730
    everyone "Sorry..."
    "Tomoe continues to talk,"

    $ char ('tto001')

    voice to0297
    tomoe "I don't know why...but we were able to borrow the money."
    yusuke "That's great! Is your hotel okay now?"

    $ char ('tto019')

    voice to0298
    tomoe "Yes, thank you... Yikes!"

    $ char ('tto037')
    $ sfx ('SE16')
    $ bgm (7)

    "She was smiling."
    "But she suddenly screams...I know why."
    "Someone grabs her breasts from behind."
    "I know there's only one person who would do such an envious...no shameless deed."

    $ char ('tna020')

    voice na0200
    namiki "Morning, Moe-Moe! Your breasts are as soft as always. What were you talking about?"
    yusuke "Oh well..."
    "Namiki doesn't like to be left out."
    "I ask Asumi and Marumu to comfort Tomoe, and then I tell Namiki what happened to Tomoe."

    call blackout from _call_blackout_6
    $ bgfx ('bg03a')
    $ char ('tna020')
    $ bgm (6)

    voice na0201
    namiki "Hmm... Your pretty breasts and the hotel are safe. Good for you."

    $ char ('tto011')

    voice to0299
    tomoe "Y...yes. Thank you, Namiki."

    $ char ('tna020')
    $ empat ('j6')

    voice na0202
    namiki "Oh, it's been a while! Say my name more."
    "Tomoe smiles without emotion."
    "Tomoe and I still don't know how to deal with her."
    "She suddenly whispers to me,"

    $ empat ()
    $ char ('tna013')

    voice na0203
    namiki "Listen, Yusuke. I picked up a man because I was bored."
    yusuke "You picked up a man?"
    "I go blank at her unexpected words."
    "She doesn't hate men."
    "She prefers girls (with big tits) to men."
    "She proudly talks about it."

    $ char ('tna001')

    voice na0204
    namiki "Because he was really good looking! He said he was turned down before an arranged marriage meeting."
    yusuke "What?"

    voice na0205
    namiki "He also said, 'I won't loan money to them!' So I scolded him."
    yusuke "What?"

    $ char ('tna004')

    voice na0206
    namiki "I said, 'If you're a man, don't do such a dirty thing!!'"
    yusuke "Is he...?"
    "The person Namiki picked up,"
    "I know who he is."

    $ char ('tna018')

    voice na0207
    namiki "He's a handsome guy. I even told him my phone number. Oh, I'm waiting for his call...heh heh."
    yusuke "......"

    $ music_stop ()
    $ bgfx ('sora01')

    "I'm sure about this."
    "He won't call, even if she sits by the phone waiting."
    "And the person who probably succeeded the most is Namiki."
    "If I tell Tomoe about this, she'll probably let Namiki grab her breasts... Nah, that won't happen."
    "She's a marvelous woman by all means."

    if F015 == 2:
        jump episode20_marumu_d
    else:

        jump episode20_asumi_d
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

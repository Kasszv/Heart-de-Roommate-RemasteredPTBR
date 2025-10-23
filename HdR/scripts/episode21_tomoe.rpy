label episode21_tomoe:

    $ bgfx ('bg03a')
    $ char ('tto001')
    $ bgm (3)

    "Her name is Tomoe Katsuragi."
    "She's my best friend."
    "I felt something different for her than the others, when I first met her."
    "She tries to understand me."
    "However, there's a language problem between us."
    "She thinks she understands me completely."

    $ bgfx ('black')
    $ bgfx ('bg01a')
    $ char ('tto025')
    $ bgm (12)

    voice to0958
    tomoe "I've got to go, Toshibo."

    voice ts0087
    nina "Be careful about cars. You're in a daze, sometimes. I can't take care of you if you get in an accident."

    $ char ('tto016')

    voice to0959
    tomoe "Okay.... Heh heh."
    yusuke "What did Toshibo say?"

    $ char ('tto025')

    voice to0960
    tomoe "He'll be wandering around, but he'll rush back if I get into any trouble."

    $ char ('tma008')

    voice ma0501
    marumu "Cool."

    $ bgfx ('black')
    $ bgfx ('bg16a')
    $ char ('tto225')
    $ bgm (13)

    voice ts0060
    nina "Hey, you're with a male today. Oh, is this guy that female-wannabe?"
    yusuke "Toshibo! It's been a long time."

    voice to0563
    tomoe "You're back. How are you?"

    voice ts0061
    nina "Let's not talk about me! Tomoe, you should choose a man more carefully!"

    $ char ('tto216')

    voice to0564
    tomoe "That's good for you."
    yusuke "(I have no idea what's being said.)"

    $ bgfx ('black')

    "Because this always happens, she misunderstands me."
    "But I'm used to it."
    "No, I give up."
    "She looks happy, knowing pleasure as a female."
    "I'm so glad for her."
    "Though she's a female, she's afraid of males..."

    jump episode21_b

label episode21_tomoe_b:

    $ cg ('ht_0601')
    $ bgm (14)

    "The male she has a relationship with is right in front of me, Yusuke Sawada."
    "He's a mysterious creature, who dresses like a female sometimes."
    "Both of them 'Love' each other."
    "I would like to know what 'Love' is."
    "If I continue watching them 'Make love,' perhaps I'll understand what it is."

    voice to0683
    tomoe "Oh, it's different this time...ahh..."
    yusuke "You're tight and warm inside..."

    voice to0684
    tomoe "Umm...aahhh...you're rubbing me so hard...ahh..."

    voice ts0048
    nina "My heart beats fast at the sight..."

    voice to0685
    tomoe "Ahh...mmm...yes, yes...aahhhh..."
    yusuke "You moan so loud, Tomoe. Someone might hear us."

    voice to0686
    tomoe "Huh... No...no...aahhh."

    voice ts0049
    nina "Tell me how you feel..."

    voice to0687
    tomoe "Hmm...ahh...I can't think of anything...aahhh."
    yusuke "Ohh, don't squeeze me so tight...ughhh..."

    voice to0688
    tomoe "You're great. Ahh...mmm...aaahhhhh!"

    voice ts0050
    nina "Excuse me...?"

    $ sfx ('SE07', loop=True)

    yusuke "Ohh...I can't hold it any longer..."

    voice to0689
    tomoe "Ahh...mmm....yes, yes... Ahh...ah...ahhh!"

    $ sfx (delay=0.3)
    call effect (None, ['white']) from _call_effect_40

    yusuke "Oh boy..."

    $ say_hide ()
    $ cg ('ht_0602')
    $ bgfx ('white')
    $ bgfx ('black')
    $ audio_stop ()

    "They fall into their own world during sex and don't even notice me."
    "Looking at them, I feel strange."
    "What should I say...? My front paws get hot."
    "Still, I don't get an answer."
    "They're so absorbed in sex, they don't know I'm here."
    "I should find the answer by myself... Oh?"

    $ bgfx ('bg02a')
    $ char ('tku001')
    $ empat ('j6')
    $ bgm (14)

    blackcat "......"
    nina "......"
    "What's this strange feeling?"
    "Is this male able to grant my wish?"
    "Will he be able to tell me what 'Love' is?"
    "I notice something."
    "This feeling...it's the legendary 'Falling in love at first sight.'"
    "I'm crazy for him."

    jump episode21_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

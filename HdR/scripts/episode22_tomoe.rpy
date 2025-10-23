label episode22_tomoe:

    "Tomoe flutters and walks around the room."
    "Abruptly, she leaves."
    "I immediately run after her."

    $ bgfx ('bg02c')
    $ char ('tto204')
    $ bgm (9)

    yusuke "Tomoe?"

    $ char ('tto213')

    voice to0984
    tomoe "Toshibo is going to be okay. Right, Yusuke?"

    voice to0985
    tomoe "But still, I'm afraid, you know. I'm just afraid of losing her..."

    $ char ('tto204')

    "She trembles with fear."
    "Then I hug her and pat her on the head."
    yusuke "Everything will be fine. Trust our friends and Toshibo, okay?"

    $ char ('tto231')

    voice to0986
    tomoe "Okay, I'll believe in everyone and Toshibo."
    "It's not only me, everybody is scared, so I should calm down!"
    "Determined, she wipes tears from her face."

    $ bgfx ('black')
    $ bgfx ('bg01c')

    jump episode22_b

label episode22_tomoe_b:

    $ char ('tto022')
    $ bgm (3)

    voice to0987
    tomoe "You're right. I love the mini Toshibos."
    yusuke "Well, don't you think we have too many cats in our dormitory?"

    jump episode22_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label episode21_asumi:

    $ bgfx ('bg01a')
    $ char ('tas001')
    $ bgm (5)

    "Her name is Asumi Hirota."
    "She's my best friend, Tomoe Katsuragi's friend."
    "I think she should choose her friends more carefully."

    $ char ('tas010')

    "Honestly, I don't want to get involved with a barbarous person like her."
    "I recently came to find out that she's not that bad, though."
    "She's still a tomboy. No males would be attracted to that female, for sure."
    "However, whimsical people really do exist in this world."

    jump episode21_b

label episode21_asumi_b:

    $ cg ('ha_02')
    $ bgm (14)

    "The male involved with Asumi is Yusuke Sawada."
    "He's a mysterious creature who sometimes dresses like a female."
    "This weird male and tomboy share a special feeling called, 'Love.'"
    "I don't understand what 'Love' is."
    "They might tell me what it is because they're strange."
    "I think it's a waste of time, but I ask them with little expectation."

    $ bgfx ('black')
    $ music_stop ()
    $ cg ('ha_0701')

    yusuke "Huh... Ohh!"

    voice ts0041
    nina "Ah...sorry to bother you, but..."

    $ bgm (7)

    yusuke "Toshibo... You're home."

    voice ts0042
    nina "Yes, I've been watching you guys for a while. May I ask you a question?"
    yusuke "It means... Whaaa!!"
    "Why is he so surprised and yelling?"
    "Is he embarrassed because I watched them having intercourse?"
    yusuke "What should we do, Asumi...?"

    $ cg ('ha_0702')

    voice as0655
    asumi "I don't know..."
    yusuke "Oh, no. This isn't good. Marutan will be home soon. What should we do...?"

    voice as0656
    asumi "Hey, calm down! We've got to think this through... Oh!"
    "Someone comes back."
    "This scent is Marumu Ogumayama."
    "She's the normal person among my friends."
    "No dirty desires or malice exist in her."
    "She's curious about the lump in the sheets in front of her."
    "I should ask her my question, not these people."

    voice ma0127
    marumu "What is this?"

    $ cg ('ha_0704')

    voice ts0043
    nina "Ah...could you answer my question?"

    voice ma0128
    marumu "Toshibo..."

    voice ma0129
    marumu "Is this your house?"

    voice ts0044
    nina "My house? I don't think so! I have a question..."

    voice ma0130
    marumu "Or is this your egg?"

    voice ts0045
    nina "Cats don't lay eggs. Jeez..."

    voice ma0131
    marumu "Let's go out, Toshibo."

    voice ts0046
    nina "Okay, okay...but you should answer my question later!"

    call blackout from _call_blackout_51

    "But I don't get the answer from her."
    "I can't predict what she'll do next."
    "I need to find the answer by myself... Oh?"

    $ bgfx ('bg02a')
    $ char ('tku001')
    $ empat ('j6')
    $ bgm (14)

    blackcat "......"
    nina "......"
    "What is this strange feeling?"
    "Is this male able to grant my wish?"
    "Is he able to tell me what 'Love' is?"
    "I notice something."
    "This feeling...it's the legendary 'Falling in love at first sight.'"
    "I'm crazy for him."

    jump episode21_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

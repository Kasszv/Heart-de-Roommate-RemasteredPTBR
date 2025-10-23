label episode23_marumu:

    yusuke "If I can, I would like to stay here. Yet..."

    $ bgfx ('bg01a')
    $ char ('tma001')

    "Suddenly, Marumu's face pops up."
    "It'd be sad to leave her."
    "Of course, I don't want to be far from the others either."
    "Yet I should move to the Kogarashi Dorm."

    jump episode23_b

label episode23_marumu_b:

    $ bgfx ('black')
    $ sfx ('SE37', loop=True)

    "One day..."
    "In the middle of the night, I hear some noise."
    "I think this has been happening a lot recently."
    "While wondering if my roommates are night owls or not, I check outside."

    $ sfx (delay=0.5)
    $ bgfx ('bg01d')
    $ char ('tma121')
    $ bgm (8)

    "I find Marumu."
    "Crouching, she's doing something in the middle of the room. If someone were to see her right now, they'd think she's a giant stag beetle having a meal."
    yusuke "Marutan, what are you doing at this hour?"

    voice ma0388
    marumu "Secret."
    "I knew she'd say that!"
    "But I don't want to give up that easily."
    yusuke "Hey, I'm your boyfriend, so tell me, please!"

    voice ma0389
    marumu "No, I can't tell even you."
    yusuke "Marutan!?"

    $ char ('tma117')

    voice ma0390
    marumu "Kidding."
    yusuke "Not again..."

    voice ma0391
    marumu "Anyway...secret."

    $ char ('tma121')

    "I continue questioning her without giving up."

    $ char ()

    "All of sudden, she runs back to her room and locks her door."
    "I think she was making something, but I'm not sure. What was it, anyway?"
    "Because she didn't tell me what her secret is, it bothers me even more."
    "Shit! I might not be able to sleep tonight again."

    jump episode23_c

label episode23_marumu_c:

    $ bgfx ('bg04a')
    $ char ('tma004')
    $ bgm (9)

    "Hikaru's attitude was too harsh."
    "Although Marumu has a poker face, I'm sure Hikaru hurt her pretty bad."
    "Tomoe and I hurriedly run up to Marumu."
    yusuke "Marutan..."

    voice ma0392
    marumu "Broken."

    voice to0866
    tomoe "I can't believe she did this to you!"

    $ char ()

    "Marumu squats down as we try to cheer her up."
    "Then, she collects the broken pin pieces."
    yusuke "......"

    $ char ('tma004')

    voice ma0393
    marumu "I'll make it again."
    "She's so patient."
    "She doesn't show us her feelings, but I'm sure she's holding it in."
    "When I think about her, I really can't stand how she's been treated."

    $ music_stop ()

    yusuke "......!!"

    $ char ('tto013')

    voice to0867
    tomoe "Hey, Yusuke! Where are you going?"

    $ bgfx ('black')

    "Ignoring her, I run up to the rooftop."
    "I've made up my mind to scold Asumi."
    "No matter what others say, I can't forgive her!"
    "I really don't understand why Asumi covered Hikaru's butt like that."
    "Marumu's supposed to be Asumi's best friend and her roommate as well."

    $ bgfx ('bg07a')

    yusuke "Puff-puff."
    "I'm totally out of breath, but I still make it to the rooftop."

    $ char ('tas021')

    "As soon as I find her, I start in on Asumi."
    "I unconsciously raise my voice,"
    yusuke "Asumi, why were you on Hikaru's side? Don't you get it's Hikaru's fault, not Marumu!?"

    $ char ('tas042')

    voice as1120
    asumi "I'm sorry, but Hikaru has nobody but me."
    yusuke "That's her problem she doesn't make any other friends. Anyway, did you forget Marumu is your best friend? She's also your roommate as well, right?"

    $ char ('tas043')

    voice as1121
    asumi "Yeah, but..."
    yusuke "I can't believe it! I'm really disappointed in you."
    asumi "......"
    "Asumi doesn't respond at all."
    "It looks like she's bearing my scorching words quite well."
    "An awkward silence falls between us."
    "Then Tomoe shows up."
    "She calms her breathing and walks toward us."

    $ char ('tto013')

    voice to0868
    tomoe "Stop, Yusuke. I'm sure Asumi had a good reason for acting that way. Isn't that right, Asumi?"

    $ char ('tas021')

    asumi "......"

    $ char ('tto013')

    voice to0869
    tomoe "Please answer me, Asumi!"

    $ char ('tas021')

    voice as1122
    asumi "I can't. I can't say anything to you guys."
    "Tomoe's usually very mild, but this time, her face turns red."
    "It's not because she's ashamed at what she said."
    "Listening to her, I can tell she's getting mad."

    $ char ('tto051')

    voice to0870
    tomoe "Everything is strictly confidential...and you don't want to help your best friend, Marumu, either. Have you lost your mind? This is definitely not like you!"

    $ char ('tas006')

    voice as1123
    asumi "What do you know about me? You're always so quiet and don't speak your mind at all. That kind of person will never understand how I feel now!"
    "She is really going overboard."
    "Without thinking, Asumi slips out the cruel words."
    "Tears well up in Tomoe's eyes."

    $ char ('tto007')
    $ bgm (9)

    voice to0871
    tomoe "I can't believe you said that."

    $ char ('tas021')

    voice as1011
    asumi "S...sorry."

    $ char ('tto007')

    voice to0872
    tomoe "I thought we're best friends, aren't we!?"
    "It doesn't sound like Asumi's apology has softened the awkward atmosphere."
    "She doesn't know where to look, so she droops her head. Suddenly, Marumu arrives."

    voice to0873
    tomoe "Hic hic..."
    "Marumu walks up to the miserable Tomoe and holds her hands as glaring at Asumi."

    $ char ('tma014')

    voice ma0394
    marumu "Asumi, cold-hearted."
    yusuke "Marumu..."
    "I feel pain, anger, and sadness in her voice."
    "She usually doesn't show her feelings to anyone, but now, I can feel it in her words."

    voice ma0395
    marumu "Cruel."
    "Her face is so grim. I've never seen her like this."
    "I feel like I'm trapped in a nightmare."
    "I know she's a bit different from others."
    "But I still can't believe she's showing such negative emotions."
    "Then her anger explodes in harsh words."

    voice ma0396
    marumu "I don't like you now."

    $ char ('tas042')

    voice as1124
    asumi "Marutan..."

    $ char ('tma020')

    voice ma0397
    marumu "I hate you."

    $ char ('tas021')

    asumi "......"

    $ char ()
    $ music_stop ()

    "At Marumu's onslaught, Asumi falls into silence and leaves."
    "Did I just see tears in her eyes when she passed me, or am I just imagining things?"
    "Marumu's face is still grim, and she continues glaring at Asumi's back."
    "Suddenly, I feel extremely uncomfortable."
    "These three were such good friends, but now, their relationship has crumbled."
    "I don't know what's going to happen to them after this."

    jump episode23_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

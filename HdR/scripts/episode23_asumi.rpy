label episode23_asumi:

    $ bgfx ('bg01a')
    $ char ('tas002')

    yusuke "Asumi..."
    "It looks weird from the perspective of others, but still, I'm living with someone I truly love."
    "If I don't define this as joy, what's true happiness?"
    "However, it doesn't mean I can't see her forever if I move to the boys' dormitory."
    "She is also my classmate, so I guess I can see her anywhere."

    $ bgfx ('sora09')

    "Of course, it's sad to live separately."
    "I don't want to be away from Tomoe, Marumu, and Toshibo either."
    "But I think I should move to the Kogarashi Dorm."
    "That's the best for my friends and me."

    jump episode23_b

label episode23_asumi_c:

    $ bgm (8)
    $ bgfx ('bg01b')

    voice to0330
    tomoe "May I have a word with you?"

    voice as0765
    asumi "...Okay."
    "While Asumi's changing her clothes, Tomoe speaks to her."

    $ chars ('tas021', 'tto051')

    "However, she doesn't sound like herself. Her voice and face are rather cold."

    voice to0331
    tomoe "About the incident at school, why were you on Hikaru's side?"

    voice as0766
    asumi "Hikaru's side? I wasn't particularly..."

    voice to0332
    tomoe "Marumu is our roommate and our best friend, isn't she!? But then why didn't you stick up for her?"
    asumi "......"
    "This isn't like Asumi at all."
    "Although Tomoe barks at her, she says nothing."
    "Her attitude irritates Tomoe even more."

    $ char2 ('tto013')

    voice to0333
    tomoe "Why don't you say something? You must have something you want to tell me. Just speak up!"
    asumi "......"

    voice to0334
    tomoe "Why can't you say anything? You mean you don't have any excuses?"

    voice as0767
    asumi "...Hikaru also has reasons, you know."

    voice to0335
    tomoe "What reasons? Is there any reason that would make it okay for her to act that way towards Marumu?"

    voice as0768
    asumi "Well, it's..."
    "She can't remain silent anymore."
    "Especially in a situation like this,"
    "I know she can't stand it anymore."
    "As Tomoe keeps howling, Asumi finally speaks up."
    "However, her remark adds fuel to their quarrel."
    "Since she doesn't know how to vent her anger, she starts blustering."

    $ char1 ('tas006')

    voice as0769
    asumi "You never tell me what's going on! You just hide your feelings behind your fake smile and pretend like everything is under control!"

    voice to0336
    tomoe "That's true. But I believe everybody has something they don't want to share with others. You have to understand, sometimes it's important to hide what's on your mind."

    $ char2 ('tto004')

    "For an instant, Tomoe looks at me."
    "I see tears on her face."
    "But soon, she turns back to Asumi."
    "It doesn't look like she can hide her emotions any longer."

    $ bgm (9)

    voice to0337
    tomoe "I couldn't tell you my true feelings because you're my friend!"

    $ chars ('tas010', 'tto007')

    voice as0770
    asumi "You always cry, but it doesn't solve anything, you know that!? Anyway, you said you couldn't tell me because I'm your friend. What a joke, Tomoe! If you think I'm your true friend, you could tell me everything!"

    $ char2 ('tto051')

    voice to0338
    tomoe "Alright, then I'll tell you exactly what's on my mind!"
    "Tomoe glares at Asumi in a tearful voice."
    "Her eyes clearly express her disgust and negative feelings toward Asumi."

    voice to0339
    tomoe "I know you've been seeing Yusuke, and I know for sure you guys really love each other!"

    $ char1 ('tas042')

    yusuke "What!?"
    "I blurt out with a surprised voice."
    "Yet Asumi is so shocked that her voice fails her."
    "Tomoe just ignores it and continues."
    "This time, her words make me freeze."

    $ char2 ('tto007')

    voice to0340
    tomoe "To tell you the truth, I'm also in love with him."
    yusuke "What!?"
    "Asumi turns pale at the unexpected blow."
    "Tomoe also turns red."
    "Then she gives vent to her pent-up feelings."

    $ chars ('tas021', 'tto013')

    voice to0341
    tomoe "I love him, but you're also my best friend. How can I tell you the truth, even though I know how you feel about him?"

    voice to0342
    tomoe "If I concealed my true feelings without telling anybody, I thought nothing would change. Then I could be your best friend forever!"

    voice to0343
    tomoe "You may not understand me, but our friendship and spending time with you are the most important things in my whole life. So..."

    voice as0771
    asumi "Tomoe..."

    $ char2 ('tto051')

    voice to0344
    tomoe "But it looks like our friendship and time aren't really important to you. You haven't told me about Yusuke. Moreover, today you were on Hikaru's side instead of speaking up for your best friend Marumu!"

    voice to0345
    tomoe "You're so selfish and always twist everybody around your little finger. You should know how you..."

    $ say_hide ()
    $ audio_stop (0.5)
    call cg_slide ('ea_0501', cls=diss_fast, tm=0.5, kind='h', start=0.0, end=1.0) from _call_cg_slide_2
    $ unlock_gallery ('g5e3')
    call effect (sound_source='SE56', graphics=['white']) from _call_effect_2

    "Suddenly, Tomoe stops howling."

    $ cg ('ea_0502')

    "I see her face start to swell up."
    "In response to what was said, Asumi slaps Tomoe."

    $ cg ('ea_0503')

    voice as0772
    asumi "Then you should have told me that! Even though you just told me, you could have done so much sooner!"

    voice as0773
    asumi "You always pretend like you're a good girl. But to tell you the truth, you're..."

    $ say_hide ()
    $ audio_stop (0.5)
    call cg_slide ('et_0401', cls=diss_fast, tm=0.5, kind='h', start=1.0, end=0.0) from _call_cg_slide_3
    $ unlock_gallery ('g5e4')
    call effect (sound_source='SE56', graphics=['white']) from _call_effect_3

    "This time, Asumi's mouth slaps shut."
    "Because the nice, kind Tomoe just slapped Asumi."
    "Tomoe trembles with anger and sheds big teardrops."
    "Asumi opens her mouth vacantly. She's dumbfounded for an instant, but she comes back right away."

    $ say_hide (diss_fast)
    $ cg ('ea_0504', diss_fast)
    call effect (sound_source='SE56', graphics=['white']) from _call_effect_4

    "She bites her lip and slaps Tomoe back."

    $ say_hide (diss_fast)
    $ cg ('et_0402', diss_fast)
    call effect (sound_source='SE56', graphics=['white']) from _call_effect_5

    "Again, Tomoe slaps Asumi and keeps sobbing."

    $ say_hide (diss_fast)
    $ cg ('ea_0504', diss_fast)
    call effect (sound_source='SE56', graphics=['white']) from _call_effect_6

    "Without a word, they hit each other again and again."

    $ say_hide (diss_fast)
    $ cg ('et_0402')
    call effect (sound_source='SE56', graphics=['white']) from _call_effect_7
    $ cg ('ea_0504')
    call effect (sound_source='SE56', graphics=['white']) from _call_effect_8
    $ cg ('et_0402')
    call effect (sound_source='SE56', graphics=['white']) from _call_effect_9

    "I'm petrified and stare at them."

    $ say_hide (diss_fast)
    $ cg ('ea_0504')
    call effect (sound_source='SE56', graphics=['white']) from _call_effect_10

    "Marumu holds back for a while, then she and Toshibo try to stop them."
    "However, the storm bounces them back."
    "They ignore everything and act as if they're the only two in the room."
    yusuke "Hey, cut it out you two! That won't solve anything!"
    "I desperately squeeze between the tempest and attempt to separate them."
    "Yet the two pairs of eyes continue glaring at each other as they continue smacking away at each other."
    "The storm is raging. It doesn't look like anyone can stop it."

    voice ma0184
    marumu "...Idiots."
    yusuke "What?"

    voice ma0185
    marumu "...Dope! You two are super-duper idiots!"

    $ bgm (9)
    $ bgfx ('bg01b')
    $ char ('tma019')

    "Her soft, sad voice echoes in the room."

    $ char ()

    "Then she runs into her room."
    "Before I realize it, I've calmed down."

    $ chars ('tas021', 'tto007')

    "Asumi and Tomoe are standing there in utter amazement."
    "I guess the chaos has finally come to an end."
    "Dead silence drifts through the air."
    "Yet, it makes all of us realize we just blew something very important."

    jump episode23_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

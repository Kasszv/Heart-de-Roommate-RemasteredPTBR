label episode20_asumi_d:

    $ bgfx ('black')
    $ bgfx ('bg07b')

    "After all, everything turns out fine."
    "All's well that ends well, I guess."

    $ bgm (10)

    yusuke "I'm glad nothing happened to Tomoe."

    $ char ('tas001')

    voice as0731
    asumi "Yusuke..."
    yusuke "What?"

    $ char ('tas047')

    "She hesitantly asks me. It's rare."
    "This pretty, shy Asumi is a side that's only for me."

    voice as0732
    asumi "If I ever have to have an arranged marriage meeting, would you..."
    yusuke "Would I ruin the meeting? That's what you want to know?"

    voice as0733
    asumi "Yeah..."
    "I understand what she wants to ask from her attitude."
    "Looking at her red face, I immediately tell her,"
    yusuke "Of course I would. Well, maybe I wouldn't do anything...it wouldn't be necessary."

    $ char ('tas042')

    voice as0734
    asumi "How come?"
    yusuke "Though I wouldn't do anything, it wouldn't work, anyway."

    $ music_stop ()
    $ char ('tas036')

    voice as0735
    asumi "Hey, what do you mean?"
    yusuke "You know what I mean... Whaaaa!!"

    $ char ('tas010')

    voice as0736
    asumi "Wait, Yusuke! Come back!!"

    $ bgm (7)
    $ say_hide (diss_flash)
    call cgeffect ('SE39', KENKA1, sound_loop=True) from _call_cgeffect_10

    "While she chases around hitting me, I notice something."
    "I said that to hide my embarrassment."
    "If I continue looking at the cute side of Asumi, I'm not sure I could control myself."

    $ sfx (delay = 1.0)
    $ bgfx ('sora05')

    yusuke "But you should act like that more often."
    "I sit down on the floor as Asumi stands next to me."
    "Watching us, Tomoe happily calls out."
    "Her voice is cheerful and merry."

    $ music_stop ()
    $ bgfx ('bg07b')
    $ char ('tto019')

    voice to0300
    tomoe "Hey, let's go home! I'll cook dinner with the utmost care. He he."

    jump episode20_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

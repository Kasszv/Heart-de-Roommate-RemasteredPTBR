label episode13:

    $ Fnum = 13
    $ save_name = "Episode 13: Shaking Heart - Part 2"

    $ bgfx ('white')
    $ bgfx ('sora01')

    yusuke "Heave-ho!"
    "I put all my daily necessities in a bag."
    "I can live for a while with this stuff, I only need to find a place."
    "Nobody wakes up this early."
    "Be quiet!!!"
    "Someone grabs the scruff of my neck and drags me to the other room."

    $ bgfx ('black')
    $ bgfx ('bg09a')

    yusuke "What's this sudden... Ah!"

    $ char ('tna122')

    voice na0184
    namiki "Good morning, Yusuke! Where are you going so early?"
    yusuke "Namiki."
    "She takes my bag. I can do nothing but explain my situation."

    $ bgfx ('black')
    $ bgm (5)
    $ bgfx ('bg09a')
    $ char ('tna118')

    voice na0185
    namiki "Wow! You're good, Yusuke. You kissed three of them!"
    yusuke "Don't make fun of me. Anyway, they were all accidents!"

    $ char ('tna102')

    voice na0186
    namiki "Not with Marutan."
    yusuke "No. But that was a really light kiss."
    "Is Namiki listening to me?"

    $ char ('tna120')

    "She's smirking and looking somewhere else."

    voice na0187
    namiki "Hmm, this is just what being young is all about!"
    yusuke "You're enjoying listening to my problem, Namiki!"

    voice na0188
    namiki "No, I'm not. But it sounds exciting!"
    yusuke "......(mad!)"
    "Anyway, I can't stay here anymore."
    "I might not be able to find a place to live very quickly, but I have to leave, even if I have to sleep out in the open."

    $ bgfx ('black')

    "I grab my bag as to avoid looking at Namiki."
    "And quietly walk to the door."
    "I can leave quietly... At least I thought I could."

    $ music_stop ()

    voice na0189
    namiki "Yusuke."
    yusuke "Yes! (Damn, she knew about it!)"

    voice na0190
    namiki "You're a man, right?"

    menu:
        " "
        "Of course I'm a man!":


            yusuke "What are you talking about. I am a man, even though I wear girls' clothing."

            voice na0191
            namiki "Then straighten things out!"

            voice na0192
            namiki "You can leave anytime, but you're the one who made this mess. It's your responsibility to clean it up!"
            "I can't look back."
            "I can't even look her in the eye."
            "I'm scared and...embarrassed."
            "Namiki's right."
            "Her words make my bag feel heavier."

            $ F019 += 1
        "I can't answer with much confidence.":


            yusuke "......"
            namiki "......"
            "She's not talking about the distinction between sex."
            "I can't answer."
            "She looks disappointed."

            voice na0380
            namiki "Well, you can't do anything because you're not really a man."
            yusuke "I don't appreciate that."
            "But she may be right."
            "I leave the room without saying another word."
            "I have only one place to go."


    call ep_start from _call_ep_start

    $ bgm (4)
    $ bgfx ('bg10a')
    $ char ('tyo101')

    yusuke "I'm sorry for leaving my stuff here, Ms. Yagami."

    voice yo0130
    yagami "No, problem. You can live here if you like."
    yusuke "Are you serious?"

    $ char ('tyo107')

    voice yo0131
    yagami "Heh heh. I'm not."
    "Anyway, I can't take all my stuff to school."
    "But if I leave it somewhere in the street, someone may think it's garbage and throw it away."
    "Or I might get caught for unlawfully dumping garbage."
    "I don't think anyone would listen to me, even if I were say, 'I'm not that kind of person.'"
    "I decided to ask Ms. Yagami to let me put my stuff in her room."

    $ char ('tyo115')

    voice yo0132
    yagami "You had to leave the room. You must really be in trouble."
    yusuke "Yes, I am."
    "I explain what's happened these last few days (except about Namiki)."

    $ bgfx ('black')
    $ bgfx ('bg10a')
    $ char ('tyo101')

    voice yo0133
    yagami "I see. You had a hard time. But I don't think you need any advice now."
    yusuke "Eh, why not?"

    voice yo0134
    yagami "You should know what you must do."
    yusuke "Should I?"
    "I'm confused. However, Ms. Yagami just looks at me kindly."

    $ char ('tyo115')

    voice yo0135
    yagami "Be honest with yourself and express your true feelings to the person you ought to tell."
    yusuke "Be honest with myself?"

    voice yo0136
    yagami "Yes. Follow your true feelings without calculating anything. That's the way youth should behave."
    yusuke "Ms. Yagami."

    menu:
        " "
        "Nod without a word.":


            $ bgfx ('black')
            $ bgm (9)

            "I nod."
            "I don't know what to do."
            "But I think I have to follow my heart at least."
            yusuke "I have to do something!"

            $ bgfx ('bg07a')

            "Eventually, I come here to the rooftop."
            "Because in the classroom, I see all three of them."
            "I can't clear my head with them around."

            $ F01A += 1
        "I can't say anything.":


            $ bgfx ('black')
            $ bgm (9)

            "I remain silent."
            "I quietly walk to school."
            "I'm thinking about what I should do."

            $ bgfx ('bg07a')

            yusuke "......"
            "I sigh again. This is no good."
            "During lunch break, I deeply regret running away up here, to the roof."
            "The three girls are in the classroom. I was uncomfortable there."
            "They look at me every once in a while."
            "But when I look back, they look away."

    $ bgfx ('black')
    $ bgm (8)
    $ bgfx ('sora01')

    "Namiki told me to clean up the mess as a man."
    "Ms. Yagami told me to be honest with myself."
    "What do I want? How can I clean up the mess?"
    "What are my true feelings?"

    $ cg ('e3_05')

    "Do I love one of them?"
    "I want someone to tell me what to do."
    "But I have to find the answer for myself."

    menu:
        " "
        "Declare my love for Asumi.":

            jump episode13_asumi
        "Declare my love for Tomoe.":

            jump episode13_tomoe
        "Declare my love for Marumu.":

            jump episode13_marumu
        "I still don't know my true feelings.":

            jump episode13_else

label episode13_end:


    call ep_finish from _call_ep_finish

    $ renpy.end_replay()
    $ unlock_episode (13)

    jump episode14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

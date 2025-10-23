label episode20:

    $ Fnum = 20
    $ save_name = "Episode 20: The First Arranged Marriage Meeting"

    $ bgfx ('sora02')
    $ bgm (6)

    yusuke "Ohh... Damn it!!"
    "I get stuck with all the shitty jobs."
    "Tomoe went home for an emergency, so I go shopping instead of her."
    "However, today's shopping is..."
    "Going to a grocery store in the next town, following Asumi's instructions."
    "They usually come out here on bargain days."
    "I didn't think it would be a big deal, but I was so wrong."
    "I didn't attach much importance to the place being out in the country."
    "And now..."
    yusuke "Where...where the hell am I!?"
    "My voice echoes in the air."
    "I didn't arrive at the store or even the town."
    "Moreover, I'm lost in an unfamiliar place."
    yusuke "Ahhh...what a bummer..."
    "I'm aimlessly wandering around."
    "That's the only thing I can do."

    $ music_stop ()
    $ bgfx ('bg14a')

    yusuke "Wow...it's so big!"
    "I'm standing at the entrance of a big park."
    "Is this...the park where I had a date with Asumi?"
    "We just happened to come here."
    "I still don't know where I am."
    "Is this...the park where I had a picnic with Tomoe?"
    "Tomoe brought me here."
    "I still don't know where I am."
    "I've never been to this park."
    "I have no idea where I am."
    "When I walk around the park trying to find a map of surrounding areas,"
    "I find a girl."
    "She stands alone on an observation platform."
    "It's kind of familiar...oh, that's my school uniform!"
    "The same uniform I put on almost everyday."
    "I walk towards the girl for help."

    $ bgfx ('black')
    $ bgfx ('bg14a')
    $ char ('thi001')
    $ bgm (8)

    yusuke "..."
    yusuke "......"
    yusuke "E...excuse me...?"

    $ char ('thi002')

    hikaru "......"

    $ char ()

    "All of a sudden,"
    "She runs away."
    "Is that...Hikaru Saeki, the new transfer student?"
    "What was she doing here?"
    "Perhaps she was taking a walk, or maybe she was lost... I don't think so."
    "At the observation platform."
    yusuke "Was she going to kill herself...?"
    "I don't think she would do that."
    "At least she could have told me where I am... Oh boy."

    $ music_stop ()
    $ bgfx ('sora08')

    "When I finally return safely to the Harukaze dorm, it's already dark."
    "I made it somehow or the other."
    "Of course, I didn't buy anything."
    "Asumi is pissed and scolds me."


    call ep_start from _call_ep_start_28

    $ bgm (13)
    $ bgfx ('bg01c')

    yusuke "Moe-Moe is late..."
    "I tell Marumu and Asumi while I'm cooking dinner."
    "Even Asumi doesn't know why she's so late."

    $ char ('tas133')

    voice as0691
    asumi "I know she went home, but it's so late."

    $ char ('tma117')

    voice ma0137
    marumu "She got lost."
    yusuke "That was me...sorry."
    "She sure is late."
    "I'm worried something might have happened to her."
    "She's a timid girl."

    if F015 == 1:

        $ bgfx ('black')

        "Should I wait for her outside as her boyfriend?"
        "'I was scared...thank you, Yusuke. I'm so happy!'"
        "She'll appreciate me and give me a hug."
        "Or will she kiss me!?"
        "Marumu smashes my imagination."

    $ music_stop ()
    $ bg ('bg01c')
    $ char ('tma104')

    voice ma0138
    marumu "She's back."

    $ char ('tas130')

    voice as0692
    asumi "How do you know, Marutan?"

    $ char ('tma117')

    voice ma0139
    marumu "I have good ears."
    "I don't hear anything."
    "Even though I listen carefully... Oh?"
    "I can barely hear footsteps."
    "They stop in front of the room, and the door slowly opens."

    $ char ('tto204')

    voice to0279
    tomoe "I'm home..."

    voice as0693
    asumi "Welcome back, Moe-Moe! You're late."

    voice to0280
    tomoe "Y...yeah."
    "She looks tired."
    "It seems something is really bothering her..."

    $ bgfx ('black')
    $ bgfx ('sora09')

    if F015 == 1:
        jump episode20_tomoe
    else:

        jump episode20_asumi_marumu

label episode20_b:

    $ music_stop ()
    $ bgfx ('bg16a')

    "We arrive at the hotel, where we usually have our regular meetings."
    "However,"
    "We can't enter the hotel."
    "Because a man and a woman are in a heated arguement."
    "But it sounds like it'll end soon."

    $ chars ('ttm004', 'tta001')
    $ bgm (16)

    man "Alright, see you next week."
    tomomi "......"
    man "Don't look at me like that, 'Sister.'"

    $ char ('tta001')

    "Then the guy walks away."
    "I meet his gaze, and he smiles at me. I'm wearing girls' clothes."

    $ char ('tas201')

    voice as0698
    asumi "As always, you're Ms. Popular."
    yusuke "Shut up..."
    "The man who smiles at me,"
    "I think I've met him somewhere."
    "But I'm not sure."

    $ music_stop ()

    "We walk over to the woman who looks tired. She's Tomoe's sister."

    $ char ('ttm003')

    voice ta0009
    tomomi "Oh, you girls are..."

    $ char ('tas242')

    voice as0699
    asumi "Well...we want to find out about Moe-Moe's arranged marriage meeting."

    $ bgm (9)
    $ bgfx ('black')

    "She starts explaining the situation."
    "She tells us about the marriage meeting and why it's taking place."
    "The guy she was talking to is Takuto Kimura. He's the one having the marriage meeting with Tomoe."
    "He and Tomoe have known each other since they were kids."
    "Both of their parents are hotel owners, so they played a lot together as children."
    "Tomoe used to say she was going to marry Takuto when she grew up."
    "In junior high, they were dating, but they broke up."
    "Tomoe's sister doesn't offer any details."
    "It was a bitter experience for Tomoe."
    "From her expression, we get the picture."

    $ bgfx ('bg16a')
    $ char ('ttm003')

    voice ta0010
    tomomi "But Tomoe made this decision by herself."
    yusuke "How come?"

    voice ta0011
    tomomi "To save this hotel. She's sacrificing herself for the hotel."
    "I remember what Tomoe once told me."
    "Because of the recession, the hotel is in dire straights."
    "Her sister has been asking for help from the local hotel association."
    yusuke "Is this arranged marriage meeting related to the support?"

    voice ta0012
    tomomi "Yes. He became the chairman of the association after taking over his parents' hotel three months ago."
    "He knew about her family's financial problems and proposed this arranged meeting."
    "His proposal includes the merger of the two hotels."
    "Since most hotels have the same problems, it's difficult to ask the association for money."
    "If the two hotels were merged, her hotel would survive the crisis for a while."

    $ char ('ttm004')

    voice ta0013
    tomomi "I know, but I can't forgive what he said!"
    "She bites her lip."

    voice ta0014
    tomomi "He said, 'Tomoe still loves me...she'll never forget about me.'"

    call blackout from _call_blackout_188

    if F015 == 1:
        jump episode20_tomoe_b
    else:

        jump episode20_asumi_marumu_b

label episode20_c:


    call ep_middle from _call_ep_middle_29

    "Today is the arranged marriage meeting day."
    "The day has come."

    $ bgfx ('bg01a')
    $ char ('tto204')

    voice to0283
    tomoe "I've got to go now..."
    yusuke "Okay, take care..."

    $ char ()

    "Staying calm, we see Tomoe off."
    "Because we don't want her to get suspicious."
    "After making sure she's left, we talk about our plan."

    $ bgfx ('bg02a')
    $ char ('tas201')
    $ bgm (5)

    voice as0706
    asumi "We call it, 'Obstruct the meeting - Code V!'"
    yusuke "What's Code V?"

    $ char ('tma207')
    $ empat ('j4')

    voice ma0146
    marumu "Victory!"
    yusuke "Oh, I see...it's a bit simple..."
    "I honestly regret joining (they forced me) their plan."
    yusuke "If we ruin the meeting, what will the hotel do without funds?"

    $ empat ()
    $ char ('tas236')

    voice as0707
    asumi "What? Are you okay with that devil wrecking her life? Don't you mind if she's treated like shit?"
    yusuke "Of course I do! But thinking about her feelings, I'm not sure about this."

    $ char ('tas201')

    voice as0708
    asumi "We can do something to save the hotel! The plan is 'Reconstruct the hotel - Code P!'"
    yusuke "What's Code P...?"

    $ char ('tma207')
    $ empat ('j4')

    voice ma0147
    marumu "Perfect plan."
    yusuke "Oh boy. I shouldn't have asked..."
    "I reluctantly follow them."

    $ empat ()
    call blackout from _call_blackout_189
    $ bgm (6)
    $ bgfx ('bg03a')
    $ chars ('tas201', 'tta001')

    voice as0709
    asumi "Excuse me...could you do me a favor?"
    takuto "Umm. I want to say yes because you're a girl, but..."
    takuto "You aren't my type. Sorry."

    $ char ('tas210')

    voice as0710
    asumi "I...I won't forget this! Yieee!!"

    $ bgfx ('black')
    $ bgfx ('bg03a')
    $ chars ('tma201', 'tta001')

    voice ma0148
    marumu "Please help us raise funds."
    takuto "Lately, everybody is having a hard time... Do your best. I'll say a prayer for you."

    $ char ('tma204')

    voice ma0149
    marumu "Tightwad..."

    $ bgfx ('black')
    $ bgfx ('bg03a')
    $ chars ('tas206', 'tta001')

    voice as0711
    asumi "Hey, hey! You can't go through this street unless you win at rock-paper-scissors."
    takuto "I didn't know that. Then I'll use a different street."

    $ char ('tas236')

    voice as0712
    asumi "Mmm... Damn!!"

    $ bgfx ('black')
    $ bgfx ('bg03a')
    $ chars ('tma201', 'tta001')

    voice ma0150
    marumu "Play with me, please?"
    takuto "Next time, little girl."

    $ char ('tma207')

    voice ma0151
    marumu "Bye..."

    $ bgfx ('black')
    $ music_stop ()

    if F015 == 1:
        jump episode20_tomoe_c
    else:

        jump episode20_asumi_marumu_c

label episode20_end:


    call ep_finish from _call_ep_finish_22

    $ renpy.end_replay()
    $ unlock_episode (20)

    jump episode21
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

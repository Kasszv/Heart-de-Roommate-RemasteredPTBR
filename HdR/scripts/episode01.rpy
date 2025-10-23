label episode01:

    $ Fnum = 1
    $ save_name = "Episode 1: The Beginning"

    $ bgfx ('white', diss_long)
    $ bgm (9)
    $ bg ('sora04', tag=0)
    $ bg ('sora02', tag=1, pos=[HIDE(3.5, 0.5)])
    $ _fx (diss_long)
    $ wait (2.0)
    $ quick_menu = True

    yusuke "Time flows...slowly in here."
    "I was so busy just two hours ago."
    "Everything seems so quiet now."
    "The time, which stopped exactly a year ago, starts quietly moving again."
    "But for the girls and I, time was like a roaring river."
    "The time we spent together, is now a long-past memory."
    "Still, I sense those fond memories in this place."
    "This air."
    "And...the days of my youth."
    "While I wait here to meet her again,"

    $ music_stop ()

    "I vividly remember...those days we spent in this place."

    call blackout (True) from _call_blackout_38
    call breakskip from _call_breakskip_2
    $ quick_menu = False
    $ _skipping = False
    $ movie ('hr_op1')
    $ bgfx ('black')
    $ quick_menu = True
    $ _skipping = True

    "Bad luck. Those are the words I choose to describe that day."
    "All hell broke loose. I was chewed up and spat out."
    "And the worst thing of all,"

    $ bgm (6)
    $ bgfx ('sora08')

    yusuke "Ohhh...ohh..."
    "I can't stop crying."
    "This is sad...no, it's too sad."
    "I carry tons of stuff on my back, and they boost my sadness even more."
    "However, it doesn't matter compared with what I'm witnessing this very moment."
    "It's smoke! I see smoke rising to the sky."
    yusuke "Why...why is it burning down...!?"
    "My desperate scream blankly echoes in the night sky."
    "My school transfer...everything started from that."
    "Sure, I was frustrated with my daily life."
    "And occasionally, I spoke it out loud."
    "When my parents told me, 'We found a new school for you!' with big smiles, I couldn't honestly say, 'Wow! Gee, thank you, Mom and Dad!'"
    "I couldn't say it...ever."
    yusuke "Don't jerk me around... What the hell were you thinking!?"
    "That's what I told them instead."
    "The school is named Aiho School. It's located far from any other cities, and many of its students live in dorms."
    "I was supposed to move into this dorm,"
    "However,"
    "My airhead parents completely forgot to register me in the dorm!"
    "The cold reality...there's no room for me."
    "The generous dorm manager introduced me to some apartments near the dorm."
    "He told me to stay there until a vacancy opened up."
    yusuke "'I know the landlord. I'll call him for you.' He told me kindly, comforting me."
    "However,"
    "The truck carrying my stuff broke down."
    "I was forced to pack up everything with a big, stupid looking sheet and walk for two miles."
    "I finally reached the apartment after the painful journey, but..."
    "the apartment was burning up like an inferno."
    "Again, I was forced to help fire fighters. I'm exhausted."
    "And you know what? People are cold."
    "When the fire died out, people went home with smiles."
    "...Because they don't need to worry about leaping sparks hitting their own homes anymore."
    "The landlord received a slight burn and was hospitalized."
    "He looked at me sadly, sitting next to my pile of luggage as he was taken into the ambulance."

    $ bgfx ('bg03c')

    "And now, I'm here."
    "I'm lost in a place I've never even visited before. Alone, I stand on the dark street."
    "I can't walk around with my stuff anymore. I don't have the strength to begin with."
    "BAM!!"
    "I kick my stuff in anger."
    "Then something slips out of the wrap..."

    "It is a lovely Onsen Tamago (boiled egg) maker called, 'Yudetama-chan.'"
    yusuke "Why am I carrying this shit anyway? It's useless."
    yusuke "It's all my airhead parents' fault!!"
    yusuke "Give it to me... Give my peaceful life back to meeeeee!!"

    voice as0001
    unknown "YOU... You give it back to ME!!" (voice_tag='v_asumi')
    yusuke "...Huh?"

    $ music_stop ()

    "While the voice sounds distant, it clearly reaches my ears."
    "But I don't see anyone around."

    $ sfx ('SE13', True)

    "Who's that? ...Ohh!?"

    $ say_hide ()
    $ ev ('ka_0201')
    $ ev ('ka_0202')
    $ ev ('ka_0203')

    $ sfx ()
    $ vox ('as0002')
    call triple_slide_from_right ('ea_03') from _call_triple_slide_from_right_1
    $ sfx ('SE36')

    $ unlock_gallery ('g1e1')

    "The direct impact knocks me out instantly."
    "In this land of the unknown,"
    "This incident becomes my worst nightmare... THUD."

    $ vox (delay=0.3)


    call ep_start from _call_ep_start_7

    $ bgm (5)
    $ bgfx ('bg03c')
    $ char ('tas007')

    voice as0003
    girl_as "Hey, wake up, you panty thief!"
    yusuke "......"

    voice as0004
    girl_as "Humph. This guy's completely out of it... Should I drag him to the police station?"
    "(Wh...what's going on...!?)"

    voice as0005
    girl_as "I can leave his stuff here, I guess... Oh?"

    $ vox ('et0001')
    $ char ('tas024')

    "Vaguely, I hear a distant scream."
    "It's a girl's scream."
    "I'm not fully awake yet, but I'm able to hear someone screaming, 'There's the panty thief!'"

    $ vox (delay=0.3)
    $ char ('tas006')

    voice as0006
    girl_as "What!? I'll be right there!"

    $ bg ('bg03c')
    $ ev ('ea_1101', tag=1)
    $ ev (tag=1)

    "The girl who kicked me quickly runs away."

    $ vox ('as0007')
    $ sfx ('SE36', delay=1.6)

    "Something must have happened over where the girl is heading."
    "For a moment, I hear screams both cheerful and painful, then the silence returns."
    "Then...the girl comes back to me."

    $ vox (delay=0.3)
    $ sfx ()
    $ char ('tas027')

    voice as0008
    girl_as "I, err... I'm sorry. I thought you were the panty thief."
    yusuke "Ahh...it's okay...as long as you understand."

    voice as0009
    girl_as "I mean you're not a panty thief, just a regular thief. Either way, it's to my credit to catch you!"
    yusuke "...She doesn't understand at all."

    $ bgfx ('sora08', cls=False)

    "Okay, she's gone too far! How come I'm mistaken for a thief in this pesky little town!?"
    "Will I be thrown in jail for nothing!? No! I'm scared of tight, cold, dark places!!"
    "I desperately start explaining my situation to her..."

    call blackout from _call_blackout_39
    $ bgfx ('bg03c')
    $ char ('tas024')

    yusuke "...and that's why I'm biting the dust! It's all because of my stupid mom and dad!!"

    $ char ('tas007')

    voice as0010
    girl_as "You call your parents stupid? No. Actually, you're the stupid one! You have to thank your parents for giving you your life!!"
    yusuke "Grrr...!"
    "I talk back at her as I remember all the punishment I received today."
    yusuke "You call me stupid? Yes, that's right!! I am the stupidest!! I should've never come to this town! I don't even care if the school in this town is good or bad anymore!"
    yusuke "This is it... I'm doomed. Everything's over... My youth is ruined!"
    yusuke "I feel like a cartoonist who has failed to gain popularity, even though he had ten weeks to show what he's got... This is it!!"
    "I lean on my luggage which is almost as big as a truck."
    "I feel like giving up on everything."
    "However, the girl suddenly grabs my collar and impatiently yells at me saying,"

    $ char ('tas010')

    voice as0011
    girl_as "You'll just give up, is that it? What are you talking about? Don't you have any balls!?"
    yusuke "I...the..."

    voice as0012
    girl_as "Don't throw everything away so easily!!"

    $ bgfx ('sora08')

    "And she throws me."
    "So easily."
    "It's almost a pleasurable sensation to float in the air."
    "Then, all my worries suddenly vanish."
    "I feel unbearable pain as I hit the ground instead."

    call effect ('SE45', ETYPE2) from _call_effect_19

    "I pass out again."


    call ep_middle from _call_ep_middle_7

    $ bgm (5)
    $ bg ('bg03c', dissolve)
    $ char ('tas012')

    voice as0013
    girl_as "Oh, I didn't mean to hurt you that much. Sorry, but I hate watching a sissy like you, ha ha ha!"
    yusuke "Is she apologizing or what...?"
    "I sink back on my luggage."
    "Now, I've officially become a hobo with all my gadgets."
    "I pick up the gadgets one by one and sigh."
    yusuke "All these things... I see no use for them, unless I have a place to live..."

    $ char ('tas030')

    voice as0014
    girl_as "...Hey, you!"
    yusuke "EEK! Wh...what now...!?"

    voice as0015
    girl_as "Isn't this the Yudetama-chan!? I saw this on some fishy infomercial the other night!"
    yusuke "How the hell would I know? Ask my dumb parents."

    $ char ('tas001')

    voice as0016
    girl_as "Oh, I want this, I want this... I've got to use this!"
    "She looks at the junk with sparkling eyes."
    "I don't care if she takes it or not."

    menu:
        " "
        "Run away from her at once!":


            yusuke "...Yes, that's right!"
            "This might be my only chance... I'll escape now!"
            "There's nothing valuable in the luggage, so I can leave it here."
            "TIPTOE..."

            $ char ('tas012')

            voice as0017
            girl_as "I'll take this back with me and show it to Moe-Moe...after I turn this suspicious-looking guy into the police station!"
            yusuke "What the? But I already told you why I'm here with this stuff..."
        "See what happens next.":


            yusuke "......"
            "But what if she catches me again? I feel a chill down my back."
            "In order to secure my own safety, I decide to stay and see what happens next... I guess."
            "And...that was a mistake."
            "The violent girl turns her happy face to me again and says,"

            $ char ('tas012')

            voice as0017
            girl_as "I'll take this back to the dorm and show it to Moe-Moe...after I turn this suspicious-looking guy into the police station!"
            yusuke "H...how dare you call me suspicious!"

            $ F016 += 1

    $ char ('tas015')

    voice as0018
    girl_as "Come on, you must have stolen all these treasures from somewhere! You don't look at all like you're just moving!!"
    yusuke "I told you...my stupid parents had me carry th...waaaaah!!"
    "The girl strangles me without warning, and she IS very strong!"

    voice as0019
    girl_as "You can't fool this lovely Asumi-chan! Nobody can!!"
    yusuke "Ugh...uh... Asumi...?"
    "It's not an unusual name... I've heard the name before."
    "Yes, I'm sure I've heard the name!"
    "Only I can't remember who she is...because this girl, Asumi, is choking me right now."

    $ music_stop ()
    $ bgfx ('sora08', diss_long)

    "This is the worst event of all."
    "It must be fate that we meet here again."
    "By the way, the fate between me and the girl, Asumi Hirota, isn't necessarily good."
    "But of course, I'm now able to find shelter for tonight because of this fate."
    "I'll find out later... if my choice of action was right or wrong."

    $ bgm (12)
    $ bgfx ('bg03c')
    $ char ('tas024')

    yusuke "Ugh...ahh... I...I remember you now...you evil girl!"

    $ char ('tas007')

    voice as0020
    asumi "What did you say...? I don't know any small fries like you!"
    "Grr, she really gets on my nerves."
    "I'm really pissed off."
    "But this is the way the real world works."
    "Those who bully forget what they've done."
    "Those who were bullied don't forget what's been done to them."
    "They just live with the emotional scars!"
    yusuke "Ohhh... I'm such a worthless piece of...hic-hic..."

    $ char ('tas011')

    voice as0021
    asumi "Guys shouldn't cry!"
    yusuke "D...don't tell me that, you bitch!"
    "Asumi and I went to the same grade school."
    "If it was just that, then there wouldn't be much of a problem."
    "The problem is she bullied me...hard."
    "So I begged people to stop her from doing it, but..."
    "\"There they go again. Another fight between husband and wife!\""
    "\"You two are so close, huh?\""
    "\"I envy you, Yusuke.\""
    "...That's what they said."
    "And that's why I was assigned to the student union staff with her."
    "My childhood memories are...awful. My mind was almost twisted, you know."
    "However, it ended when Asumi moved out of town when we were in the sixth grade."
    "Now she comes back in my life again!"
    "I should've escaped from her while I could...but it's too late now. I really shouldn't have come to this cursed land!"
    "I sink into the abyss of despair."
    "Suddenly, Asumi loosens her hold around my neck."

    $ char ('tas030')

    voice as0022
    asumi "Are you...Yusuke Sawada?"
    yusuke "Finally, you remember! My name, who I am, and what you did to me."

    voice as0023
    asumi "Oh no! Are you really Yusuke? Did you come here too...!?"
    yusuke "???"
    "She completely loosens her arms and unsteadily steps back in shock."

    $ char ('tas042')

    voice as0024
    asumi "Are you here to threaten me?"
    yusuke "Huh? You're the one who's threatening me, you devil!"

    voice as0025
    asumi "You're pathetic!"
    yusuke "What the hell are you talking about? I don't get it."

    $ char ('tas033')

    "She looks weakened and starts thinking about something."
    "She thinks seriously."
    "I have no clue what she just said, so I just wait for her to say something."

    call blackout from _call_blackout_40

    "About three minutes later,"

    $ bgm (5)
    $ bgfx ('bg03c')
    $ char ('tas018')

    voice as0026
    asumi "...Okay, you coward."
    yusuke "Now you're calling me a coward, huh? And what do you mean, 'okay?'"

    $ char ('tas006')

    voice as0027
    asumi "I don't want people to owe me anything. So, I'll help you out under one condition."
    yusuke "That's what I'm saying... What do I owe you...?"

    $ char ('tas007')

    voice as0028
    asumi "The condition is to keep THAT a secret forever!! Do you understand?"
    yusuke "Didn't you hear me? I don't understand what you're..."

    voice as0029
    asumi "Okay, done deal. But IF you break this contract...you won't leave this town alive!"
    yusuke "I...whatever you say, ma'am."
    "I fall on the cold ground."
    "I'm really, really exhausted."
    "Asumi doesn't care about me and continues,"

    $ char ('tas037')

    voice as0030
    asumi "Now, what do you want from me?"

    menu:
        " "
        "I don't want to spend the night outside!":


            $ F016 += 1
        "I'm freezing. Could you warm me up?":


            yusuke "P...please, warm me up...with your..."

            $ char ('tas036')

            asumi "......"
            yusuke "Actually, I'm okay."
            "...She looks really scary. I withdraw."
            "Then, I come up with a more tamed request."
        "Lend me some money for food and a place to stay.":


            yusuke "P...please, lend me some money for a motel..."

            $ char ('tas036')

            asumi "......"
            "She quietly takes her wallet out."
            "And it is very thin... I know what she wants to say."
            "Any requests involving money issues are a no-no."

    yusuke "What I want is...only one thing. I want a place to spend the night...with a roof."

    $ char ('tas011')

    voice as0031
    asumi "How dare you ask me something like that! But...a promise is a promise..."
    "Again, I pass out as I hear her nagging. I'm pretty much beaten up all right..."

    call blackout from _call_blackout_41

    voice as0032
    asumi "Moe-Moe, Marutan, come over here!"
    "PITTER-PATTER. I hear footsteps in return."
    "Sounds with different tempos which are made by four feet."

    $ bgfx ('bg01c', diss_long)
    $ bgm (3)
    $ chars ('tto007', 'tma004')

    voice to0002
    leftone "Oh, Asumi! I was beginning to worry about you. Where have you been? EEK!"

    $ char1 ('tto022')

    rightone "......"
    "Two girls show up in front of us."
    "They look totally different than Asumi."
    "The beautiful girl with long hair panics seeing me, and she clings to Asumi."

    $ char1 ('tto007')

    voice to0003
    leftone "Asumi, Asumi! Who is this boy? Why did you bring him here...?"

    voice as0033
    asumi "Moe-Moe, you're doing it wrong! Call me, 'Asumin!!'"

    voice ma0001
    rightone "...Asumin."

    voice as0034
    asumi "Marutan, you know me well!"

    voice ma0002
    rightone "...Who the hell is this?"

    "This girl barely reaches Asumi's shoulder in height."

    "She ignores the panicking girl who's asking Asumi questions. Asumi answers the other girl by saying,"

    voice as0035
    asumi "Oh, this? This thing is called, Yusuke Sawada. It's nothing, so you don't need to worry about it."

    voice ma0003
    rightone "...Humph."

    voice to0004
    leftone "Anyway, Asumi...you know you can't bring boys inside this dormitory! Oh, look, he's hurt... Look at those big bumps on his head. Oh my...!"

    voice as0036
    asumi "Nooooo! Call me A-SU-MIN! We're happy roommates, remember!? Stop calling me by my first name!!"

    voice ma0004
    rightone "...Hey, Asumin."

    voice as0037
    asumi "Oh yeah, Marutan rocks! What did you say?"

    voice ma0005
    rightone "The guy... What are you going to do?"

    voice as0038
    asumi "Oh, this guy? Well..."
    "Asumi throws a glance at me."
    "She sees a man... with numerous scars and bumps, which of course, are her fault."

    voice as0039
    asumi "This chap will stay here for a while! He's kinda unlucky, so please take good care of him!"

    $ empat ('j5')
    $ char1 ('tto013')

    voice to0005
    leftone "Oh no...Asumi, it's against dorm regulations to invite a boy! And I don't want to share the room with a boy...!"

    voice as0040
    asumi "Asumin! Asumin! It's ASUMIN! If you ever call me Asumi again, I'll have you share your bed with this sucker!"

    $ empat ()
    $ char1 ('tto007')

    voice to0006
    leftone "Noooo! I...err...sob-sob..."

    voice ma0006
    rightone "...Asumin?"

    voice as0041
    asumi "Yeah? What is it, Marutan?"

    voice ma0007
    rightone "...Nothing."

    $ chars ()
    $ music_stop ()

    "Marutan quickly goes back to her room. She's a strange girl."
    "On the other hand, Moe-Moe is a weakling. She falls on the floor and sobs."

    $ char ('tas001')

    "And of course...there's Asumin smiling at me."
    "Do I detect anger and a grudge in her big eyes?"

    voice as0042
    asumi "...You!"
    yusuke "Wh...what is it?"

    $ char ('tas003')

    "Asumi points at me as if she's sticking a gun barrel at me and whispers,"

    $ bgm (5)

    voice as0043
    asumi "I'll let you stay here, BUT if you try to do something stupid..."
    yusuke "...Then what?"

    voice as0044
    asumi "I'll harm you! So be careful. Heh heh."
    yusuke "......"
    "Shivers run down my spine."
    "The same feeling arose a long time ago...just like today."
    "But still, I manage to avoid the worst case scenario."
    "Because somehow, I find shelter and avoid becoming a hobo."
    yusuke "Now...where should I stay?"

    $ char ('tas002')

    voice as0045
    asumi "There's no extra space in here... Well, there it is!"

    call blackout from _call_blackout_42

    "She pushes me into a closet."
    "It's dark, it's tight, and it's cold."
    "There's not much of a difference from spending the night outside..."
    yusuke "Am I really lucky...?"
    "So I cry. I cry hard the whole night."
    "Today was supposed to be bright and shiny. Instead, my new life begins like this..."

    $ bgfx ('sora09')
    $ bgm (8)

    "Yet,"
    "meeting up with Asumi Hirota gives me a place to live."
    "And that's how my youth began to turn with unexpected twists."
    "The happiest, most unforgettable life with three roommates started like this..."


    call ep_finish from _call_ep_finish_6

    $ renpy.end_replay()
    $ unlock_episode (1)
    jump episode02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

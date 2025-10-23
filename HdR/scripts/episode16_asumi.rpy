label episode16_asumi:

    yusuke "I feel empty now..."

    $ cg ('e3_0309', pos=[ALIGN(0.59, 0.0)])

    voice as0548
    asumi "What's wrong, Yusuke? You look so sad and depressed."
    yusuke "Leave me alone."

    call cg_slide (picture='e3_0309', tm=0.5, kind='h', start=0.59, end=0.45, cls=diss_fast) from _call_cg_slide_4
    $ cg ('e3_0305', pos=[ALIGN(0.45, 0.0)])

    voice as0549
    asumi "Heh-heh, you're still upset. How cute!"
    yusuke "A guy isn't too happy being called cute. I'm a man!"
    "I didn't realize it a minute ago, but only Asumi has a towel wrapped around her."
    "This is unbelievable."
    "Under the towel, the beautiful body I saw last semester is..."

    call cg_slide (picture='e3_0305', tm=0.5, kind='h', start=0.45, end=0.59, cls=diss_fast) from _call_cg_slide_5
    $ cg ('e3_0312', pos=[ALIGN(0.59, 0.0)])

    voice ma0117
    marumu "Yusuke, your nose is bleeding."
    yusuke "Sorry..."

    $ cg ('e3_0310', pos=[ALIGN(0.59, 0.0)])

    voice as0550
    asumi "I know you were thinking something perverted. Lech!"

    voice ma0118
    marumu "Lech!"

    $ bgm (7)
    $ bgfx ('black')
    call effect ('SE39', ETYPE2, sound_loop=True) from _call_effect_15

    "Asumi and Marumu suddenly start hitting me."

    $ bgfx ('sora05')

    "I can faintly see Namiki talking to Tomoe over in the corner...GLUB-GLUB."

    $ sfx (delay = 0.5)

    "I don't want to drown, but I want to take a bath with Asumi alone someday."
    "Some guy will probably come along and interrupt our relationship later, but I can't even imagine such a thing right now."

    jump episode16_b

label episode16_asumi_b:

    $ bgm (5)
    $ char ('tas050')

    voice as0551
    asumi "Oh, Yusuke. Pooh...heh-heh."
    "Asumi runs up to me."
    "She's smiling. I hardly ever see her smiling like that."
    yusuke "Asumi...what's so funny?"

    $ char ('tas015')

    voice as0552
    asumi "Because... No, I won't tell you."
    yusuke "What? Come on, tell me!"

    voice as0553
    asumi "I'll tell you someday. He-he-he..."

    $ char ('tas050')

    yusuke "......"

    $ music_stop ()
    $ char ()

    "Did Misaki make her smile like this?"
    "Did he really do this? He's the king of shitty attitudes!"
    "I clench my fist tightly."
    "I've never felt this much anger before."
    "What happened between Asumi and Misaki?"

    $ bgfx ('black')
    $ bgfx ('bg03b')
    $ bgm (12)

    yusuke "Humph!"
    "Once I hate him, I'll always hate him."
    "I notice him walking 30 feet behind us."
    "I can tell...he's after Asumi."
    "Why is he following her? Do they have a 'special relationship?'"
    "Ms. Yukimura asked him, 'Are you seeing someone?'"
    "The person he likes is..."
    "Not many people successfully make Asumi laugh so hard."
    yusuke "Tut...what a dick."

    $ char ('tto001')

    voice to0260
    tomoe "Misaki? Oh, there he is again."
    yusuke "Again?"

    $ char ('tto002')

    voice to0261
    tomoe "Yeah, I see him a lot on the way back to the dorm. I wonder if this is on his way home?"

    $ char ('tas050')

    voice as0554
    asumi "Pooh...!"
    "Asumi looks back at him and bursts out laughing."
    "Something is definitely going on between them."
    yusuke "I see him a lot lately. His purpose is..."

    $ char ('tma003')

    voice ma0119
    marumu "He likes Marumu."

    voice as0555
    everyone "I don't think so."
    "Everybody agrees."

    call blackout from _call_blackout_15
    $ bgfx ('sora01')

    yusuke "Maybe she likes him. No, she's not that kind of person."
    "She told me that she loves me."
    "There's only one possibility left. Misaki's hitting on her."
    yusuke "He's good looking, smart, and he can do everything better than I can."
    "I feel I'm okay now with Asumi."
    "I can tell from her attitude."
    "However, if a handsome guy like him continues to hit on her, she might..."
    yusuke "Oh, what should I do?"
    "I realize I can't do anything about this."
    "I couldn't find a more worthy opponent."

    $ bgm (12)
    $ bgfx ('bg06b')

    yusuke "Hmm..."

    $ char ('tas002')

    voice as0556
    asumi "What are you sighing about? Let's go home!"
    yusuke "Where are Moe-Moe and Marutan?"

    voice as0557
    asumi "Moe-Moe wants to stop by some place, and Marutan has a secret duty."
    yusuke "A secret duty?"

    $ char ('tas001')

    voice as0558
    asumi "Yeah, she said, 'Because it's secret, I won't tell you.'"
    yusuke "She's really a mystery."

    $ char ('tas045')

    "Asumi smiles all over."

    voice as0559
    asumi "I like going home with you alone, you know. It's like a date!"
    yusuke "Y...yeah. Oh, I have something I've got to take care of. Could you go back alone?"

    $ char ('tas018')

    voice as0560
    asumi "Really? How disappointing."

    call blackout from _call_blackout_16

    "She complains for a while but leaves alone."
    "Of course I want to go home with her."
    "But I found him."
    "Misaki's looking at Asumi from behind."

    $ bgfx ('bg06b')

    yusuke "......"

    $ char ('tmi001')
    $ bgm (16)

    misaki "......"
    "He walks toward me."
    "Of course he does that."
    "Asumi has already left."
    "He has to go through the front gate to follow her."
    "However, he stops in front of me."
    "He's looking at me with sharp eyes."
    "Is he threatening me? Feeling his menace, I bullishly tell him,"
    yusuke "Asumi left. She's not here anymore."
    misaki "......"
    yusuke "You're always following her. I don't think that's cool."

    $ char ('tmi002')

    misaki "......!!"
    "I scream in my mind."
    "His eyes are telling me his strong feelings."
    "I feel weak and wussy."
    "If I don't show him I've got some cojones, I'm going to lose."
    "I want to believe her. She's madly in love with me."
    "Then...I'll fight him for her. That's the only way."
    yusuke "You should say what you feel! If you love Asumi, then..."
    misaki "Yes, I do."
    yusuke "I know...I know it. However, she already has a boyfriend."
    misaki "No...I love...you, not Asumi."

    $ music_stop ()

    yusuke "Huh...?"
    misaki "I...love...you."
    yusuke "......"

    $ bgfx ('black')

    "I can't think of anything."
    "Right now, the womanizer stands in front of me."
    "I don't understand what he just said to me."
    "I slowly look down at my chest, my hips and my legs."
    "I'm a 'girl' now."


    call ep_middle from _call_ep_middle_1

    jump episode16_c

label episode16_asumi_c:

    $ bgfx ('black')
    $ bgm (9)
    $ bgfx ('sora09')

    "I feel so depressed."
    "Misaki isn't my opponent."
    "If I were to venture an opinion, I would say he's Asumi's opponent. What a weird love triangle."
    "Looking at her smiling irresponsibly, I have only one thing on my mind."
    "I think going steady with Asumi was all a big mistake."

    call blackout from _call_blackout_17
    $ bgfx ('bg05a')
    $ bgm (6)

    "Since then..."
    "Misaki hasn't tried any moves on me."
    "However, I'm often conscious of him."
    "I feel him looking at me from somewhere with passionate eyes."

    $ char ('tas037')

    voice as0569
    asumi "Are you a moron or what?"
    yusuke "What do you mean?"

    $ char ('tas007')

    voice as0570
    asumi "Misaki doesn't look at you. He loves 'Sakurako Yamanobe.'"
    yusuke "I know, but..."

    $ bgfx ('black')
    $ bgfx ('bg03b')

    yusuke "I feel his affectionate eyes on me after school."

    $ char ('tto001')

    voice to0263
    tomoe "Oh, there he is again. He might be..."

    $ char ('tma017')

    voice ma0120
    marumu "He might be interested in Marumu."
    yusuke "Stop that!"

    $ char ('tto025')

    voice to0264
    tomoe "He might like you. You look so cute in girls' clothes."
    yusuke "You're exactly right."

    $ char ('tas051')

    voice as0571
    asumi "Pooh... Ha ha ha ha!"
    "Poor me..."

    jump episode16_d

label episode16_asumi_e:

    call blackout from _call_blackout_18
    $ bgfx ('bg06a')
    $ char ('tas024')
    $ bgm (13)

    voice as0575
    asumi "I think you're right, Yusuke."
    yusuke "Yeah..."
    "I inwardly heave a sigh of relief."
    "Misaki doesn't tell my secret to anyone, even after he finds out the truth."
    "It's been a week, and I still go to school from the girls' dorm."
    "My opinion about him has changed."
    "As a man, I should learn something from him."

    $ char ('tas001')

    voice as0576
    asumi "By the way, what would you do if he told everyone about your secret?"
    yusuke "Of course, I'd take full responsibility and leave the dorm. I'd probably be expelled as well."

    $ char ('tas012')

    voice as0577
    asumi "Wow, you're ready for that. I'm impressed. Then I would leave with you. I don't want Moe-Moe and Marutan to get involved."
    yusuke "What?"

    $ bgm (9)
    $ char ('tas044')

    voice as0578
    asumi "I think I'm a little bit responsible."
    yusuke "Asumi..."

    $ char ('tas015')

    voice as0579
    asumi "Oh, are you moved? Right? I'm a..."

    $ bgm (7)

    yusuke "How can you say, 'A little?' It's all your fault!"

    $ char ('tas012')

    voice as0580
    asumi "Tee-hee."
    "I thought this would end the trouble."

    call blackout from _call_blackout_19
    $ bgfx ('bg05a')

    yusuke "Misaki..."

    $ char ('tmi002')

    misaki "Huh...?"
    yusuke "Thanks..."

    $ char ('tmi001')

    misaki "Y...yeah."
    "I return the umbrella to him."
    "We look at each other with mixed emotions."
    "I know he has complicated feelings, but I need to return his umbrella."

    voice et0002
    girl "Did you see that?"

    voice et0003
    girl "I didn't believe it at first, but the rumor might be true."
    "Girls are passing by us and gossiping."
    "They look at us with curious eyes."
    "I feel something is wrong."

    voice et0004
    girl "They're really a couple."
    yusuke "A...couple?"

    $ char ('tmi004')

    misaki "......!!"
    "My anxiety is getting worse and worse."

    $ bgm (7)
    $ bgfx ('bg07a')

    yusuke "Asumi!!"

    $ char ('tas002')

    voice as0581
    asumi "Hey, what's up, boys?"
    yusuke "It's you, isn't it?"
    yusuke "Asumi..."

    $ char ('tas015')

    voice as0582
    asumi "Hey, half of it is true, right? Ha ha ha ha!"

    $ char ('tas051')

    "She bursts out laughing, without any sense of guilt."

    $ char ('tas013')

    voice as0583
    asumi "No girls hit on you, Yusuke. I'm so happy!"

    $ unlock_gallery ('g1e2')

    jump episode16_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

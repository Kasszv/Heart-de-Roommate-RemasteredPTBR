label episode04:

    $ Fnum = 4
    $ save_name = "Episode 4: Emergency Meeting at the Hot Spring"

    $ bgm (12)
    $ bgfx ('bg01a')
    $ char ('tas002')

    voice as0109
    asumi "It's time to go!"
    "Asumi hurries us as she finishes her breakfast and quickly changes her clothes."

    $ char ('tma001')

    "Marumu shows up after Asumi."
    "However, Tomoe doesn't."
    "I change into the girl version of myself in the tight closet. Tomoe still doesn't show up."
    yusuke "Tomoe definitely isn't a morning person."

    $ char ('tto001')

    voice to0027
    tomoe "Sorry to have you wait, everyone. Oh, thanks for your help, Toshibo."

    $ char ('tts001')

    voice ts0012
    toshibo "Meow!"
    yusuke "Just what are they...!?"
    "I'm a little bit jealous about their mysterious relationship. Anyway, I follow them out of the room."
    "Then, something terrible happens."


    call ep_start from _call_ep_start_3

    $ bgm (16)
    $ bgfx ('bg13a')
    $ char ('tik999')

    voice yu0001
    girl "Oh? I've never seen you before. Which room do you live in?"
    yusuke "M...me? Well I...guhhhh!"

    $ sfx ('SE03')

    "Asumi tramples on my foot really hard."
    "She pushes me back as she comes forward."

    $ sfx ()
    $ char ('tas006')

    voice as0110
    asumi "None of your business, you Trio de Bitches! Go away!!"

    $ char ('ths001')

    voice hs0001
    girl "Uh, you're quite the conversationalist, Miss Hirota. I must admit you're certainly the leader amongst a group of stupid roommates."

    $ char ('tfu001')

    voice fu0001
    girl "According to my data, she's right."

    $ char ('tas006')

    voice as0111
    asumi "You want a piece of me?"

    $ char ('tik999')

    "Asumi and the three girls are facing off."
    "I can almost see a burning fire between them."
    "Then, the middle girl in the trio speaks up."

    voice yu0002
    girl "Anyway. You, the girl behind, I must warn you you'd better stay away from these stupid girls. You'll regret it, otherwise."

    voice hs0002
    girl "Uh-huh, that's right. One selfish idiot, one fainthearted dork, and one extra weirdo."

    voice fu0002
    girl "A very unique trio, in a sense. And needless to say, you guys are morons."
    "Can we let them talk like that?"
    "Oh, gee. I can't keep watching this."

    $ char ('tto007')

    voice to0028
    tomoe "You call me a fainthearted dork... I...I...sob-sob."

    $ char ('tma023')

    marumu "......"

    $ char ('tas011')

    voice as0112
    asumi "Hey, you two. Say something!"
    "Asumi turns around and yells at us."
    "The 'Trio de Bitches' laugh at us. Their eyes rove amorously at me and say,"

    $ char ('tik999')

    voice yu0003
    girl "You should choose your friends wisely. A pretty girl like you is welcome to join our team."

    voice hs0003
    girl "You speak and behave like a boy...heh heh."

    voice fu0003
    girl "You and I can get along since we both wear glasses."

    $ music_stop ()
    $ char ()

    "The trio joyfully laugh and leave."
    "I see the enraged Asumi shaking, the crying Tomoe, and the nonchalant Marumu behind me."

    $ char ('tas006')

    voice as0113
    asumi "Moe-Moe, tomorrow is Wednesday, right?"

    $ char ('tto001')

    voice to0029
    tomoe "Y...yeah."

    $ char ('tas007')

    voice as0114
    asumi "We'll have a meeting then. The subject is: 'How to screw up the Trio de Bitches.'"

    $ char ()

    "Asumi starts walking away after saying so."

    $ vox ('as0115')
    $ bgfx ('black')

    "I can hear her mumbling in anger."
    "We follow her and head to the school."

    $ vox (delay=0.3)
    $ bgfx ('sora01')

    "What was that all about?"
    "I look up at the sky and kick back during the lunch break."
    "Then, my peaceful time suddenly comes to the end at the hands of an enraged, savage girl."

    $ bgfx ('bg05a')
    $ char ('tas001')

    voice as0116
    asumi "There you are, Parasite One!"
    yusuke "Please, stop calling me by that name at school."

    $ char ('tas006')

    voice as0117
    asumi "All right, all right. YOU! Don't go out of the classroom without my permission!"
    yusuke "But why? It's none of your business what I do during lunch break."

    $ char ('tas007')

    voice as0118
    asumi "Because I have to tell you something. MUMBLE-MUMBLE..."
    "She grabs me by my ear and whispers."
    "I listen to her and sincerely appreciate her."

    $ bgm (6)
    $ char ('tas001')

    yusuke "You're absolutely right. My apology is deeper than the Japan Deep."

    voice as0119
    asumi "Good! As long as you understand."
    "She warned me about the way I behaved in front of that trio this morning."
    "It was okay because they just thought I was a tomboy."

    voice as0120
    asumi "If they find out you're living with us, the result would be catastrophic."
    yusuke "I'll be careful next time, so please forgive me, my master!"

    $ char ('tas015')

    voice as0121
    asumi "I'm not cold blooded enough to throw you out."
    yusuke "Phew."
    "To be honest, she almost doesn't care about my situation. She just worries about THAT secret that I'm supposed to know about."
    "Still, I have to rely on Asumi now."
    "I keep my timid manner and ask Asumi about THAT."
    yusuke "By the way Asumin...guh!?"

    $ char ('tas036')
    $ music_stop ()
    call effect ('SE43', ETYPE1) from _call_effect_16
    $ bgm (7)

    "DONK!"
    "She gives me a hard right punch in my face!"
    "I hold my smashed nose and protest."
    yusuke "What are you doing!? I just wanted to ask you a question!"

    voice as0122
    asumi "You! You just called me Asumin!"
    yusuke "Huh? Well, yeah."

    $ char ('tas007')

    voice as0123
    asumi "You can't call me by that name for another ten years! Only my roommates can call me that. And you're not my roommate!!"
    yusuke "BOO!"

    $ char ('tas036')

    voice as0124
    asumi "You want another punch to balance your face?"
    yusuke "...No thanks."
    "I hate to admit it, but I'm no match for her with my physical strength."
    "I wipe up my nosebleed and ask her again."

    $ music_stop ()

    yusuke "Those girls... Trio de Bitches. Who are they?"

    $ char ('tas034')

    asumi "......"
    "Asumi becomes quiet. She looks angry as well."
    "Then, she starts explaining about the trio...full of spite."

    $ bgm (16)
    $ bgfx ('black')
    $ bgfx ('bg13a')
    $ char ('tyu001')

    "Akane Yukimura."
    "Akane is a leader of the trio and also came from the same middle school as Asumi."
    "She's ranked as their commander."
    "Akane is said to be very selfish (just like Asumi)."
    "During a health check at their old school, Akane marked an inch less than Asumi in her bust measurement. She's been hating Asumi with a passion ever since."
    "Asumi thinks she's superior in every sense, but I'm sure Akane would say the same thing."

    $ char ('ths001')

    "Kaoru Hisame."
    "Kaoru executes various missions according to their leader's plan."
    "She's athletic and good at every sport."
    "She's the ace of our school's swimming club, but she doesn't participate in the activities lately."
    "'She's smart, has a pretty face and body, but...she's twisted!' That's what Asumi described about Kaoru."
    "True, she sounds very cold and seems to look down on people."

    $ char ('tfu001')

    "Midori Fubuki."
    "She's in charge of data collection and analysis."
    "She's full of curiosity and enjoys studying."
    "She used to be bullied about her glasses when she was kid, so the stress turned her into an eyeglass fanatic."
    "That explains her friendly attitude towards me, a guy with glasses."
    "However...she's basically mean and her high-pitched voice really gets on people's nerves (again, so Asumi said)."

    call blackout from _call_blackout_23

    "To be honest, I don't think our side has any chance against them."
    "We can overwhelm them character-wise, though."
    "Asumi's face reddens in anger as she finishes explaining."

    $ bgm (12)
    $ bgfx ('bg05a')
    $ char ('tas007')

    voice as0125
    asumi "In any case, they're in our way. They're our rivals. We have to defeat them in any way. Get it!?"
    yusuke "Yeah, I guess..."
    "I answer her blankly."
    "I'm getting tired of hearing her. This is enough."
    "I look up at the blue sky to relieve some stress."
    "But Asumi forcibly turns my face to her and stresses me out by saying,"

    $ char ('tas006')

    voice as0126
    asumi "You know, you need to attend our meeting tomorrow."

    voice as0127
    asumi "It's supposed to be only for our roommates, but as long as you live with us, I want you to follow up on what's going on."

    menu:
        " "
        "Sure, I'll join you.":


            yusuke "Good, but what's this meeting anyway?"

            voice as0128
            asumi "You'll find out. 4:00pm tomorrow after school. Be on time!"

            $ F016 += 1
        "No thanks.":


            yusuke "I have something tomorrow, so..."

            voice as0128
            asumi "You'll be here at 4:00pm tomorrow after school. Be on time!"
            yusuke "...You're not listening to me, huh?"

    "A hard-to-understand hand written map."

    $ char ()

    "Asumi passes it to me and runs away."
    "She's such a self-centered person."
    yusuke "Well, it's better than being left out. Still, what's this meeting all about?"

    $ music_stop ()
    $ bgfx ('sora01')

    "She ordered me to join the meeting before I could ask her any questions."
    "Later on, I would regret this on an astronomical level."

    $ bgm (6)
    $ bgfx ('bg16c')

    yusuke "It must be around here... Oh yeah, there it is!"
    "I've been asking people around and struggling to find the place, and finally, I arrive."
    "This isn't because of my bad field perception. It's because of Asumi's crappy map."
    yusuke "Why did she include Mt. Fuji and Lake Biwa, which are hundreds of miles apart in this map!?"
    "I'm very late, but I can blame it on Asumi."
    yusuke "All right... Oh?"

    $ char ('ttm001')

    "I finally reach the hot spring hotel."
    "I see a woman standing in front of the hotel."
    "As soon as she sees me, she starts beckoning me."
    yusuke "......?"
    "I've never seen this lady in my life, but I walk up to her anyway."

    voice ta0001
    woman "Hey, are you Yusuke?"
    yusuke "Yes, I am."

    $ char ('ttm002')

    voice ta0002
    woman "You're late. I was beginning to worry about you."
    yusuke "And you are...???"

    voice ta0003
    woman "Don't worry about it! Just follow me."
    yusuke "H...hey!?"

    $ bgfx ('sora09')

    "She looks kind and sexy. And the place she leads me into...almost stops my heart."


    call ep_middle from _call_ep_middle_3

    call triple_slide_from_right ('e3_0301') from _call_triple_slide_from_right
    $ sfx ('SE15')
    $ unlock_gallery ('g5e1')

    yusuke "Is this place...!?"

    $ sfx ()

    voice as0129
    asumi "You're late!! You have to buy us some cold drinks as a penalty!"

    voice ma0065a
    marumu "......(nod)"
    yusuke "Anyway, this is too...ah!?"
    tomoe "......"
    "I'm freaked out by the sight I'm seeing right now."
    "Then my eyes and Tomoe's meet."
    yusuke "Th...this is...I mean, Asumi forced me to...err..."

    voice to0030
    tomoe "...EEK!"
    yusuke "Tomoe...?"

    voice to0031
    tomoe "YAAAAAAA!!"

    $ bgm (7)
    $ bgfx ('sora08')
    $ sfx ('SE10', loop=True)
    $ vox ('to0032')

    "Where are these things coming from!?"
    "Tomoe hits me with tons of stuff she's throwing."
    "That quiet, cute Tomoe."
    "No matter how loud I scream, she's panicked and doesn't listen to me."

    $ vox (delay=0.3)
    $ sfx (delay = 0.5)

    "Then a towel, which is wrapped around Tomoe's body, slips down. All hell breaks loose now!"

    $ sfx ('SE39')

    "Her screams grow louder as she starts hitting me with a wooden bath chair."
    "I receive two critical hits on the back of my head. How can she smack me that hard with her thin arms!?"

    $ sfx ()

    yusuke "Tomoe's titties are...huge... THUD."

    voice as0130
    asumi "H...hey, you! Are you all right!?"
    "This is unusual. Asumi worries about me while Tomoe attacks me. I sink into the tub as I think this."

    call blackout from _call_blackout_24

    voice as0131
    asumi "...Wake up, Parasite One!"

    voice to0033
    tomoe "Please wake up, Yusuke! I'm so sorry. Waaa..."
    marumu "......"

    $ sfx ('SE12')

    "THAK."
    "Something sharp is jabbed in my head, and I still feel dizzy."
    "I jump up from the unbearable pain."

    $ sfx ()
    $ cg ('e3_0302', pos=[ALIGN(0.59)])

    yusuke "What the hell!?"

    voice as0132
    asumi "Marutan, why are you sticking that miniature flag in his head?"

    voice ma0026
    marumu "...Acupuncture."

    $ cg ('e3_0303', pos=[ALIGN(0.59)])

    voice as0133
    asumi "Good job, Marutan! I must reward you with the Asumin Prize!"

    voice to0034
    tomoe "Oh, thank God. You came back...ohhh."
    yusuke "You! I almost..."
    "I realized I'm just a toy to these girls."

    $ bgm (12)

    yusuke "Oh, it hurts."

    voice to0035
    tomoe "I'm really sorry, Yusuke."
    yusuke "I'm all right now, I guess."
    "But still, Tomoe looks scared and keeps a distance from me."
    "The numerous wounds from Tomoe's attacks sting in the hot water."
    "But I heard these hot springs are good for healing wounds. I sincerely hope so."
    "Tomoe shyly looks away from me and faces Asumi. She asks Asumi in a harsh tone,"

    voice to0036
    tomoe "Asumi, why didn't you tell me Yusuke would be joining us!?"

    call cg_slide ('e3_0303', tm=0.5, kind='h', start=0.59, end=0.0, cls=diss_fast) from _call_cg_slide_8
    $ cg ('e3_0304', pos=[ALIGN(0, 0)])

    voice as0134
    asumi "Asumin! Call me Asumin!!"

    voice to0037
    tomoe "ASUMI!"

    $ cg ('e3_0301', pos=[ALIGN(0, 0)])

    "Asumi shrinks back as Tomoe furiously yells."
    "I swear, I'll never, ever provoke Tomoe. She's too scary."

    voice as0135
    asumi "I'm sorry I didn't inform you but look at Marutan. She doesn't care, you see? Besides, I don't consider him a man."
    yusuke "Boy, do I feel bad."
    "They ignore me anyway, and Tomoe still seems to disagree with Asumi."

    voice to0038
    tomoe "But I do care! I can cancel having our meetings in here, you know."

    $ cg ('e3_0304', pos=[ALIGN(0, 0)])

    voice as0136
    asumi "You're mean. You're too mean, Moe-Moe! Even though your family runs this place, you have no right to take this place away from us!"
    yusuke "Wow. You're really a selfish bastard."

    call cg_slide ('e3_0304', tm=0.5, kind='h', start=0.0, end=0.59, cls=diss_fast) from _call_cg_slide_9
    $ cg ('e3_0303', pos=[ALIGN(0.59)])

    voice as0137
    asumi "Oh. You want to sink to the bottom again?"
    yusuke "I...said nothing, ma'am."

    voice as0138
    asumi "Anyway, Wednesday isn't that busy here, and that's why we have meetings at this hot spring, am I correct?"
    "Tomoe can't talk back as Asumi speaks with power."
    "Gosh, Tomoe is giving us a place...her house...for free, and still scolded like this. This is wrong!"

    menu:
        " "
        "Admonish Asumi.":


            "I'm a man! I can fight!"
            "I want to show off my manhood sometimes, you know."
            "I'll talk to Asumi. I stand up and walk up to her."

            $ F017 += 1
        "I'd better keep quiet.":


            "I can't say a thing to Asumi."
            "She's too ferocious."
            "I still haven't recovered from the damage I received from Tomoe."
            "Tomoe was angry that I saw her breasts... Those big, plump breasts..."

    $ music_stop ()
    call cg_slide ('e3_0303', tm=0.5, kind='h', start=0.59, end=0.0, cls=diss_fast) from _call_cg_slide_10
    $ cg ('e3_0304', pos=[ALIGN(0, 0)])

    voice as0139
    asumi "Hey! Why are you erecting!? You pervert!"
    yusuke "But I can't control it in this situation."

    voice as0140
    asumi "You should!!"

    call cgeffect ('SE10', KENKA1) from _call_cgeffect
    $ unlock_gallery ('g5e10')
    $ bgfx ('white')
    $ bgfx ('black')
    $ sfx ('SE47')

    "GLUB-GLUB-GLUB..."

    $ sfx (delay=0.2)
    $ bgfx ('sora09')

    "I've sunk to the bottom, even before I confront her."
    "Asumi and Tomoe continue to argue and come to an agreement; Asumi will announce my participation prior to the meeting."

    $ bgm (5)
    $ bgfx ('bg08c')
    $ char ('tas312')

    voice as0141
    asumi "It was a good meeting. Parasite One, buy us cold drinks before we go home."

    $ char ('tto304')

    voice to0039
    tomoe "...My house isn't a public bath, you know."

    $ char ('tma308')

    marumu "......"
    yusuke "Marumu...you're completely exposed."
    "Today's meeting finally ends."
    "It was a painful, yet exciting hour."
    yusuke "Wait a minute. Didn't they have a subject to talk about?"
    "TAP-TAP. Somebody pats my back."

    $ char ('ttm001')

    "As I look back, I see the mysterious woman who led me here."
    yusuke "Yes, what can I do for you?"

    voice ta0004
    woman "Take your time and do it right!"
    yusuke "...What are you talking about?"

    voice ta0005
    woman "Clean up this place. You do the cleaning, we lend you this place for free, right?"
    yusuke "...So?"

    $ char ('ttm002')

    voice ta0006
    woman "Asumi told me you'd clean up this place alone."
    yusuke "What!?"
    "Man... I wasn't expecting this. Sob-sob..."

    call blackout from _call_blackout_25
    $ bgfx ('bg01a')
    $ char ('tas002')

    voice as0142
    asumi "All right, let's have a bright school day today!"

    $ char ('tma007')

    marumu "......"

    $ char ('tto007')

    voice to0040
    tomoe "YAWN... Okay."

    $ char ('tts001')

    voice ts0013
    toshibo "Meow!"
    "Toshibo sees us off, including the sleepy-eyed Tomoe."
    "But the peaceful morning suddenly comes to the end."

    $ bgm (16)
    $ bg ('bg13a')
    $ char ('tik999', diss_long)

    voice yu0004
    akane "You. You're still with them."

    voice hs0004
    kaoru "You'll become stupid when you're with a stupid. You'll become a dork when you're with a dork."

    voice fu0004
    midori "According to my data, they're right. Leave them and join us."

    $ char ('tas036')

    voice as0143
    asumi "Grrrrr!!"
    "The trio passes us."
    "Asumi looks at us and declares,"

    $ bgm (7)
    $ char ('tas007')

    voice as0144
    asumi "We're going to have a meeting next Wednesday! We'll talk about how to beat the Trio de Bitches!"
    marumu "......"
    yusuke "W...wasn't that the subject for last night?"

    voice as0145
    asumi "You come with us! You're already part of our war potential!"
    yusuke "Please exclude me from the meetings for a while!"
    "I know Tomoe's thinking the same thing while standing next to me."
    "However, the room leader (as Asumi calls herself) doesn't listen to me."

    $ char ('tas036')

    voice as0146
    asumi "Shut up and think about how to defeat those bitches!!"
    yusuke "Oh no..."


    call ep_finish from _call_ep_finish_2

    $ renpy.end_replay()
    $ unlock_episode (4)
    jump episode05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

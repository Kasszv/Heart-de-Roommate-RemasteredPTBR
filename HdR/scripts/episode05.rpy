label episode05:

    $ Fnum = 5
    $ save_name = "Episode 5: My Savage Sister!"

    $ bgfx ('bg06b')
    $ char ('tas006')

    voice as0147
    asumi "...You're late!"
    yusuke "You didn't need to wait for me. I can go home by myself. I'm not a six year old, you know."

    $ char ('tas007')

    voice as0148
    asumi "That's not my point. You might go home without changing your clothes, right? Like yesterday."
    yusuke "...I'm sorry."
    "Tomoe is helping Ms. Yagami print out some handouts."
    "Marumu said that she had something to take care of, so she went home early."
    "And that's why only Asumi and I are going home together."
    "I wish I could take a walk and explore this town alone,"
    "Without wearing this girls' uniform, that is."
    "However, I appreciate Asumi's concern later."
    "Because...there's terror closing in on me, without my knowing."


    call ep_start from _call_ep_start_24

    $ bgm (6)
    $ bgfx ('bg03b')
    $ char ('tna202')

    voice na0001
    unknown "Hey, you! You, the pretty girl!" (voice_tag='v_namiki')

    $ char ('tas002')

    voice as0149
    asumi "Yes, may I help you?"
    "Asumi happily turns around."
    "But the girl ignores Asumi and walks up to me instead."
    "I'm freaked out, like a frog in front of a snake, as soon as I see who it is."

    $ char ('tna207')

    voice na0002
    girl_na "Have we ever met before? Do you know me?"
    yusuke "N...no...we haven't..."

    $ char ('tna202')

    voice na0003
    girl_na "Are you sure? Anyway, can I ask you something?"

    $ char ('tas006')

    voice as0150
    asumi "...Hey, you!"
    "Irritated, the ignored Asumi yells at the girl, who's now talking to me in much too familiar of a way."

    $ char ('tas010')

    voice as0151
    asumi "You call her pretty!? I'm much prettier than she is!!"

    $ char ('tna204')

    voice na0004
    girl_na "You're really conceited, huh? But the truth is that this girl is much cuter than you are."

    $ char ('tas037')

    voice as0152
    asumi "Mmm...mmm..."
    "I see her face twitching."
    "I guess she's badly wounded."

    $ char ('tas010')

    voice as0153
    asumi "This girl...this girl is really a b...mguhhh!"
    yusuke "OUCH!!"
    "Asumi's so agitated, she almost exposes our secret."
    "I hurriedly cover her mouth with my hand, and her white teeth sink into my fingers."
    "Looking at our stupid act, the girl leaves us with a sullen face."

    $ char ('tna202')

    voice na0005
    girl_na "I wanted to ask you where the Aiho School boys' dorm is, but...I'll find it by myself."

    $ char ()

    yusuke "Good, she's gone."

    $ char ('tas010')

    voice as0154
    asumi "I won't forgive that bitch! Hurry, we'll chase her!"
    yusuke "Please, don't do that! Sis...Namiki hasn't found out about me yet!"

    $ char ('tas006')

    voice as0155
    asumi "Sis...? Namiki...?"
    "I feel gloomy as I rub my hand with Asumi's teeth marks all over it."

    $ music_stop ()
    $ bgfx ('bg01b')
    $ char ('tas001')

    voice as0156
    asumi "I didn't know you had a sister."
    yusuke "Actually, she isn't my real sister; she's my cousin."

    $ char ('tas037')

    voice as0157
    asumi "Is that so? What the hell is that nearsighted bitch doing here, anyway?"
    yusuke "She must have come to see me. By the way, she isn't nearsighted."

    $ char ('tas007')

    voice as0158
    asumi "She must be! Her eyes must be bad! They're clouded! She said you're cuter than I am!!"

    $ char ('tma016')

    voice ma0027
    marumu "...Parasite One is cuter."
    yusuke "Waaaah!"
    "Marumu suddenly comes out of nowhere."
    "And her appearance interrupts our conversation."
    "Then, I start explaining about Namiki."

    $ bgfx ('black')
    $ bgm (6)
    $ bgfx ('bg03b')
    $ char ('tna202')

    "Namiki Honjo."
    "She's proud of her big tits and calls herself, 'Yusuke's big sister.'"
    "She takes care of me too much."
    "Some people call her 'the perfect sister,' but from my point of view, she's just a busybody."
    "She loves meddling in everything I do."
    "When I told her that I was transferring schools, she said, 'I'll tell them not to mess with you!'"
    "...Who's them?"

    $ bgm (12)
    $ bgfx ('bg01b')

    yusuke "Still, I didn't really expect her to show up."

    $ char ('tto001')

    voice to0041
    tomoe "What? What? What are you guys talking about?"

    $ char ('tas001')

    voice as0159
    asumi "Welcome back, Moe-Moe!"

    $ char ('tma007')

    marumu "......"

    $ char ('tas001')

    voice as0160
    asumi "Okay, Parasite One. Why don't you tell us about her again?"
    yusuke "Ahh!? But I just told you!"

    $ char ('tas021')

    voice as0161
    asumi "You're so mean... Are you trying to shun Tomoe out from us? That cute, kind Tomoe...oh, poor, poor girl."

    $ char ('tto001')

    voice to0042
    tomoe "Asumi, I really don't..."

    $ char ('tas006')

    voice as0162
    asumi "A-SU-MIN!!"
    yusuke "...Okay, alright. I'll tell you one more time."
    "Again, I'm forced to tell them about Namiki from the start."

    call blackout from _call_blackout_149
    $ bgm (6)
    $ bgfx ('bg03b')
    $ char ('tna202')

    "Namiki Honjo."
    "She's proud of her big tits and calls herself, 'Yusuke's big sister.'"
    "She takes care of me too much... I omit the rest."

    $ music_stop ()
    $ bgfx ('bg01b')

    yusuke "...Whew."
    "I'm exhausted."
    "As I finish talking, Asumi stands up straight and declares,"

    $ bgm (5)
    $ char ('tas007')

    voice as0163
    asumi "Anyway, that nearsighted moron came here to see you!"
    yusuke "I told you, she's not nearsighted..."

    voice as0164
    asumi "Once she finds you, everything will be exposed for sure. Listen, folks!"

    $ char ('tto001')

    voice to0043
    tomoe "Y...yes?"

    $ char ('tma001')

    voice ma0065a
    marumu "......(nod)"

    $ char ('tts002')

    voice ts0014
    toshibo "Meow!"
    yusuke "What's Number Two...I mean Toshibo doing here?"

    $ char ('tas006')

    "When she gets everybody's attention, Asumi shouts,"

    voice as0165
    asumi "No matter what happens, we'll keep hiding Parasite One from that nearsighted moron! Let's become a team and help him!"
    yusuke "...What do you mean by 'help me?'"

    $ char ('tas036')

    "Asumi glares at me."

    voice as0166
    asumi "Are you saying that it's okay for her to know about our secrets?"

    voice as0167
    asumi "Things like you live here by blackmailing me?"
    yusuke "Of course not, but..."

    $ bgfx ('bg20a', diss_long)
    $ char ('tto709', diss_long)

    voice to0044
    tomoe "Asumi, is Yusuke blackmailing you?"

    $ char ('tas702', diss_long)
    $ empat ('j5')

    voice as0168
    asumi "...Ah!?"

    $ empat ()
    $ bgfx ('bg01b')

    "Asumi and I turn pale at Tomoe's question."
    "Asumi doesn't even say, 'Call me Asumin!!'"

    $ char ('tto007')

    voice to0045
    tomoe "Asumi?"

    $ char ('tas030')

    voice as0169
    asumi "No! No! That's not true! I wanted to say that his sister might think that way once she finds out...that's all!"

    voice as0170
    asumi "Do you think this wimp could blackmail me!? Do you?"
    yusuke "...This is not easy to take."
    "I swear I'll recall THAT about Asumi and tell everybody about it on the day I leave here."
    "She might beat me to death, but...you never know."

    $ char ('tas007')

    voice as0171
    asumi "It shouldn't be for more than a couple of days; she won't stay in this town that long! We can do it!!"
    yusuke "Wow, you're so energetic about saving me."

    $ char ('tas010')

    voice as0172
    asumi "But of course! I'll make that nearsighted bitch regret what she's done to me!"
    yusuke "Oh...I get it."
    "Harassing Namiki."
    "That's what Asumi wants to do."

    call blackout from _call_blackout_150

    "The next morning..."

    $ bgm (6)
    $ bgfx ('bg02a')
    $ char ('tas006')

    voice as0173
    asumi "Are you guys ready?"

    $ char ('tto004')

    voice to0046
    tomoe "Y...yeah."

    $ char ('tma002')

    voice ma0028
    marumu "...Okay."
    yusuke "......"

    $ char ('tts001')

    "Toshibo sees us off as usual."
    "However, something unusual happens next."

    $ char ('tik999')

    voice yu0005
    akane "...Hey, Trio de Stupid! What are you doing?"

    voice hs0005
    kaoru "Look at that tight formation. Are they scared of us?"

    voice fu0005
    midori "We'd better be careful. That pattern isn't in our database."

    $ char ('tas034')

    voice as0174
    asumi "...Humph!"
    "The three roommates tightly walk together."
    "And I'm hiding in the center of this formation."
    "The only chance Namiki has of finding me is while I'm walking outside."
    "During my commute to the school."
    "So, the three girls will act as walls until we confirm Namiki has left town."

    $ bgfx ('bg03a')
    $ char ('tas001')

    voice as0175
    asumi "This is perfect! That super, nearsighted moron can't beat our teamwork!"

    $ char ('tto007')

    voice to0047
    tomoe "Ahh...Yusuke, don't poke me...there."
    yusuke "But I'm not doing anything!"

    voice to0048
    tomoe "Ahh, there you go again."

    $ char ('tas037')

    voice as0176
    asumi "You! If you make Moe-Moe cry...!!"
    yusuke "I'm saying it's not me!!"

    $ char ('tma017')

    marumu "......"

    $ bgfx ('sora01')

    "Nobody knows Marumu is doing it. We finally arrive at school without any trouble except for a few curious passersby."

    $ music_stop ()
    $ bgfx ('bg05a')

    yusuke "Oh, I'm exhausted."
    "I'm burned out, yet school hasn't even started."
    "I change my uniform in the restroom. Should I escape to the rooftop for the day?"
    yusuke "Ohh, I don't want to go home like that."

    voice na0006
    girl_na "Gotcha! Yusuke, there you are!"
    yusuke "...What the!?"

    $ bgfx ('black')

    "Now, I realize all our efforts were in vain."


    call ep_middle from _call_ep_middle_24

    $ bgm (6)
    $ bgfx ('bg07a')
    $ char ('tna202')

    yusuke "I didn't know you would come this far to find me."

    $ char ('tna204')

    voice na0007
    namiki "AHEM! Did I surprise you? But it's your fault, you know. You didn't tell me where you were going."
    "On the rooftop, during my lunch break."
    "I'm having a conversation with Namiki."
    "Three shadows are observing us; the would-be sister and brother."
    "Needless to say, they're Asumi, Tomoe, and Marumu."

    $ char ('tna202')

    "Namiki sticks her arms out to me with a big smile."

    voice na0008
    namiki "You must've been lonely. Come, jump into my big breasts!"
    yusuke "Wh...what?"
    "I don't think I can do that while those girls are watching me."
    "Well, even if they weren't here, I still wouldn't want to do that."

    voice na0009
    namiki "Come on! Don't be a stranger."
    yusuke "I'm okay, really! Anyway, what are you doing here? What happened to your school?"

    voice na0010
    namiki "Oh, don't worry about my school. They're out on a school trip somewhere."
    yusuke "What the hell are you doing here then; playing hooky?"

    voice na0011
    namiki "Don't say hooky! I'm just enjoying my life here. It's freedom!"
    yusuke "You canceled your school trip...to see me. Oh, I'm so moved..."

    $ char ('tna219')

    voice na0012
    namiki "Humph. The school trip doesn't include a hot spring. It's worthless."
    yusuke "Ouch."
    "She's as hyper as always."
    "Then, she suddenly gets serious and looks at me."

    $ char ('tna210')
    $ bgm (8)

    voice na0013
    namiki "You know what? I was worried about you. You get bullied so easily."
    yusuke "Sis..."
    "Sure, Namiki is a busybody, but at least she cares for me."
    "She cares for me more than my own parents do."

    $ music_stop ()
    $ char ('tna204')

    voice na0014
    namiki "Only I have the right to bully you! I want everyone to know that."

    $ bgm (6)

    yusuke "I'll be damned."

    voice na0015
    namiki "Yeah, you must know you're stupid. Okay, I'll see you later in your room."
    yusuke "Oh!?"

    $ char ('tna202')

    voice na0016
    namiki "The dorm manager told me that you live in an apartment now. I can't believe Uncle forgot to take care of a place for you to live."
    yusuke "So you went to the dorm."

    call blackout from _call_blackout_151

    "This is it. Everything is over."
    "Namiki discovered that I don't live in the male dorm."
    "I don't think I can mystify her any longer."
    "I'm driven into a corner. I turn pale and stare at Namiki's back as she leaves."

    $ bgfx ('bg04a')
    $ char ('tas006')

    voice as0177
    asumi "You run away! That's it!"
    yusuke "Oh no!"
    "Asumi shouts after school."
    "I suggest Asumi explain everything to Namiki."
    "Asumi just won't listen to me."

    $ char ('tas007')

    voice as0178
    asumi "I told you! We'll be doomed if someone finds out about you!!"

    voice as0179
    asumi "We'll support you to reach the dorm. Got it!?"
    yusuke "Support me for what...?"
    "Marumu shows up while I'm at a loss."

    $ char ('tma003')

    voice ma0029
    marumu "...Trust us."
    yusuke "Huh?"

    voice ma0030
    marumu "I'll protect you."
    yusuke "Oh, Marumu."

    $ char ('tma007')

    voice ma0031
    marumu "...I'm kidding."
    yusuke "I don't understand you."

    $ bgfx ('sora01')

    "The four of us gather and begin a strategy meeting."
    "Well, there's no strategy in this."
    "I'll just try sneaking up to Harukaze dorm,"
    "While the other three distract Namiki and buy some time."
    "Namiki probably has no idea that I live in the girl's dorm."
    "That's why I'll be safe, once I get inside the dorm."

    $ bgfx ('bg06a')

    yusuke "Is this really going to work? I have a bad feeling about this."
    "I don't know what to do."
    "But there's a girl who's panicking worse than I am."
    "Needless to say, it is..."

    $ char ('tto007')

    voice to0049
    tomoe "Oh...why is this happening to me?"
    yusuke "......"
    "It's all my fault. It's because I'm living in the girls' dorm."
    "Inwardly, I apologize to Tomoe."
    "(Sorry, Tomoe.)"

    $ char ('tas001')

    voice as0180
    asumi "Let's rock 'n' roll!"

    $ char ('tma007')

    voice ma0032
    marumu "...Oh, yes."
    yusuke "...Yeah."

    $ char ('tto007')

    voice to0050
    tomoe "...Uh-huh."

    $ bgfx ('sora01')

    "Operation Over the Road starts like this:"

    $ bgm (5)
    $ bgfx ('bg06a')
    $ char ('tna202')

    namiki "......"

    $ char ('tma004')

    marumu "......"

    $ char ('tna202')

    voice na0017
    namiki "What do you want?"

    $ char ('tma007')

    marumu "......"

    $ char ('tna202')

    voice na0018
    namiki "Bye now."

    $ bgfx ('black')
    $ char ('tma622')

    voice ma0033
    marumu "...The mission failed."

    $ char ()
    $ bgfx ('bg12a')
    $ char ('tas006')

    voice as0181
    asumi "H...hey, you down there!"

    $ char ('tna202')

    voice na0019
    namiki "What's up? I'm in a hurry."

    $ char ('tas006')

    voice as0182
    asumi "Do you remember me? We met yesterday!"

    $ char ('tna207')

    voice na0020
    namiki "Hmmm..."

    $ char ('tas024')

    asumi "......"

    $ char ('tna203')

    voice na0021
    namiki "Uh, I remember you now. That cute girl..."

    $ char ('tas002')

    voice as0183
    asumi "Yes! You finally acknowledge the truth!"

    $ char ('tna202')

    voice na0022
    namiki "Yeah, you were with that cute girl. Where is she? I don't want to see your ugly face. See ya."

    $ bgfx ('black')
    $ char ('tas707')

    voice as0184
    asumi "Ummm...mmm..."

    $ char ()
    $ bgfx ('bg16a')
    $ char ('tna219')

    voice na0023
    namiki "Where the hell is Yusuke, anyway!?"

    $ char ('tto007')

    voice to0051
    tomoe "Ahh..."

    $ char ('tna219')

    voice na0024
    namiki "I'll really give it to him, once I find him!"

    $ char ('tto007')

    voice to0052
    tomoe "Err...excuse me...?"

    $ char ('tna202')

    voice na0025
    namiki "I'll go check the train station now. DASH!"

    $ sfx ('SE13')
    $ bgfx ('black')
    $ char ('tto707')

    voice to0053
    tomoe "Ohhh, I'm so useless."

    $ sfx (delay=0.2)
    $ char ()
    $ bgfx ('bg16a')
    $ char ('tna207')

    namiki "(The girl I just saw looked tasty. Heh.)"

    $ bgfx ('black')
    $ bgfx ('bg03a')

    yusuke "Phew-phew. I came a long way to avoid the regular commuting route. Namiki will never find me here."

    voice na0026
    namiki "Oh, there you are! The cute girl from yesterday!!"
    yusuke "Ahh!?"

    $ char ('tna202')

    "I see her as I turn around. Yes, it's Namiki."
    "She walks straight at me."
    "Which means: the three girls have failed."
    "This is it! The moment of truth."

    menu:
        " "
        "I just give up.":


            "I give up and stand there, looking dumb."
            "Namiki comes to me with a big smile."

            voice na0027
            namiki "Yes, you ARE cute. Heh."
            yusuke "Sis..."

            voice na0028
            namiki "You call me, Sis? Wow, this is only our first meeting, you know? You're an aggressive girl."
            yusuke "......"
            "She's already living in her own world now. Yep, it's Namiki."
            "Doesn't she know that it's me?"
            yusuke "Oh, I see!"
            "I'm in the girl mode now."
            "Maybe I can fool her and...what the!?"

            $ char ('tna218')

            voice na0029
            namiki "Don't be shy. I'll be gentle."
            yusuke "What are you doing in the middle of the street!? Wow!!"
            "Namiki completely misunderstands and smoothly slides her hands over my breasts."

            $ sfx ('SE16')

            "Then, she grabs them tightly."

            $ F019 += 1
        "Run away!":


            "Wait a minute!"
            "The other girls' effort will be in vain if I give up now."
            "I'll give it a shot!"
            "I turn around again and start running away as I think of the three girls."

            voice na0379
            namiki "Hey, hey! Wait up!!"

            $ bgfx ('black')

            "Thirty seconds later,"
            "I realize that this is useless."
            "Namiki is a sprinter."

            $ bgfx ('bg03a')
            $ char ('tna218')
            $ sfx ('SE16')

            "Namiki easily catches up with me and holds me from behind. She grabs my fake boobies, which Tomoe made especially for me."

    $ music_stop ()
    $ sfx ()
    $ char ('tna219')

    voice na0030
    namiki "...Are they fake?"
    yusuke "......"

    voice na0031
    namiki "...Are you a man?"
    yusuke "......"

    voice na0032
    namiki "......(gazing)"
    yusuke "......(sweating)"

    voice na0033
    namiki "...Yusuke?"
    yusuke "...I'm sorry."

    $ bgfx ('sora01')

    "Everything has failed."

    $ bgfx ('black')
    $ bgfx ('bg01a')
    $ char ('tna207')

    voice na0034
    namiki "...Umm."
    yusuke "......(Is she mad?)"

    voice na0035
    namiki "Umm, mmm..."
    yusuke "......(Is she really mad?)"

    $ char ('tna220')

    voice na0036
    namiki "I...envy you."
    yusuke "What?"
    "She strangles me and smiles."

    $ bgm (5)
    $ char ('tna213')

    voice na0037
    namiki "I really envy you! What a nice environment you've managed to fit yourself in!! Uh-huh!"
    yusuke "I...I can't breathe..."

    $ bgfx ('black')

    "Namiki looks happy as well as jealous when I tell her everything."
    "The three girls and the cat stare astoundingly at the 'fake brother and sister' hugging each other."
    "As soon as Namiki finishes demonstrating her love towards me, she sneaks up to Tomoe and starts entreating her."

    $ bgfx ('bg01a')
    $ char ('tna213')

    voice na0038
    namiki "Hey, Tomoe. I heard your family runs a hotel with a hot spring."

    $ char ('tto004')

    voice to0054
    tomoe "Yusuke...did you tell her that?"
    yusuke "...Umm."
    "I'm still freaked out and can't even move a muscle."

    $ char ('tna213')

    voice na0039
    namiki "Oh, how sweet! I want to go to the hot spring... May I?"

    $ char ('tto004')

    voice to0055
    tomoe "Well...yes, you may, but...I..."

    $ char ('tas006')

    voice as0185
    asumi "Yusuke. Your sister is sneaky! She must behave!"

    $ char ('tna216')

    voice na0040
    namiki "Your dormitory prohibits males, doesn't it? It'll be a big problem if you bring a boy inside, am I correct?"

    $ char ('tas040')

    voice as0186
    asumi "Moe-Moe. I beg you to invite Sis to your hot spring."

    $ char ('tna218')

    voice na0040a
    namiki "Please, Moe-Moe."

    $ char ('tas010')

    voice as0187
    asumi "You're an outsider! You can't call her Moe-Moe!"

    call blackout from _call_blackout_152

    "With a bit of coercion, we head to Tomoe's house."
    "I know Tomoe doesn't like it, but I'm forced to join them as well."
    "No one can go against Namiki because she knows our secret now."

    $ bgm (6)
    call cg_slide (picture='e3_0305', tm=2.0, kind='h', start=1.0, end=0.44, cls=diss_fast) from _call_cg_slide_18
    $ sfx ('SE15')

    voice na0041
    namiki "Whew, I had no idea Yusuke lives with these cute girls. That's fantastic!"

    voice as0188
    asumi "Good. I guess your eyes are getting better, since you admit to my beauty at least."

    voice na0042
    namiki "I'm talking about Moe-Moe and Marutan."

    $ sfx ()
    $ cg ('e3_0306', pos=[ALIGN(0.44)])

    voice as0189
    asumi "Don't call them by those names! And your eyes are awful, too!!"

    voice to0057
    tomoe "Did she say I'm pretty? Heh."
    marumu "......"
    "I can do nothing but quietly stare at them taking a bath."
    "I'm speechless as I try to make my lower-half behave."
    "Because I'm certain Asumi and Namiki will beat me to death if I lose control."
    "Tomoe shyly stays as far from me as possible."
    "Namiki sneaks up to Tomoe and snuggles up to her."

    $ cg ('e3_0307', pos=[ALIGN(0.44)])

    voice na0043
    namiki "Anyway, Tomoe is the best! Your boobies are bigger than mine."

    voice to0058
    tomoe "What are you... YAAAA!!"
    yusuke "...FOOOSH (nosebleed)"

    $ cg ('et_0106')
    $ bgm (7)
    $ unlock_gallery ('g2e7')

    "The water in front of me turns red."
    "What can I say? It's a natural reaction, and I have no way to prevent it."
    "Because I see Tomoe's titties pop out of the towel as Namiki touches them."

    voice na0044
    namiki "See? They're just as big and beautiful as I had thought. And they're soft, too."

    voice ts0015
    toshibo "Meow!!"

    $ cg ('et_0107')

    voice to0059
    tomoe "Don't look at me, please!"

    voice na0045
    namiki "Hey, don't worry about Yusuke, alright? I don't consider him a boy."

    $ cg ('et_0108')

    voice to0060
    tomoe "But...ohh!"
    "The towel around Tomoe slips down."
    "Namiki smirks and flips Tomoe's nipples."

    voice na0046
    namiki "Yusuke is cuter than that cheesy girl there when he's cross-dressed, isn't he? I don't think he'll harm you, Tomoe."

    voice as0190
    asumi "You call me cheesy!? True, Tomoe has bigger boobs, but look at mine! They aren't that bad!!"

    voice na0047
    namiki "Humph. They look okay, but they're no match to mine."
    yusuke "...WOOSH."

    $ sfx ('SE47')

    marumu "...SPLASH!"

    voice na0048
    namiki "Marutan is pretty too. However, she's not for everyone. Heh."
    yusuke "Ohhh."

    $ sfx ()

    voice na0049
    namiki "In any case, mine are best suited for Yusuke. PLUMP."
    yusuke "I...I...can't...GLUB-GLUB-GLUB."

    menu:
        " "
        "Asumi is the best.":


            yusuke "She's a bit twisted, but her boobs are well shaped. GLUB-GLUB."

            $ F016 += 1
        "Tomoe is the best.":


            yusuke "They're beautiful and big...GLUB-GLUB."

            $ F017 += 1
        "Marumu is the best.":


            yusuke "She's not for everyone, but she suits my taste for sure...GLUB-GLUB-GLUB."

            $ F018 += 1
        "Namiki is the best.":


            yusuke "I'm most familiar with those...GLUB-GLUB-GLUB."

            $ F019 += 1

    $ bgfx ('black')

    "They let me sink and continue fighting while showing off their breasts except for Tomoe."

    $ music_stop ()
    $ bgm (12)
    $ bgfx ('bg08b')
    $ char ('tna301')

    voice na0050
    namiki "Whew. It was great! I'm such a hot spring fanatic, and I must admit that this place is great. It's moderately hot, and I like that."

    $ char ('tto334')

    voice to0061
    tomoe "Well, thank you..."

    $ bgfx ('black', diss_long)
    $ bgfx ('bg03b')
    $ char ('tna202')

    voice na0051
    namiki "Okay, I've made sure Yusuke is having a wonderful life here, so I'm going back now."

    $ char ('tas037')

    voice as0191
    asumi "Yeah, yeah. Don't let the door hit you on the way out."

    $ char ('tna202')

    voice na0052
    namiki "Okay, I'll see you folks later. I'll be back!"

    $ char ('tas018')

    voice as0192
    asumi "Please, don't!!"

    $ char ('tma008')

    marumu "......"

    $ char ('tts001')

    voice ts0016
    toshibo "Meow!"

    $ char ('tna202')

    voice na0053
    namiki "Marumu and Toshibo, thank you for seeing me off. And Tomoe?"

    $ char ('tto001')

    voice to0062
    tomoe "Yes?"

    $ char ('tna218')

    voice na0054
    namiki "I kinda like you. Let's meet up sometime and get to know each other better. Heh heh."

    $ char ('tto011')

    tomoe "......"
    "Ah, poor Tomoe."
    "Yep. She's as unhappy as I am."

    $ char ('tna202')

    voice na0055
    namiki "Take it easy, Yusuke. I'll come back and check on your progress."
    yusuke "You don't need to come that often, Sis."

    voice as0193
    asumi "Please, don't ever come back, Sis!"

    $ bgfx ('sora05')

    "Namiki leaves damage like a hurricane."
    "She builds up a tense relationship between Asumi and herself."
    "She also builds up (forcibly) an intimate relationship between Tomoe and herself."
    "At this moment, I have no idea the hurricane will return to do more damage."
    "I realize it later on..."

    voice na0056
    namiki "Let's play together again. Heh heh."


    call ep_finish from _call_ep_finish_20

    $ renpy.end_replay()
    $ unlock_episode (5)
    jump episode06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label episode02:

    $ Fnum = 2
    $ save_name = "Episode 2: Transformation"

    $ bgm (6)
    $ cg ('es_0101')
    $ unlock_gallery ('g4e10')

    yusuke "...Excuse me."

    voice as0046
    asumi "Shut up and don't move!"

    $ cg ('es_0102')

    "I don't want to admit to the reality in front of my eyes."

    $ cg ('es_0103')

    "If someone I know sees this, I'll hang myself."

    $ cg ('es_0104')

    "This is simply...unbearable."

    $ cg ('es_0105')

    voice ma0008
    marutan "...Heh."

    $ cg ('es_0106')

    voice to0001
    moemoe "You look very good...with these."

    $ cg ('es_0107')

    voice as0047
    asumi "...Good, it's done. Yeah, you look really cute! In fact, someone might give you a love letter or something."

    voice to0007
    moemoe "Are you really a...boy?"
    "This girl avoided me like the plague yesterday."
    "Still, this girl Tomoe Katsuragi a.k.a. Moe-Moe, keeps some distance between me and herself."
    "I understand her feelings, of course. I'm nothing but a nuisance in the male-prohibited dormitory."
    "She jumped and stepped back every time I came close to her last night."
    "Now, she gently smiles and looks at my reflection in the mirror."
    "Moe-Moe helped me a lot in this lame 'Yusuke Costume-play Project,' which Asumi suggested, by the way."
    "On the other hand, the mysterious girl Marumu Ogumayama, a.k.a. Marutan, quietly gazes at me and does nothing."


    call ep_start from _call_ep_start_23

    $ bgm (12)
    $ bgfx ('bg01a')
    $ char ('tas001')

    "I whisper weakly as I look at the girls getting ready for school."
    yusuke "Excuse me, but...do I really need to go to school like this?"

    $ char ('tas013')

    voice as0048
    asumi "But of course! Like I told you, this Harukaze Dorm has a strict code regarding males."

    voice as0049
    asumi "If someone finds out that a guy's in here, we'll all be kicked out! You got that!?"

    $ char ('tto019')

    voice to0008
    tomoe "...You look great, Yusuke."

    $ char ('tma004')

    voice ma0065a
    marumu "......(nod)"
    "Are we talking about the same subject...?"
    "In any case,"
    "I can't escape from this cold reality."
    "I must go to Aiho School as a 'female' transfer student."

    $ bgfx ('black')
    $ bgfx ('bg05a')

    yusuke "...Ohh."
    "I can't stop sighing, even after I turn back into 'me.'"
    "As soon as I reach the school, I enter a girls' restroom with my uniform hidden in my bag."
    "Then, I switch my identity in a stall and crawl out of the restroom."
    yusuke "How long do I need to continue doing this...?"
    "Okay, I'll go to the boys' dormitory after school."
    "I'll ask the manager to let me in ASAP!"
    yusuke "What can I do...what can I do...?"

    voice as0050
    asumi "Hey, Mister transfer student!"
    yusuke "Waaaaaah!"

    call effect ('SE43', ETYPE2) from _call_effect_41

    "I fall to the ground as somebody slaps me on the back."
    "It's a powerful hit!"
    "I mean, it's severe. Not like a tap or a pat."
    "I thought my back was almost broken or something."

    $ bgm (5)
    $ char ('tas001')

    yusuke "Guhhh, it hurts... Why did you do that, Asumi!?"

    voice as0051
    asumi "It's my welcome greeting. Anyway, you know our deal about THAT, right?"
    yusuke "...What?"

    $ char ('tas036')

    voice as0052
    asumi "Are you trying to play dumb? THAT! THAT! You can stay in our room because of THAT!"
    yusuke "Ahh...yes, THAT."
    "I still can't remember what she's referring to."
    "And it's said to be Asumi's weak spot."
    "And she says I'm taking advantage of her because of THAT. The problem is I have no idea what THAT thing is."
    "Anyway, now I can sleep under a roof, thanks to THAT or whatever."

    voice as0053
    asumi "If you expose THAT to someone..."
    yusuke "Which I will not. I won't tell anyone!"
    "I can't say anything about things I don't remember."
    "Even if I were to remember, I wouldn't say a thing about it. Besides, I'm kind of scared of her."
    "After all, I am a man."
    "It's against my rules to take advantage of a girl (she is a girl, isn't she?) by blackmailing her."
    "To be honest, I want to escape from this savage beast, but for now, she's the only one I can rely upon, in this land of the unknown."
    "Otherwise, I might've dried up and died outside with all my stuff."
    "I need Asumi's help in order to survive."
    "...Why are tears welling up in my eyes? Hic-hic."

    call blackout from _call_blackout_145

    "I run away from Asumi and head to the teachers' office."
    "A charming lady with a bright smile welcomes me in the office."

    $ bgm (4)
    $ bgfx ('bg04a')
    $ char ('tyo001')

    voice yo0001
    yagami "...Okay, introduce yourself to us now!"
    yusuke "Yes. My name is Yusuke Sawada from Tokyo. Nice to meet you folks."

    $ char ('tyo007')

    voice yo0002
    yagami "Everybody, take good care of Yusuke. Okay, this is it for today's homeroom."
    "My new school life starts in Ms. Yoshiko Yagami's classroom."
    "I'm assigned a desk near the windows. Then..."

    menu:
        " "
        "Have a seat.":


            "I head to my desk right away."
            "Whew! The desk and the chair are beautiful. Yes, this is a new school for sure."
        "Go out of the room with Ms. Yagami.":


            $ bgfx ('bg05a')

            "I follow Ms. Yagami outside the classroom."
            "She shows me the bright smile again."
            "My worries quickly vanish as I see her warm, gentle smile."

            $ char ('tyo001')

            voice yo0003
            yagami "Take your time to fit in, okay? Ask me anything if you have any problems."
            yusuke "O...okay. Thank you very much."

            $ char ('tyo007')

            voice yo0004
            yagami "We'll do some paperwork after school. Today is only your first day, so take it easy, all right?"

            $ char ()

            "Wow, she's such a beautiful and kind teacher!!"
            "I start feeling lucky for coming to this school."

            $ bgfx ('bg04a')
            $ F01A += 1

    $ bgm (12)

    yusuke "This school is...unique."
    "Sure, this Aiho School is famous for its relaxed mood, but still, the school is filled with a unique atmosphere."
    "I became chummy with my classmates by noon."
    "Maybe, because the class has only twenty students."
    "It'll be easy for me to memorize the names and faces of my classmates."
    "I look around the room and see the face of a student sitting next to me."

    $ char ('tko001')

    "Our eyes meet. Oh, well...I've got to say something to him."
    yusuke "H...hi."
    kosuke "You're Yusuke, right? I'm Kosuke Fujisawa. Nice to meet you."
    yusuke "Nice to meet you too. Please tell me about things around this place. I'm new to this town, you know."
    kosuke "No problem. Why don't I show you around during break time?"

    $ char ()

    "Again, I was lucky to meet Kosuke at this moment."
    "He's easygoing and kind."
    "I'm able to quickly feel at ease at the school because of his help."
    "Later on, I greet everybody in the class."
    "Kosuke helps me to do so. I might get along well with some of my classmates."
    "However...there are at least two students who obviously avoid me in this classroom."
    "Or are they simply ignoring me?"
    "They are Moe-Moe and Marutan."

    $ char ('tas018')

    voice as0054
    asumi "You... What did you do to them?"
    yusuke "I didn't! I didn't do anything, I swear!!"
    "Asumi glares at me with suspicion."
    "Why are we all in the same class...!?"

    call blackout () from _call_blackout_146
    $ bgfx ('bg04a')

    man "Y...you live in the Kogarashi Dorm, don't you? Can I visit your place later?"
    yusuke "Th...that's...I haven't finished organizing my room and...it's messy, so..."
    man "Okay, some other day, huh?"
    "This guy, Iijima, came from Tokyo too. He's very talkative."
    "However, neither him nor Kosuke can visit my room now."
    yusuke "Ohhh, I can't invite them...hic-hic."

    $ char ('tas007')

    voice as0055
    asumi "You there! Change your uniform before you leave the school, you got that!?"
    yusuke "...Yes, ma'am."
    "My tears won't stop flowing."


    call ep_middle from _call_ep_middle_23

    $ bgm (12)
    $ bgfx ('bg01b')

    yusuke "I'm home... Phew! I'm exhausted."
    "The first day of my new school life finally ends. I come back home and head straight to my room (closet) in exhaustion."
    "But Asumi drags me out of there like a mole."

    $ char ('tas003')

    voice as0056
    asumi "Hey you! Don't rest yet. You have tons of stuff to do in here."
    yusuke "Tons of stuff? Say, where is..."
    "I don't see Tomoe in here."
    "She's head of the student union. I know she's busy."
    "Still, it doesn't make sense not to see her here."

    $ char ('tas001')

    voice as0057
    asumi "Moe-Moe went to buy some groceries. She's in charge of dinner here."
    yusuke "Oh, I see. That's awesome!"

    voice as0058
    asumi "What the hell do you mean 'Oh?' You have to work for us too!"
    yusuke "Really?"
    "I understood what she said. I just couldn't think about those rules, since I had more important things to take care of."
    "However, there's something else that really gets my attention."

    $ char ('tas015')

    voice as0059
    asumi "Huh!? Of course, you...what?"
    yusuke "...You keep calling me 'you' or 'it.'"
    "I feel bad."
    "Asumi seems to be looking for another 'title' for me now."

    $ char ('tas033')

    voice as0060
    asumi "Well then...Yusuke? Sawada? Hmm, they're both hard to pronounce."
    yusuke "What!?"

    $ char ('tas012')

    voice as0061
    asumi "Ummm...okay. Your nickname will be 'Parasite One.'"
    "She announces this all of a sudden."
    yusuke "What the heck!? I definitely prefer you to call me by my first name..."

    $ char ('tas015')

    voice as0062
    asumi "Shut up, you parasite! Now, let me tell you about your tasks in here..."
    yusuke "Ohhh..."
    "I can't take this!"
    "However, Asumi looks satisfied with her decision and changes the subject."
    "These are the responsibilities of each person in this room:"
    "Asumi and Marumu are in charge of breakfast."
    "I've been added to that rotation...even though I have no confidence in cooking at all."
    "Since Tomoe is not a morning person, she takes care of dinner instead."
    "And that's not all."
    "Dishwashing, vacuuming, garbage dumping, etc... The list goes on and on."
    "Then, she explains to me about the rules and regulations of this place."
    "She repeatedly tells me to remember that I live in a girls' dormitory, which is very strict about males being here."
    "Whatever she says, you know. I'm not planning to stay here that long."
    "I'm going to move out pretty soon..."

    $ bgm (6)

    yusuke "Oh, by the way...where's my stuff?"

    $ char ('tas027')

    voice as0063
    asumi "Oh, that... You know what? We have one great rule in here, which is: 'Your property is our property.'"
    yusuke "Haven't I heard that somewhere before...?"

    voice as0064
    asumi "Heh heh."
    yusuke "So, where's my stuff?"

    voice as0065
    asumi "Heh heh heh."
    yusuke "I said...ahhh!?"

    $ char ('tma401')

    voice ma0009
    marumu "Thank you for this."
    "Marumu shows up from nowhere and tells me this."
    "She's holding one of my gadgets. It's an automatic nutcracker called, 'New Omame-chan Deluxe.'"
    "It's a novelty item from some infomercial."

    $ char ()

    "I assume they've already spread out my belongings amongst themselves."
    "No wonder my room (closet) looks so spacious now."
    "These girls are vultures..."
    "Whatever. I don't need those things anyway."
    "However...do they have the right to do that? This is outrageous!"

    $ char ('tto001')

    voice to0009
    tomoe "I'm back. The supermarket was so crowded and...oh?"
    yusuke "...Welcome...back."

    voice to0010
    tomoe "What's wrong, Yusuke? You look somewhat depressed."
    yusuke "I'm...I'm all right."

    $ char ('tto016')

    voice to0011
    tomoe "Oh, by the way, thanks for this. This will make it easier for me to peel vegetables."
    "As she tells me this, she shows me what she has."
    "A handy vegetable peeler, 'EZ-EZ Peeler.'"
    "I like this one personally."
    "And it belongs to me."
    "Yes, I won't stay silent in this situation."

    menu:
        " "
        "Get miffed.":


            yusuke "......"

            $ char ('tto004')

            tomoe "......"
            "Tomoe's gentle smile fades away."
            "My silence makes her do that."
            "It's too late for regrets... I'm disappointed in myself."
        "Talk to Tomoe.":


            "Let me make a spiteful remark!"
            "I make up my mind and tell her,"
            yusuke "Yes, please make good use of it... Sob-sob."

            $ F017 += 1

    $ music_stop ()
    $ char ('tas001')

    voice as0066
    asumi "Uh, welcome home, Moe-Moe! We're all together now."
    "Asumi looks at us and speaks."
    "She smiles and continues as we stare at her."

    $ bgfx ('bg20a', diss_long)
    $ bgm (5)
    $ char ('tas709', diss_long)

    voice as0067
    asumi "Let's introduce ourselves to happy community life!"
    yusuke "Huh!?"

    $ char ('tto709')

    voice to0012
    tomoe "Are you...sure about that?"

    $ char ('tma608')

    voice ma0010
    marumu "...Introduction."

    $ bgfx ('bg01b')
    $ char ('tas007')

    voice as0068
    asumi "That's right! What if we need a blood transfusion and don't know each other's blood type? See?"
    yusuke "Isn't that a bit extreme...?"

    $ char ('tas015')

    "Asumi looks at me as I speak up. Her face lights up."
    "Uh-oh. She must've come up with another stupid idea. I really have a bad feeling about this."

    voice as0069
    asumi "...Hey! Why don't we have a welcome party for Yusuke?"
    yusuke "Huh? Where?"

    $ char ('tas002')

    voice as0070
    asumi "Hmm...at the usual place. Yes!"

    $ char ('tto007')

    voice to0013
    tomoe "But Asumi, I already bought the groceries for tonight."

    $ char ('tas018')

    voice as0071
    asumi "...It's ASUMIN! Well, we can use them tomorrow. Okay, let's go to Okonomidama Restaurant!"

    $ char ('tas002')

    "There's a bunch of plastic bags full of groceries inside."
    "Tomoe sighs as she gazes at the bags."
    yusuke "Asumi is so pushy..."

    $ music_stop ()
    $ bgfx ('bg03c')
    $ bgm (6)

    "Asumi takes us to a restaurant called, 'Okonomidama.'"

    "I can tell this is an okonomiyaki (Japanese style pancake) restaurant from the name and the savory smell."
    "Asumi shouts as soon as she passes through the shop curtain at the entrance."

    voice as0072
    asumi "Madam! Give me the usual stuff! Hey guys, order whatever you like. Parasite One will take care of the bill tonight."

    voice to0014
    tomoe "Parasite One... Are you talking about Yusuke?"

    voice ma0011
    marumu "...Thank you in advance."
    "This is totally unexpected. I talk back to her by saying,"
    yusuke "Why do I have to buy you girls dinner!?"

    voice as0073
    asumi "Why not? You're the one who's moving in!"
    yusuke "But you said this is a welcoming party for me..."

    voice as0074
    asumi "Oh, yeah! I welcome you!"

    voice ma0012
    marumu "...Welcome."
    "Marumu is swinging a flag. Where did that come from!?"
    "But it sure expresses her feeling of joy."
    "There's one girl who looks at me with some sadness in her eyes."
    "It's Tomoe... Her glance pierces my heart."
    yusuke "O...okay. This party is on me..."
    "A sigh."
    "We start introducing ourselves as soon as the grill starts smoking."
    "Of course, Asumi leads this party."

    $ cg ('e3_0101')
    $ unlock_gallery ('g4e11')

    $ bgm (5)

    voice as0075
    asumi "Okay, let me start this... My name is Asumi Hirota. Call me Asumin, please...especially you, Moe-Moe."
    "Asumi starts introducing herself all right. And it's extremely long."
    "I get exhausted listening to her."
    "She hasn't changed a bit since grade school."
    "She's so energetic...well, too energetic maybe. She's also self-centered."
    "Asumi speaks an awful lot and finishes her speech with a satisfied look on her face."
    "She then points the spatula in her hand at the other side of the table."

    voice as0076
    asumi "Moe-Moe, you're next!"

    $ cg ('e3_0102')

    "Tomoe throws a glance at me and shyly starts speaking."

    $ bgm (3)

    voice to0015
    tomoe "I...my name is Tomoe Katsuragi."

    $ cg ('e3_0103')

    voice as0077
    asumi "People call her Moe-Moe, okay? And her family runs a nice hotel with a natural hot spring! In fact, this hot spring is awesome."
    tomoe "......"
    "Tomoe is forced to shut her mouth."
    "Instead, Asumi enthusiastically continues to speak as if she's talking about herself."
    "Asumi introduces Tomoe... Yep, she hasn't changed a bit."
    "When Asumi finally shuts up, Tomoe makes her 'greeting of sorrow.'"

    $ cg ('e3_0104')

    voice to0016
    tomoe "Nice to meet you...Yusuke."
    yusuke "H...hi."

    $ cg ('e3_0101')

    "Asumi said Tomoe's family runs a nice, traditional hotel, and she's also in charge of the student union."
    "And there's one more thing I understand about this girl, Tomoe."
    "Beneath her gentle demeanor,"
    "I see her true feelings toward me. I'm not welcome here."
    "And I can understand why."
    "I'm nothing more than an outsider in the dorm...and there's still something more."
    "She's keeping a distance between me and herself...intentionally."
    "Asumi ignores my concerns and continues to run the event."

    voice as0078
    asumi "Okay. Marutan, you're next!"

    $ cg ('e3_0105')
    $ bgm (2)

    voice ma0013
    marumu "...Marumu Ogumayama."
    "Marumu states her full name, and suddenly, she takes a flag out of nowhere again."
    "It's a tiny flag."
    "She sticks it out to me and tells me without any emotion in her voice,"

    $ cg ('e3_0106')

    voice ma0014
    marumu "...Hi."
    "Then the silence continues..."
    yusuke "Err...is that it?"

    $ cg ('e3_0101')

    voice as0079
    asumi "Marutan is so mysterious, isn't she? You have to find out all her secrets on your own!"

    voice ma0015
    marumu "...A mystery."

    $ music_stop ()

    "I don't understand any of this."
    "Finally, it's my..."
    yusuke "O...okay, my name is..."

    $ cg ('e3_0102')

    voice as0080
    asumi "Yeah! Here comes my pork mix!"

    $ bgm (5)

    "Asumi screams as soon as I speak up."
    "Then, she starts mixing her pork bowl."

    $ cg ('e3_0107')

    voice as0081
    asumi "Hey, hey! Watch it! Marutan, is the grill hot enough?"

    voice ma0016
    marumu "...OK."
    yusuke "Ahhh!?"

    $ sfx ('SE14')

    "Marumu checks the plate's temperature as Asumi orders."
    "However, the way she checks it stuns me."
    "Marumu puts her palm on the hot plate to check the temperature!"
    "Asumi calmly watches and yells at Tomoe."

    voice as0082
    asumi "Take your time, Moe-Moe. Don't rush mixing the stuff, okay? You always screw up."
    "Our table gets busy."
    "I feel like I've been left out."
    yusuke "Please...let me introduce myself and..."

    $ cg ('e3_0108')

    voice to0017
    tomoe "It's too late now. Asumi won't let you do anything, once she starts cooking."
    yusuke "Ohhh..."
    "Asumi gives me an order as well."

    voice as0083
    asumi "You, Parasite One! Put some oil on the plate evenly! Do it!"
    yusuke "...Yes, ma'am."
    "My introduction abruptly ends like this."
    "Is this really a welcoming party for me...? It sure doesn't feel like it...sob-sob."

    call blackout from _call_blackout_147
    $ bgfx ('bg03c')
    $ char ('tas012')
    $ bgm (3)

    "Asumi looks very satisfied on our way home."

    voice as0084
    asumi "Whew, I'm so full!"

    $ char ('tma001')

    voice ma0017
    marumu "...Thank you."

    $ char ('tto001')

    voice to0018
    tomoe "Yusuke, are you okay...financially?"
    yusuke "Yeah, sure. I guess..."
    "I'm about to burst into tears."
    "I didn't have any valuable things to begin with, but they took everything away from me, anyway."
    "Furthermore, I end up paying for their dinner."
    "My wallet gets so thin the wind could blow inside of it."

    $ char ('tas001')

    voice as0085
    asumi "Oh, yeah. There's one more thing."
    "Asumi suddenly stops and faces me."
    "Does she finally remember that she skipped my introduction? However, my assumption turns out to be too optimistic."

    voice as0086
    asumi "I need to assign you, Parasite One!"
    yusuke "Assign me...for what?"
    "She gets my attention."
    "She really gets my attention."
    "I wait for Asumi's words with extreme apprehension and a little bit of expectation."

    $ char ('tas013')

    voice as0087
    asumi "I'll assign you to be our bodyguard!"

    voice ma0018
    marumu "...Oh, yeah."
    yusuke "Your...bodyguard?"

    $ char ('tas015')

    voice as0088
    asumi "Yes. It's absolutely imperative that you protect us maidens!!"
    yusuke "Is that so...?"
    "A bodyguard. It sounds cool."
    "A knight who protects three beautiful girls (even though one of them is pretty ferocious) from incoming danger!"
    "Asumi asks for my help as I fantasize."

    $ char ('tas001')

    voice as0089
    asumi "We need to ask you to do something as soon as we get back. We'll be counting on you!"

    $ char ('tma010')

    voice ma0019
    marumu "...Protect me."
    yusuke "S...sure. Let me see what I can do for you."
    "Good, they need my help. I'll do my best!"
    "No girl has ever asked me for any sort of help my whole life."

    call blackout from _call_blackout_148

    "Asumi passes me something when we return to the dorm."
    "It's a rolled up newspaper."

    $ bgm (5)
    $ bgfx ('bg01c')
    $ char ('tas044')

    voice as0090
    asumi "I saw three yesterday. Kill them."
    yusuke "...Yes, ma'am."

    $ char ('tto007')

    voice to0019
    tomoe "I appreciate it, Yusuke."
    "The first duty as a knight in shining armor is...to exterminate roaches."
    "The girls say they saw a huge one a couple of days ago."
    "They don't like roaches."
    "Well...most people don't really like them."
    "I desperately chase the roaches around with emptiness in my heart."
    "Am I doing okay...? I really hope so."


    call ep_finish from _call_ep_finish_19

    $ renpy.end_replay()
    $ unlock_episode (2)
    jump episode03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

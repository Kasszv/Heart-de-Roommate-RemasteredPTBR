label episode17_tomoe:

    $ bgfx ('sora02')

    "One fine weekend."
    "The weather is so nice and I oversleep."
    "When I get up, only Tomoe is here."

    $ bgm (3)
    $ bgfx ('bg01a')

    yusuke "Where's Marutan and Asumin?"

    $ char ('tto102')

    voice to0554
    tomoe "I don't know where they are."
    "While we were sleeping, they went out."
    "Tomoe usually sleeps until noon on weekends."
    "She's really grouchy in the morning."
    "If she doesn't go out, just the two of us will be here today."
    "I ask Tomoe with expectation,"
    yusuke "What are your plans for today?"

    voice to0555
    tomoe "Me? I'm thinking about going home."
    yusuke "Is that so..."
    "My dreams are completely shattered."
    "She'll go out as well."
    "Then, I'll stay here alone...I feel lonely."
    "As I sit there depressed, she asks me,"

    $ char ('tto113')

    voice to0556
    tomoe "Uh...Yusuke."
    yusuke "Yes, what?"

    voice to0557
    tomoe "If you'd like...would you go with me?"
    yusuke "Where?"

    $ char ('tto134')

    voice to0558
    tomoe "To my house..."

    $ music_stop ()
    $ bgfx ('sora02')

    "I never expected this!"
    "I agree to go to the Hotel Katsuragi with her."
    "A wonderful, significant weekend begins..."


    call ep_start from _call_ep_start_20

    $ bgm (13)
    $ bgfx ('bg03a')
    $ char ('tto225')

    "We're walking on the promenade in the warm autumn sunshine, side by side."
    "To the Hotel Katsuragi."
    yusuke "We hardly have opportunities to walk together like this, don't you think?"

    voice to0559
    tomoe "I don't think so. We often go shopping together."
    yusuke "Oh, that's..."
    "Actually, she's right."
    "I go shopping with her lately."
    "Smiling, she holds my arm."

    $ char ('tto219')

    voice to0560
    tomoe "This is like a date."
    yusuke "Don't say 'like'...it is a date."

    voice to0561
    tomoe "Yeah, you're right. Heh heh."
    "I can't stop smiling. I'm in such a good mood."
    "We take a detour in town."

    call blackout from _call_blackout_129
    $ bgfx ('bg16a')
    $ char ('ttm001')

    "A beautiful woman is cleaning out in front of the hotel."
    "She's Tomoe's sister."

    $ char ('tto225')

    voice to0562
    tomoe "I'm home, Sis."

    $ char ('ttm001')

    voice ta0020
    tomomi "Welcome back Tomoe...and hello, Yusuke."
    yusuke "How are you? Oh?"
    "Something is touching my leg."
    "As I look down, I find a chubby round thing."

    $ bgm (5)
    $ char ('tts002')

    voice ts0060
    toshibo "Meow!"
    yusuke "Yo, Toshibo! It's been a long time."

    voice to0563
    tomoe "You came home too. How are you?"

    voice ts0061
    toshibo "Meow! Mew, mew, meoooww!"

    $ char ('tto216')

    voice to0564
    tomoe "That's good for you!"
    yusuke "(I have no idea what they're talking about.)"
    "2 mysterious people...no a girl and a cat."
    "Toshibo makes us even happier."

    $ char ('ttm003')

    "However, Tomoe's sister looks serious."

    $ music_stop ()
    $ char ('tto231')

    voice to0565
    tomoe "Sis...?"

    $ char ('ttm001')

    voice ta0021
    tomomi "What? Is something wrong, Tomoe?"

    $ char ('tto213')

    voice to0566
    tomoe "What's wrong with YOU? You're in a daze."

    $ char ('ttm003')

    voice ta0022
    tomomi "Really? I guess I'm just a bit tired."
    "Worried about her sister, Tomoe continues to talk."
    "The reason Tomoe comes home is,"
    "To have a family meeting."

    $ char ('tto213')

    voice to0567
    tomoe "What are we going to talk about? How long will it take?"

    $ char ('ttm003')

    voice ta0023
    tomomi "I don't know..."

    $ char ('tto204')

    "Tomoe sadly looks at me."
    "She senses it won't be over for a while."
    "I need to spend time alone today."
    yusuke "Ah...I'll take a walk, then."

    voice to0568
    tomoe "Yusuke..."
    "She's sorry for me."
    "Toshibo tries to say something to her."

    $ char ('tts002')

    voice ts0062
    toshibo "Meow, meow!"

    $ char ('tto204')

    voice to0569
    tomoe "All right. Thanks Toshibo."
    yusuke "What did he say?"

    $ char ('tto225')

    voice to0570
    tomoe "Toshibo will give you a tour. Take care of him, Yusuke."
    yusuke "O...okay."

    $ char ('ttm003')

    voice ta0023a
    tomomi "Sorry, Yusuke."

    $ char ()

    "Tomoe and her sister disappear into the hotel."
    "After I see them off, I take a walk with Toshibo."

    $ bgfx ('black')
    $ bgm (6)
    $ bgfx ('sora02')

    voice ts0063
    toshibo "Meow, mew, mew, meow!"
    yusuke "Okay, okay..."

    voice ts0064
    toshibo "Meoow, meow! Mew?"
    yusuke "All right, all right..."
    "Toshibo explains everything to me."
    "Enthusiastically."
    "But the sad thing is I don't understand at all."
    "I buy some flavored boiled eggs for him as my appreciation."

    $ bgfx ('bg16a')
    $ music_stop ()

    yusuke "It was kind of weird with just the 2 of us, but thanks anyway, Toshibo."

    $ char ('tts002')

    voice ts0007
    toshibo "Meow!"
    yusuke "I wish I could take a walk with Tomoe..."

    $ char ('tta001')

    man "Tomoe...?"
    yusuke "......??"

    $ char ()

    "I meet a guy's gaze who passes by."
    "A handsome man with sharp eyes."
    "He looks at me as well, I guess."
    yusuke "Has he fallen in love with me too? Nah!"

    $ char ('tts004')

    toshibo "......"
    yusuke "Sorry..."

    $ char ()

    "I'm not wearing girls' clothes now."
    "If he's really fallen in love with me...oh no, I don't want to think about it!"
    "Tomoe might like it...she has a fantasy."

    $ bgfx ('sora08', diss_long)
    $ bgm (8)

    "Night falls on the town."
    "When I return to the hotel, Tomoe is waiting for me at the gate."
    "She looks serious like her sister."

    $ bgfx ('bg16c')
    $ char ('tto204')

    voice to0572
    tomoe "Sorry, Yusuke."
    yusuke "What's wrong, Tomoe?"
    tomoe "......"
    "She looks sorry."
    "She tells me she'll stay home tonight."
    "The family meeting will continue this evening."
    "From her gloomy face, they're talking about something really serious."
    "Or are things going to get more complicated...?"
    "I want to know what's going on, but I can't intervene in her family matters."
    "I should go back to the dorm alone."
    "I had a date with Toshibo, not with Tomoe...I had an interesting weekend."
    yusuke "Well, I'll go back to the dorm."

    voice to0573
    tomoe "I'm so sorry, Yusuke."
    yusuke "Never mind. Take care..."

    $ music_stop ()

    "Someone calls out of me."

    $ char ('ttm001')

    voice ta0024
    tomomi "Wait a minute, Yusuke."
    yusuke "Y...yes?"

    voice ta0025
    tomomi "If you'd like, why don't you stay here tonight?"
    "Her sudden suggestion makes us look at each other."
    "Looking at us, she's smiling."


    call ep_middle from _call_ep_middle_21

    $ bgfx ('sora08')
    $ sfx ('SE15')

    "I end up staying at the Hotel Katsuragi."

    $ sfx ()

    "Before dinner, I take a bath."
    "This hot spring makes me so relaxed."
    "The temperature is perfect and it smells good."
    "I wonder if the reason Tomoe's skin smells so good is because she takes a bath everyday..."
    yusuke "What am I thinking?"
    "I push my stupid thoughts away and think about her."
    "She looked so gloomy...what's happening in her house?"
    "Suddenly, the door opens."
    "As I look back, the shadow of a person comes towards me."
    "I recall the first night we became intimate."
    "Is that her...!?"

    $ bgm (3)
    $ bgfx ('bg08c')
    $ char ('ttm001')

    voice ta0026
    tomomi "Good evening."
    yusuke "It's Tomoe's sister..."

    $ char ('ttm002')

    voice ta0027
    tomomi "Sorry, I'm not Tomoe, heh heh."
    "Tomoe's sister walks in the bathroom."
    "She calmly smiles, as if she knows what I'm thinking."

    $ char ('ttm001')

    tomomi "......"
    yusuke "What can I do for you?"
    "She's been looking at me for a while."
    "My blood rushes to my head, but I can't get out of the tub."
    "Then she murmurs,"

    $ char ('ttm002')

    voice ta0028
    tomomi "I was worried a little...but it's all right."
    yusuke "???"

    $ char ('ttm001')

    voice ta0029
    tomomi "Your dinner will be served in the 'Lobster Hall' on the second floor."
    yusuke "Thank you so much..."

    $ char ()

    "Then she leaves the bathroom."
    "I jump out of the tub."
    "However, she comes back and tells me,"

    $ char ('ttm001')

    voice ta0030
    tomomi "Tomoe already took a bath, so she won't come."
    yusuke "I...I wasn't expecting her..."

    $ char ('ttm002')

    voice ta0031
    tomomi "Get out of the tub before you get dizzy, heh heh."
    yusuke "Err..."
    "I already feel dizzy..."

    $ char ()

    "She leaves the bathroom at last."
    "I heave a sigh of relief."

    call blackout from _call_blackout_130

    "I feel tired because I walked around the town with Toshibo."
    "I go back to my room and hit the sack right away."
    "The futon is so comfortable."
    "But I have a nightmare about being smashed by something."
    "Disturbed by the bad dream, I cry out in my dream."
    "I find a big round thing on the futon next morning."

    $ bgm (5)
    $ bgfx ('sora01')

    yusuke "That was...YOU!!"
    "Toshibo is sleeping on top of me."
    "He brought the nightmare to me last night."
    "I'm grouchy when I wake up, but breakfast makes me happy."
    "Seaweed, eggs, beans, miso soup and rice...I love Japanese breakfasts."
    "On the other hand, Tomoe looks sleepy."
    "I'm worried about her."
    "But I can't interfere in their affairs."
    "There is nothing I can do."

    $ music_stop ()
    $ bgfx ('bg16a')

    "After breakfast, Tomoe and I leave the hotel."
    "She told me the meeting's over."

    $ bgm (13)
    $ char ('tto225')

    voice to0574
    tomoe "Bye, Sis."
    yusuke "Thank you for taking care of me."

    $ char ('ttm001')

    voice ta0032
    tomomi "Visit us anytime, Yusuke. Oh, one more thing."
    yusuke "Yes?"

    $ char ('ttm002')

    "Tomoe's sister shows me the same smile she gave me in the bathroom."
    "She says,"

    voice ta0033
    tomomi "Please take care of Tomoe. She's still a child."
    yusuke "Y...yes."

    $ char ('tto213')

    voice to0575
    tomoe "Hey! Sis!"

    $ chars ('tto213', 'ttm002')

    "Tomoe's sister is chuckling."
    "Tomoe is complaining to her with a beet-red face."
    "Does she know Tomoe and I are a couple?"
    "I guess it's obvious."
    "They're happily arguing."
    "The only thing I can do is just watch them with mixed feelings of embarrassment and joy."

    call blackout from _call_blackout_131
    $ bgm (12)
    $ bgfx ('sora01')

    "Tomoe and I are slowly walking to the Harukaze Dorm."
    "Toshibo is with us."
    "Does he want to visit the other girls?"
    "I look up at the blue sky."
    yusuke "Umm...we'll be at the dorm before noon."

    voice to0576
    tomoe "I guess so..."
    "When we left, she had a parcel wrapped in cloth."
    "It looked heavy, so I asked her if she wanted me to carry it, but she declined my offer."
    "I want to know what's inside."
    "I take the plunge and ask her."

    $ bgfx ('bg03a')
    $ char ('tto225')

    yusuke "Uh...Tomoe, what's inside?"

    $ char ('tto234')

    voice to0577
    tomoe "This? This is...err..."
    yusuke "......?"

    voice to0578
    tomoe "Lunch boxes..."
    yusuke "Lunch...?"
    "She hesitantly tells me."
    "If we go back to the dorm and eat lunch, she doesn't need to carry lunch boxes."
    "She's carrying these lunch boxes for a purpose."
    "I guess she's trying to make up for yesterday."
    "If so, I'm delighted."
    yusuke "It's really a nice day today."

    $ char ('tto201')

    voice to0579
    tomoe "Yes..."
    yusuke "We aren't in a hurry, and you have some lunch boxes..."
    tomoe "......"
    yusuke "How about a picnic?"

    $ char ('tto225')

    "She smiles all over when she hears this."
    "Toshibo suddenly jumps in front of her."

    $ char ('tts004')

    voice ts0065
    toshibo "Meow, meow, meow!!"

    $ char ('tto210')

    voice to0580
    tomoe "He said it's a great idea...heh heh."
    "Toshibo looks so happy, ready to fly at the lunch boxes."
    "Tomoe and I look at each other and smile."
    "This is how we end up having a picnic at a park on the hill."

    call blackout from _call_blackout_132
    $ bgfx ('sora01')

    "The park is big and a perfect place for a picnic."
    "It has a nice view with many trees."
    "On top of that..."

    $ bgm (3)
    $ bgfx ('bg14a')

    yusuke "Wow, it's big."

    $ char ('tts004')

    voice ts0066
    toshibo "Meow!"

    $ char ('tto225')

    voice to0581
    tomoe "The breeze feels good."
    "Her long hair is floating in the air."
    "I'm fascinated with her beauty."

    $ char ('tto234')

    "She notices and looks at me shyly."
    "I'm startled and tell her in a fluster,"
    yusuke "We need this kind of relaxed time."

    $ char ('tto210')

    voice to0582
    tomoe "You always take it easy."
    yusuke "I don't think so. That's YOU."

    $ char ('tto225')

    voice to0583
    tomoe "You're right. He he."
    "Smiling, she moves closer to me."

    voice to0584
    tomoe "We both like being relaxed...then, let's be relaxed."
    yusuke "Yeah, together..."

    $ char ('tts001')

    voice ts0066a
    toshibo "Meow..."
    "Toshibo is clinging on our legs. He wants food."
    "Looking at him, we giggle."
    "We sit in the sun and start eating."

    $ bgfx ('sora02')

    "The lunch she made looks great in the fancy lunch boxes."
    "And there's a lot; even Toshibo is satisfied."
    "Toshibo and I enjoy eating the food while Toshibo happily looks at us."
    "We have more than enough."

    $ bgfx ('bg14a')
    $ char ('tto201')

    yusuke "Whew...it was good! Thank you. When did you make it?"

    voice to0586
    tomoe "I got up a little early..."
    yusuke "You already planned this, didn't you?"

    $ char ('tto202')

    voice to0587
    tomoe "Yes..."
    yusuke "......"
    "She shyly nods."
    "I hold her shoulder."
    "And she leans on me."
    "We look like the perfect couple."
    "Then, Toshibo taps me on the back."

    $ char ('tts004')

    voice ts0067
    toshibo "Meow!"
    yusuke "......?"
    "What does he want to say? Oh, maybe...!?"
    "I think I understand what he wants to say for the first time."
    "'Good luck, you two!'"
    "I think he said that."
    "I feel friendship from him."

    $ bgfx ('sora01')

    "Sitting side by side...Tomoe and I look up at the sky."
    "I happen to think about yesterday."
    "Her family meeting."
    "I have pent-up feelings since yesterday."
    "After considering it for a while, I ask her anyway,"

    $ bgfx ('bg14a')
    $ char ('tto201')

    yusuke "Tomoe..."

    voice to0588
    tomoe "Yeah?"
    yusuke "Was the meeting about something serious?"

    $ char ('tto204')

    tomoe "......"
    "I immediately understand it's serious."
    "Is it related to the hotel's financial difficulties she mentioned before?"
    "I make her uncomfortable."
    yusuke "I...I'm sorry. It's none of my business."

    voice to0589
    tomoe "What would you do?"
    yusuke "What do you mean?"

    $ char ('tto213')

    voice to0590
    tomoe "Which is more important, yourself or your family?"
    yusuke "......"
    "She asks me the question with a gloomy face."
    "It's not easy to answer."
    "I'm at a loss for an answer."
    "She apologizes as she looks at my face."

    $ char ('tto204')

    voice to0591
    tomoe "I'm sorry I asked you such a strange question."
    yusuke "No, it's not strange..."
    "Silence reigns between us."
    "She's worried about something that has to do with choosing between herself and her family."
    "I try to say something to her."
    "Using my own words..."
    yusuke "I think..."

    $ char ('tto201')

    voice to0592
    tomoe "What?"
    yusuke "If there are two important things, and you have to chose one of them..."
    tomoe "......"
    yusuke "If both are equally important to you, then take care of them equally."

    $ char ('tto202')

    voice to0593
    tomoe "Yusuke..."
    "Surprised, she stares at me."
    yusuke "Maybe it's hard or even impossible..."

    $ char ('tto225')

    voice to0594
    tomoe "It's so you, Yusuke."
    yusuke "Do you think so?"
    "I'm suddenly happy."
    "But it's just for a moment."

    $ char ('tto219')

    voice to0595
    tomoe "You're the king of indecision."
    yusuke "Are you praising me or making fun of me?"

    voice to0596
    tomoe "Heh-heh. Take a guess."

    $ char ('tto225')

    voice to0597
    tomoe "I feel a little bit better."
    "I still think about what she said about me, but it's okay."
    "Her serious look softens."
    yusuke "Tomoe..."

    voice to0598
    tomoe "Thank you, Yusuke."
    "She smiles all over."

    $ char ('tto511')

    "She suddenly brings her face close to me."

    $ char ('tto512')

    "Then she kisses me."
    "I feel her appreciation and affection from her kiss."

    $ char ('tto234')

    yusuke "......"
    tomoe "......"
    "After the kiss, we passionately look at each other."
    "She instantly blushes."
    "I quietly look at her."
    "Time peacefully glides with us."

    call blackout from _call_blackout_133
    $ bgm (10)
    $ bgfx ('bg12b')
    $ char ('tto225')

    tomoe "......"
    yusuke "......"
    "We hold hands on the way back to the dorm."
    "I feel her warmth through my hand, and it feels good."
    "I had a wonderful date."
    "She suddenly stops near the dorm."

    $ char ('tto213')

    voice to0599
    tomoe "Oops...!"
    yusuke "What's wrong?"

    $ char ('tto201')

    voice to0600
    tomoe "I have to go to the grocery store for dinner!"
    yusuke "Ha ha..."
    "I'm pulled back to reality and feel deflated."
    "That's Tomoe, but I like her."
    yusuke "Then, let's go together!"

    $ char ('tto219')

    voice to0601
    tomoe "Yeah!"
    "Still holding hands, we head to the store."

    call blackout from _call_blackout_134

    "The sun almost sinks below the horizon."
    "After shopping, we return to the dorm."
    "Asumi and Marumu are waiting for us with strange looks."

    $ bgm (6)
    $ bgfx ('bg01c')
    $ char ('tto225')

    voice to0602
    tomoe "We're home... I'll make dinner right away."

    $ char ('tas105')

    voice as0982
    asumi "Welcome back. Oh, Yusuke is with you."
    yusuke "Hi, girls..."

    $ char ('tas137')

    voice as0983
    asumi "I can't believe what young people are doing nowadays..."
    "Asumi accuses us like an old woman and I talk back to her."
    yusuke "You're misunderstanding, Asumi."

    $ char ('tma216')

    voice ma0236
    marumu "You stayed out overnight."
    "They act very strange!"
    "They know about our intimate relationship and tease us."

    $ char ('tas137')

    voice as0984
    asumi "Ah, it's hot in here... Please make dinner, Tomoe."

    $ char ('tma117')

    voice ma0237
    marumu "We're waiting."

    $ char ('tto210')

    voice to0603
    tomoe "O...okay."
    yusuke "What's that...?"
    "Drinking green tea, they talk like mothers-in law."
    "Where did they get the information that Tomoe and I are dating?"
    "Did Namiki tell them!?"

    $ music_stop ()
    $ bgfx ('sora08')

    "After dinner, Tomoe takes me outside."
    "And she tells me some shocking news."
    "She told them we're dating."

    $ bgfx ('bg02c')
    $ bgm (3)
    $ char ('tto234')

    yusuke "What? Seriously?"

    voice to0604
    tomoe "Seriously, yes..."
    yusuke "How come...?"

    voice to0605
    tomoe "Well...ah...it's kind of complicated."
    "She mumbles out an excuse."
    "She's not the type of girl who proudly tells people she has a boyfriend."
    "While we're talking, Asumi and Marumu walk up to us."

    $ char ('tas112')

    voice as0985
    asumi "We'll leave you guys alone!"

    $ char ('tma117')

    voice ma0238
    marumu "Good luck..."
    yusuke "Oh, geeze..."
    "I'll bet they make fun of us for a while."
    "Thinking about it, I get depressed."
    "Poor me..."

    jump episode17_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label episode20_tomoe:

    $ bgfx ('sora08')

    "Tomoe comes back and tells us the shocking news."
    "It's especially shocking to me."

    $ bgfx ('bg01c')
    $ char ('tto204')

    voice as0694
    everyone "An arranged marriage meeting?"

    voice to0623
    tomoe "Y...yeah...I'll meet the guy...next week."

    $ empat ('SE49')

    yusuke "But...why...?"
    "She has me, right?"
    "How could she do this to me!?"
    "Then, what am I?"
    "Without noticing my depression, Asumi and Marumu merrily start talking."

    $ empat ()
    $ char ('tas105')
    $ bgm (7)

    voice as0695
    asumi "I envy you! I want to have one too. You can eat good food and dress up."

    $ char ('tma108')

    voice ma0141
    marumu "It sounds fun."

    $ char ('tto213')

    voice to0624
    tomoe "It's not fun! I...I..."

    $ music_stop ()
    $ char ('tto207')
    $ char ()
    $ bgm (9)

    "Tomoe rushes into her room crying."
    "And she doesn't come out."
    "Asumi and Marumu look at each other."
    "They know Tomoe and I are a couple."
    "Tomoe is the kind of girl who always has faith in her boyfriend."
    "All of us know her well."
    "Tomoe will have an arranged marriage meeting."
    "We love each other."
    "Right, Tomoe?"

    call blackout from _call_blackout_169
    $ bgfx ('sora09')

    "I can't sleep."
    "I think about Tomoe and the arranged meeting over and over again."
    "As I suffer in mental anguish, I sense someone next to the door."

    $ bgfx ('bg01d')

    "I slowly open it and peep out."
    "Tomoe is standing there."
    "She doesn't notice me and goes outside."
    "Feeling agitated, I follow her."

    $ bgfx ('black')

    "She looks up at the night sky in the cold air."
    "I call out to her,"

    $ bgm (8)
    $ bgfx ('bg02c')

    yusuke "Tomoe..."

    $ char ('tto204')

    voice to0625
    tomoe "Yusuke..."
    "Surprised, she looks back at me."

    $ char ('tto207')

    "She looks ready to cry."
    "Before I can say anything, she throws herself at me."

    voice to0626
    tomoe "Sorry, Yusuke...I'm sorry."
    "Her tears soak my shirt."
    "She looks so vulnerable."
    yusuke "Don't apologize...but what happened?"

    voice to0627
    tomoe "Sorry..."
    yusuke "......"

    $ bgfx ('sora09')

    "She continues to apologize."
    "I don't know what to do unless she explains the reason."
    "Though I'm frustrated, I stroke her head."
    "Until she stops crying."

    $ bgfx ('black')
    $ bgfx ('bg02c')
    $ char ('tto204')
    $ bgm (9)

    "After a while, she calms down and sadly tells me,"

    voice to0628
    tomoe "Do you remember what you said to me the other day?"
    yusuke "The other day?"

    voice to0629
    tomoe "When we went on the picnic, you said, 'If both are equally important to you, then take care of them equally.'"
    yusuke "Y...yeah."
    "Of course I remember."
    "Those were my true feelings."
    "However, my words make her suffer."

    voice to0630
    tomoe "But I can't do that...I just can't."
    yusuke "Tomoe..."

    $ char ('tto207')

    voice to0631
    tomoe "That's why...I'm sorry."

    $ char ()

    "She turns around and runs away."
    "It happens so suddenly, I can't hold on to her."
    "I go back inside the dorm and vacantly look at her."
    "She's worried about her family and herself."
    "I don't know what it is."
    "Because she didn't tell me the details."
    "However, it concerns the arranged meeting."
    "I'm sure of that."

    call blackout from _call_blackout_170

    "The next day."
    "Asumi, Marumu and I are heading to the Hotel Katsuragi."
    "Because we care about her."

    jump episode20_b

label episode20_tomoe_b:

    $ bgfx ('bg03a')

    "We feel her anger."

    $ bgm (5)
    $ chars ('tas210', 'tma201')

    voice as0700
    asumi "How could he say that? I'll never, ever forgive him!!"

    voice ma0143
    marumu "Liquidation..."
    "I'm surrounded by severe rage."

    $ char ('tas236')

    voice as0701
    asumi "He's a typical devil!"
    yusuke "Yeah, I agree with you, but..."

    $ char ('tas201')

    voice as0702
    asumi "But what?"
    yusuke "Tomoe feels the hotel is more important than herself..."

    $ char ('tas210')

    voice as0703
    asumi "No way! You're so naive!!"
    "Holding her fist up to the sky, she declares,"

    $ char ('tas206')

    voice as0704
    asumi "Sacrificing herself for her family...that's not right!"

    $ char ('tma201')

    voice ma0144
    marumu "Liquidation..."
    "Asumi and Marumu hold hands."
    "They grab my hands and form a circle."

    $ bgfx ('sora01')

    voice as0705
    asumi "We'll ruin Moe-Moe's arranged marriage meeting!"

    voice ma0145
    marumu "Yeah!"
    yusuke "Are we right to do such a thing...?"

    voice as0991
    asumi "Hey, you're the one who should stand up to this!"

    voice ma0239
    marumu "You're Moe-Moe's boyfriend."
    yusuke "Y...yeah."
    "I know they're right, but I'm not sure if I can ruin the meeting."

    call blackout from _call_blackout_171

    "The night before the arranged marriage meeting."
    "I hesitantly knock on Tomoe's door."

    $ sfx ('SE44')
    $ wait (0.5)
    $ bgfx ('bg01d')

    voice to0632
    tomoe "Who is it?"

    $ sfx ()

    yusuke "It's me..."
    tomoe "......"
    "She won't come out."
    "Silence remains between us."
    "I want to talk to her."
    "Just before I give up, the door slowly opens."
    "She looks depressed. I've never seen her like this before."
    "Still, she comes out of her room."

    $ bgm (9)
    $ char ('tto204')

    tomoe "......"
    yusuke "......"

    voice to0633
    tomoe "Sorry, Yusuke..."
    yusuke "Why are you apologizing? I know you have a reason."
    "I know the reason."
    "That's why I don't want her to apologize to me."
    "However, she tells me with a tear-filled voice,"

    $ char ('tto213')

    voice to0634
    tomoe "Talking to you just before the meeting really hurts!"
    "She turns around and tries to go back to her room."
    "But I grab her arm and tell her,"
    yusuke "I know the reason. Your sister told me about it."

    $ char ('tto207')

    voice to0635
    tomoe "What...?"
    "She suddenly stops."
    "She's astonished that I know."

    $ char ('tto204')

    "She tells me gloomily but clearly,"

    voice to0636
    tomoe "I can't be selfish. I can't think of myself first."
    yusuke "Tomoe, you're wrong. You're not selfish thinking like that."

    $ char ('tto213')

    voice to0637
    tomoe "No! Discarding the hotel that my sister, father, and grandpa take care of is selfish!"
    yusuke "......"
    "I want to talk back to her."
    "However, I don't say anything."
    "The hotel is precious to her."
    "She would sacrifice herself for the hotel."
    "She also cares about me."

    $ char ('tto204')

    voice to0638
    tomoe "My meeting someone else must seem selfish to you."
    yusuke "But that's..."

    voice to0639
    tomoe "Sorry, Yusuke. I'm sorry."
    yusuke "Please, don't apologize anymore."
    "She doesn't need to torture herself."
    "I understand her painful feelings."
    "But I can't tell her."

    $ char ('tto207')

    voice to0640
    tomoe "Ugh....hic...mmm."
    yusuke "Don't cry...please."

    $ bgfx ('sora08')

    "She sobs on my chest."
    "Holding her, I secretly decide something."
    "I'll join the other girls and ruin the arranged meeting!"
    "The hotel is important, but I can't let her have the meeting."
    "I'll do it, even though she'll get pissed off or even hate me."
    "This is my selfishness."

    jump episode20_c

label episode20_tomoe_c:

    "All our plans failed."
    "Takuto walks toward the entrance."
    "Asumi and Marumu are bewildered."
    "But I haven't given up yet."

    $ bgfx ('bg16a')
    $ char ('tas243')

    voice as0992
    asumi "What shall we do now?"

    $ char ('tma201')

    voice ma0240
    marumu "Yusuke, where are you going?"
    yusuke "......"
    "I unconsciously walk up to him."
    "And I stand in front of him."

    $ char ('tta001')
    $ bgm (16)

    man "Hey, I remember you...what's wrong? Whaaa!?"

    $ char ('tta002')

    "I take my wig off."
    "Then I throw it against him, as if challenging him to a duel."
    yusuke "I won't let you go inside!"
    man "Who are you? I'm not interested in boys, though you're pretty cute."
    yusuke "Neither am I!"
    man "Then get out of my way!"
    yusuke "Hell no! I'll never move!"

    voice as0993
    asumi "Wow, Yusuke's different today."

    voice ma0241
    marumu "It's the power of love."
    "Takuto's face turns red."
    "He looks really mad."
    man "I said get the hell out of my way! If you continue bothering me, I'll force you to leave."
    yusuke "Go ahead! Bring it on!"
    "I inwardly suppress my fear."
    "If I let him go, there's nothing more we can do."
    "This is the last option."

    $ bgfx ('black')
    $ music_stop ()
    $ bgfx ('bg16a')
    $ char ('tas242')
    $ empat ('j7')

    voice as0994
    asumi "Yusuke..."
    "Asumi's cheerful voice changes to worry."
    "After all, I'm not a fighter."
    "I try to stand up, and Takuto tells me irritated,"

    $ empat ()
    $ bgm (9)
    $ char ('tta002')

    takuto "Don't push yourself so hard. I know you have your reasons, but don't give me problems!"
    yusuke "YOU'RE giving Tomoe problems!"
    takuto "I don't think so. She agreed to the meeting. I didn't force her to accept this!"
    "He doesn't get it."
    "I definitely need to stop him."
    yusuke "Tomoe isn't willingly doing this. She's doing it to protect the hotel!"
    takuto "To protect that hotel? Even though she's kind and gentle, she wouldn't go that far."
    yusuke "But that's her! She always thinks about others first!"
    "I don't want to let him have Tomoe."
    "He's annoyed at my words."
    takuto "Shut up! Tomoe still loves me!!"

    $ music_stop ()

    "He suddenly becomes quiet."
    "Not only him, but Asumi, Marumu and I also see the girl."
    "All of us clam up."

    $ char ('tto204')

    yusuke "Tomoe..."

    $ char ('tto213')

    voice to0641
    tomoe "Takuto... Yusuke!"
    "I sit down on the ground with bruises and scratches. She's surprised looking at me."
    "She runs up to me."

    $ char ('tto207')

    "Then she helps me up and puts her handkerchief on my wounds."
    "Being ignored, Takuto gets mad and tells her in an angry voice,"

    $ char ('tta002')

    takuto "Tomoe, is that true? Did you accept it just to protect that old hotel?"

    $ char ('tto204')

    tomoe "......"

    $ char ('tta002')

    takuto "Say something! You still love me, right? That's why you agreed to have the arranged meeting."

    $ char ('tto204')

    voice to0642
    tomoe "I can't forget..."
    "She whispers in a soft voice."
    "Takuto smirks listening to her."
    takuto "Did you guys hear what she said?"
    "However, Takuto and the rest of us are misunderstanding her meaning."

    $ bgm (9)
    $ char ('tto213')

    voice to0643
    tomoe "I want to forget, but I can't! You hurt me so much!"
    takuto "Tomoe..."
    "She holds me tight."
    "And she fiercely glares at him."

    $ char ('tto251')

    "I want to say something to her, but I can't find the words."
    "Mixed emotions are swirling in her."
    "Soon, they change to the courage to tell the truth."

    voice to0644
    tomoe "I'm finally over it."

    voice to0645
    tomoe "Because I met Asumi, Marumu and him."
    takuto "What are you saying? Don't tell me you love him more than me..."
    tomoe "......"
    "She doesn't reply to his question."
    "Yet her serious look gives him her answer."
    takuto "Are you serious? Did you do this for the hotel? Don't you still have some feelings for me?"

    $ char ('tto213')

    voice to0646
    tomoe "No...I don't love you anymore."
    yusuke "Tomoe..."
    "Tomoe finally tells him the truth with a sad, sorrowful face."
    "Tomoe's sister comes out of the hotel and tells him,"

    $ music_stop ()
    $ char ('ttm004')

    voice ta0034
    tomomi "Please cancel the arranged marriage meeting. Please."
    takuto "No way!!"

    $ char ('ttm003')

    voice ta0035
    tomomi "Please..."
    "Bowing to him deeply, she apologizes."
    "Politely, she suppresses her anger."
    "He clenches his fist and yells at her."

    $ char ('tta002')

    takuto "Forget about the loan! We won't finance your hotel."

    $ char ('ttm003')

    voice ta0036
    tomomi "That's okay. We'll take care of our own problems."

    $ char ('tto204')

    voice to0647
    tomoe "Tomomi..."
    "We now know her sister's name."
    "Tomomi holds her little sister."
    "She holds her, as if telling Tomoe that she doesn't have to worry about the hotel."
    "Takuto looks away and then turns back."

    $ char ('tta002')

    takuto "Fine! Do whatever you want! I won't help you!"

    $ char ()

    "Then he walks away."
    "Looking at his back, I loosen up."
    "I feel relaxed, but I hurt and am suddenly very tired."

    $ bg ('bg16a')
    $ char ('tas212')
    $ bgm (10)

    voice as0995
    asumi "Umm, you didn't look very cool, but you won!"

    $ char ('tma222')

    voice ma0242
    marumu "Victory."
    "Asumi and Marumu shout for joy."
    "I fought for her alone, though I didn't look cool..."

    $ char ('tto225')

    "Tomoe holds me tight again."

    voice to0648
    tomoe "Yusuke, thank you."
    yusuke "......"

    $ char ('tto213')

    voice to0649
    tomoe "Yusuke? Yusuke!"

    $ bgfx ('black')

    "I'm exhausted in her arms."
    "And I pass out."

    $ music_stop ()
    $ bgfx ('sora05')

    "A few days later."
    "Tomoe is holding many books in her arms, and as usual, walks to the library."

    $ bgfx ('bg05b')
    $ char ('tto025')
    $ bgm (3)

    yusuke "Are you going to organize them again?"

    voice to0650
    tomoe "Yeah. Help me again, please, Yusuke."
    yusuke "Of course!"

    $ char ('tto019')

    voice to0651
    tomoe "After we finish, let's go home together!"
    "I help her."
    "But I only hold the ladder or hand books to her."
    "As I help her, I remember what she told me..."
    "She told me about the past with Takuto."

    call blackout from _call_blackout_172
    $ bgm (13)

    "Since she was a kid, she liked her cousin Takuto."
    "He was handsome, cool and her hero."
    "When she was in the seventh grade, they started dating."
    "Tomoe felt she was changing after they started dating."

    $ cg ('raf_19')
    $ unlock_gallery ('g6e5')

    "I didn't have any self-confidence. I was timid and shy."
    "He said he loved me."
    "I hated myself, but I was loosing that feeling."
    "I did my best for him...because I loved him."
    "He said he loved me."
    "And he cared about me."
    "I did my best because I wanted him to love me more."
    "I gradually started liking myself."

    $ bgfx ('black')
    $ bgm (9)

    "One day, I found out."
    "He was dating me, but he was also seeing another girl."
    "When I found out, it really hurt."
    "He didn't need me. I wasn't good enough."
    "But I still wanted to believe him."
    "He gave me confidence and courage."

    $ cg ('raf_2001')

    "I called him to ask about his true feelings."
    "After I heard he and the other girl were going to go out on a date."
    "'I'll wait for you until you come...'"
    "I told him with all the strength I had."
    "But he didn't come."
    "I waited. I waited for a long time."
    "He didn't come."

    $ cg ('raf_2002')

    "Snow started to fall."
    "I still waited for him in the snow."
    "Tomomi heard about me from one of her friends and came to pick me up."
    "I didn't want to go home."
    "I believed him; I wanted to believe him..."
    "I needed him because he changed me."
    "My sister tried to convince me otherwise, but I didn't want to listen."
    "'Takuto'll come. He'll come any minute!'"
    "She stayed with me."
    "Until I gave up."
    "Until I accepted the despair and sorrow."

    $ bgfx ('black')

    "After I finally accepted them, I sat there clinging to her sobbing."
    "I continued crying until we got home."
    "The next day, she went to see him."
    "She slapped him and said,"
    "'Never call her or get close to her again...'"
    "Since the incident, my old self returned."
    "'I'm a slow, timid girl, who nobody wants.'"
    "That's the only way I could think of myself."

    $ music_stop ()
    $ bgfx ('sora05')
    $ bgm (10)

    "Recalling her sad story, I murmur,"
    yusuke "I think you've become stronger."

    voice to0652
    tomoe "What are you saying?"
    "Trying not to look at her panties, I look up at her smiling."
    yusuke "Asumin and Marutan helped you to become stronger. They're useful, I guess."

    voice to0653
    tomoe "He he, but you helped too."
    "I'm happy to hear that."
    yusuke "Actually, I've been waiting for you to say that."

    voice to0654
    tomoe "Gee, Yusuke..."
    yusuke "I've changed too, thanks to you."

    voice to0655
    tomoe "Oh, I'm so embarrassed.. Yikes!!"

    $ bgm (7)

    "The ladder suddenly shakes."
    "But I don't let go."
    "Did she lose her balance?"
    "She's swinging her arms to keep her balance."
    "I think I'm shaking too... Yeow!"

    voice to0656
    tomoe "Y...Yusuke. Please hold the ladder tight... Ahh!"
    yusuke "I'm not shaking it... Whaaa!"
    "Everything is shaking."
    "The building itself is shaking too...is this an earthquake?"

    voice to0657
    tomoe "Whaaa!!"
    "She falls down on me screaming."
    "Again, we collapse."

    call blackout (True) from _call_blackout_173
    call effect ('SE40', ETYPE3) from _call_effect_43

    "I think I had the same experience before."

    $ cg ('ht_0201')

    "This time, mother nature caused it."
    "How many times do we have to do the same thing?"
    yusuke "Oh...ouch. Yikes!?"

    $ cg ('ht_0202')

    voice to0658
    tomoe "Oh, no..."
    "Tomoe's crotch is right in front of my eyes."
    "It's a very embarrassing situation."
    "But one thing is different from the first time."
    "Tomoe and I are more intimate."

    $ cg ('ht_0205')

    yusuke "......"
    tomoe "......"
    "It's still embarrassing."
    "She's so embarrassed, she can't move at all."
    "If I help her to her feet, nothing will happen."
    "But it's too late to control my desires."

    $ bgm (14)

    "I reach my hand inside her panties and touch her womanhood."
    "She instantly twitches."

    $ cg ('ht_0206')

    voice to0659
    tomoe "No, Yusuke...stop it..."

    voice to0660
    tomoe "I said no...aahhh..."
    yusuke "It's getting moist."
    "The front of her panties are getting sticky as I drool all over her pussy."
    "Sexual desire takes over and I run my fingers all over her."

    voice to0661
    tomoe "Ahh...mmm...ah...ahh."
    "She said no, but she doesn't refuse me."
    "Soon, she relaxes."
    "I slide her panties to the side."
    "Her womanhood is exposed and I softly kiss it."

    voice to0662
    tomoe "Yieee, no...stop...aahhh!"
    "I touch and lick her pussy."
    "She moans with joy."
    "My pants have a huge bulge in them."
    "She instantly notices it."

    voice to0663
    tomoe "Ahh...mmm...ahhh..."
    yusuke "CHAP...SLURP...mmm...!?"
    "She unzips my fly."
    "My dick pops out of my pants."
    "Touching my dick, she breathes hard and tells me,"

    $ bgfx ('black')

    voice to0664
    tomoe "Ahh...I'll...give you...pleasure too."
    "She's good at blowjobs."
    "Thinking about having sex at school makes me even harder."
    "She starts jerking me off."
    "Then she kisses the tip."
    "I'll soon cum if she continues doing that."
    "She passionately licks my cock."

    voice to0665
    tomoe "Mmm... SLURP...mmm..."
    yusuke "Ohh...you're great..."

    voice to0666
    tomoe "Mmm...mmm... SLURP..."
    "She's on top of me, and her tongue dances over my dick while I shiver with pleasure."
    "Her big breasts occasionally touch my dick and give me more pleasure."
    "A new desire rises within me."
    "Her gorgeous breasts."
    "With these..."
    yusuke "Tomoe..."

    voice to0667
    tomoe "Yes?"
    yusuke "Do me a favor...?"
    "I whisper in her ear."
    "Then...she turns beet-red."
    tomoe "......"
    yusuke "Of course you don't need to do it if you don't want to. Ah, actually, forget what I said."
    "I'm so embarrassed."
    "Looking at her confused expression, I can't ask her to do it."
    "Yet Tomoe slightly nods."

    voice to0668
    tomoe "Okay...I'll try."
    yusuke "Huh...really?"
    "She shyly takes her blouse off."
    "Then she takes her bra off as well."
    "She kneels down in front of me and wraps her breasts around my dick."
    "Her timid movements make me more excited."
    yusuke "(Pant! Pant!)"

    voice to0669
    tomoe "Don't look at me..."
    yusuke "O...okay."

    voice to0670
    tomoe "Mmm...mmm..."

    $ cg ('ht_0501')
    $ unlock_gallery ('g3e1')

    "She holds her breasts and clumsily tries to jerk me off with them."
    "The sight and touch are unbelievable."
    "Only the tip of my cock sticks up between her big breasts."
    "Only girls with big tits can do this."
    yusuke "Oh...jeez...it's incredible..."

    $ cg ('ht_0502')

    voice to0671
    tomoe "Do you feel good?"
    yusuke "Oh, yeah."

    voice to0672
    tomoe "Mmm... SLURP... SLURP...mmm..."
    "She hangs her head down, holding my dick between her breasts."

    $ cg ('ht_0504')

    "She puts the tip of my dick in her mouth, sealing her soft lips around it."
    "I've never felt this much pleasure before."
    "My dick is getting even harder and bigger."
    "I'm surprised myself."
    yusuke "Oh...mmm...it's so good..."

    voice to0673
    tomoe "SLURP...mmm...mmm..."
    "Her tongue swirls around as she slurps and sucks away at me."
    "The build-up of sexual tension inside me skyrockets to the top."
    "I can't hold it any longer."
    yusuke "Uhg...I'm...I'm cumming...aaahhhh!!"

    voice to0674
    tomoe "Mmm...yow! Ahh...mmm..."

    $ bgfx ('white')
    $ bgfx ('black')

    "It suddenly happens."
    "My cum spurts out and gushes all over her face."
    "She yelps in surprise."
    "I understand how she feels."
    "I feel guilty seeing her face and uniform with my hot cum all over her."
    "But I get excited at how dirty this is."

    $ cg ('ht_0503')

    voice to0675
    tomoe "Mmm... You came a lot..."
    yusuke "Y...yeah."
    "She's licking my cum."
    "What an erotic sight."

    $ cg ('ht_0504')

    "She cleans my dick up with her tongue."

    voice to0676
    tomoe "SLURP...mmm..."
    yusuke "T...Tomoe?"
    "She continues licking me."
    "She bewitchingly shakes her breasts on my dick again."

    $ cg ('ht_0502')

    voice to0677
    tomoe "I'll make it big again, Yusuke."
    yusuke "But...Tomoe."

    $ cg ('ht_0503')

    voice to0678
    tomoe "Please love me with this...please?"
    yusuke "O...of course."
    "Who could refuse such an erotic temptation with that cute voice?"
    "Looking at me, she shyly smiles."
    "My heart beasts faster and faster."
    "She jerks me off with her breasts again."
    "Almost instantly, my dick snaps back at full attention."

    $ bgfx ('black')

    "Bearing the pleasure, I draw her close to me."
    "I softly touch her womanhood."
    "Her juice is overflowing."

    $ sfx ('SE04')

    yusuke "Wow. You're soaking wet, Tomoe."

    voice to0679
    tomoe "Don't tease me..."
    "Her love juice is stuck on my fingers."
    "Her pussy is drooling, even on the insides of her thighs."
    yusuke "You got wet jerking me off with your breasts."

    $ sfx (delay=0.2)

    voice to0680
    tomoe "I...I can't help it."
    yusuke "I guess you're ready."
    "Her pussy is contracting and her juices are spilling out."
    "My fingers are easily swallowed inside her."

    $ sfx ('SE05', loop=True)

    "As I rub inside, I tell her,"
    yusuke "Tomoe, turn around."

    voice to0681
    tomoe "Huh...?"
    yusuke "Raise your hips...yeah."

    voice to0682
    tomoe "Is this...ah...ahhh!"

    $ sfx (delay = 0.5)

    "I raise her hips higher in front of me."
    "And I push her cheeks apart to expose her slit."
    "I'm trying to jam my dick inside, inching my way in from behind... Finally, I give a hard shove and plunge in all the way."
    "Confused, she shakes her hips from side to side."

    $ cg ('ht_0601')
    $ unlock_gallery ('g3e2')

    voice to0683
    tomoe "Ah...it feels different...ah...ahhh."
    yusuke "Your pussy is so tight and warm."

    voice to0684
    tomoe "Mmm...ah...ahh...you're ramming me hard...aahhh."
    "I'm a slave to my passions."
    "Erotic sounds are coming from between us."
    "She's bearing the pleasure, holding her hands on the wall."
    "My balls slap against her tight butt as I do her doggy-style."
    "The tip of my dick sometimes hits the end of her womb."

    voice to0685
    tomoe "Ahh...mmm...good...I feel good...yes, yes!"
    "I tease her and stir up her embarrassment."
    yusuke "You're screaming so loud, Tomoe. Someone might hear us."

    voice to0686
    tomoe "What...no...aaahhhh."
    "Hearing this, her inner walls squeeze around me tight."
    "It almost seems as if I can hear squeaky sounds."
    "Embarrassed, her pussy squeezes me tighter and tighter."

    voice to0687
    tomoe "Ohhh...mmm...I can't think straight anymore...ahhh."
    yusuke "Ughhh...don't squeeze me so tight..."
    "Her pussy squeezes around my shaft with every stroke as I slam away at her."
    "Tomoe and I are reaching our limits."

    voice to0688
    tomoe "Oooh...yes...yes...ahh...ahhhh."
    "Neither of us can hold on much longer."
    "Yet, we fiercely move our hips, searching for more pleasure."

    $ sfx ('SE07', loop=True)

    yusuke "I...I can't hold on...ughhhh..."

    voice to0689
    tomoe "Ahh...mmm...ah...ah...aaahhh!!"
    "Though I already came once, I might cum again before her."
    "She's still bearing the pleasure."
    "I try to move my hips harder to make her feel better."
    "Finally, we reach the limit."
    yusuke "Hmm...ughhh..."

    voice to0690
    tomoe "Ohh...I...I can't hold it any longer...ahh..ahh...AHHH!!!"
    yusuke "Ughh...ahhh!!"

    $ sfx (delay=0.2)
    call effect (None, ['white']) from _call_effect_44

    "Calling out my name, she convulses."

    $ say_hide ()
    $ cg ('ht_0602')

    "With a groan, I explode and shoot her full of my hot lava."
    "I'm really jerking around."
    "And as she cums, Tomoe collapses on the floor."
    "I also collapse on her."
    "I hold her sweaty body tight."

    $ bgfx ('black')
    $ music_stop ()
    $ bgfx ('bg03b')
    $ char ('tto034')
    $ bgm (13)

    "On the way home to the Harukaze dorm."
    yusuke "......"
    tomoe "......"
    "Embarrassed, we don't talk."
    "Yet, we hold hands."
    "It's enough for now."
    "Someone is walking towards us."
    "We recognize the person. He's the last person we want to see."
    yusuke "Oh...!"

    $ char ('tta002')

    takuto "......"

    voice to0691
    tomoe "Takuto..."
    "By reflex, I almost let go of her hand."
    "Tomoe holds my hand tight and looks at him."
    "He's looking at her as well, but then he looks away."
    yusuke "Humph..."
    takuto "......"
    "He doesn't say anything."

    $ char ('tto025')

    "Tomoe politely bows to him."
    "He gave Tomoe's family a loan."
    "She once loved him."
    "Watching his departure, I tell her,"
    yusuke "Tomoe...?"

    $ char ('tto001')

    voice to0692
    tomoe "What?"
    yusuke "I think he loved you."

    $ char ('tto004')

    tomoe "......"
    "Tomoe clams up with mixed feelings."
    "I don't know why he loaned the money to her family."
    "He loved her from bottom of his heart, I guess."
    "I want to tell her something."
    yusuke "But...I seriously...ah..."

    $ char ('tto025')

    tomoe "......"
    "She stares at me and I can't continue."
    "I can't say anymore with her expectant eyes staring at me."
    yusuke "Well, let's go!"

    $ char ('tto002')

    voice to0693
    tomoe "Hey! You should say it clearly, once in a while...heh-heh."

    $ char ('tto019')

    "She pouts but holds on to my hand smiling."
    "I hold her hand back as well."
    "We slowly walk back to the dorm holding hands."
    "No matter what happens in the future, I won't let go of her hand."

    jump episode20_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

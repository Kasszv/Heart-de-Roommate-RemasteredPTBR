label episode24_tomoe:

    "I didn't sleep well last night."
    "Asumi said she loves me."
    "I'm confused."
    "Asumi...what should I do?"
    "I've thought about her all night."
    "I wake up early feeling tired."
    "I don't hear anything but the chirping of birds."
    "Looking up at the ceiling, I come up with one thought."
    "If I stay here, Asumi and Tomoe won't make up."
    "If I didn't live with them, the fight wouldn't have been so big."
    "Then..."
    "To solve the problem,"
    "It's time to make a decision."
    "I relied on them too much."
    "I decide to secretly leave."
    "I hope Asumi and Tomoe will make up."
    "If they'd become friends again, I'd leave here immediately."
    "Am I a coward just running away from them?"
    "Am I selfish and unfair?"
    "But this is the only way I can think of."

    $ music_stop ()
    $ sfx ('SE37', loop=True)

    "I hear a noise."
    "Is someone up?"
    "It's still very early."
    "After I put my bag under my futon, I get out of the closet."

    $ sfx (delay=0.5)
    $ bgfx ('bg01a')
    $ char ('tas021')

    yusuke "Asumi..."

    $ char ('tas039')

    voice as1012
    asumi "Yusuke..."
    "Asumi stands there."
    "She already has her uniform on. Is she leaving?"
    "We feel awkward."
    "Our glances collide."
    "As I remember what Tomoe said yesterday, I blush."

    $ char ('tas047')

    "She remembers it and blushes as well."
    "She tells me in a fluster to hide her embarrassment,"

    $ char ('tas042')

    voice as1013
    asumi "Yusuke..."
    yusuke "Y...yes?"

    $ char ('tas027')

    voice as1014
    asumi "Never mind what Moe-Moe said yesterday. Please forget about it."
    yusuke "O...okay."
    "I nod at her."
    "Dead silence sits between us."

    $ char ('tas043')

    asumi "......"
    yusuke "......"

    $ char ('tas047')

    voice as1015
    asumi "Ah...I've got to go."
    "Feeling awkward, she's leaving the room."
    "I call out to her."
    yusuke "Asumi...uh...yesterday's fight..."

    $ char ('tas043')

    voice as1016
    asumi "I know...it's all my fault."

    voice as1017
    asumi "But could you leave me alone for a while?"
    yusuke "......"

    $ char ()

    "She leaves the room."
    "As I see her off, I make my decision."
    "I want them to make up."

    $ bgfx ('sora01')

    "The others are starting to get up."
    "Asumi already left."
    "I lost the opportunity to leave the dorm this morning."

    $ bgfx ('bg01a')
    $ char ('tto001')

    voice to0718
    tomoe "Morning, Yusuke."
    yusuke "Morning, Tomoe..."
    tomoe "......"
    "Tomoe looks tired."
    "Didn't she sleep last night?"
    "She restlessly looks around."
    "I know who she's looking for."
    yusuke "Asumi already left."

    $ char ('tto004')

    voice to0719
    tomoe "Oh...I see."
    "She looks relieved but sorry."
    "She's worried about Asumi after all."
    "I tell her,"
    yusuke "Ah...I think it was Asumi's fault, but..."

    $ bgm (14)

    voice to0720
    tomoe "I know...but I think we're both to blame."

    voice to0721
    tomoe "If I were strong and had more self-confidence, she would trust me more."

    $ char ('tto007')

    voice to0722
    tomoe "She thought I would give up on you if she told me her true feelings."
    yusuke "Tomoe..."
    "What a good girl; like an angel."
    "I admire her."
    "Smiling, she tells me,"

    $ char ('tto025')

    voice to0723
    tomoe "Asumi's very gentle. She's kinder than I am..."
    "They care about each other."
    "They just can't show their true feelings very well."
    "I'm sure about that."
    "I'll do anything to have them make up."

    call blackout from _call_blackout_179

    "During recess..."
    "I look around for Hikaru."
    "Even if I leave, nothing will probably change."
    "Another problem is Asumi cares about Hikaru too much."
    "So, I want to talk to Hikaru."
    "I can understand what Asumi's thinking."
    "I walk around campus looking for her."

    jump episode24_b

label episode24_tomoe_b:

    "Asumi told me about Hikaru's past."
    "I'm forbidden to tell anyone about it."
    "She doesn't want other girls to get involved in the trouble."
    "I understand how she feels."
    "That's why I tell Tomoe and Marumu."

    $ bgfx ('black')
    $ bgfx ('bg01b')
    $ char ('tto004')
    $ bgm (9)

    yusuke "......"
    tomoe "......"

    $ char ('tma004')

    marumu "......"
    "Tomoe and Marumu remain silent after I tell them."
    "They're in a state of shock."
    "Then Tomoe opens her mouth."
    "She tells us in a low but clear voice,"

    $ char ('tto013')

    voice to0724
    tomoe "I want to help Asumi..."

    $ char ('tma001')

    voice ma0244
    marumu "Me too."
    "Marumu agrees with Tomoe."
    "I try to stop them."
    "I didn't tell them to help Asumi."
    "I just wanted them to understand Asumi's feelings."
    yusuke "Tomoe, Marumu... Asumi said she doesn't want your help..."

    $ char ('tto013')

    voice to0725
    tomoe "I want to do it anyway. I understand Hikaru's feelings a little..."

    voice to0726
    tomoe "Fortunately, I met Asumi. I've changed because of her."

    $ char ('tma001')

    marumu "......(nod)"
    yusuke "......"
    "I still want to stop them."
    "But I know nobody can."
    "These three girls came through a lot of difficulties. I realize the fact."
    "Their bonds of friendship emerged from crisis and have gotten stronger."
    "However, Hikaru's stubbornness bothers me."
    "Tomoe and Marumu will get hurt."
    "They surely will."
    "If that happens, Asumi's efforts will all be in vain."
    "On second thought, I should stop them."
    yusuke "I don't think you should do this. Just let Asumi handle it."

    $ char ('tto002')

    voice to0727
    tomoe "But you won't let her do it alone, right?"
    yusuke "What...?"

    voice to0728
    tomoe "It's obvious. I can tell from your face."
    yusuke "Ah...that's.... Well."
    "I'm inwardly shocked."
    "I want to stop them."
    "But it's different with myself."
    "They know what I'm thinking."
    "I'm glad that we've come to understand each other."

    $ char ('tma017')

    voice ma0187
    marumu "Yusuke, you're a liar."

    $ char ('tto025')

    voice to0729
    tomoe "Let's do it together!"
    yusuke "But...I don't know."
    "Now it's difficult to stop them."
    "I can do it but they can't...I don't think they're okay with it."
    "Marumu ends this conflict."

    $ char ('tma011')

    voice ma0245
    marumu "We'll do this together."
    yusuke "But...yeah, you're right."

    $ bgm (10)

    "There's no way I can win against these girls."
    "We won't help Asumi individually; we'll do this together."

    $ bgfx ('sora05')

    "Before Asumi comes back, we make plans."

    jump episode24_c

label episode24_tomoe_c:

    $ bgfx ('sora01')

    "Our 'Approach Hikaru plan' has begun."
    "Tomoe and I start it off."

    $ bgfx ('bg05a')
    $ char ('tto001')
    $ bgm (3)

    voice to0730
    white "Ah...would you like to go home together, Hikaru?"

    $ char ('thi001')

    voice hi0085
    hikaru "With whom?"

    $ char ('tto002')

    voice to0731
    white "With Yusuke and me..."

    $ char ('thi002')

    voice hi0086
    hikaru "Why don't you two go home together?"
    servant1 "Don't say that...we're classmates."

    $ char ('tto013')

    voice to0732
    white "Besides, we want to talk to you..."

    $ char ('thi004')

    voice hi0087
    hikaru "You're bothering me..."

    $ char ()

    "She coldly tells us and walks away."
    "We tried to talk to her but we've failed so far."
    servant1 "Ohh...our mission failed..."

    $ char ('tto004')

    voice to0733
    white "Sorry, Yusuke."
    servant1 "Don't be, Tomoe. It's not your fault. I'm useless..."

    $ char ('tto013')

    voice to0734
    white "I don't think so, Yusuke. You did your best."
    servant1 "YOU did your best, though Hikaru was very harsh on you."
    "We cover up for each other."
    "We're interrupted by a third person."

    $ char ('tas037')
    $ bgm (6)

    voice as1018
    red "Well, well. You two are very good friends."

    $ char ('tto034')

    voice to0735
    white "A...Asumi."
    "Asumi sarcastically tells us."
    "Feeling uneasy, I clam up."
    "Tomoe turns beet-red and looks down."
    "The leader scolds us."

    $ char ('tas007')
    $ bgm (5)

    voice as1019
    red "Okay, guys. That's enough. White, during your duty you should call me Red!"

    $ char ('tto013')

    voice to0736
    white "Roger, Red. I'll go into our next phase."
    "Did they already make arrangements?"
    "I ask Tomoe about the details."
    servant1 "What's the next phase?"

    voice to0737
    white "I'm going to the grocery store for dinner."

    $ char ('tas012')

    voice as1020
    red "Thank you."
    "That's nothing new."
    "Then..."
    servant1 "I'll go with you."

    $ char ('tas007')

    voice as1021
    red "Servant 1, go scouting!"
    servant1 "Oh no..."

    call blackout from _call_blackout_180

    "I'm banned from accompanying Tomoe (she's White now) and given another mission."
    "The mission is to run after her and observe her."
    "But I can't find her."

    $ bgfx ('bg05a')
    $ char ('tas018')
    $ bgm (7)

    voice as1022
    red "Gosh...you're so slow, Servant 1. You're pathetic, though you've transformed."
    servant1 "I haven't transformed! Besides, Asumi..."
    "I talk back to her but she interrupts."

    $ char ('tas007')

    voice as1023
    red "Call me Red! Don't forget you're still on duty!"

    $ music_stop ()

    voice yo0174
    yagami "Asumi..."

    jump episode24_d

label episode24_tomoe_f:

    $ bgfx ('black')

    "A few days later, gossip spreads through the school."
    "It's about Hikaru and me."
    "'They met secretly.'"
    "'Actually, they're a couple.'"
    "'They had sex up on the roof...'"
    "That was a close one."
    "I don't know who started it, and most of the students don't believe it."
    "Kosuke laughs it off."
    "Yet, it bothers a particular person."

    $ bgfx ('bg04b')
    $ char ('tto004')
    $ bgm (16)

    voice to0738
    tomoe "Ah...Yusuke?"
    yusuke "Tomoe...what?"

    voice to0739
    tomoe "Well, I...I have a question..."
    yusuke "Yeah? You can ask me anything."

    $ char ('tto034')

    voice to0740
    tomoe "Yusuke...do you like Hikaru?"
    yusuke "W...why?"

    voice to0741
    tomoe "Did you do something intimate with...Hikaru?"
    yusuke "Ugh......( I'm shocked!)"
    "Tomoe heard the rumor, I guess."
    "Hesitantly, she gets right to the point."
    "I don't want to lie to her."
    "Feeling nervous, I grab her hand and take her where no one is around."

    call blackout from _call_blackout_181

    "If I give her a lame excuse, the situation might get worse."
    "I'll never make the same mistake again."
    "I gather my courage and tell her what really happened with Hikaru."

    $ bgfx ('bg04b')
    $ char ('tto004')

    tomoe "......"
    yusuke "Ah...well. Ah..."
    "She clams up and looks down after she hears the story."
    "I understand her feelings."
    "A certain coolness has come between us."
    "I shouldn't have told her... Should I have made something up?"
    "I regret telling her the truth."
    yusuke "Tomoe..."

    $ char ('tto001')

    voice to0742
    tomoe "Yusuke...can I ask you one thing?"
    yusuke "Y...yeah."
    "The question she wants to ask is,"
    "The thing she really wants to know."

    $ char ('tto034')

    voice to0743
    tomoe "Do you...love me?"
    yusuke "......"
    tomoe "......"
    yusuke "Yes. More than anyone."

    $ char ('tto025')

    voice to0744
    tomoe "Then...I won't ask you anything more."

    $ bgm (14)

    "The pursuit of doubt is over."
    "She puts on a smile of mixed emotions."
    "I know it's hard to accept."
    "Fortunately, she believes the most important thing."
    "Her smile is proof of my trust."
    "I feel something warm begin to rise within."
    "Her trust makes me happy."
    "I softly hold her hand."
    "Then I want to hold her in my arms...!?"

    $ music_stop ()
    $ char ('tto037')

    yusuke "Whaaa... Gah!"

    $ bgfx ('black')
    call effect ('SE43', ETYPE2) from _call_effect_45

    "The next moment, I fall on my face."
    "Because I get hit from behind."
    "Someone's angry voice echoes in the air."

    $ bgfx ('bg04b')
    $ char ('tas036')
    $ bgm (16)

    voice as1024
    asumi "I found you, Yusuke. You ass!"

    voice to0745
    tomoe "What's wrong, Asumi?"

    $ char ('tas010')

    voice as1025
    asumi "Moe-Moe, how you can be so calm? Did you hear what he did?"
    "Asumi heard the rumor, I guess."
    "A sudden attack."
    "It was so Asumi...but it hurt."

    $ bgfx ('sora05')

    "If Tomoe hadn't stopped Asumi, what would have happened to me?"
    "I shudder at the very thought."
    "After hearing Tomoe's explanation (summary), Asumi finally stops attacking me."

    $ music_stop ()
    $ bgfx ('bg04b')
    $ char ('tas012')
    $ bgm (4)

    voice as1026
    asumi "I didn't think you'd do such a thing to Hikaru."
    yusuke "Then why did you attack me from behind?"
    "Tomoe softly rubs the lump on my head."

    $ char ('tto007')

    voice to0746
    tomoe "Are you all right, Yusuke?"
    yusuke "Yeah, don't worry. I'm used to it."

    voice to0747
    tomoe "You have a bruise. I'll go and wet my handkerchief."
    yusuke "I'm okay, Tomoe."

    $ char ('tto013')

    voice to0748
    tomoe "I don't think so. If you leave it...oops."

    $ music_stop ()
    $ char ('tas037')

    asumi "......"
    "Asumi's silence and menacing look pierce us."
    "We often flirt with each other like this."
    "Asumi's quietly staring at us."

    $ char ('tto034')

    "Tomoe immediately steps back."
    "She knows Asumi's feelings toward me."
    "However, Asumi puts on a smile."

    $ char ('tas012')

    voice as1028
    asumi "Oh, don't worry about me! Go ahead."
    yusuke "But..."

    $ char ('tas013')

    voice as1029
    asumi "Listen, Tomoe. I like Yusuke, but it's natural to feel like that."

    $ char ('tto013')

    voice to0749
    tomoe "What?"
    "Not just Tomoe, but everybody would be surprised at her words."
    "Of course, I'm surprised too."
    "Asumi starts explaining."

    $ char ('tas045')
    $ bgm (14)

    voice as1030
    asumi "All the other roommates are all girls, so being with him all the time makes me feel like that."

    voice as1031
    asumi "Couples in movies often become couples in real life. It's the same thing."

    $ char ('tas001')

    voice as1032
    asumi "So my feelings toward Yusuke are different than yours."

    $ char ('tto025')

    voice to0750
    tomoe "Asumi..."
    "We don't know if she's telling us the truth."
    "But Asumi want us to believe her."

    $ char ('tas015')

    voice as1033
    asumi "Well, don't worry about small things; enjoy youth!"
    yusuke "Asumi..."
    "I want to say something nice to her, but she interrupts me."

    $ char ('tas013')

    voice as1034
    asumi "Anyway, stop packing to move out secretly! I won't let you do that, though Moe-Moe might."
    yusuke "Huh...?"
    "Asumi knew about it."
    "She's the leader after all...I'm impressed."
    "Then she whispers to me,"

    $ char ('tas401')

    voice as1035
    asumi "You know my Achilles' heel..."
    yusuke "Y...yeah."
    "Her secret..."
    "It's the reason I started staying at the Harukaze dorm in the first place."
    "I don't think I'll ever remember what it is."
    "But that's okay with me."

    $ char ('tas404')

    "I'm just happy at her kindness."

    call blackout from _call_blackout_182

    "After school."
    "Tomoe and I are talking about Asumi on the way to the market."

    $ bgfx ('bg03b')
    $ char ('tto025')
    $ bgm (13)

    yusuke "What can I say about Asumi..."

    voice to0751
    tomoe "I guess she's the leader after all."
    yusuke "You think so too...but she's so selfish."

    $ char ('tto019')

    voice to0752
    tomoe "I agree, heh-heh... Oh!"

    $ char ('tto022')

    yusuke "What's the matter, Tomoe?"

    $ char ('tto002')
    $ music_stop ()

    tomoe "Hikaru..."
    "She looks ahead down the street."
    "Hikaru's walking."
    "Our mission has begun again!"
    "We have to talk to her, anyway."
    "I start to walk over to talk to her."
    "But Tomoe prevents me from leaving."

    $ char ('tto013')

    voice to0753
    tomoe "Wait, Yusuke...I'll go."
    yusuke "How about together...?"

    voice to0754
    tomoe "Let me handle this alone...please?"
    yusuke "Okay..."
    "I nod."
    "She trusts me."
    "But the gossip is still floating around school."
    "Tomoe knows it isn't just a rumor."
    "As a girl, she doesn't want me to talk to Hikaru."
    "I know how she feels, and that's why I just nod at her."

    $ bgfx ('black')
    $ bgfx ('bg03b')
    $ bgm (8)

    "Tomoe walks toward Hikaru."
    "She gathers all her courage and talks to Hikaru."

    $ char ('tto013')

    voice to0755
    tomoe "Ah...Hikaru."

    $ char ('thi001')

    voice hi0088
    hikaru "What?"

    $ char ('tto004')

    voice to0756
    tomoe "Uh...ah..."

    $ char ('thi004')

    hikaru "......"
    "She almost loses in the silence."
    "But she stirs herself up and continues to talk."

    $ char ('tto013')

    voice to0757
    tomoe "I...I want to ask you something..."

    $ char ('thi004')

    hikaru "......"

    $ char ('tto013')

    voice to0758
    tomoe "Oh, wait!"
    "Hikaru ignores her and walks away."
    "Tomoe follows her."
    "Of course, I follow them as well."

    $ bgfx ('black')

    "Tomoe continues talking to her about various stuff."
    "But Hikaru remains silent."
    "Tomoe won't give up and follows her."
    "Finally, Hikaru looks at Tomoe with a disgusted face."

    $ bgfx ('bg03b')
    $ char ('tto001')

    voice to0759
    tomoe "Hikaru..."

    $ char ('thi004')

    voice hi0089
    hikaru "What? If you have something to ask, just say it."
    "Hikaru answers her at last."
    "Tomoe quickly asks her what she wants to know."

    $ char ('tto001')

    voice to0760
    tomoe "What are you doing?"

    $ char ('thi004')

    voice hi0090
    hikaru "Nothing..."

    $ char ('tto002')

    voice to0761
    tomoe "You don't look like you enjoy shopping, you're just killing time."

    $ char ('thi002')

    voice hi0091
    hikaru "Yeah...so what?"
    "Tomoe and I are at a loss for words."

    $ char ('tto002')

    voice to0762
    tomoe "But why...?"

    $ char ('thi006')

    voice hi0092
    hikaru "You're annoying...because I don't want to go home! There's no place for me!"

    voice hi0093
    hikaru "Now do you get it? Then go away!"

    $ music_stop ()
    $ char ('tto007')

    tomoe "......"
    "Her words shock us."
    "We live in peace and enjoy our lives, but she lives in a different world."
    "That's why Asumi can't leave her alone."
    "But Tomoe and I are..."
    "Tomoe shuts her mouth."
    "Hikaru glances at her and walks away."

    $ bgfx ('black')
    $ bgfx ('bg03b')
    $ bgm (9)

    "After Hikaru leaves, I rush over to Tomoe."
    "She looks pale."
    yusuke "Tomoe...are you okay?"

    $ char ('tto007')

    voice to0763
    tomoe "She said she doesn't want to go home and there isn't a place for her."
    "She looks like she's going to cry."
    yusuke "Tomoe..."

    voice to0764
    tomoe "That's sad, awful...I feel sorry for her."
    "Hikaru's pain...I remember the story I heard from Asumi."
    "Tomoe now feels her sorrow."
    "All negative feelings from Hikaru."
    "I can't leave her alone, either."
    "No place for her...Hey, wait."
    yusuke "A place to live... Yeah, Tomoe!"

    $ music_stop ()
    $ char ('tto002')

    voice to0765
    tomoe "Yusuke...?"

    $ bgm (5)

    "I just came up with a good plan."
    "It sounds like one of Asumi's ideas!"
    yusuke "Let's try it, though there's little chance of it succeeding."

    voice to0766
    tomoe "Try...what?"
    yusuke "Let's go back to the dorm and talk about it. We need Asumi's opinion..."

    $ char ('tto013')

    voice to0767
    tomoe "Hey, Yusuke!"
    "We'll try anything we can possibly think of!"
    "I don't want Hikaru and Tomoe to cry!"
    "I'll put my plan past Red."

    jump episode24_g
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

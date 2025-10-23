label episode24_marumu:

    $ bgfx ('black')
    $ bgm (9)

    "I didn't sleep well last night."
    "Everybody is separated...they were such good friends."
    "I wake up feeling tired."
    "I hear nothing but the chirping of birds."
    "My secret might come out."
    "I don't want them to get involved in more trouble."
    "Then..."
    "It's time to make a decision."
    "I've relied on them too much."
    "I start packing to quietly leave."

    $ music_stop ()
    $ sfx ('SE37', loop=True)

    "I hear a noise."
    "Did someone get up?"
    "It's still early."
    "I put my bag under my futon and leave the closet."

    $ sfx (delay=0.5)
    $ bgfx ('bg01a')
    $ char ('tma021')

    marumu "......"
    "Marumu is there."
    "She already has her uniform on."

    $ char ()

    "She often appears in unexpected places at unexpected moments."
    "Leaving at this hour is usual for her, I guess."
    "But something bothers me."
    "Her back has a sternness that makes her difficult to approach."
    "She's obviously different."
    "I want her back to her true self."
    "I wish she and Asumi would make up."
    "But I have to do something for them."

    $ bgfx ('black')

    "During recess,"
    "I look around for Hikaru."
    "Even if I leave, nothing will probably change."
    "Another problem is Asumi cares about Hikaru too much."
    "That's why I want to talk to Hikaru."
    "I can understand what Asumi's thinking."
    "I walk around campus looking for her."

    jump episode24_b

label episode24_marumu_b:

    $ bgfx ('black')

    "Asumi told me about Hikaru's past."
    "Before she leaves, she asks me not to tell anyone about it."
    "She doesn't want others to get involved in the trouble."
    "I understand how she feels."
    "However, I decide to tell Marumu the truth."
    "Asumi always interferes in others' affairs too much."
    "I'll tell Marumu because Asumi's a caring person."

    $ bgfx ('bg01b')
    $ bgm (9)

    yusuke "Marutan..."

    $ char ('tma021')

    marumu "......"
    yusuke "I want to talk to you."
    marumu "......"
    "I explain to her what happened to Hikaru in the past."
    "I also explain why Asumi is trying to handle it alone."
    "After I finish, she's still wearing a poker face."
    "Her heart still seems closed off."
    "I desperately continue talking."
    yusuke "Marutan, that's Asumi. She always sets her heart on a matter, does whatever she wants, and she's a busybody..."
    yusuke "But she hates loneliness, even if it's someone else's."
    yusuke "She can't leave them alone."

    $ char ('tma004')

    voice ma0398
    marumu "Asumin..."
    "Marumu's eyes are shining."
    "I guess she already knew it."
    yusuke "I don't ask you to understand what she's doing. But just forgive her and let her handle it."

    voice ma0399
    marumu "No."
    yusuke "Marutan..."
    "She tries to understand."
    "But can she forgive Asumi? I misunderstand her intentions."

    $ char ('tma001')

    voice ma0400
    marumu "I'll help her."
    yusuke "Huh?"

    voice to0874
    tomoe "Yeah, we can't let Asumi do it alone."

    $ music_stop ()
    $ char ('tto025')

    yusuke "Tomoe..."
    "Was she eavesdropping?"
    "She can't remain silent any longer."
    "Both of them decide to help Asumi."

    voice to0875
    tomoe "Let's do it together! Right, Marutan?"

    $ char ('tma007')

    voice ma0401
    marumu "Yeah."
    yusuke "......"

    $ bgm (10)

    "I can't stop them now."
    "I remember the story of how they first met."
    "They didn't get along with each other in the beginning."
    "But they came through the difficulties together."
    "Hikaru's case isn't someone else's affair to Asumi."
    "Tomoe and Marumu have also been changed by her."
    "The only thing left to do is to persuade Asumi."
    yusuke "Okay, ladies. We'll have a meeting to convince the stubborn Asumi!"

    $ char ('tto019')

    voice to0876
    tomoe "Yeah, let's talk!"

    $ char ('tma008')

    voice ma0402
    marumu "Agree."
    "It sounds like the usual Marumu."
    "I'm glad about that."
    "I'm really happy to tell them the story I heard from Asumi."

    jump episode24_c

label episode24_marumu_c:

    $ bgfx ('sora01')

    "Our 'Approach Hikaru plan' has begun."
    "Marumu and I start it off."

    $ bgfx ('bg05a')
    $ char ('thi001')
    $ bgm (2)

    servant1 "......"

    $ char ('tma001')

    magenta "......"

    $ char ('thi001')

    hikaru "......"
    "They're just looking...no, staring at each other."

    $ char ()

    "Then Hikaru ignores Marumu and walks away."
    servant1 "Marutan, why didn't you talk to her?"

    $ char ('tma001')

    voice ma0403
    magenta "Eye contact..."
    servant1 "I see...but it didn't look like it."

    $ char ('tma004')

    voice ma0404
    magenta "You didn't do anything..."
    servant1 "Ah...you're right."
    "Hikaru is hard to deal with."
    "Marumu is doing better without saying a word."
    "I just don't know how to deal with her."
    "Both Hikaru and Marumu are quiet, but they're totally different."
    "Asumi shows up."

    $ bgm (5)
    $ char ('tas006')

    voice as1125
    red "You guys are useless!"
    servant1 "Asumin..."

    voice as1126
    red "Call me Red! Servant 1, you're helpless! Come with me!"
    servant1 "Oh no... WHAAA!"

    $ char ('tma008')

    voice ma0405
    magenta "Hang in there, Servant."
    "Marumu sees us off."

    call blackout from _call_blackout_83

    "Then..."

    $ bgfx ('bg20a')
    $ char ('tas703')
    $ bgm (7)

    voice as1127
    red "Don't stop! No wonder Hikaru makes a fool of you!"
    servant1 "How are doing 100 push-ups related to getting along with Hikaru?"

    $ char ('tas705')

    voice as1128
    red "Your attitude for quibbling isn't good! Shut up and put some effort in it!"
    servant1 "Please...I need a break, Asumin."

    $ bgfx ('bg04a')
    $ char ('tas007')

    voice as1129
    red "How many times do I need to tell you? I'm Red during duty!"

    $ music_stop ()

    voice yo0174
    yagami "Asumi..."

    jump episode24_d

label episode24_marumu_f:

    $ bgfx ('black')

    "A few day later, gossip spreads through the school."
    "It's about Hikaru and me."
    "'They met secretly.'"
    "'In fact, they're a couple.'"
    "'They had sex up on the rooftop...'"
    "That was a close one."
    "I don't know who started it, but most of the students don't believe it."
    "Kosuke laughs it off."
    "However, it bothers a particular person."

    $ bgfx ('bg05b')
    $ char ('tma001')
    $ bgm (16)

    voice ma0406
    marumu "Yusuke..."
    yusuke "Yeah, Marutan?"

    $ char ('tma004')

    voice ma0407
    magenta "Magenta..."
    yusuke "Okay. What can I do for you?"

    voice ma0407
    magenta "Magenta..."
    yusuke "All right, Magenta."
    "It's not fair! She calls me Yusuke."
    "On second thought, it's better than to be called Servant."
    "Thinking about it, I feel depressed."
    "She hesitantly asks me,"

    $ char ('tma021')

    voice ma0408
    magenta "Do you like Hikaru?"
    yusuke "Umm...she's difficult to deal with..."

    voice ma0409
    magenta "Is she your girlfriend?"
    yusuke "No way. Why would you ask me such a question?"

    voice ma0410
    magenta "A rumor..."
    yusuke "I knew it."
    "She heard the rumor about Hikaru and me."
    "But I can't control the gossip."
    "Besides, part of the rumor is true."
    "I don't know what to say to her."
    "Looking straight at me, she tells me with pure, innocent eyes,"

    $ char ('tma001')
    $ bgm (14)

    voice ma0411
    marumu "Yusuke..."
    yusuke "Yes...?"

    $ char ('tma003')

    voice ma0412
    marumu "I trust you, Yusuke."
    "Tears come to my eyes."
    "She trusts me with her pure, innocent heart."
    "I appreciate her from the bottom of my heart."
    yusuke "Thank you, Marutan."

    $ char ('tma004')

    voice ma0413
    magenta "Magenta..."
    yusuke "......"

    call blackout from _call_blackout_84

    "The tears keep coming..."
    "She often ruins a nice atmosphere."
    "At least she trusts me. I'll engrave it in my mind."

    $ bgfx ('bg03b')

    "After school."
    "It happens on the way back to the dorm."
    "We find Hikaru walking ahead of us."
    yusuke "Hikaru..."
    "I try to run over and talk to her."
    "However, Marumu prevents me from leaving."

    $ char ('tma004')

    "She decidedly tells me,"

    $ char ('tma001')

    voice ma0414
    marumu "Wait here, Yusuke."
    yusuke "How come?"
    "She's worried about the rumor, I guess."

    $ char ('tma010')

    voice ma0415
    magenta "Magenta can handle this."
    yusuke "Sure...go ahead."

    $ char ('tma007')

    voice ma0416
    magenta "Free..."
    "This is so Marumu."

    $ char ()

    "Marumu walks over to Hikaru."
    "I'm worried about her."
    "Then I follow them secretly."

    $ bgfx ('black')
    $ bgfx ('bg03b')
    $ char ('thi004')
    $ bgm (8)

    hikaru "......"

    $ char ('tma001')

    magenta "......"
    "Both of them remain quiet."
    "Hikaru ignores her and walks away."
    "Marumu follows her."
    "It looks so strange; they look like complete strangers."

    $ char ('thi004')

    hikaru "......"

    $ char ('tma001')

    magenta "......"
    yusuke "What are they doing?"

    $ char ('thi001')

    "Hikaru's aimlessly strolling around town."
    "It looks like she's just killing time."
    "As Marumu wonders about her strange behavior, she opens her mouth."
    "She suddenly asks her,"

    $ char ('tma001')

    voice ma0417
    magenta "Are you having fun?"

    $ char ('thi004')

    voice hi0094
    hikaru "Not really."

    $ char ('tma001')

    voice ma0418
    magenta "Aren't you going home?"

    $ char ('thi002')

    voice hi0095
    hikaru "Eventually..."

    $ char ('tma004')

    magenta "......"
    "Silence sits between them again."

    $ char ()

    "Soon, Marumu walks back to me."

    call blackout from _call_blackout_85
    $ bgfx ('bg03b')

    yusuke "Did you get anything, Magenta?"

    $ char ('tma001')

    voice ma0419
    magenta "Scouting accomplished."
    yusuke "Oh, you were scouting her..."
    "It might have looked like that..."
    "Marumu reports the outcome."

    voice ma0420
    magenta "Hikaru doesn't like her home."
    yusuke "She...doesn't?"

    $ bgm (9)

    "I remember the story about Hikaru I heard from Asumi."
    "Does she aimlessly hang around town because she doesn't want to go home?"
    "Hikaru doesn't like her home."
    yusuke "Then, just like me...!!"

    $ bgm (5)

    "I suddenly come up with a good idea."
    "It sounds like one of Asumi's ideas."
    yusuke "Let's try it, though there's little chance of it succeeding."

    $ char ('tma017')

    magenta "???"
    yusuke "Let's go back to the dorm and talk about it! We need Asumi's opinion."
    "We'll try anything we can possibly think of!"
    "I don't want Hikaru to cry anymore."
    "I'll present my plan to Red."

    jump episode24_g

label episode24_marumu_g:

    call blackout from _call_blackout_86

    "Things turned out quite favorably."
    "I have nothing to regret."
    "All I have to do is leave here."
    "A room is available in the men's dorm now. I should move there."
    "I return to my closet and grab my packed bag."
    "However, it looks different."
    "My bag looks flat now."
    "There's a memo with 'Confiscated' written on it."
    "Did Marumu do that?"

    $ bgfx ('sora09')
    $ bgm (14)

    "I guess she knew."
    "She knew I was going to leave the Harukaze dorm."
    "And she hinders my work..."
    "I can't even guess what she's thinking."
    "But I'm happy about what she did."
    "I guess I can stay here a little longer..."

    jump episode24_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

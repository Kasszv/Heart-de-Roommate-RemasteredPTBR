label episode24:

    $ Fnum = 24
    $ save_name = "Episode 24: Harmony of Minds"


    call ep_start from _call_ep_start_5

    if F015 == 0:
        jump episode24_asumi

    elif F015 == 1:
        jump episode24_tomoe

    elif F015 == 2:
        jump episode24_marumu

label episode24_b:

    "I follow Hikaru after school."
    "It's hard to follow her because she walks so fast in the crowded hallway."
    "She disappears inside the door to the stairs."
    "Those stairs only go up."

    $ bgfx ('bg07a')

    yusuke "The rooftop... Oh!"

    $ bgm (8)

    "I instinctively hide behind the door."

    $ chars ('tas042', 'thi001')

    "Asumi, the rooftop queen, is there."
    "She left early in the morning to avoid Tomoe."
    "They're talking about something."
    "Asumi looks like she's trying to convince Hikaru of something. But in return, Hikaru is coldly returning her glance."
    "I don't hear anything behind the door."
    yusuke "How many times have I been in the same situation?"
    "As I stand there looking at them, they're about to finish."
    "Because I'm coward."
    "Because I don't have the courage to face them."
    yusuke "It's not good. I should do this..."
    "I summon all my courage and slowly walk over to them."
    "If I stay here and peep, not a thing will change."

    call blackout from _call_blackout_26
    $ bgfx ('bg07a')
    $ chars ('tas021', 'thi001')

    voice as0774
    asumi "Yusuke..."
    hikaru "......"

    $ char ('tas036')

    "Hikaru turns around and walks away."
    "Asumi's looking at me with disgust."
    "As I think carefully, I realize there's no place to hide on the rooftop."

    $ char ('tas006')

    voice as0775
    asumi "What the hell are you doing here?"
    yusuke "I secretly followed her."

    voice as0776
    asumi "Whatever. Hey, Hikaru left because of you!"
    yusuke "Sorry, but it's your fault too."

    voice as0777
    asumi "Huh? Are you mad because you can't find any other excuse?"
    yusuke "No! It's true everybody feels uncomfortable because of your strange reaction. I can't leave the dorm like this."

    $ char ('tas037')

    voice as0778
    asumi "Leave?"
    yusuke "We'll talk about that later. Anyway, you really care about Hikaru a lot lately. Why?"

    $ char ('tas043')

    voice as0779
    asumi "Because..."
    "The words stick in her throat."
    "Is it something hard to say?"
    "But I won't let it go."
    "If I withdraw, Asumi, Tomoe, and Marumu won't go back to being good friends again."
    "For their friendship..."
    "Confused, she looks at me."
    "She looks hesitant."

    $ bgfx ('sora01')

    "She quickly decides to tell me."
    "It's a shocking story about Hikaru."

    $ bgm (9)
    $ bgfx ('black')
    $ cg ('raf_21')
    $ unlock_gallery ('g6e7')

    "Hikaru was born between her father and his mistress."
    "After her mother died, her father took custody of her for appearance's sake."
    "He's the director of a hospital and one of the political leaders in her hometown."
    "However, she had hard times as an illegitimate child."
    "She was a burden to her family."
    "All the time."
    "Growing up like that, she hasn't trusted anyone."
    "That's why she's so cold at school."
    "Two years ago, she had a friend."
    "The girl was kind, gentle, and shy."
    "She was one of Hikaru's classmates."
    "Hikaru was perplexed at first when she talked to Hikaru."
    "They gradually got close and became best fiends."
    "Hikaru changed and sometimes smiled."
    "One day, she accidentally found out the truth."
    "Her best friend...she became Hikaru's friend because her teacher asked her to."
    "The teacher was worried about Hikaru, an introvert, a loner."
    "Her kindness and the plan backfired."
    "Hikaru pressed her only friend for an answer."
    "As she admitted the fact, something snapped in Hikaru's mind."
    "But she was wrong."
    "The 'friend' felt true friendship with Hikaru."
    "She wanted to tell Hikaru."
    "She wanted her to understand her feelings."
    "Unfortunately, it was too late. Hikaru didn't listen to her."
    "She became the lonely, introverted girl again."
    "'Who would believe you... Liar!'"
    "Hikaru insulted her and ran away."
    "But the girl ran after Hikaru to make her understand her feelings."
    "Hikaru thought she was a hypocrite and pushed her away."
    "She lost her balance and fell down the stairs."
    "There's still a big scar on her leg."
    "Hikaru felt loss, suspicion, jealousy, and remorse."
    "Suffering with these negative feelings, she was driven to despair."
    "She even regretted being born."
    "That's why she tried to kill herself."
    "By cutting her wrist really deep."
    "Fortunately, she didn't die."
    "However, Hikaru has never trusted others since."
    "She didn't attend classes and finally stopped going to school."
    "Never to trust others again."
    "She doesn't want to hurt others...and moreover, she doesn't want to be hurt."
    "She denied everything even to herself."
    "Her family only cared about their reputation and wanted to send her to the country. They transferred her to Aiho School."
    "A guard came with her to prevent her from committing suicide and also to take care of her."
    "She's lonely."
    "She's forced to live without any hope."
    "And she refuses to get involved with others."
    "Hikaru has nothing."
    "No meaning for living..."
    "Asumi happened to hear about her past."
    "Ms. Yagami and another teacher were talking about it."
    "Listening to them, Asumi thought about it."
    "She couldn't leave Hikaru alone."
    "She came into this world, so it's unforgivable to kill herself."

    call blackout from _call_blackout_27
    $ bgfx ('bg07a')
    $ char ('tas044')

    yusuke "......"

    voice as0780
    asumi "Do you understand? That's why I can't leave her alone!"
    "I'm at a loss for words for a moment."
    "Because I'm shocked at the story."
    "Yet, I have to tell her one thing."
    yusuke "I understand your feelings, but..."

    $ char ('tas006')

    voice as0781
    asumi "But what?"
    yusuke "I think you're just interfering."
    asumi "......"
    "I thought Asumi would beat me up with anger."
    "But she doesn't do anything but wear a gloomy face."
    "She just takes her irritation out on me."

    $ char ('tas010')

    voice as0782
    asumi "I know that. I know it very well!"

    voice as0783
    asumi "I'm just a busybody! I don't need you to tell me that!"
    yusuke "(Hikaru must have really told her off.)"
    "I can easily conclude this from her attitude."
    "But Asumi won't give up."

    $ char ('tas007')

    voice as0784
    asumi "I can't leave her alone, even if I am bothering her. I just can't!"

    voice as0785
    asumi "I'm a selfish busybody!"

    voice as0786
    asumi "I don't want the other girls to get involved with my trouble! So please let me do this alone!"
    yusuke "But, Asumi..."

    $ char ()

    "After yelling at me, she runs away."

    if F015 == 0:
        jump episode24_asumi_b

    elif F015 == 1:
        jump episode24_tomoe_b

    elif F015 == 2:
        jump episode24_marumu_b

label episode24_c:

    call blackout from _call_blackout_28
    $ bgfx ('sora08')

    "Asumi returns late."
    "I guess she feels uneasy coming back tonight."

    $ bgfx ('bg01c')
    $ char ('tas043')

    voice as0787
    asumi "I'm home..."
    yusuke "Hey, Asumi. Could you sit down there?"
    "I take her to the back of the room."
    "Her two roommates are seriously staring at her."

    $ chars ('tto002', 'tma004')

    tomoe "......"
    marumu "......"

    $ char ('tas021')

    asumi "......"
    "We're quietly looking at Asumi."
    "I feel an awkward atmosphere."
    "Asumi looks confused and doesn't say anything. Tomoe hesitantly opens her mouth."

    $ chars ('tto013', 'tma004')

    voice to0369
    tomoe "Asumin..."

    voice as0788
    asumi "W...what?"

    $ char2 ('tma001')

    voice to0370
    tomoe "The three of us...will help you."

    $ char ('tas042')

    voice as0789
    asumi "Huh...what!?"
    "Asumi yelps with surprise."

    $ char ('tas036')

    "Then she glares at me. Her eyes are blaming me."
    "I can't withdraw now."
    yusuke "Why don't you share your problems with us...because..."

    $ chars ('tto013', 'tma001')

    voice ma0191
    marumu "Help the leader."
    "Marumu interrupts me, and I can't continue with the cool phrase I prepared."
    "It bothers me, but I should be patient."
    "However, Asumi doesn't accept our offer."

    $ char ('tas010')

    voice as0790
    asumi "No way! I'll do this by myself!"

    voice as0791
    asumi "This is none of your business!"
    "We predicted her answer and smirk at each other."
    "The plan is carried out."

    $ bgm (6)
    $ chars ('tto031', 'tma007')

    yusuke "Hmm...did you hear that? She wants to do this all by herself."

    voice to0371
    tomoe "That's the problem a leader has when she wants to do something without telling anybody."

    voice ma0192
    marumu "Disqualified."

    voice as0792
    asumi "H...hey, wait..."
    "Asumi's bewildered as we clearly say to her,"

    $ bgm (4)
    $ chars ('tto051', 'tma016')

    voice to0372
    tomoe "We can't follow such a selfish leader anymore."
    yusuke "So...we'll do whatever we want to, Asumin!"

    voice ma0193
    marumu "Whatever!"

    voice as0793
    asumi "You'll do whatever... Do you mean!?"
    "I speak up at last."
    yusuke "We'll help the selfish leader, and that's our decision."

    $ char1 ('tto025')

    voice to0373
    tomoe "We can do anything we want, right?"

    $ char2 ('tma008')

    voice ma0194
    marumu "Freedom."
    "Looking at us, Asumi's amazed."
    "She gives us a wry smile, despite herself."

    $ bgm (10)
    $ char ('tas024')

    voice as0794
    asumi "What a gang..."
    yusuke "Heh heh..."
    "I think we'll break her wall, but a moment later, she stares at us again."

    $ char ('tas007')

    voice as0795
    asumi "I still won't admit it! I'll do it by myself!"
    yusuke "Yah, yah. Go ahead!"
    "She looks vexed at our response."
    "We studied her personality and made plans."
    "I guess she learns her lesson."

    $ music_stop ()
    $ char ('tas033')

    "Asumi clams up for a while."
    "Suddenly, she claps her hands and tells us,"

    $ bgm (5)
    $ char ('tas005')

    voice as0796
    asumi "Yeah! We should think of a nice one together!"
    yusuke "Think about what?"
    "Her answer disgusts us."

    voice as0797
    asumi "Our team name!! Even the pert neighbors have one, 'The Trio de Bitches.'"
    yusuke "You call them that, they don't..."

    $ char ('tas036')

    voice as0798
    asumi "You! Did you say something?"
    yusuke "N...nothing! But I don't think we need a team name."

    $ char ('tas005')

    voice as0799
    asumi "Are you nuts? This is very important! Umm...let me see..."

    $ char ('tas033')

    "She's seriously thinking."
    "The moment Tomoe and I look at each other to stop this stupid idea,"

    $ char ('tma011')

    voice ma0195
    marumu "Marutan's Pirates."
    yusuke "Marutan, that's not good..."
    "In fact, I really want to say, 'What are you saying?'"
    "It sounds like everyone is willing to go with the name!"
    "But it's too late."

    $ char ('tas005')

    voice as0800
    asumi "Simple is best! The name is, 'Friendship Rangers: Harukaze 3!'"

    voice to0374
    everyone "Hell no!"

    $ char ('tas002')

    voice as0801
    asumi "It's decided by the selfish leader. My color is red."
    "She's already decided her color."
    "Sure, we all agree Asumi's selfish, but..."
    yusuke "She's really pushy..."

    $ char ('tto002')

    voice to0375
    tomoe "If I can chose a color, I like white..."

    $ char ('tma008')

    voice ma0197
    marumu "Magenta..."
    "I'm the only one left against her idea."
    "The tremendous impact of her selfishness!"
    "The tremendous impact of her power!"
    "Yet, there's one thing I can't agree with."
    yusuke "Then, we should change the name..."

    $ char ('tas013')

    voice as0802
    asumi "Yusuke, you're 'Servant 1.'"
    "Mine is promptly decided."

    $ char ('tts002')

    voice ts0055
    toshibo "Meow!"

    $ char ('tas013')

    voice as0803
    asumi "Hey, Servant 2! You stay here this time!"

    $ char ('tto016')

    voice to0376
    tomoe "We're counting on you Toshi...oops, Servant 2."
    "Servant 2 is Toshibo."
    yusuke "How did this happen...?"

    $ bgfx ('sora08')

    "It doesn't matter now."
    "Feeling disgusted, I break into a smile."
    "Their relationship is back to normal."
    "I'm happy to see them like that!"


    call ep_middle from _call_ep_middle_5

    $ bgfx ('sora02')
    $ bgm (5)

    "'Friendship Rangers: Harukaze 3' is now activated."
    "I still don't like the team name."
    "Asumi does her own thing as usual."
    "Red (she makes us call her that) sometimes gives us orders."

    if F015 == 0:
        jump episode24_asumi_c

    elif F015 == 1:
        jump episode24_tomoe_c

    elif F015 == 2:
        jump episode24_marumu_c

label episode24_d:

    $ char ('tas036')

    voice as0806
    red "I said don't call me Asumi... Oh, Ms. Yagami!"

    $ char ('tyo001')

    voice yo0175
    yagami "Can I talk to you a minute?"
    "She takes us to her office."

    $ bgfx ('black')

    "I think she's going to preach to us about Hikaru."
    "My premonition is half right."

    $ bg ('bg04a')
    $ char ('tas021')
    $ bgm (4)

    asumi "......"
    yusuke "Ah..."

    $ char ('tyo001')

    voice yo0176
    yagami "You guys have been bothering Hikaru."
    yusuke "It...it's not that..."
    "I try to offer an excuse, but Asumi interrupts."

    $ char ('tas006')

    voice as0807
    asumi "Yes, we're bothering her! But I can't leave her alone..."
    "Ms. Yagami smiles at Asumi."

    $ char ('tyo007')

    voice yo0177
    yagami "I can't help you, but hang in there!"
    yusuke "Huh?"

    $ char ('tas002')

    voice as0808
    asumi "Th...thank you very much!"
    "I'm still confused."
    "New enthusiasm is breathed into her."

    $ bgm (5)
    $ char ('tas007')

    voice as0809
    asumi "All right! We've got the commander's permission, so we'll show more spirit! Let's go, Servant 1."
    yusuke "O...okay."
    "Who's the commander, anyway? I'm bewildered."

    call blackout from _call_blackout_29
    $ bgfx ('sora01')

    "A day after starting to get tired of the Friendship Rangers' activities,"
    "I go up to the rooftop to get refreshed."
    "Hikaru and I run into each other."
    "I should talk to her."

    $ bgfx ('bg07a')

    yusuke "Hi, Hikaru..."
    hikaru "......"
    "She ignores me. She doesn't even look at me."
    "But I continue to talk,"
    yusuke "I know it's none of my business, but Asumi and the others are trying hard..."
    hikaru "......"
    yusuke "......"
    "She walks towards me."
    "Oh well. She passes by me and...what?"

    $ char ('thi001')

    "She stops in front of me."
    "She grabs my hand and pulls it close to her."

    $ bgfx ('black')
    $ bgm (8)

    yusuke "H...hey..."
    hikaru "......"
    "A place unseen by others."
    "She drags me over and does something unbelievable."
    "She starts taking her clothes off."
    yusuke "Wha...what are you doing? Stop..."
    hikaru "......"
    yusuke "Stop doing such a thing..."
    "However, I can't look away from her."
    "This isn't good."
    "Feeling troubled, I step back."
    "Then Hikaru calmly tells me,"

    voice hi0008
    hikaru "If you back off any further, I'll scream."
    yusuke "Hikaru..."
    "All I can do is simply stare at her, like a frog being stared at by a snake."

    $ bgfx ('bg07a')
    $ char ('thi010')

    "Now, she's naked and moves closer to me."
    "And she whispers,"

    voice hi0009
    hikaru "Love me..."
    yusuke "What...!?"

    voice hi0010
    hikaru "Love me..."
    yusuke "But why?"
    "What should I do? I'm thrown into confusion."
    "She coldly looks at me."

    $ char ('thi012')

    voice hi0011
    hikaru "Just because... You'll comfort me, right?"
    yusuke "Ah...well. Become friends with Asumi and me..."

    voice hi0012
    hikaru "Are you trying to help me? Then, do it."
    yusuke "Yeah, but I mean..."

    voice hi0013
    hikaru "Love me, please... If you can't, I'll..."
    yusuke "Gulp..."
    "I have a bad feeling about this...and I'm right."

    voice hi0014
    hikaru "I'll kill myself right here."
    yusuke "Uh...mmm..."
    "Hearing such desperation, I can't refuse her."
    "I get irritated, excited, and dizzy."
    "I'm almost in a panic."

    $ char ('thi010')

    voice hi0015
    hikaru "Please...touch me."
    yusuke "......"

    voice hi0016
    hikaru "You won't even touch me...?"
    yusuke "......"

    $ char ('thi012')

    voice hi0017
    hikaru "You're the same. You're afraid of touching me."

    voice hi0018
    hikaru "Touch me and get hurt...and it will remain a scar."

    voice hi0019
    hikaru "If you don't want to get hurt, don't come close to me anymore..."

    voice hi0020
    hikaru "You're afraid of me, aren't you?"
    yusuke "I...I'm not..."
    "I don't want her to feel sad anymore."
    "Or maybe I don't want to be sad..."
    "I hesitantly stretch my hand out to her..."
    "I'll lose if I withdraw."
    "I feel that way."

    $ char ('thi010')

    voice hi0021
    hikaru "You have the courage to touch me...ahh."
    yusuke "......"
    "She should be warm."
    "But she feels cold to touch."
    "Fascinated, she looks at me."

    voice hi0022
    hikaru "You have the courage to accept me...even a naive person like you."
    yusuke "......"
    "I touch her breast with my palm."
    "She feels my hand."

    $ char ('thi012')

    voice hi0023
    hikaru "Hmm...your hand is warm..."
    yusuke "Uh...mmm..."

    voice hi0024
    hikaru "Warm me up with your hands, though it will only last a moment."
    "What should I do?"
    "What can I do?"
    "I feel guilty but also desire."
    "With those mixed feelings, I continue to touch her."
    "On her white, smooth skin like snow."

    voice hi0025
    hikaru "Ah...aahh..."

    voice hi0026
    hikaru "Umm...yes...ahh...ahhh..."

    voice hi0027
    hikaru "Umm...harder...yes...do whatever you want..."

    voice hi0028
    hikaru "Ahh...mmm...more..."

    voice hi0029
    hikaru "You don't need to hold back...yes...ah, ahh..."
    "With my hands and mouth."
    "Before I'm aware of it, I'm completely enraptured with her."
    "A hickey remains on her breast."
    "She holds her arms out to me."
    "Then she pulls me close to her."

    $ char ('thi010')

    voice hi0030
    hikaru "Accept me and warm me up, though it won't last forever."
    yusuke "Gulp!"

    voice hi0031
    hikaru "Come...please..."

    menu:
        " "
        "Remain calm":

            jump episode24_e
        "Have sex with her":

            pass

label episode24_sex:

    $ cg ('hh_0101')
    $ unlock_gallery ('g4e9')

    yusuke "Umm...ahh...mmm..."

    voice hi0032
    hikaru "Yes...ahh...do me harder..."
    "I bring my mouth to her firm breasts, licking them, running my tongue over her."
    "Sliding my finger in her wet pussy, I pull out and then shove back inside her."
    "She accepts me without any resistance."

    voice hi0033
    hikaru "Oh, yes...yes...deeper...aahhh..."

    voice hi0034
    hikaru "Ahh...mmm...harder...harder..."
    yusuke "Hmm...oohhh...."
    "I've never felt like this before."
    "I feel like I'm falling."
    "Falling into pleasure, a world of corruption."
    "I want to do this forever, though I'll lose everything... She makes me feel like that."

    $ cg ('hh_0102')

    voice hi0035
    hikaru "Umm...ah, ahh...aahhhh..."

    voice hi0036
    hikaru "Ah..ahh...mmm..."
    yusuke "Ohh...ugh..."

    $ say_hide ()
    $ cg ('hh_0103')
    $ bgfx ('white', diss_long)
    $ bgfx ('black', diss_long)
    $ music_stop ()

    "We both cum together."
    "I've never felt such hot, ardent ecstasy."
    "However, it's left a bad taste..."
    "It's completely different when I make love with my lover."
    "Shame."
    "Guilt."
    "Regret."
    "Those words are running around in my head, and I feel miserable."
    "I'm dazed for a while."
    "On the other hand, she's putting her clothes on."
    "Then she thanks me."

    $ bgfx ('bg07a')
    $ char ('thi001')

    voice hi0037
    hikaru "Thanks...I feel better now."
    yusuke "......"
    "I recall what I'm trying to do."
    "Open her heart and alleviate her sorrow..."
    "But her eyes refuse me."

    $ char ('thi002')

    voice hi0038
    hikaru "Nothing has changed...I'm still the same."

    voice hi0039
    hikaru "But you're different...I think you lost something important."
    yusuke "What...!?"

    $ char ('thi009')
    $ bgm (9)

    voice hi0040
    hikaru "You look sad...heh heh."
    "I see her smile for the first time."
    "It's a cold smile, colored with negative feelings."
    "She placed part of her sorrow in my mind."
    "I'm chilled with the illusion."

    $ char ('thi004')

    voice hi0041
    hikaru "The thing you lost will never return as long as you live..."
    yusuke "Ugh..."
    "I want to cry."
    "Actually, I am crying. Then she walks away."

    $ char ('thi002')

    voice hi0042
    hikaru "Goodbye..."
    "Seeing her off, I feel as if I've walked onto the road to hell."

    $ bgfx ('black')

    "I can't love the person I really love with my dirty hands anymore."
    "I feel a tightness in my chest."
    "I'm thrown into deep despair."

    $ music_stop ()

    jump game_over

label episode24_e:

    call blackout from _call_blackout_30

    "Her arms reach out to hold me."
    "I feel fear through her arms."
    "Then I look at her wrist."
    "I see a big scar."
    "She got it trying to kill herself."
    "I've been delirious, but I'm gradually calming down."
    "I softly push her arms down."

    $ bgfx ('bg07a')
    $ char ('thi010')
    $ bgm (9)

    yusuke "......"

    voice hi0043
    hikaru "What's...wrong?"
    yusuke "I can't..."
    hikaru "......"
    yusuke "I can't do this! We shouldn't!"
    "I pull myself together and tell her."
    "I was losing control."
    "Her scar brought me back."
    yusuke "I can't lie or betray anyone any further..."

    $ char ('thi012')

    if F015 == 0:

        voice hi0044
        hikaru "Because of her...? Your girlfriend, Asumi?"
        yusuke "If Asumi were to find out about this, she would be really mad...and hurt."

    elif F015 == 1:

        voice hi0102
        hikaru "Because of her...? Tomoe Katsuragi?"
        yusuke "If she were to find out about this, she would be hurt."

    elif F015 == 2:

        voice hi0103
        hikaru "Because of her...? Marumu Ogumayama, right?"
        yusuke "If she were to find out about this, she would be sad. She might not cry, but she would be hurt."

    voice hi0045
    hikaru "So...you can't betray her..."
    yusuke "No..."
    "I shake my head side to side."
    "Looking straight at her, I clearly say,"
    yusuke "I can't betray myself."

    $ char ('thi010')

    voice hi0046
    hikaru "Yourself...?"
    "Confused, she looks at me."
    "Looking the other way, I continue talking,"
    yusuke "I can't do this. Because I don't love you..."

    $ char ('thi012')

    voice hi0047
    hikaru "Hypocrite..."
    yusuke "You can't betray yourself either! You don't want me to do this."
    "I pick her clothes up and hand them to her."
    "She receives them without saying anything."
    yusuke "You'll catch a cold..."

    $ char ('thi010')

    hikaru "..."
    hikaru "......"
    "She doesn't threaten me and quietly sees me off."

    call blackout from _call_blackout_31
    $ bgfx ('sora01')

    "That was a horrific experience."
    "Hikaru's attitude has changed since that day."
    "She sometimes stares at me."
    "I don't think she's opened her heart yet."
    "She looks even tougher than before."
    "It seems as if she's watching us."

    if F015 == 0:
        jump episode24_asumi_f

    elif F015 == 1:
        jump episode24_tomoe_f

    elif F015 == 2:
        jump episode24_marumu_f

label episode24_g:

    call blackout from _call_blackout_32
    $ bgfx ('sora01')

    "The next day, after school."
    "All of us are waiting for Hikaru at the gate."
    "The plan we made last night is hard-core."
    "But we execute it, anyway."
    "People sometimes need to be forcible...yet I feel a little nervous."

    $ bgfx ('bg06a')
    $ char ('thi004')
    $ bgm (5)

    hikaru "......"
    "Hikaru finally shows up."
    "She has to go through this gate to go home."
    "Asumi calls out to us,"

    $ char ('tas007')

    voice as0830
    red "White, Magenta, Servants...we'll carry out the Friendship Rangers' last mission!"

    $ char ('tma008')

    voice ma0198
    magenta "Yeah!"

    $ char ('tto013')

    voice to0377
    white "I...I'll do my best!"
    servant1 "All right."

    $ char ('tts002')

    voice ts0056
    servant2 "Meow!"
    "Tomoe and I still feel embarrassed."
    "Now, we perform our duty."

    $ char ('thi004')

    voice hi0053
    hikaru "H...hey, you guys... Wh...whaaaaa!!"

    $ bgfx ('black')

    "Hikaru is forcefully taken by four people and a cat."
    "She's taken to..."

    $ music_stop ()
    $ bgfx ('bg13a')
    $ char ('thi001')

    hikaru "......"

    $ char ('tas002')
    $ bgm (3)

    voice as0831
    asumi "Welcome to the Harukaze Dormitory!"

    $ char ('tto025')

    voice to0378
    tomoe "We'll live together starting today."

    $ char ('tma008')

    voice ma0199
    marumu "Welcome..."

    $ char ('tts002')

    voice ts0057
    toshibo "Meowww!"
    yusuke "Another person knows my secret...oh my..."

    $ char ('thi004')

    "However, Hikaru stares at us with piercing eyes."
    "With annoyed, angry eyes."

    voice hi0054
    hikaru "What the hell is this?"

    $ char ('tas005')

    voice as0832
    asumi "If you don't want to go home, don't go home then."

    $ char ('tto025')

    voice to0379
    tomoe "We'll live together...so we can share sad and happy things together."

    $ char ('tma001')

    voice ma0200
    marumu "Friends."
    "Hikaru's confused at what she hears."

    $ music_stop ()
    $ char ('thi006')

    voice hi0055
    hikaru "Friendship? I don't need such an uncertain thing..."

    voice hi0056
    hikaru "Don't put me in your stupid circle of friends. You're kidding, right?"

    $ char ('tas044')

    voice as0833
    asumi "This isn't a joke. We're serious."

    $ char ('thi004')

    hikaru "......"
    "Looking at us, Hikaru realizes this isn't a joke."
    "That's why she desperately turns on us."

    voice hi0057
    hikaru "Idiots...all of you are idiots. You kidnapped me..."

    voice yo0178
    yagami "That wasn't kidnapping, Hikaru."

    $ char ('tyo001')
    $ bgm (4)

    "A soft mature voice...it's the commander...no, it's Ms. Yagami."
    "Hikaru looks agitated."

    $ char ('thi001')

    voice hi0058
    hikaru "Ms. Yagami..."

    $ char ('tyo019')

    voice yo0179
    yagami "Oh, I like to be called that. It sounds so polite."
    "She looks happy."

    voice yo0180
    yagami "Some students call me 'Yoshiko.' I feel I don't have any respect from students."

    $ char ('tas006')

    voice as0834
    asumi "But they're just being friendly. Besides, you've never complained about it."

    $ char ('tto002')

    voice to0380
    tomoe "Cough..."

    $ char ('tyo019')

    voice yo0181
    yagami "Oh, I'm digressing from the subject."
    "Tomoe brought her back."
    "Ms. Yagami tells Hikaru,"

    $ char ('tyo015')

    voice yo0182
    yagami "Anyway Hikaru, I already told your family that you'll be living in this dorm starting from today."

    $ char ('thi001')

    hikaru "......"
    "Hikaru's more flabbergasted than disgusted."
    "She didn't think even her homeroom teacher would go this far."
    "Ms. Yagami...she's a cool teacher."

    $ music_stop ()
    $ char ('thi002')

    "Hikaru tries to say something but stops."
    "Her parents already agreed. She has to challenge them to reverse their decision."
    "That's the last thing she wants."
    "She gives up in despair."
    "There's no place for her to go. She has to live here."
    "We all hope she'll change with this experience."
    "Of course, we'll help her."

    $ bgm (13)

    yusuke "By the way, where will she live?"

    $ char ('tyo013')

    voice yo0183
    yagami "Good question. Asumi's room is full..."

    $ char ('tas005')

    voice as0835
    asumi "Don't worry! I know a place she can comfortably live!"
    yusuke "Where?"

    $ bgfx ('black')

    "Asumi mentions Namiki's room."

    $ bgfx ('bg09a')
    $ char ('tna019')
    $ bgm (7)

    voice na0208
    namiki "What? Wait!"

    $ char ('tma001')

    voice ma0201
    marumu "A new arrival."

    $ char ('thi001')

    hikaru "......"

    $ char ('tna022')

    voice na0209
    namiki "Are you planning to bother my comfy, quiet life? Are you going against the older sister?"

    $ char ('tma008')

    voice ma0202
    marumu "Older..."

    $ char ('tna023')

    voice na0210
    namiki "Ugh..."
    "Hikaru was held back an extra year."
    "She's one year older than us."
    "Hikaru's the oldest."
    "Namiki makes us call her 'Sis,' but she's the same age as us."
    "However, she won't give up so easily."

    $ char ('tna018')

    voice na0211
    namiki "If that's the case, I want to live with Moe-Moe."

    $ char ('tto007')

    voice to0381
    tomoe "Sorry, Namiki."

    $ music_stop ()
    $ char ('tna023')
    $ empat ('j5')

    namiki "......"

    $ bgfx ('sora08')

    "The resistance is futile."
    "Namiki collapses in despair."
    "Our plan succeeds, though not quite satisfactorily."

    $ empat ()
    $ bgm (14)
    $ bgfx ('bg09c')

    "Asumi greets Hikaru with cheers."

    $ char ('tas002')

    voice as0836
    asumi "Anyway, we're happy to have you!"

    $ char ('thi004')

    voice hi0059
    hikaru "Humph..."
    "Hikaru still wears her poker face."
    "But I feel the dark shadow in her begin to fade out."

    if F015 == 2:

        jump episode24_marumu_g

label episode24_end:


    call ep_finish from _call_ep_finish_4

    $ renpy.end_replay()
    $ unlock_episode (24)

    jump episode25
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

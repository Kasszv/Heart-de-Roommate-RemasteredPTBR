label episode19_tomoe:

    $ bgfx ('bg03b')

    "On my way home after school, I see Tomoe heading to the shopping center."
    "I remember we're short on a few things."

    $ bgm (3)

    yusuke "Tomoe!"

    $ char ('tto025')

    voice to0606
    tomoe "Oh, Yusuke."
    "She smiles all over."
    "I talk to the lovely Tomoe."
    yusuke "Shopping again, right?"

    $ char ('tto001')

    voice to0607
    tomoe "Come with me again, alright?"
    yusuke "Yes, but of course!"

    $ char ('tto025')

    voice to0608
    tomoe "He he, thanks!"

    $ bgfx ('sora05')

    "We walk together to the shopping center."
    "It's a 'regular date like newly weds.'"
    "Walking side by side, we talk about various things."
    "We talk about Tomoe now."

    $ bgfx ('bg03b')
    $ char ('tto001')

    yusuke "I guess you're a caring person. You accept other's requests, including troublesome jobs."

    voice to0609
    tomoe "Do you think so? But I like it...I feel it's my role."
    "That's why people take advantage of her...I'm the same kind of person."
    "But from now on, we can be stronger!"
    "I let her know how I feel."
    yusuke "No, you should stop it! Asumi's the sort of girl who'll take advantage of you."

    $ char ('tto013')

    voice to0610
    tomoe "She's not like that. Marutan is a good girl, too."
    yusuke "She's a 'good' girl? Whatever..."
    "Looking up at the autumn sky, she recalls her past."

    $ char ('tto025')

    voice to0611
    tomoe "I love them. They're my first best friends..."
    yusuke "I see...but why are you girls so close?"

    voice to0612
    tomoe "What do you mean 'why?'"
    yusuke "You girls are totally different. I think you're an odd trio, by all means."

    $ char ('tto002')

    voice to0613
    tomoe "Umm... We weren't close like this in the beginning."
    yusuke "Really? Tell me how you girls met and became friends."

    $ char ('tto004')

    voice to0614
    tomoe "Okay. It was really tough..."

    call blackout from _call_blackout_56

    "She sighs and starts telling me the story."
    "Life was hard; all the way up until then."


    call ep_middle from _call_ep_middle_9

    $ bgm (8)

    "The beginning was painful."
    "To be honest with you, I was so nervous with Asumi and Marumu."

    $ bgfx ('bg19a')
    $ chars ('tas711', 'tma625')

    voice as0986
    asumi "Hi, my name is Asumi Hirota! Nice to meet you."

    voice ma0133
    marumu "Hello..."

    voice to0269
    tomoe "N...nice to...meet you too..."
    "I wasn't sure if I could live with them."

    $ bgfx ('black')
    $ bgfx ('bg19a')
    $ char ('tas712')

    "Asumi spoke so frankly and was really pushy."
    "When she said something in a loud voice, I would unintentionally apologize to her."
    "She was irritated by my timid, faint-hearted attitude. "
    "I knew how she felt, that's why I was even more nervous."

    voice as0987
    asumi "Why did it happen!?"

    voice to0615
    tomoe "I...I don't know..."

    voice as0988
    asumi "Come on! Be more steady!"

    voice to0616
    tomoe "O...okay."

    $ bgfx ('black')
    $ bgfx ('bg19a')
    $ char ('tma625')

    "And I didn't understand what Marumu was thinking at all."
    "Though I talked to her, we didn't have any conversations."
    "She replied with signs, but I had no idea what she was trying to say."
    "It was harder to communicate with her than Asumi."

    $ bgfx ('black')

    "However, I felt more relaxed with Marumu than Asumi because I was so shy."
    "Asumi always said,"

    $ bgfx ('bg19a')
    $ char ('tas712')

    voice as0989
    asumi "We're roommates! We should be strong!"

    voice to0617
    tomoe "I guess so..."

    voice as0990
    asumi "Don't guess, just do it! Our days of youth are short!"

    $ bgfx ('black')

    "She was always like that."
    "I didn't want to count on my sister like a little kid any longer."
    "That's what brought me to live in this dorm in the first place."
    "But I didn't enjoy living with them."
    "I even asked Ms. Yagami to relocate me to a different room."

    $ bgm (13)
    $ bgfx ('bg19b')
    $ char ('tyo003')

    voice to0618
    tomoe "Ms. Yagami, I would like to talk about it again..."

    voice yo0211
    yagami "I guess it isn't working out right, yet. But please hang in there a little bit longer."

    voice yo0212
    yagami "I'll bet you girls will be able to get along with each other. Stronger bonds are made by completely different personalities."

    voice to0619
    tomoe "I see..."
    "I didn't believe her at the time. Of course, I believe her now."

    call blackout from _call_blackout_57

    "And then, Asumi finally exploded."
    "She was irritated and mad as hell."

    $ bgfx ('bg19a')
    $ char ('tas712')

    "She said, 'We'll fight to decide who the leader is.'"
    "Of course I didn't want to do that."
    "Marumu didn't want to either."

    voice as0676
    asumi "The person who wins becomes the leader! The others have to obey her, okay?"

    voice to0273
    tomoe "B...but I can't do that..."

    voice ma0135
    marumu "No way..."

    voice as0677
    asumi "Shut up! Are you ready?"

    $ bgfx ('black', cls=True)
    call cgeffect ('SE10', KENKA2, sound_loop=True) from _call_cgeffect_6
    $ bgm (9)

    "I cried. I cried a lot."
    "But I counterattacked Asumi without realizing it."
    "I desperately thrashed out with my arms and legs."
    "I felt I had to do this."
    "Otherwise, this fight wouldn't end."
    "That's why I did it."

    $ audio_stop ()
    $ bgfx ('bg19a')
    $ chars ('tas713', 'tma626')

    voice to0274
    tomoe "...Hic...hic..."
    marumu "......"

    voice as0678
    asumi "You girls are good fighters, heh heh."
    "Asumi was smiling."
    "She looked so happy."
    "I hadn't seen her smiling like that before."
    "But our hair was totally messed up."
    "We all looked like we had bird nests."
    "Then..."

    voice as0679
    asumi "Wait here!"
    "Asumi ran back to her room."
    "She came back holding something in her hand."

    $ bg ('bg19a')
    $ ev ('raf_23')
    $ bgm (10)

    voice as0680
    asumi "These are for you, girls!"

    voice to0275
    tomoe "For me..."
    marumu "......"
    "She gave me a large scarf."
    "Marumu got two round hair pins."

    voice as0681
    asumi "Are these pretty or what? Yellow brings happiness to people."

    voice to0276
    tomoe "Really..."
    marumu "......"

    $ bg ('bg19a')
    $ chars ('tto719', 'tma627')

    "I was happy about the present."
    "We had the same color of hair accessories...I felt like we'd became real friends."
    "That wasn't the only time I felt like that."
    "I've felt like that since then."

    $ cg ('raf_24')

    "That was the first day we laughed together."
    "And that was the day we became 'roommates.'"
    "Everything started from that day."

    call blackout from _call_blackout_58
    $ bgfx ('bg12b')
    $ char ('tto001')

    voice to0620
    tomoe "That's how we became best friends..."
    "She tells me the story while we shop."
    "As I listen to her long story, I finally understand the origin of their friendship."
    yusuke "Asumi hasn't changed at all. But..."
    "I look at the scarf tied to her hair."

    $ bgm (10)

    yusuke "Is that the one Asumi gave you?"

    $ char ('tto025')

    voice to0621
    tomoe "Yes...my lucky charm."

    voice to0622
    tomoe "She was right. Yellow brings happiness to people."
    yusuke "Tomoe..."
    "Perhaps it's a good thing that Tomoe met Asumi."
    "I met Tomoe because she's one of Asumi's roommates."
    "Honestly... Yellow brings happiness to people."

    jump episode19_b
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

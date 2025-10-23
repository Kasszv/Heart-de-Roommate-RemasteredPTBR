label episode16:

    $ Fnum = 16
    $ save_name = "Episode 16: Love Storm"


    call ep_start from _call_ep_start_22

    $ cg ('e3_0309', pos=[ALIGN(0.59, 0.0)])
    $ sfx ('SE15')
    $ bgm (12)

    voice na0198
    namiki "Hmm, this hot spring is the best!"

    $ sfx ()

    voice as0547
    asumi "Hey, what are you doing here? This is our regular meeting!"

    voice na0199
    namiki "Because I'm the brains."

    $ cg ('e3_0310', pos=[ALIGN(0.59, 0.0)])

    voice ma0116
    marumu "Here comes our brains, Marumu."

    voice to0259
    tomoe "Girls, stop fighting..."
    "This is an unbelievable sight. "
    "Just how is it that I can be with these girls in a hot spring?"
    yusuke "Because I'm one of their roommates, I guess."

    voice ts0038
    toshibo "Meow!"
    yusuke "Hey, you. It's been a while."
    "The four girls (plus a cat) and I come to the hot spring together."
    "All the guys envy me for sure."
    "Even Misaki couldn't do this!"
    "I'm the luckiest man in the world!"

    if F015 == 0:
        jump episode16_asumi

    elif F015 == 1:
        jump episode16_tomoe

    elif F015 == 2:
        jump episode16_marumu

label episode16_b:

    call blackout from _call_blackout_140
    $ bgfx ('sora05')

    "After school."
    "I have something I've got to do."
    "I've finally gotten used to changing my clothes in the men's restroom."
    "Tomoe would say, 'If you'd take better care of your appearance, you'd look cuter.'"
    yusuke "Okay, nobody is here."
    "This is the scariest moment."
    "The moment I leave the men's room."
    "If someone sees me, there'll be hell to pay!"
    "Once, I thought of changing my uniform in the girls' restroom, but I have to go in with men's clothes on."
    "If I were to run into a girl, just think of the problems it would cause."
    "I look out from between the door and the wall."
    "Then I make a mad dash to the hallway, where I don't think anyone is."

    $ bgfx ('bg05b')
    $ char ('tyu002')

    yusuke "Whaaa!"

    voice yu0022
    akane "Yikes!"

    $ bgm (7)

    "Someone is here!"
    "I almost crash into the person running down the hallway."
    "I avoid the collision, but it's still bad... Oh, shit!"

    $ bg ('bg05b')
    $ char ('tyu003')

    "A female student looks at me."
    "Ms. Yukimura, one of the 'Trio de Bitches' who lives next door."
    "She's the one who's suspicious of me being in Asumi's room."
    "How come SHE saw me running out of the men's room?"

    menu:
        " "
        "Apologize to her.":

            pass
        "Think of an excuse.":

            jump episode16_b_continue

    $ music_stop ()
    $ char ()

    yusuke "Whaaa! I'm sorry, I'm sorry! This is all my fault. I live in the girls' dorm! I'm so sorry!"
    yusuke "I didn't have any other place to live! I'm sorry, so sorry...oh?"

    $ bgfx ('sora07')

    "Ms. Yukimura is already gone."
    "She didn't hear what I said...but,"

    $ bgm (9)

    "Two people are standing there looking at me."
    "The vice principal and the supervisor."
    "And they listened to my confession."
    "I, Asumi, and the other girls had a hard time keeping our secret."
    "I dug my own grave so easily... I'm such a dumb-ass!"

    call blackout (True) from _call_blackout_141

    jump game_over

label episode16_b_continue:

    yusuke "Ah...well..."

    $ bg ('bg05b')
    $ char ('tyu004')

    voice yu0023
    akane "I...I've got to go..."
    yusuke "Huh...?"

    $ bgfx ('bg05b')
    $ sfx ('SE13', loop=True)

    "I was thinking of an excuse, but I feel deflated."
    "Then, she runs away."

    $ sfx (delay=1.0)

    "Phew, I'm glad...no, wait!!"
    yusuke "I don't think she would...but..."
    "Will she go to the teacher's office and rat on me?"
    "Students once talked about me as the mysterious girl at school."
    "Even I think a girl coming out of the men's room is weird."
    yusuke "Hey, wait. Wait a minute."
    "I run after her."
    "It's not easy to run in a skirt."

    call blackout from _call_blackout_142

    yusuke "Wait...oh?"
    "She disappears into one of the classrooms."
    "This is her classroom."
    "I thought she was going to go to the teachers' office."
    yusuke "I'm just imagining things. She might have forgotten something... Hmm?"
    "I can hear a ruckus from inside."
    "It sounds like arguing."
    "It's not my business, but..."
    "I'm standing here, anyway."
    "So I might as well take a peep... I quietly open the door a little."
    "To see what's going on inside."

    $ bgm (8)
    $ bgfx ('bg04b')
    $ chars ('tyu004', 'tmi001')

    voice yu0024
    akane "...Say yes, please?"
    misaki "...No."
    yusuke "Misaki! Why is he here...!?"
    "I almost speak up."
    "I slap my hand over my mouth and continue peeping."

    voice yu0025
    akane "Misaki...are you seeing someone?"
    misaki "......"

    $ char1 ('tyu002')

    voice yu0026
    akane "You're seeing someone, right? That's why..."
    misaki "Sorry..."

    $ char ('tyu002')

    voice yu0027
    akane "Hold on please..."
    yusuke "(This situation is...)"
    "Ms. Yukimura is confessing her feelings to Misaki, and he's turning her down."
    "I didn't expect to see this."
    "She's a bitch, but I feel sorry for her when I see her sad face."
    "Misaki...he's a dick!"
    "He could have said something nice to her... Oops!"

    $ music_stop ()
    $ bg ('bg05b')
    $ char ('tmi001')

    "He almost catches me."
    "I immediately run away and hide behind the wall, thinking I don't like him at all."
    "I try to recall why I don't like him."

    if F015 == 2:
        jump episode16_marumu_b

    $ bgfx ('black')
    $ bgfx ('bg07a')
    $ chars ('tas001', 'tmi001')

    misaki "Hmm...?"
    "Is this deja vu?"
    "It was a long time ago, at the end of the first semester."
    "I have a bad taste in my mouth."
    "There are only two people on the rooftop."
    "Misaki and Asumi, smiling."
    "I saw the same situation before..."

    $ bgm (16)

    misaki "......"
    yusuke "(I just think he's an ass!)"

    $ char ('tmi001')

    "Misaki passes by me with a snobbish glare."
    "I finally remember why I don't like him."

    $ music_stop ()

    if F015 == 0:
        jump episode16_asumi_b

    elif F015 == 1:
        jump episode16_tomoe_b

label episode16_c:

    $ bgfx ('bg01c')
    $ char ('tas051')
    $ bgm (7)

    voice as0561
    asumi "Boo! Ah ha ha ha! He finally told you. Ha ha ha...ouch, my stomach hurts. Ha ha ha."
    yusuke "You knew about this, didn't you?"
    "She continues to laugh as if she's been waiting for this to happen."
    "She knew this a long time ago."
    "Misaki loves me, the girl Yusuke."

    voice as0562
    asumi "Because... Ha ha ha ha!"
    "Still laughing, she starts to explain."

    $ bgfx ('black')

label episode16_c2:

    "Misaki asked Asumi about me at the end of last semester."
    "He wanted to know who the girl with glasses was that came to school with her."
    "Of course she didn't tell him about the girl."
    "If she did, she'd expose the secret."
    "Yet, he seriously asked her again and again."
    "She was impressed and told him about me little by little."
    "The story she made up about me..."

    $ cg ('es_0107')
    $ bgm (14)

    "NAME: Sakurako Yamanobe"
    "HEIGHT: 5'5 WEIGHT: 115lb (She made it up!)"
    "VISION: 20/60 (It's a lie.)"
    "HOBBIES: Gardening, home repairs, and collecting teddy bears."
    "FAVORITE FOOD: Extra spicy garlic noodles and spaghetti with beans."
    "NOTE: Due to her morbid fear of meeting people, she's taking counseling and regular classes in a special classroom."

    $ music_stop ()
    $ bgfx ('bg01c')
    $ char ('tas005')

    voice as0563
    asumi "What do you think? Isn't she unique and cute?"
    yusuke "That's awful. If he finds out it's also a lie, what will you do?"

    $ char ('tas027')

    voice as0564
    asumi "He'll never find out...or so I thought."
    "Still chuckling, she quietly tells me,"

    $ char ('tas043')

    voice as0565
    asumi "I didn't expect him to tell you how he feels about you. I thought he would get over it without ever saying anything."
    yusuke "It was totally a surprise."

    $ char ('tas051')

    voice as0566
    asumi "Yeah... Pooh, ha ha ha...but it's so funny!"

    $ bgm (7)

    "She starts laughing again."
    "She doesn't feel any responsibility about causing this complex situation."
    yusuke "What are you going to do? What should I do tomorrow?"
    yusuke "He said, 'Please consider my offer. I'll wait until you're ready.'"

    $ char ('tas001')

    voice as0568
    asumi "Then think about his offer by yourself. You don't need to hurry, right?"
    yusuke "Yeah, but... Whatever!"

    if F015 == 0:
        jump episode16_asumi_c

    elif F015 == 1:
        jump episode16_tomoe_c

    elif F015 == 2:
        jump episode16_marumu_c

label episode16_d:

    call blackout from _call_blackout_143

    "I somehow feel comfortable with him looking at me everyday. This is definitely not good."
    "I can feel his sincere, passionate feelings."
    yusuke "I'm not sure I can control myself any longer."
    "Thinking about him, I look at the hill far away...oh?"
    yusuke "Dark clouds are coming this way."

    $ bgfx ('bg05e')

    "My forecast is right."
    "Rain starts before school is over."
    "It began as a sprinkle, but it's raining cats and dogs after school."
    yusuke "If I'd known this would happen, I should have asked someone to wait for me."
    "I have to get wet."
    "Who knows when it will stop... Shit!"
    "A male student is walking towards me."
    "He's the last person I want to see."
    "I hurriedly look for somewhere to hide, but I can't find a place."

    $ char ('tmi002')

    "He stands in front of me."
    yusuke "(Damn it.)"
    misaki "......"
    "I step back at his seriousness."
    "I can't think of anything to say to him."
    "I'm thinking of a way to get out of this mess."
    "I'm just flurried."
    "If I were a girl, I'd look cute, I guess."
    "He suddenly sticks his hand out."
    "As if trying to hit me."
    "I take another step backwards and see something in front of me."
    "It's an umbrella."

    $ bgm (9)

    yusuke "Is...is this for me?"
    misaki "......"
    "He doesn't say yes or no, but he tells me his strong decision."
    misaki "If you honestly tell me what you think of me, I won't bother you again."
    yusuke "Honestly?"
    misaki "If you don't like me...please say so."
    yusuke "I...I... Hey!?"

    $ char ()

    "As I'm thinking what I should say, he runs away."
    "Without an umbrella in the heavy rain."
    "Looking at his back, I murmur,"
    yusuke "If I were a girl...I would have fallen in love with him."

    call blackout from _call_blackout_144

    "I really feel guilty."
    "I want to share this feeling with the ringleader!"

    if F015 == 1:
        jump episode16_tomoe_d

    $ bgm (6)
    $ bgfx ('bg01c')
    $ char ('tas012')

    voice as0572
    asumi "Hey, how's it going lately? Are you getting along with Misaki?"
    yusuke "I'll rape you, you bitch..."

    $ char ('tas002')

    voice as0573
    asumi "Yikes! Even you say something like that. However, I kind of like that idea..."
    yusuke "Huh? Are...are you serious?"

    $ char ('tas037')

    voice as0574
    asumi "Of course I'm just kidding. Do you know what would happen if you were to really do that to me?"
    yusuke "Y...yes, I know."
    "I'm useless before the ringleader."
    "I have to solve this problem alone."
    "This is one thing I can't talk about with the love experts, Ms. Yagami or Namiki."
    "They'd make fun of me for sure."

    $ music_stop ()
    $ bgfx ('sora09')

    "I'm being tormented."
    "I think about it really hard."
    "Because Misaki is serious about me."
    "I can tell from his eyes and attitude."

label episode16_e:

    $ bgfx ('black')

    "What should I do with him?"
    "The answer suddenly jumps out at me."
    "However, I'm not brave enough to do that."
    "Because I'm not ready to give up everything I have now..."
    "I want to avoid him until I make up my mind."
    "I have to pay extra attention to my conduct after school."
    "After I change my clothes in the men's restroom, I slowly open the door and... Augh!"

    $ bgfx ('bg05b')
    $ char ('tmi002')

    "The door is suddenly opened."
    "A guy stands there."
    "I'm surprised at the clear and present danger, but he's even more shocked."
    "I complain to God for placing me in this situation."
    "How could you do this to me?"
    "Misaki is standing there in front of me."

    $ bgm (9)
    $ bgfx ('black')
    $ bgfx ('bg07b')
    $ char ('tmi002')

    yusuke "I think this is it."
    misaki "......"
    "Up on the rooftop, I take my wig off in the autumn wind."

    $ char ('tmi004')

    "He usually wears a poker face, but he looks flabbergasted."
    "The girl that came out of the men's restroom is really a guy. He's still in a state of shock."
    "However, I knew it was coming."
    "No, I should say I was going to do this anyway."
    "The only way to show my faith to him is disclosing the truth."
    "That's the only way."
    "We ran into each other in the men's restroom. It just makes everything clear much earlier than I expected."
    "To expose the truth means to tell him I live in the girls' dorm."
    "Of course, it's going to get me in a lot of trouble."
    "Though I know what will happen to me, I can't lie to him any longer."
    "Because if I were him, I couldn't pull myself together easily."
    "For instance, if I were to find out that Asumi were a man... She sometimes acts like a man."
    yusuke "Misaki...?"

    $ char ('tmi005')

    misaki "Mmm..."
    "His lips seem to curl up."
    "It was just for a moment, and he maintains his usual poker face."
    misaki "I still lack experience."
    yusuke "I don't know about that, but..."

    $ char ('tmi001')

    misaki "I'm sorry to have troubled you..."
    yusuke "Misaki..."

    $ bgfx ('sora05')

    "I want to say something to him."
    "But I can't find the words."

    if F015 == 0:
        jump episode16_asumi_e

    elif F015 == 1:
        jump episode16_tomoe_e

    elif F015 == 2:
        jump episode16_marumu_e

label episode16_end:


    call ep_finish from _call_ep_finish_18

    $ renpy.end_replay()
    $ unlock_episode (16)

    jump episode17
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

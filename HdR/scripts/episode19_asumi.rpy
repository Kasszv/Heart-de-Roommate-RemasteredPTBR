label episode19_asumi:

    $ bgm (13)
    $ bgfx ('bg05b')
    $ char ('tas002')

    voice as0666
    asumi "Yusuke, let's go home together!"
    yusuke "Hey, Asumi."
    "I don't want her to call me by my real name when I dress like a girl."
    yusuke "What would you do if someone heard?"

    $ char ('tas015')

    voice as0667
    asumi "Oh, then do you want to be called 'Ms. Yamanobe' or 'Sakurako?'"
    yusuke "I don't like those either..."
    "She's not the kind of girl who's popular in class."
    "But I love her anyway."
    yusuke "The reason you girls get along so well is because your roommates are so generous, I guess."

    $ char ('tas036')

    voice as0668
    asumi "What's that? I can't ignore what you just said!"
    yusuke "Then, do you think it's because of you?"

    $ char ('tas015')

    voice as0669
    asumi "Of course! My persistent efforts have made a solid, marvelous friendship."
    yusuke "Are you crazy...!?"

    $ char ('tas036')

    "She suddenly grabs my collar and forces me to shut up."

    call blackout from _call_blackout_153
    $ bgfx ('bg06b')
    $ char ('tas005')

    voice as0670
    asumi "I guess I have to explain how we met and became friends."
    yusuke "Let me hear it."
    "Rubbing my head, I listen to her story."


    call ep_middle from _call_ep_middle_25

    $ bgm (8)

    "I cursed my destiny in the beginning."
    "My new days of youth were just beginning."
    "At the Harukaze dorm, surrounded by nature."
    "What kind of roommates would I spend shiny, unforgettable days with?"
    "My pure, small (they're not that small) breasts were swollen with hope."
    "However, my dreams were shattered when I opened the door."

    $ bgm (6)
    $ bgfx ('bg19a')
    $ chars ('tto717', 'tma625')

    voice to0269
    tomoe "Ah... How do...you...do?"

    voice ma0133
    marumu "Hi..."

    $ bgfx ('black')

    "The atmosphere was so blue."
    "I felt sorry for myself."
    "Why did God give me such a harsh test?"
    "Why were they selected as my roommates?"

    $ char ('tto717')

    "'Tomoe Katsuragi'"
    "She looked like a weak, timid girl."
    "But her tits were bigger than mine."
    "Just talking to her made me irritated."

    $ char ()
    $ char ('tma625')

    "'Marumu Ogumayama'"
    "She was a weird, mysterious girl."
    "She barely talked and showed no emotion."
    "Her short, disheveled hair reminded me of a wild boy in a jungle."

    $ char ()

    "Did I have to live with these girls?"
    "We hardly talked to each other."
    "Though I talked to them, they always gave me the same reaction."

    $ bgfx ('bg19a')
    $ char ('tto717')

    voice to0270
    tomoe "Y...yeah. Ms. Hirota is right. Let's do it."
    "One just accepted the other's opinion, passive pacifists."

    $ bgfx ('black')
    $ bgfx ('bg19a')
    $ char ('tma625')

    marumu "......(nod)"
    marumu "......(shake)"
    "The one would say yes or no without enthusiasm; a queer girl."

    $ bgfx ('black')
    $ bgfx ('bg19a')
    $ chars ('tto717', 'tma625')

    voice as0671
    asumi "Hey, girls! That's enough! Why don't you communicate with each other?"

    voice to0271
    tomoe "I...I'm sorry."
    marumu "......"
    "I couldn't stand it any longer."

    $ bgfx ('black')
    $ bgfx ('bg19b')
    $ char ('tyo003')
    $ bgm (4)

    voice as0672
    asumi "Excuse me...could you relocate me to another room in the dorm?"

    voice yo0165
    yagami "My goodness. It's only been a month. It's too early to understand or get along with each other in such a short time."

    voice as0673
    asumi "It's impossible with them! Anyway, my days of youth are gray, no pitch black!"

    voice yo0166
    yagami "The pairings for students in the dorm are arranged only once a year. Take it as life training and do your best. Okay?"

    voice as0674
    asumi "Okay..."

    $ bgfx ('black')

    "Then I had to do it by myself."
    "No one could help me."
    "To spend a year with no regrets with them, I had to make something we needed each other for."
    "The motive power of youth: 'Friendship!!'"

    $ music_stop ()

    "However, my efforts went unrewarded."
    "Though I talked cheerfully and explained how important friendship was, they didn't change."
    "They didn't take it seriously."
    "It felt like there were walls between us."
    "It bothered me a lot."
    "At last, I reached my limit."

    $ empat ('j5')
    $ bgfx ('bg19a')
    $ chars ('tto717', 'tma625')

    voice as0675
    asumi "I challenge you girls to a duel!"

    voice to0272
    tomoe "A...d...duel?"

    voice ma0134
    marumu "...A duel."
    "That was the only thing I could think of."

    voice as0676
    asumi "The one who wins becomes the leader of this room!! The others have to obey the leader. Okay?"

    voice to0273
    tomoe "B...but I can't...do that."

    voice ma0135
    marumu "No way..."

    voice as0677
    asumi "Shut up! Are you ready!?"

    $ empat ()
    $ say_hide ()
    $ bgfx ('black')
    call cgeffect ('SE10', KENKA2, sound_loop=True) from _call_cgeffect_11

    "I jumped on them."
    "I put up a long, hard fight."
    "It was not hatred, detestation, or unforgivable feelings."
    "I was unbearably mad."
    "At both of them and at myself."
    "I tried to make them accept my selfishness."
    "I couldn't do anything else."
    "The only thing I could do was show my true feelings to them."

    $ sfx (delay=1.0)
    $ bgfx ('bg19a')
    $ chars ('tto718', 'tma626')
    $ bgm (9)

    voice to0274
    tomoe "...Hic...hic..."
    marumu "......"

    voice as0678
    asumi "You girls are good fighters...heh-heh."
    "Hitting, kicking, pulling each other's hair."
    "We heard a complaint from next door."
    "We continued fighting, and then it was over."
    "We said and did whatever we wanted...and somehow, we felt better."
    "The two girls ran away at first, but soon after, they counterattacked."
    "Tomoe struck back crying."
    "However, I was happy."
    "Our hair was totally messed up."
    "Like bird nests."

    $ music_stop ()

    voice as0679
    asumi "Wait here!"
    "I rushed back to my room."
    "Looking in my drawer, I found them."

    $ bgm (10)

    voice as0680
    asumi "These are for you girls!"

    $ char (fx=None)
    $ ev ('raf_23')

    voice to0275
    tomoe "For me..."
    marumu "......"
    "The things I gave them were to fix their hair."
    "A large scarf for Tomoe."
    "Two round hair pins for Marumu."
    "They were bright yellow."

    voice as0681
    asumi "Are these pretty or what? Yellow brings happiness to people."

    voice to0276
    tomoe "Really..."
    marumu "......"

    $ ev (fx=None)
    $ chars ('tto719', 'tma626')

    "After Tomoe wiped the tears from her eyes, she tied her hair with the scarf."
    "Good, she looked cute!"
    "Marumu tried to put the pins in her hair, but she didn't do it right."
    "I tied up her hair on both sides and put the pins on her."

    $ char2 ('tma627')

    voice as0682
    asumi "Wow, you look cute..."
    tomoe "......"
    marumu "......"

    voice as0683
    asumi "...He he... You look like a big stag beetle."

    voice to0277
    tomoe "Pooh... Ha ha ha..."

    voice ma0136
    marumu "Bug, bug..."

    $ cg ('raf_24')
    $ unlock_gallery ('g6e3')

    "That was the first day we laughed."
    "It was also the first day for us as 'roommates.'"
    "We've become closer and closer since then."
    "We gave nicknames to each other and made plans for fun."
    "This is how our eternal friendship was born."

    call blackout from _call_blackout_154
    $ bgm (5)
    $ bgfx ('bg12b')
    $ char ('tas015')

    voice as0684
    asumi "Do you get it? Now do you understand how wonderful a person I am?"
    yusuke "Wonderful...umm..."
    "I understand her pushy attitude produced a good relationship among them."
    "Luckily, it worked well."
    "As I sink into silence, she smirks."

    $ char ('tas012')

    voice as0685
    asumi "You're one of our roommates... Do you want a yellow lucky charm?"
    yusuke "N...no thanks..."

    voice as0686
    asumi "Don't be shy. Oh, I have a cute ribbon."
    yusuke "Would you please...?"

    jump episode19_b
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

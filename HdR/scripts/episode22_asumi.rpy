label episode22_asumi:

    "All of a sudden, I notice Asumi is not in the room."
    yusuke "By the way, where's Asumi?"
    "It disturbs me, so I decide to go look for her."
    "If I recall correctly, she's been researching some stuff."
    "On the spur of the moment, I glance out the window."
    "I see Asumi leaving our dormitory."
    "In a rush, I call out to her to stop."

    $ bgm (16)
    $ bgfx ('bg02c')

    yusuke "Hey, Asumi! Where are you going at a time like this?"

    $ char ('tas206')

    voice as1329
    asumi "It's none of your business! Just take care of Toshibo, okay?"
    "Of course, I'm worried about Toshibo."
    "But I'm also worried about Asumi, who looks pale as she takes off somewhere at this late hour."
    yusuke "I can't do that! I'm concerned about you too, Asumi!"

    $ char ('tas244')

    voice as1330
    asumi "...All right, then come with me!"

    $ bgfx ('black')

    "We start running in the dark as Asumi grabs my arm."
    "Are we heading toward a mountain?"

    $ bgfx ('sora09')

    "She told me she did some research on plants."
    "She found a plant called Lycium Chinense from the botanical dictionary."
    "It is a perennial parsley, which can only be found in rocky mountains."
    "From ancient times, people have been using the root as a tonic, a tranquilizer, and as a painkiller."
    "It's usually used to treat women's diseases, so Asumi thinks it may work for Toshibo."
    "On the way to the mountain, Asumi explains all about it."
    "If Asumi's assumptions are correct, we might be able to find the root at the mountain."
    "If the probability isn't zero, we should try to find it!"
    "At any cost, I swear to get it for Toshibo."

    $ bgfx ('bg12c')
    $ char ('tas201')

    voice as1331
    asumi "Alright, Yusuke. Let's find it!"
    yusuke "Okay! I'll search around here, so why don't you look over there?"

    $ char ()

    "As I recall the characteristics of the plant, I look in every nook and cranny."
    "I don't think it's rare, but still, it may take a long time to find it."
    "Visibility is very bad at night, so I'm having a difficult time."
    yusuke "Oh no. I can't find any. Huh!?"
    "I think I just heard Asumi's voice from over there."
    "I get excited because perhaps she found it, but..."

    $ music_stop ()

    voice as1332
    asumi "Oh, shoot!!"
    "That sounds like Asumi's scream!"
    "In a rush, I head towards the direction where the scream came from."

    $ bgfx ('sora09')

    "Since I don't have a flashlight, I can only count on the moonlight."
    "I find Asumi at a steep slope where dozens of trees are crowded together."
    "It looks like she'll slide down at any moment."
    "I don't think she'll die, but she might get injured."
    "She's in a risky situation."
    "I see her holding some kind of root in her hand."
    "I move closer to the edge of the cliff."
    yusuke "Asumi, are you all right?"

    voice as1333
    asumi "I'm fine! I finally found the root, so we should take it back to Toshibo right away."
    "I see more dirt falling down around her feet."
    "She's in danger more than ever."
    yusuke "I'll help you, so hang in there. Oh, shit!!"
    "I grab her arm, but I lose my balance."
    "...I should exercise more and get in shape."
    "Anyway, it's too late regretting not having strong arms."
    "My strength reaches its limit and both of us slide down the slope."
    "Now, I can protect her only by wrapping my arms around her."

    $ bgfx ('black')
    $ sfx ('SE45')

    "I'm crushed under her, and we finally stop sliding."
    "I calm down and catch my breath."

    $ sfx ()
    $ bgfx ('bg12c')
    $ char ('tas221')

    yusuke "Are you okay, Asumi?"

    voice as1334
    asumi "Thanks to you, I'm fine. But don't ever do such a reckless thing again, Yusuke!"

    $ bgm (10)

    "It looks like she's already full of energy."
    "And I'm pretty sure she's not hurt at all."
    "I bear my pains and smile at her."
    yusuke "I guess I'm getting to be like you, Asumi."

    $ char ('tas245')

    voice as1335
    asumi "Hey, don't tease me!"
    "Well, at least we got what we came here for."
    "Spurring my bruised body on, Asumi and I hurry back to the Harukaze Dorm."

    call blackout from _call_blackout_20
    $ bgfx ('bg01c')
    $ char ('tts021')

    "I briefly explain to Tomoe about the medicine we got for Toshibo."
    "After we steam and grind the root, we give it to Toshibo."
    "For a while, we don't see any change in her condition."
    "She's still breathing hard."

    $ char ('tts020')

    "After a while, the medicine finally starts kicking in."
    "It looks like she's calming down."
    "She can definitely breathe easier than before."
    "From this point on, it's up to her now."

    $ char ()

    jump episode22_b

label episode22_asumi_b:

    $ char ('tas112')
    $ bgm (5)

    voice as0758
    asumi "Good, good. They look very healthy!"
    yusuke "I guess it's fortunate to have these new buddies."

    jump episode22_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

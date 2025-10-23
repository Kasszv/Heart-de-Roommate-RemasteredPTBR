label episode19:

    $ Fnum = 19
    $ save_name = "Episode 19: Then the Three Meet"

    $ bgfx ('bg01a')
    $ char ('tas136')
    $ bgm (3)

    yusuke "Good morning, Asumin. What's wrong? You look grouchy."

    $ char ('tas110')

    voice as0663
    asumi "I had a bad dream! I'm pissed off."
    "Asumi kicks the floor."

    voice as0664
    asumi "How come I had a dream about her?"
    yusuke "About who...?"

    $ char ('tas136')

    voice as0665
    asumi "I'm talking about Hikaru! When I think about her snobby face, I get mad!"
    "I think about her."
    "Hikaru...the transfer student without a smile."
    "She stands out at school, and she makes huge walls around herself."
    "She probably won't make any friends before she graduates."
    "Asumi often approaches Hikaru, but she hasn't succeeded so far."
    "That's why she had a dream about Hikaru. I don't know what kind of dream she had."
    yusuke "By the way..."

    $ cg ('e3_0204')

    "I look around the room."
    "These three girls."
    "I think there are invisible bonds among this unique trio."
    "It's been six months since I moved in. I feel they're stronger than before."
    "It's because of the bonds of friendship."
    "I kind of envy their relationship."


    call ep_start from _call_ep_start_14

    $ bgfx ('bg04a')
    $ bgm (4)

    "The math teacher gave us homework."
    "It seems pretty hard."
    "All our classmates are worried."
    "Asumi suddenly stands up."
    "And she walks to Hikaru."
    "Is she going to talk about the dream she had this morning?"

    $ char ('tas012')

    voice as1353
    asumi "Hey, Hikaru! The homework looks really difficult."

    $ char ('thi001')

    hikaru "......"

    $ char ('tas001')

    voice as1354
    asumi "We're going to do our homework together. Why don't you join us?"

    $ char ('thi002')

    voice hi0116
    hikaru "No thanks..."
    "However, Asumi doesn't give up."
    "She tries to get her interest."

    $ char ('tas012')

    voice as1355
    asumi "Come on! Don't say that! Moe-Moe will make a delicious apple pie."
    yusuke "Excuse me, Asumin."

    $ char ('tas036')

    voice as1356
    asumi "What, Yusuke? I'm busy now."
    yusuke "Hikaru is already gone."

    $ char ('tas030')

    voice as1357
    asumi "Oh...!"
    "Hikaru quietly left the classroom."
    "I guess she felt annoyed at Asumi."
    yusuke "Why don't you stop asking her? She wants to be left alone."

    $ char ('tas006')

    voice as1358
    asumi "I know, but...I feel like I've been defeated!!"
    "She kicks the floor a couple of times."
    "Oh well, she hates losing."

    call blackout from _call_blackout_77

    if F015 == 0:
        jump episode19_asumi

    elif F015 == 1:
        jump episode19_tomoe

    elif F015 == 2:
        jump episode19_marumu

label episode19_b:

    call blackout from _call_blackout_78
    $ bgfx ('bg03a')
    $ char ('tas001')

    "Time goes by."
    "We get used to going to school together."
    "I don't feel like an alien among them anymore. It's as if I've forgotten I'm really a man."
    "However, some people struggle or withdraw into themselves to cope with others."
    "For instance, the girl who just passed us."

    $ bgm (5)
    $ char ('tas002')

    voice as0687
    asumi "Nice weather! I... Ahh!!"

    $ char ('thi001')

    hikaru "......"

    $ char ('tas002')

    voice as0688
    asumi "Hey, Hikaru! Don't be so snobbish. Let's go together."

    $ char ('thi001')

    hikaru "......"

    $ char ('tas006')

    voice as0689
    asumi "Hey, hey! Wait!"

    $ bgfx ('sora01')

    "Hikaru ignores her and walks away."
    "Then she speeds up."
    "Asumi's 'Approach Hikaru plan' has failed again."

    $ bgfx ('bg03a')
    $ char ('tto001')

    voice to0278
    tomoe "Don't be disappointed, Asumi. People are all different."

    $ char ('tma004')

    voice ma0065a
    marumu "......(nod)"

    $ char ('tas007')

    voice as0690
    asumi "No way! Someday, I'll be her friend! I won't give up!"
    yusuke "Heh heh..."
    "Asumi might touch Hikaru's heart, and they'll become friends."
    "Watching this, I feel proud of her."


    call ep_finish from _call_ep_finish_13

    $ renpy.end_replay()
    $ unlock_episode (19)

    jump episode20
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

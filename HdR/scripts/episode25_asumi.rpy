label episode25_asumi:

    $ bgm (16)

    "We divide into two groups."
    "Tomoe pairs with Marumu, and I and Asumi form the other team."
    "Since we don't know where Hikaru is, it's better to separate into two groups to find her."

    $ bgfx ('bg12a')

    yusuke "I know we're going to look for her, but where should we start?"

    $ char ('tas007')

    voice as0847
    asumi "Don't think! Just use your feet and look for her, alright? I'm pretty sure she's around here somewhere."
    yusuke "......"
    "Asumi looks so cool when she tries to lead people."
    "She never gives up in any situation. I really admire her spirit."
    "However, because I'm totally out of shape, I start to push myself into a little trouble."
    yusuke "...I can't stand anymore."

    $ char ('tas010')

    voice as0848
    asumi "YOU are a guy! So, show me your guts!"
    yusuke "But you look out of breath too."

    $ char ('tas006')

    voice as0849
    asumi "Shut up! That's not..."

    $ music_stop ()
    $ char ()

    yusuke "...Asumin?"
    "Something is wrong with her."
    "She squats down on the ground and falls into a long silence."
    asumi "......"
    yusuke "Asumi!"

    $ char ('tas021')

    voice as0850
    asumi "I'm alright, so don't shout at me. I guess I got a little tired too."
    "But still, she doesn't look well."
    "First of all, I must find some water for her."

    $ bgfx ('black')
    $ bgfx ('bg12a')
    $ char ('tas043')
    $ bgm (13)

    voice as0851
    asumi "GLUB-GLUB. Phew!"
    yusuke "Are you really okay, Asumi?"

    $ char ('tas045')

    "After gulping down the water, she thanks me, which is extremely rare."

    voice as0852
    asumi "Thanks, I'm really okay now. By the way, do you know...?"
    yusuke "What?"

    voice as0853
    asumi "Where Hikaru might be hiding."
    yusuke "How am I supposed to know? Since you often chased her, I think you know more about her than I do."

    $ char ('tas037')

    "As I bark at her, she smirks."

    voice as0854
    asumi "Oh, really? Well, because you're Hikaru's lover, I thought you might have a clue where she is now."
    yusuke "Hey, that's not funny at all!"

    $ char ('tas012')

    voice as0855
    asumi "Just joking, silly!"
    "If it's really a joke, I can bear it. But if it's not, even I am going to be pissed."
    "I'm not interested in Hikaru at all!"
    yusuke "How am I supposed to know where Hikaru goes? Are you...oh!"

    call blackout from _call_blackout_59

    "Something flashes into my mind."
    "I just happened to be passing by and saw Hikaru THERE once."
    "She was staring at the view, as if there was nobody around but her."

    $ bgfx ('bg14a')

    "Finally, I recall the place from my memories."
    "I clearly remember her standing alone at the observatory."

    $ bgfx ('black')
    $ bgfx ('bg12a')
    $ char ('tas024')
    $ bgm (5)

    yusuke "She might be there..."

    $ char ('tas012')

    voice as0856
    asumi "Great, you have a clue!? Then after all, you are her lover!"
    yusuke "Hey! No more jokes, please!"

    $ char ('tas005')

    voice as0857
    asumi "Good job, Honey!"
    "I can put her ridiculous jest aside for now."
    "Anyway, I should concentrate on Hikaru right now."
    yusuke "But to tell you the truth, I only saw her there once."

    $ char ('tas003')

    voice as0858
    asumi "That's okay! We can try there anyway, alright? But if we can't find her, be ready to pay a penalty!"
    yusuke "That's not fair!"

    jump episode25_b

label episode25_asumi_b:

    call cg_slide (picture='eh_0101', tm=4.0, kind='b', start=1.0, end=0.0) from _call_cg_slide_12
    $ unlock_gallery ('g4e8')
    $ bgm (8)

    "There she is!"
    "Hikaru is standing there like I saw her the last time."
    "Asumi takes a deep breath and slowly walks toward her."

    voice as1336
    asumi "Hey, Hikaru!"

    $ cg ('eh_0102')

    voice hi0104
    hikaru "...Asumi."

    voice as1336a
    asumi "What are you doing? I think you forgot something important, didn't you!?"

    voice to0981
    tomoe "That's right, Hikaru! Why did you...?"
    marumu "......"

    voice hi0105
    hikaru "I'm really chicken, you know."
    "She takes off her shoe and stares at it."
    "It looks as if she's going to disappear."

    voice hi0106
    hikaru "I thought I'd changed a lot, and my world became brighter than before."

    voice hi0107
    hikaru "From the day you started dragging me around, I believed I could change little by little."

    $ cg ('eh_0103')

    voice hi0108
    hikaru "But I've got it all wrong. I haven't changed a bit!"

    voice hi0109
    hikaru "So I want to end everything here. Because I have no reason to keep going anymore."
    "I'm not going to give up on you!"
    "A silent scream from Asumi, and then she starts yelling at Hikaru."

    voice as1337
    asumi "Did you say you have no reason? That's bullshit! Not just you, we all have a lot more time!"

    voice as1338
    asumi "Over a long period of time, everybody keeps changing little by little. That's our world, isn't it!?"

    voice as1339
    asumi "But you've changed a bit, right? And from now, you'll change more than ever!"

    voice hi0110
    hikaru "It's impossible for me! After all, I've got nothing!"

    voice as1340
    asumi "Wait, Hikaru!"

    $ cg ('eh_0104')

    "She slowly lets go of the handrail."
    "The next moment, Asumi's body disappears from sight."

    $ music_stop ()
    $ bgfx ('sora01')

    "Then I realize Asumi tried to tackle her at breakneck speed."
    "But she was going too fast."
    "As a result, Asumi went sailing through the air, off the cliff..."

    voice as1341
    asumi "Yah, yaaaaaaa!!"

    voice hi0111
    hikaru "Shit, Asumi!!"

    voice to0982
    tomoe "Asumi!"

    voice ma0515
    marumu "...Asumin!"
    yusuke "A...Asumiiii!"
    "That's it. Game over..."
    "The next moment, I notice Hikaru is holding something very heavy."
    "It's Asumi's arm! And Hikaru is trying to pull her up!"
    "We rush towards Hikaru and try to save her."

    $ bgfx ('black')
    $ bgfx ('bg14a')
    $ chars ('tas043', 'thi004')

    voice as1342
    asumi "Thank you, Hikaru."

    voice hi0112
    hikaru "Why are you thanking me?"

    $ char1 ('tas045')

    voice as1343
    asumi "Because you saved my life, you know."

    $ chars ('tas039', 'thi002')

    voice hi0113
    hikaru "No, you saved my life! It wasn't your business, but you still kept your big nose in my problems."
    "As Hikaru thanks her in her awkward way, she smiles."

    $ char1 ('tas015')

    voice as1344
    asumi "You're such a slowpoke! Remember, I'm a nosy person!"

    voice to0983
    tomoe_marumu "...Good, good."
    "As a softer atmosphere prevails, tears well up in Hikaru's eyes."
    "We stopped her from jumping off the observatory, but her heart is still breaking with grief."

    voice hi0114
    hikaru "I really can't stand it anymore. My life sucks, you know."

    jump episode25_c

label episode25_asumi_c:

    $ bgfx ('black')
    $ bgm (14)
    $ bgfx ('bg02c')

    "After the party is over, I linger outside. I suddenly notice somebody walking towards me."

    $ char ('tas105')

    voice as0895
    asumi "Yusuke, I found you at last."
    yusuke "What's up, Asumi?"

    $ char ('tas136')

    voice as0896
    asumi "Hey, watch your mouth, darling!"

    $ char ('tas412')
    $ char ('tas106')

    "As Asumi puffs her cheeks out, I abruptly kiss her."
    "She's surprised at my sudden move and glares at me."

    voice as0897
    asumi "Hey!"
    yusuke "Nobody's around, so I just thought I could kiss you now."

    $ char ('tas147')

    voice as0898
    asumi "You're so fresh."
    "She's muffed, and her face turns completely red."
    "My face gets red too."
    "I usually don't do such bold things. Was it because of the excitement from the party?"
    "Anyway, we're now alone under the quiet night sky."
    "There's something I've wanted to tell her for a long time."
    yusuke "Hey, Asumi."

    $ char ('tas145')

    voice as0899
    asumi "What?"
    yusuke "Well, I was really surprised when Tomoe told me she loved me."

    $ char ('tas142')

    voice as0900
    asumi "Oh yeah?"
    "She somehow looks blue."
    "However, I continue talking."
    yusuke "I used to like her so much, you know."

    $ char ('tas137')

    voice as0901
    asumi "...I'll bet you and Moe-Moe would make a great couple."
    "She sounds kind of sour now."
    "But I continue while staring at her sullen face."
    yusuke "If I had to choose one of you, I'd still pick you."

    $ char ('tas127')

    voice as0902
    asumi "Oh, I'm very pleased to hear that."
    "She sarcastically tells me."
    "Yet I ignore her sarcasm and suddenly hold her tight."

    $ char ('tas130')

    voice as0903
    asumi "Hey, Yusuke!"
    yusuke "I want to be with you forever. You're the one for me, you know. I can't imagine not having you in my life."

    $ char ('tas146')

    voice as0904
    asumi "...Yusuke."
    yusuke "Although we've graduated and will take different paths, I still want you to be with me."

    $ char ('tas121')

    asumi "......"
    "I just told her how deeply I love her."
    "Asumi falls silent and stares at me."
    yusuke "Is that a problem?"

    voice as0905
    asumi "I'm sorry, but I can't answer right this minute. I have to think about it first, you know."
    "It may be a proper answer in this kind of situation."
    "It's true we've been girlfriend-boyfriend for six months."
    "But it doesn't mean she wants to be with me forever. Thus, I totally understand why she hesitates a little."
    "All of sudden, she shows me her big smile."

    $ char ('tas145')

    voice as0906
    asumi "Because you're so serious, I shouldn't give you an irresponsible answer."

    voice as0907
    asumi "But Yusuke..."
    "Asumi puts her arms around my neck."
    "Then she hugs me tight, as if clinging to me."

    $ char ('tas411')

    voice as0908
    asumi "Tonight, I want to be with you all night long."
    yusuke "...Okay."

    call blackout (True) from _call_blackout_60
    $ bgm (10)
    call cg_slide (picture='raf_2501', kind='v', tm=5.0, start=1.0, end=0.0) from _call_cg_slide_13
    $ unlock_gallery ('g6e8')

    voice as0909
    "We hug each other tight."

    $ vox ('as0910')

    "Tomorrow morning, we both have to leave the place we've become so accustomed to, the Harukaze Dorm."

    $ vox (delay=0.3)

    "This will be our final night."

    $ vox ('as0911')

    "I swear I will never forget it."

    $ vox (delay=0.3)

    "Until the last moment, we will continue making new memories."

    $ vox ('as0912')

    "The memories of our love."

    $ vox (delay=0.3)

    "We hug and kiss again and again."

    $ vox ('as0913')

    "So we won't forget each other's warmth."

    $ vox (delay=0.3)

    "I try to memorize her voice, her smell, and the feel of her skin."

    $ vox ('as0914')

    "I don't know whether six months was long enough for us or not."

    $ vox (delay=0.3)

    "But we definitely spent time together and walked down the same path."

    $ vox ('as0915')

    "That's why I want to cherish every minute I spend with her."

    $ vox (delay=0.3)

    "For our everlasting love."

    $ cg ('raf_2502')
    $ bgfx ('white')
    $ bgfx ('black')

    "To keep our memories strong, we make love the entire, final night in the Harukaze Dorm."

    $ bgfx ('sora09')
    $ music_stop ()

    "Our time has come to an end."
    "We lay down and snuggle up together."
    "We want to feel each other's love till the last moment."

    $ bgm (14)

    voice as0916
    asumi "Yusuke..."
    yusuke "What?"

    voice as0917
    asumi "I'll never forget you, though I can't see you everyday anymore."
    yusuke "...Asumi."

    voice as0918
    asumi "...I love you so much."
    "She brings her lips to mine."
    "I passionately kiss her back."
    "After a long kiss, Asumi suddenly mutters,"

    voice as0919
    asumi "Yusuke, thank you for the happiest time I've ever had."

    jump episode25_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

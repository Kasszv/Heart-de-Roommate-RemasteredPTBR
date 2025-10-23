label episode22:

    $ Fnum = 22
    $ save_name = "Episode 22: The New Life"

    $ bgfx ('sora02')

    "It's happened when I wake up a bit earlier than the others."

    $ bgm (13)

    yusuke "It's such a good day!"
    yusuke "I thought it used to be noisier. I wonder... Oh, that's right!"
    "Until a little while ago, the cats were in heat."
    "That's why the cats made so much noise every night."
    "That reminds me of my roommate, Toshibo, who is also a cat."
    "I haven't seen him recently."
    "I guess he's chasing female cats somewhere."
    yusuke "I wonder if he's falling in love. Well, I don't think that fat cat will find a girlfriend so easily...heh heh."
    "As I wonder about such things, I hear everyone getting up."
    "It's my turn to make breakfast, so I'd better start cooking."

    $ bgfx ('black')
    $ cg ('e3_0212')

    "I decide to ask Tomoe about Toshibo at breakfast."
    yusuke "Hey, Tomoe!"

    $ cg ('e3_0203')

    voice to0301
    tomoe "What?"
    yusuke "......"
    "Because she has low blood pressure, she's a super-duper bad morning person."
    "If a man were to see her like this, he'd be disappointed and even lose interest in her."
    "Well, I guess I can see her like this because I'm her roommate."
    "I ask the sleeping beauty the question on my mind."
    yusuke "Do you know what Toshibo is doing? I haven't seen him recently."

    voice to0302
    tomoe "I heard he fell in love or something."

    $ cg ('e3_0212')

    "What? He fell in love? That's unbelievable!"
    "I guess he's in his prime."
    "However, it's hard to believe this story."
    "I'm saying that because I know Toshibo's personality."
    "Oh well. I guess he is a cat, after all."
    "There are a lot of mysterious things in the world...or so I thought."


    call ep_start from _call_ep_start_29

    "Several days later, I forget all about this odd story."

    $ bgm (2)
    $ bgfx ('bg02a')

    yusuke "...Huh?"

    $ sfx ('SE37')

    "I see bushes moving unnaturally near the dormitory."
    "Wondering what's going on, I go near the bushes."
    "Asumi and Marumu follow me."

    $ sfx (delay=0.3)
    $ char ('tas002')

    voice as0737
    asumi "What's going on, Yusuke?"
    yusuke "I thought the bushes moved a little."
    "Suddenly, Marumu guesses the mysterious identity."

    $ char ('tma004')

    voice ma0163
    marumu "It's a TSUCHINOKO."
    yusuke "I don't think so."
    "I don't think we'll find such an imaginary creature here."

    $ char ('tma014')

    voice ma0164
    marumu "If it bites us, we'll die!"
    yusuke "I told you there's no such thing."
    "Despite what I just said, I shrink back."
    "If a creature like the 'Tsuchinoko' really exists, its bite can be fatal."
    "Marumu says it seriously."
    "For a split second, I wonder if she may possibly be right."
    "As I start backing up, Asumi moves forward with curiosity."

    $ music_stop ()
    $ char ('tas002')

    voice as0738
    asumi "Let's capture the creature!"

    $ char ('tma008')

    voice ma0165
    marumu "Show time!"

    $ bgm (7)

    "When Marumu cheers, Asumi plunges her hand in the bushes."
    "If the creature bites her hand, it'll be a disaster!"

    $ char ('tas012')

    voice as0739
    asumi "Let's see... Oh, I got it!"
    "Asumi captures the mysterious creature too easily."
    "However, the creature looks like...Toshibo."
    "But I wasn't sure because..."

    $ bgm (6)
    $ char ('tts020')

    voice as0740
    asumi "You really got fat, Toshibo."
    yusuke "Did you eat a lot of boiled eggs from a hot spring? You look so full."

    voice ma0166
    marumu "Toshibo, a sumo wrestler!"
    "It's been ages since I last saw him. Now, he's like a balloon!"
    "In a way, he looks like he's suffering."
    "As we continue our discussion about him, the bushes unnaturally move again."
    "Asumi plunges her hand in at once."

    $ char ('tas024')

    voice as0741
    asumi "What? Is there another cat?"

    $ char ('tma001')

    voice ma0167
    marumu "A black cat."

    $ char ('tku001')

    "Asumi captures an odd black cat."
    "Although the cat is caught, it doesn't fight. It's just looking at Toshibo."

    $ music_stop ()

    "It looks like it's worried about Toshibo."

    $ char ('tts020')

    voice ts0048
    toshibo "...meooow."

    voice ma0168
    marumu "Toshibo said something."
    "I know he wants to tell us something, but I don't get it."
    "Somehow, he sounds weak."

    voice as0742
    asumi "How about...we wait for the interpreter to come back!"
    "For now, we decide to take Toshibo back to our dormitory."
    "We wait for his special interpreter, Tomoe."
    "As Asumi frees the black cat, it starts to check around."

    $ bgfx ('black')

    "Right before sunset, Tomoe comes back from shopping."
    "When she sees our fat cat, she looks astonished."

    $ bgfx ('bg01b')
    $ char ('tto022')

    voice to0303
    tomoe "Toshibo, what happened to you? Have you been eating dozens of boiled eggs from a hot spring?"
    yusuke "I guess everybody thinks the same."
    "As Toshibo sees his lovely Tomoe, he tries to tell her something."

    $ char ('tts020')

    voice ts0049
    toshibo "meow meow meooow."

    voice to0304
    tomoe "Toshibo, you said you are in pain?"

    voice ts0050
    toshibo "...meow."

    $ char ()

    "After he says this, he faints."
    "It happens so suddenly, we all fall down in a panic."
    "Tomoe clings to me."

    $ bgm (16)
    $ char ('tto007')

    voice to0305
    tomoe "Toshibo!? What should we do, Yusuke!?"
    yusuke "We should take him to a vet."
    "My answer is too ordinary, and Asumi gives us some frank advice."

    $ char ('tas043')

    voice as0743
    asumi "There isn't a vet around here! There might be one in the next town, though."

    $ char ('tma004')

    voice ma0169
    marumu "An hour by train to the next town."
    yusuke "Does it take that long? Anyway, let's take him there!"

    voice ma0170
    marumu "But only five trains a day."
    yusuke "Really?"
    "Suddenly, I'm reminded this town isn't like Tokyo."

    $ char ('tto007')

    voice to0306
    tomoe "What should we do?"

    $ char ('tas033')

    voice as0744
    asumi "As the leader, I should do something..."

    $ music_stop ()
    $ sfx ('SE52')

    yusuke "I have an idea!"

    $ bgm (5)

    "A bright idea pops into my mind before Asumi has one."
    "I remember Ms. Yagami used to be a director of 'Gather animal lovers! The vet club.'"

    $ sfx (delay=0.3)
    $ bgfx ('sora05')

    "In desperation, everybody rushes to the school."
    "When we arrive, I notice the black cat is following us."

    $ bgfx ('black')

    "We immediately explain to Ms. Yagami what happened to Toshibo."
    "She starts checking his condition."
    "She isn't a vet, but I think she knows more than we do."

    $ music_stop ()
    $ bgfx ('bg04b')
    $ bgm (8)
    $ char ('tyo015')

    "For a while, she keeps checking him everywhere."
    yusuke "How's Toshibo?"

    voice to0307
    tomoe "Ms. Yagami, please save him. Please..."
    "Suddenly, Ms. Yagami tilts her head."

    $ char ('tyo014')

    voice yo0167
    yagami "His name is Toshibo..."

    voice as0745
    asumi "Do you think he's been eating too much lately? Or, does he have stomach cancer?"

    voice ma0171
    marumu "...Toshibo."
    "She doesn't say what's wrong with him, even though we all worry about him so much."
    "I raise my voice."
    yusuke "Ms. Yagami!"

    voice yo0168
    yagami "...I think she's pregnant."
    yusuke "Pregnant? Not because Toshibo ate dozens of carrots?"

    $ music_stop ()
    $ char ('tas036')
    call effect ('SE43', ETYPE2) from _call_effect_47

    "Asumi hits my head hard."
    "Ms. Yagami told us something we weren't expecting."
    "Just to confirm it, Asumi asks her again,"

    $ char ('tas030')

    voice as0746
    asumi "Pregnant? That means Toshibo is going to have a baby?"

    $ char ('tto013')

    voice to0308
    tomoe "Ms. Yagami, is Toshibo really pregnant?"

    $ char ('tyo002')

    voice yo0169
    yagami "Yep! It looks like she's carrying a couple of babies."

    $ char ('tma008')

    voice ma0172
    marumu "Baby kitties!"
    "I guess Ms. Yagami is right."
    "I ask Tomoe a question because I know exactly why Ms. Yagami is puzzled about Toshibo's pregnancy."

    $ bgm (3)
    $ char ('tto004')

    yusuke "Hey, Tomoe."

    voice to0309
    tomoe "Toshibo is going to have babies..."
    yusuke "Are you listening, Tomoe!?"

    $ char ('tto022')

    voice to0310
    tomoe "What, Yusuke?"
    yusuke "I didn't know Toshibo was a she, not a he."

    $ char ('tto011')

    voice to0311
    tomoe "Yeah, I guess so."
    "Oh my goodness."
    "Although Tomoe named her Toshibo, she didn't know it was a female cat."

    $ char ('tas030')

    voice as0747
    asumi "Didn't you know Toshibo's sex, Moe-Moe? Then, why did you name her Toshibo? That's supposed to be a male cat name."

    $ char ('tto007')

    voice to0312
    tomoe "...Sorry."

    $ char ('tma004')

    voice ma0173
    marumu "Many mysterious things in the world."
    "It's already happened, so we can't change the past."

    $ char ('tts020')

    "My lovely friend is still the same Toshibo, even though she's not a 'he.'"
    "If she's pregnant, then something concerns me."
    yusuke "Who's the father?"

    $ char ('tas024')

    voice as0748
    asumi "Probably him."

    $ music_stop ()
    $ char ('tku001')

    "Asumi picks up the black cat, who's been prowling around."
    "Ah-ha! That's why he followed us to school."

    $ bgfx ('black')

    "Ms. Yagami assembles the vet club members."
    "It seems everybody knows about animals more than she does."
    "According to their examination,"
    "They're sure Toshibo is pregnant, and she will probably have babies tomorrow."
    "But her body is very weak now."
    "She may have a hard time delivering her babies."
    "Although Tomoe knows what's going on with Toshibo, she can't stop worrying about her."

    $ bgm (9)
    $ bgfx ('bg01c')
    $ char ('tts020')

    voice to0313
    tomoe "Are you okay, Toshibo?"

    voice ts0051
    toshibo "...meow."

    voice to0314
    tomoe "Get some rest, okay?"
    "All I can do is stare at Tomoe cheering up Toshibo."
    "...I'm so powerless."
    yusuke "I guess we can't do anything for her right now."

    $ char ('tas042')

    voice as0749
    asumi "We should take her to a vet."
    "I see Marumu coming back from somewhere."

    $ char ('tma001')

    voice ma0174
    marumu "I called a vet."

    $ char ('tas001')

    voice as0750
    asumi "You're so quick, Marutan. Let's take her to the vet!"

    $ char ('tma020')

    voice ma0175
    marumu "It's closed until Monday."
    yusuke "Oh noooo!!"

    $ char ('tto007')

    voice to0315
    tomoe "That's not good."
    "Tomoe becomes speechless when she is informed of the gloomy situation."
    "I also hopelessly stand there."
    "There is a dark, heavy atmosphere in the room. Suddenly, Asumi speaks up,"

    $ bgm (5)
    $ char ('tas007')

    voice as0751
    asumi "We should all pull together, okay? Let's think of what we can do for her!"

    $ char ('tto007')

    voice to0316
    tomoe "...Asumi."
    "That's right!"
    "If we stick together and think, we probably can find something we can do!"
    yusuke "You're right! Let's do something for her!"

    $ char ('tma013')

    voice ma0176
    marumu "I'll help Toshibo too!"

    $ char ('tas006')

    voice as0752
    asumi "Yep! We'll all stick together and save Toshibo and her babies' lives!"
    "As Asumi cheers us on, we start the 'Save Toshibo & Her Babies' project."


    call ep_middle from _call_ep_middle_30

    "First, we divide into teams and discuss what we can do."
    "One team researches, and the other takes care of Toshibo."
    "I get some advice from a member of the vet club."
    "Everybody works very hard to save the little lives."
    "The black cat flutters around, but he still stays close to Toshibo."
    "I think he's also worrying about her as well."

    $ sfx ('SE53')

    "All of a sudden, someone knocks on the door."
    "Just in case, I run into the closet."
    "After making sure nobody can see me, Asumi opens the door."

    $ sfx (delay=0.3)
    $ bgfx ('bg01c')
    $ char ('tyu001')
    $ bgm (16)

    voice yu0059
    akane "Hey, are you having a party or what?"
    asumi "......"
    "She can't say a word."
    "If she says something wrong, the others will find out about Toshibo."
    "However, the leader from the next door doesn't stop questioning about what's going on."

    $ char ('tyu002')

    voice yu0060
    akane "Just tell me what's going on here!"

    $ char ('tas021')

    voice as1368
    asumi "...All right."

    $ bgfx ('black')
    $ music_stop ()

    "It's true we've been making too much noise."
    "Asumi starts explaining while Tomoe gives her an anxious look."
    "Asumi tells Akane about Toshibo and her condition."

    $ bgfx ('bg01c')
    $ char ('tyu002')

    "After Akane hears her story, she stares at Asumi."
    "Again, one more secret from this room has been revealed."
    "She may say something sarcastic. In the dark, I keep an eye on them."
    "Then she asks,"

    $ char ('tyu001')

    voice yu0061
    akane "Is there anything...?"

    voice as1369
    asumi "Excuse me?"

    $ char ('tyu003')

    voice yu0062
    akane "I said I'll help you, idiot!"

    $ char ('tas044')

    voice as1370
    asumi "You girls..."

    $ bgm (10)

    "Asumi is astonished by what Akane just said."
    "Asumi didn't expect her to say such a thing."
    "Akane continues,"

    $ char ('tyu002')

    voice yu0063
    akane "Don't misunderstand, okay!? I just want you guys to be quiet; that's all!"

    $ char ('ths001')

    voice hs0033
    kaoru "It's a hassle, but we have some spare time."

    $ char ('tfu001')

    voice fu0030
    midori "Don't you think it's okay to help others once in a while?"
    yusuke "......"

    $ bgfx ('black')

    "I guess the Trio de Bitches aren't so bitchy, after all."
    "I may be simple-minded."
    "I'm sure Asumi also thinks the same way."

    $ music_stop ()
    $ bgfx ('sora08')

    "Since everybody worked so hard to help Toshibo, nothing bad happened all night. And the next day..."

    $ bgfx ('sora01')

    "Fortunately or not, it's Sunday."
    "We still can't get a vet, but everybody nurses Toshibo all day long."

    $ bgfx ('sora05')

    "For twenty-four hours, we're terribly anxious about her."

    $ bgfx ('sora09')

    "At night, Toshibo starts suffering awful pains."
    "I'll bet it's the turning point now."

    $ bgm (8)
    $ bgfx ('bg01c')
    $ char ('tts021')

    "Because everybody has been taking care of Toshibo all night, we all look completely exhausted."
    "Yet, we still take turns nursing her."

    voice ts0052
    toshibo "...me...ow."

    $ char ('tto204')

    voice to0317
    tomoe "It looks like she's in so much pain. Are you okay, Toshibo?"
    "I try to cheer up Tomoe, who's about to cry any minute."
    yusuke "Toshibo is a strong guy, Tomoe. Oh, excuse me. She is a strong GIRL, so she'll be fine."

    $ char ('tma101')

    voice ma0177
    marumu "Hang on, Toshibo!"
    "We've already done everything we can."
    "Now, we have to trust her vitality."

    call blackout from _call_blackout_190

    if F015 == 0:
        jump episode22_asumi

    elif F015 == 1:
        jump episode22_tomoe

    elif F015 == 2:
        jump episode22_marumu

label episode22_b:

    $ bgm (14)
    $ char ('tas144')

    voice as0753
    asumi "Hang on, Toshibo. Be patient, you're almost there!"

    $ char ('tto207')

    voice to0318
    tomoe "Please...please hang in there, Toshibo!"

    $ char ('tma101')

    voice ma0178
    marumu "...Toshibo."

    $ char ('tts020')

    "We did everything we could for her."
    "From this point on, we can only keep an eye on her and cheer her up."
    "We keep talking to her."
    "Desperately, we pray she and her babies will survive."
    "Soon it grows late."
    "When it's almost morning, I lose the battle and fall into a deep sleep."

    call blackout from _call_blackout_191
    $ bgfx ('white')
    $ bgfx ('bg01a')

    "I see a shaft of bright, white light coming in through the window."
    "I guess the sun rose a little while ago."

    voice to0319
    tomoe "Toshibo...zzz..."

    voice ma0179
    marumu "...zzz."
    "Tomoe and Marumu are sleeping right next to me."
    "We've been nursing Toshibo for two nights straight, so I bet they're tired as well."
    "However, I don't see Asumi in the room."
    "If I'm right, she's been staying up all night long by herself."
    "With her back turned, she's staring at something."
    "After gazing at her for a while, I start talking,"
    yusuke "Were you awake all night?"
    asumi "......"
    "She doesn't answer me."
    "Is her head drooping?"
    "Perhaps..."
    yusuke "Hey, Asumi. Are you sleeping or what?"

    voice as0754
    asumi "...Toshibo did it."
    "She whispers."
    "Her voice is so calm and kind."
    yusuke "What?"

    voice as0755
    asumi "Her babies were born!"

    $ bgfx ('white')
    $ cg ('ea_02', pos=[ALIGN(0.0, 1.0)])
    $ unlock_gallery ('g1e3')
    $ bgm (10)

    "Asumi turns her head and shows me a baby kitten."
    "I see tears on her face."
    "It looks as if she's staring at her own baby."

    call cg_slide (picture='ea_02', tm=3.0, kind='v', start=1.0, end=0.0, cls=diss_fast) from _call_cg_slide_21

    voice as0756
    asumi "The baby kitten is trying its best to move."
    yusuke "Yeah, it's such a healthy kitten."
    "I think I can describe her warm smile as 'motherly love.'"
    "She continues smiling and talking to the babies,"

    voice as0757
    asumi "Happy birthday, Pumpkins."
    yusuke "Asumi..."
    "I've never seen Asumi smile so happily like this."
    "She's very pleased as though her own baby was just born."
    "It's a very touching sight to see."
    "And now, a happy feeling arises in me as well."
    "Finally, Toshibo's babies were born!"

    $ bgfx ('sora02')

    "I put my arm on her shoulders."
    "Then we wake up Tomoe and Marumu, and we celebrate this happy moment."

    call blackout from _call_blackout_192

    "After a couple of days, Toshibo gets her strength back."
    "Her babies are doing very well too."

    $ bgm (6)
    $ say_hide (diss_fast)
    $ cg ('en_01', pos=[ALIGN(0.0, 0.0)])
    $ unlock_gallery ('g6e11')

    voice ts0053
    toshibo "Meow!"
    yusuke "Hey, Toshibo. Are you going for a walk?"

    voice ts0054
    toshibo "Meoooow!"

    call cg_slide ('en_01', cls=diss_fast, tm=2.0, kind='h', start=0.0, end=0.335) from _call_cg_slide_22

    voice et0005
    kitten1 "meow."

    call cg_slide ('en_01', cls=diss_fast, tm=2.0, kind='h', start=0.335, end=0.672) from _call_cg_slide_23

    voice et0006
    kitten2 "meoow."

    call cg_slide ('en_01', cls=diss_fast, tm=2.0, kind='h', start=0.672, end=1.0) from _call_cg_slide_24

    voice et0007
    kitten3 "meowwww..."
    "Now, I understand why Toshibo's belly was swelled up like a balloon."
    "It was outrageous."
    "Anyway, everybody watches and smiles as the kittens parade around."

    $ bgfx ('bg01a')

    if F015 == 0:
        jump episode22_asumi_b

    elif F015 == 1:
        jump episode22_tomoe_b

    elif F015 == 2:
        jump episode22_marumu_b

label episode22_end:

    "I sympathize with their daddy black cat, who has to take care of these new faces. I watch them marching around."


    call ep_finish from _call_ep_finish_23

    $ renpy.end_replay()
    $ unlock_episode (22)

    jump episode23
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

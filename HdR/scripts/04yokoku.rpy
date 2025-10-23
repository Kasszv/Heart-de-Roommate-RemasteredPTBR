

label ep_finish:

    call blackout (True) from _call_blackout_98
    call breakskip from _call_breakskip_5


    python:
        audio_stop (0.0)
        audio_stop (0.0, 'story')
        audio_stop (0.0, 'decoration')

        if Fnum < 22:
            ANI = [
                ('m', 'j3', 0.5),
                ('i', ('nt_a', None, None), (0.5, 2.0)),
                ]
        else:
            ANI = [('i', ('nt_b', None, None), (0.5, 1.0))]

        CB = 0 if Fnum != 19 else 2
        SUBS = None



        if Fnum == 1:
            
            
            
            ANI += [
                ('v', 'to0909a', 0),
                ('i', ('nt0201', None, None), (0.2, 1.0)),
                ('i', ('nt0202', None, None), (0.2, 1.0)),
                ('i', ('nt0203', None, None), (0.2, 1.0)),
                ('i', ('nt0204', None, None), (0.2, 1.0)),
                ('i', ('nt0205', None, None), (0.2, 1.0)),
                ('i', ('nt0206', None, None), (0.2, 1.0)),
                ('i', ('nt0207', None, None), (0.2, 1.0)),
                ('i', ('nt0208', None, None), (0.2, 1.0)),
                ('i', ('nt0209', None, None), (0.2, 1.5)),
                ('i', ('nt0210', None, None), (0.2, 3.0)),
                ]
            SUBS = {
                (2.5, 5.5, 1): "Having to suddenly live with a boy under the same roof...",
                (5.5, 7.8, 1): "what is Asumi thinking?",
                (8.2, 10.2, 1): "No way!",
                (10.6, 12.7, 1): "What am I going to do...?!",
                (13.8, 17.0, 1): "Wait! I just came up with a great idea.",
            }

        elif Fnum == 2:
            
            ANI += [
                ('v', 'as1241', 0),
                ('i', ('nt0301', None, None), (0.5, 3.15)),
                ('i', ('nt0302', None, None), (0.5, 3.15)),
                ('i', ('nt0303', None, None), (0.5, 3.15)),
                ('i', ('nt0304', None, None), (0.5, 3.15)),
                ('i', ('nt0305', None, None), (0.5, 3.15)),
                ]
            SUBS = {
                (2.5, 4.8, 0): "It came to us out of the nowhere.",
                (4.8, 8.8, 0): "A mysterious creature shows up at our peaceful Harukaze dormitory.",
                (8.8, 10.9, 1): "Asumi, it's a cat!",
                (11.5, 14.8, 0): "We encounter an extra-terrestrial!",
                (14.8, 17.0, 1): "I said it's a cat!",
                (17.0, 21.0, 0): "Where did he come from? What's his purpose? What is his favorite food?",
            }

        elif Fnum == 3:
            
            ANI += [
                ('v', 'as1243', 0),
                ('i', ('nt0401', None, None), (0.2, 2.5)),
                ('i', ('nt0402', None, None), (0.2, 2.5)),
                ('i', ('nt0403', None, None), (0.2, 3.0)),
                ('i', ('nt0404', None, None), (0.2, 3.0)),
                ('i', ('nt0405', None, None), (0.2, 3.0)),
                ('i', ('nt0406', None, None), (0.2, 3.0)),
                ]
            SUBS = {
                (2.5, 5.5, 0): "Damn, the 'trio de bitches'. Screw them!",
                (6.0, 12.0, 0): "Moe-Moe and Marutan, we'll have an emergency meeting to talk about the situation!",
                (12.5, 15.0, 0): "Let's meet at the usual place.",
                (15.5, 18.2, 0): "Yusuke, you come with us too.",
                (18.7, 21.0, 0): "I'll kick your ass if you're late!",
            }

        elif Fnum == 4:
            
            ANI += [
                ('v', 'na0368', 0),
                ('at', ('nt0501', [MOVE_VERTICAL(tm=3.5, delay=6.0, start=1.0, end=0.0)], 'bg'), (0.2, 9.5)),
                ('i', ('nt0502', None, None), (0.5, 8.5)),
                ]
            SUBS = {
                (2.5, 5.5, 3): "Hey, you. Pretty girl!",
                (6.0, 7.7, 3): "No, not you.",
                (8.2, 10.8, 3): "I'm talking to the girl with the ribbon.",
                (11.5, 13.2, 3): "Oh my! Is that you, Yusuke?",
                (13.5, 15.8, 3): "Why are you in girls' clothing?",
                (16.2, 20.8, 3): "I know why...that ugly girl forced you to wear them.",
            }

        elif Fnum == 5:
            
            ANI += [
                ('v', 'as1245', 0),
                ('i', ('nt0601', None, None), (0.0, 1.0)),
                ('i', ('nt0602', None, None), (0.0, 1.0)),
                ('i', ('nt0601', None, None), (0.0, 1.0)),
                ('i', ('nt0602', None, None), (0.0, 1.0)),
                ('i', ('nt0601', None, None), (0.0, 1.0)),
                ('i', ('nt0602', None, None), (0.0, 1.0)),
                ('i', ('nt0603', None, None), (0.0, 0.5)),
                ('i', ('nt0604', None, None), (0.0, 0.5)),
                ('i', ('nt0603', None, None), (0.0, 0.5)),
                ('i', ('nt0604', None, None), (0.0, 0.5)),
                ('i', ('nt0603', None, None), (0.0, 0.5)),
                ('i', ('nt0604', None, None), (0.0, 0.5)),
                ('i', ('nt0603', None, None), (0.0, 0.5)),
                ('i', ('nt0604', None, None), (0.0, 0.5)),
                ('i', ('nt0603', None, None), (0.0, 0.5)),
                ('i', ('nt0604', None, None), (0.0, 0.5)),
                ]
            SUBS = {
                (2.5, 5.5, 0): "Yusuke, you're always screwing up, aren't you?",
                (5.8, 8.0, 0): "Show us some manhood.",
                (9.1, 13.0, 0): "Toshibo is more reliable than you are.",
            }

        elif Fnum == 6:
            
            ANI += [
                ('v', 'yo0363', 0),
                ('i', ('nt0701', None, None), (0.2, 3.6)),
                ('i', ('nt0702', None, None), (0.2, 3.6)),
                ('i', ('nt0703', None, None), (0.2, 3.6)),
                ('i', ('nt0704', None, None), (0.2, 3.6)),
                ]
            SUBS = {
                (2.5, 5.5, 4): "I've heard there's a strange girl in the dorm recently.",
                (5.7, 7.7, 4): "Yusuke, do you know anything about this?",
                (9.0, 11.0, 4): "Silly me.",
                (13.0, 16.2, 4): "You're a man; you wouldn't know anything about the girls' dorm.",
                (17.0, 18.0, 4): "Heh-heh.",
            }

        elif Fnum == 7:
            
            ANI += [
                ('v', 'na0370', 0),
                ('i', ('sora01', None, None), (0.5, 0.0)),
                ('i', (None, None, 'tna001'), (0.0, 0.85)),
                ('i', (None, None, 'tna002'), (0.0, 0.85)),
                ('i', (None, None, 'tna001'), (0.0, 0.85)),
                ('i', (None, None, 'tna002'), (0.0, 0.85)),
                ('i', (None, None, 'tna001'), (0.0, 0.85)),
                ('i', (None, None, 'tna002'), (0.0, 0.85)),
                ('i', (None, None, ''), (0.0, 0.0)),

                ('i', (None, 'sde_0501', None), (0.0, 0.8)),
                ('i', (None, 'sde_0502', None), (0.0, 0.8)),
                ('i', (None, 'sde_0501', None), (0.0, 0.8)),
                ('i', (None, 'sde_0502', None), (0.0, 0.8)),
                ('i', (None, 'sde_0601', None), (0.0, 0.8)),
                ('i', (None, 'sde_0602', None), (0.0, 0.8)),
                ('i', (None, 'sde_0601', None), (0.0, 0.8)),
                ('i', (None, 'sde_0602', None), (0.0, 1.3)),
                ]
            SUBS = {
                (2.5, 6.5, 3): "All you female fans out there, thank you for waiting!",
                (7.0, 8.0, 3): "I'm finally back.",
                (8.2, 10.3, 3): "I've waited for three episodes.",
                (10.3, 12.0, 3): "Moe-Moe has been enduring some hard and distressing days.",
                (12.5, 15.8, 3): "I'll end the tyranny for her!",
            }

        elif Fnum == 8:
            
            ANI += [
                ('v', 'to0912a', 0),
                ('at', ('em_0101', [MOVE_VERTICAL(tm=8.0, delay=4.0, start=0.0, end=1.0)], 'cg'), (0.5, 15.0)),
                ]
            SUBS = {
                (2.5, 6.5, 1): "After everybody goes to sleep, Marumu looks up at the sky.",
                (7.5, 13.0, 1): "She looks beautiful yet sad under the moonlight.",
                (13.7, 18.0, 1): "What is the mysterious girl thinking about, looking at the moon?",
            }

        elif Fnum == 9:
            
            ANI += [
                ('v', 'yu0041', 0),
                ('i', (None, 'et_0201', None), (0.0, 2.0)),
                ('i', (None, 'et_0203', None), (0.5, 1.0)),
                ('i', (None, 'et_0201', None), (0.0, 2.0)),
                ('i', (None, 'et_0203', None), (0.5, 1.0)),
                ('i', (None, 'et_0201', None), (0.0, 2.0)),
                ('i', (None, 'et_0203', None), (0.5, 1.0)),
                ('i', (None, 'et_0201', None), (0.0, 2.0)),
                ('i', (None, 'et_0203', None), (0.5, 1.6)),
                ]
            SUBS = {
                (2.5, 4.5): "Ha ha ha.",
                (5.0, 12.0): "If that slowpoke girl joins in the game, our class will win for sure.",
                (13.0, 14.5): "Is she practicing now?",
                (15.0, 17.0): "It's too late and it's useless.",
            }

        elif Fnum == 10:
            
            ANI += [
                ('v', 'na0372', 0),
                ('at', ('nt1101', [MOVE_VERTICAL(tm=3.0, delay=2.0, start=1.0, end=0.0)], 'bg'), (0.0, 5.2)),
                ('at', ('nt1102', [MOVE_VERTICAL(tm=3.0, delay=2.0, start=1.0, end=0.0)], 'bg'), (0.2, 5.0)),
                ('i', ('nt1103', None, None), (0.5, 4.0)),
                ]
            SUBS = {
                (2.5, 8.0, 3): "Yusuke, stop dilly-dallying and make up your mind.",
                (8.7, 13.3, 3): "All right, I'll help you.",
                (14.3, 16.3, 3): "Which girl do you like the most?",
                (16.3, 17.5, 3): "Tell your sis!",
            }

        elif Fnum == 11:
            
            ANI += [
                ('v', 'to0914', 0),
                ('at', ('nt1201', [MOVE_HORIZONTAL(tm=2.0, delay=0.0, start=1.0, end=0.0)], 'bg'), (0.1, 3.1)),
                ('at', ('nt1202', [MOVE_HORIZONTAL(tm=2.0, delay=0.0, start=0.0, end=1.0)], 'bg'), (0.1, 3.1)),
                ('at', ('nt1203', [MOVE_HORIZONTAL(tm=2.0, delay=0.0, start=1.0, end=0.0)], 'bg'), (0.1, 3.1)),
                ('at', ('nt1204', [MOVE_HORIZONTAL(tm=2.0, delay=0.0, start=0.0, end=1.0)], 'bg'), (0.1, 3.3)),
                ]
            SUBS = {
                (2.8, 5.8, 1): "There's a man among the girls.",
                (6.2, 9.3, 1): "We're living in the same room together.",
                (10.8, 15.8, 1): "It's not strange to have some feelings toward him... I guess.",
            }

        elif Fnum == 12:
            
            ANI += [
                ('v', 'as1247', 0),
                ('i', ('bg01a', None, 'tas047'), (0.0, 1.0)),
                ('i', (None, 'ka_01', None), (0.2, 1.5)),
                ('i', ('bg05b', None, 'tto034'), (0.0, 1.0)),
                ('i', (None, 'kt_01', None), (0.2, 1.5)),
                ('i', ('bg03c', None, 'tma003'), (0.0, 1.0)),
                ('i', (None, 'km_01', None), (0.2, 1.5)),
                ('i', (None, 'e3_05', None), (0.2, 2.5)),
                ('i', ('white', None, None), (1.5, 0.0)),
                ('i', (None, 'e3_0211', None), (0.2, 3.5)),
                ]
            SUBS = {
                (2.5, 6.2, 0): "It was a mistake to bring Yusuke here, after all.",
                (7.2, 11.3, 0): "Flirting with all three girls...what's the big idea?",
                (12.3, 14.2, 0): "I've run out of patience.",
                (15.0, 19.0, 0): "Yusuke, make up your mind!",
            }

        elif Fnum == 13:
            
            ANI += [
                ('v', 'as1249', 0),
                ('at', ('ea_03', [MOVE_HORIZONTAL(tm=2.0, start=1.0, end=0.0)], 'cg'), (0.0, 2.0)),
                ('i', (None, 'sde_0101', None), (0.0, 1.0)),
                ('i', (None, 'sde_0108', None), (0.0, 1.0)),
                ('i', (None, 'sde_0101', None), (0.0, 1.0)),
                ('i', (None, 'sde_0108', None), (0.0, 1.0)),
                ('at', ('em_0101', [MOVE_VERTICAL(tm=3.5, start=0.0, end=1.0)], 'cg'), (0.0, 3.5)),
                ('i', (None, 'ey_0105', None), (0.0, 1.0)),
                ('i', (None, 'ey_0110', None), (0.0, 1.0)),
                ('i', (None, 'ey_0105', None), (0.0, 1.0)),
                ('i', (None, 'ey_0110', None), (0.0, 1.0)),
                ('at', ('e3_0305', [MOVE_HORIZONTAL(tm=3.0, start=1.0, end=0.0)], 'cg'), (0.0, 5.0)),
                ]
            SUBS = {
                (2.7, 5.6, 0): "The second half of Heart de Roommate has begun.",
                (6.6, 9.7, 0): "The story is heading to it's climax.",
                (10.5, 13.0, 0): "What will happen to Yusuke's love?",
                (13.5, 15.4, 0): "What are Moe-Moe's true intentions?",
                (16.0, 18.0, 0): "When will Marumu go back to the moon?",
                (18.4, 22.8, 0): "Is Toshibo really a cat?",
            }

        elif Fnum == 14:
            
            if F015 == 0:
                ANI += [
                    ('v', 'as1251', 0),
                    ('i', ('sora01', None, 'tas708'), (0.0, 1.3)),
                    ('i', (None, None, 'tas706'), (0.0, 1.3)),
                    ('i', (None, None, 'tas708'), (0.0, 1.3)),
                    ('i', (None, None, 'tas706'), (0.0, 1.3)),
                    ('i', (None, None, 'tas708'), (0.0, 1.3)),
                    ('i', (None, None, 'tas706'), (0.0, 1.3)),
                    ('at', ('nt1501', [MOVE_VERTICAL(tm=2.4, delay=1.5, start=1.0, end=0.0)], 'bg'), (0.5, 3.9)),
                    ('i', ('nt1502', None, None), (0.2, 2.1)),
                    ]
                SUBS = {
                    (2.5, 4.3, F015): "A new semester begins.",
                    (4.6, 5.5, F015): "Yusuke!",
                    (5.5, 9.4, F015): "Don't be slovenly, even if you do have a pretty girlfriend.",
                    (9.7, 11.5, F015): "Straighten yourself out!",
                    (12.5, 17.0, F015): "A transfer student is the sign of an approaching storm.",
                }
            
            elif F015 == 1:
                ANI += [
                    ('v', 'to0917', 0),
                    ('i', ('sora01', None, 'tto713'), (0.0, 1.4)),
                    ('i', (None, None, 'tto709'), (0.0, 1.4)),
                    ('i', (None, None, 'tto713'), (0.0, 1.4)),
                    ('i', (None, None, 'tto709'), (0.0, 1.4)),
                    ('i', (None, None, 'tto713'), (0.0, 1.4)),
                    ('i', (None, None, 'tto709'), (0.0, 1.4)),
                    ('i', (None, None, 'tto713'), (0.0, 1.2)),
                    ('at', ('nt1501', [MOVE_VERTICAL(tm=2.4, delay=1.5, start=1.0, end=0.0)], 'bg'), (0.5, 3.9)),
                    ('i', ('nt1502', None, None), (0.2, 2.2)),
                    ]
                SUBS = {
                    (2.5, 5.5, F015): "I'm ready to start the new semester.",
                    (6.0, 8.9, F015): "Yusuke and I spend the night together.",
                    (9.6, 11.8, F015): "How come my heart is beating so fast?",
                    (13.0, 19.0, F015): "I've heard a rumor about a rival against the heroine (me).",
                }
            
            else:
                ANI += [
                    ('v', 'ma0476', 0),
                    ('i', ('sora01', None, 'tma602'), (0.0, 1.3)),
                    ('i', (None, None, 'tma621'), (0.0, 1.3)),
                    ('i', (None, None, 'tma602'), (0.0, 1.3)),
                    ('i', (None, None, 'tma621'), (0.0, 1.3)),
                    ('i', (None, None, 'tma602'), (0.0, 1.3)),
                    ('i', (None, None, 'tma621'), (0.0, 1.3)),
                    ('at', ('nt1501', [MOVE_VERTICAL(tm=2.4, delay=1.5, start=1.0, end=0.0)], 'bg'), (0.5, 3.9)),
                    ('i', ('nt1502', None, None), (0.5, 0.8)),
                    ]
                SUBS = {
                    (2.5, 5.5, F015): "A new semester, I'll do my best.",
                    (6.0, 8.6, F015): "I'm studying about love with Yusuke.",
                    (9.0, 10.8, F015): "We spend fulfilling days together.",
                    (11.4, 15.6, F015): "A rival of few words is against me...!?",
                }

        elif Fnum == 15:
            
            ANI += [
                ('v', 'to0919', 0),
                ('i', ('sora02', None, 'tto020'), (0.0, 0.8)),
                ('i', (None, None, 'tto019'), (0.0, 0.8)),
                ('i', (None, None, 'tto020'), (0.0, 0.8)),
                ('i', (None, None, 'tto019'), (0.0, 0.8)),
                ('i', ('bg07a', None, 'tmi001'), (0.0, 1.6)),
                ('i', ('sora02', None, 'tto036'), (0.0, 1.0)),
                ('i', ('black', None, None), (-1.0, 1.0)),
                ('i', ('sora02', None, 'tto020'), (0.0, 0.8)),
                ('i', (None, None, 'tto019'), (0.0, 0.8)),
                ('i', (None, None, 'tto020'), (0.0, 0.8)),
                ('i', (None, None, 'tto019'), (0.0, 0.8)),
                ('i', ('bg04a', None, 'tko001', 'tmi001'), (0.0, 2.2)),
                ('i', ('sora02', None, 'tto011'), (0.0, 3.4)),
                ]
            SUBS = {
                (2.7, 4.8, 1): "Everyone enjoys their youth.",
                (4.8, 8.0, 1): "Girls are interested in handsome boys and want to know who likes whom.",
                (8.6, 14.5, 1): "A lot of people find their lovers during summer and winter...",
                (14.5, 15.4, 1): "Yikes!",
                (15.8, 19.0, 1): "Oh, please forget what I just said...",
            }

        elif Fnum == 16:
            
            if F015 == 0:
                ANI += [
                    ('v', 'as1253a', 0),
                    ('i', ('sora02', None, None), (0.5, 3.0)),
                    ('i', (None, 'ea_0101', None), (0.5, 7.0)),
                    ('i', ('white', None, None), (1.0, 0.0)),
                    ]
                SUBS = {
                    (2.5, 5.6, F015): "I want to relax on the weekends.",
                    (6.5, 10.1, F015): "However, there's a place I can visit only on weekends.",
                    (11.0, 14.3, F015): "I can be a cute heroine once in a while...right?",
                }
            
            elif F015 == 1:
                ANI += [
                    ('v', 'to0921', 0),
                    ('i', ('sora02', None, None), (0.5, 3.0)),
                    ('i', ('bg03a', None, None), (0.5, 3.0)),
                    ('i', ('bg16a', None, None), (0.5, 3.0)),
                    ('i', ('bg14a', None, None), (0.5, 2.5)),
                    ('i', (None, None, 'tto220'), (0.5, 2.0)),
                    ]
                SUBS = {
                    (2.5, 5.5, F015): "I'll go back to my parents' place!",
                    (6.2, 9.8, F015): "But just for the weekend.",
                    (10.4, 11.0, F015): "What?",
                    (11.5, 13.8, F015): "Is Yusuke coming with me?",
                    (14.6, 18.9, F015): "Is this our first date!?",
                }
            
            else:
                ANI += [
                    ('v', 'ma0478', 0),
                    ('i', ('sora02', None, None), (0.5, 5.0)),
                    ('i', (None, None, 'tma602'), (0.0, 1.0)),
                    ('i', (None, None, 'tma621'), (0.0, 1.0)),
                    ('i', (None, None, 'tma602'), (0.0, 1.0)),
                    ('i', (None, None, 'tma621'), (0.0, 1.0)),
                    ('i', (None, None, 'tma602'), (0.0, 1.0)),
                    ('i', (None, None, 'tma621'), (0.0, 1.0)),
                    ]
                SUBS = {
                    (2.6, 5.0, F015): "I study on the weekends.",
                    (5.3, 7.5, F015): "I study with Toshibo.",
                    (8.1, 10.6, F015): "Yusuke detected, Yusuke detected.",
                    (11.0, 14.0, F015): "I'll show him what I've learned.",
                }

        elif Fnum == 17:
            
            ANI += [
                ('v', 'as1253', 0),
                ('i', (None, 'raf_12', None), (0.2, 3.5)),
                ('i', ('red', None, None), (0.3, 0.0)),
                ('i', (None, 'raf_12', None), (0.0, 1.0)),
                ('i', ('red', None, None), (0.3, 0.0)),
                ('i', (None, 'raf_12', None), (0.0, 1.0)),
                ('i', (None, 'raf_15', None), (0.2, 3.8)),
                ('i', (None, 'raf_16', None), (0.2, 3.8)),
                ('i', (None, 'raf_13', None), (0.2, 3.8)),
                ]
            SUBS = {
                (2.5, 5.0, 0): "Alarm! Everybody, alarm!",
                (5.4, 6.9, 0): "Earth is in danger.",
                (7.2, 8.6, 0): "The end of the world!",
                (9.0, 11.0, 0): "Judgment day is coming!",
                (12.0, 16.8, 0): "Hey, Moe-Moe and Marutan, we don't have time to drink tea and relax!",
                (17.5, 22.0, 0): "If we don't defend Earth, who will?",
            }

        elif Fnum == 18:
            
            if F015 == 0:
                ANI += [
                    ('v', 'as1255', 0),
                    ('i', ('bg19a', None, 'tas711'), (0.0, 1.0)),
                    ('i', (None, None, 'tas712'), (0.0, 1.0)),
                    ('i', (None, None, 'tas711'), (0.0, 1.0)),
                    ('i', (None, None, 'tas712'), (0.0, 1.0)),
                    ('i', (None, None, 'tas711'), (0.0, 1.0)),
                    ('i', (None, None, 'tas712'), (0.0, 1.0)),
                    ('i', ('white', None, None), (0.5, 0.0)),
                    ('i', ('bg19a', None, 'tas712'), (0.0, 2.0)),
                    ('i', ('bg19a', None, None), (0.0, 0.0)),
                    ('at', ('raf_23', [], 'ev'), (0.0, 2.0)),
                    ('i', ('white', None, None), (0.5, 0.0)),
                    ('i', ('bg01a', None, 'tas013'), (0.0, 2.2)),
                    ]
                SUBS = {
                    (2.5, 6.5, F015): "What? Why are we girls so close?",
                    (7.0, 10.0, F015): "Do you want to know the secret?",
                    (11.3, 15.8, F015): "Of course, it's because of MY efforts.",
                }
            
            elif F015 == 1:
                ANI += [
                    ('v', 'to0923', 0),
                    ('i', ('bg19a', None, 'tto717'), (0.0, 1.0)),
                    ('i', (None, None, 'tto718'), (0.0, 1.0)),
                    ('i', (None, None, 'tto717'), (0.0, 1.0)),
                    ('i', (None, None, 'tto718'), (0.0, 1.0)),
                    ('i', (None, None, ''), (0.0, 0.0)),
                    ('at', ('raf_23', [], 'ev'), (0.0, 2.0)),
                    ('i', ('white', None, None), (1.0, 0.0)),
                    ('i', ('bg19a', None, 'tto719'), (0.0, 1.0)),
                    ('i', ('bg01a', None, 'tto019'), (0.0, 2.0)),
                    ]
                SUBS = {
                    (2.5, 4.0, F015): "Asumin and Marutan.",
                    (4.5, 7.3, F015): "They're my best friends.",
                    (7.9, 12.5, F015): "But we weren't this close in the beginning.",
                }
            
            else:
                ANI += [
                    ('v', 'ma0480', 0),
                    ('i', ('bg19a', None, 'tma625'), (0.0, 3.5)),
                    ('i', ('white', None, None), (1.0, 0.0)),
                    ('i', (None, 'raf_01', None), (0.0, 0.8)),
                    ('i', (None, 'raf_02', None), (0.0, 0.5)),
                    ('i', (None, 'raf_03', None), (0.0, 0.3)),
                    ('i', (None, 'raf_04', None), (0.0, 0.3)),
                    ('i', (None, 'raf_05', None), (0.0, 0.15)),
                    ('i', (None, 'raf_06', None), (0.0, 0.15)),
                    ('i', (None, 'raf_07', None), (0.0, 0.15)),
                    ('i', ('white', None, None), (1.5, 0.0)),
                    ('i', ('bg01a', None, 'tma001'), (0.0, 2.7)),
                    ('i', (None, None, 'tma008'), (0.0, 2.7)),
                    ]
                SUBS = {
                    (2.6, 5.0, F015): "All legends have beginnings.",
                    (5.6, 8.2, F015): "Nobody was born a hero or a heroine.",
                    (8.8, 11.9, F015): "Fate gives guidance to a person.",
                    (12.6, 16.5, F015): "Another girl is involved in this particular fate...",
                }

        elif Fnum == 19:
            
            ANI += [
                ('v', 'as1257', 0),
                ('i', ('bg16a', None, 'tto007'), (0.0, 1.5)),
                ('i', ('white', None, None), (1.0, 0.0)),
                ('i', ('sora02', None, 'tas708', 'tta001'), (0.0, 1.0)),
                ('i', (None, None, 'tas703', 'tta001'), (0.0, 1.0)),
                ('i', (None, None, 'tas708', 'tta001'), (0.0, 1.0)),
                ('i', (None, None, 'tas703', 'tta001'), (0.0, 1.0)),
                ('i', (None, None, 'tma605', 'tta001'), (0.0, 1.5)),
                ('i', (None, None, 'tma615', 'tta002'), (0.1, 1.5)),
                ('i', (None, None, 'tma605', 'tta001'), (0.1, 1.5)),
                ('i', (None, None, 'tma615', 'tta002'), (0.1, 1.5)),
                ]
            SUBS = {
                (2.5, 3.5, 0): "Listen everybody!",
                (3.8, 7.0, 0): "Moe-Moe is going to attend a meeting for an arranged marriage!",
                (7.5, 9.0, 0): "I can't let that happen.",
                (9.5, 10.8, 0): "Yusuke, I know you agree with me.",
                (11.5, 13.0, 0): "We'll obstruct the meeting!",
                (13.5, 15.5, 0): "Commence code-V!",
            }

        elif Fnum == 20:
            
            ANI += [
                ('v', 'ts0079', 0),
                ('i', ('bg01a', None, 'tts001'), (0.0, 1.0)),
                ('i', (None, None, 'tts002'), (0.0, 1.0)),
                ('i', (None, None, 'tts001'), (0.0, 1.0)),
                ('i', (None, None, 'tts002'), (0.0, 1.0)),
                ('i', (None, None, 'tts004'), (0.0, 1.0)),
                ('i', (None, None, 'tts007'), (0.0, 1.0)),
                ('i', (None, None, 'tts010'), (0.0, 1.0)),
                ('i', (None, None, 'tts013'), (0.0, 1.0)),
                ('i', (None, None, 'tts017'), (0.0, 1.0)),
                ('i', (None, None, 'tts019'), (0.0, 1.0)),
                ]
            SUBS = {
                (2.5, 4.8, 14): "Meow! Meow, meow, meow!",
                (4.8, 6.2, 14): "Meoooow!!",
                (7.0, 9.8, 14): "Huh? Can I talk, meow?",
                (10.4, 12.6, 14): "I'm happy, meow!!",
            }

        elif Fnum == 21:
            
            ANI += [
                ('v', 'to0925', 0),
                ('i', ('nt0304', None, None), (0.2, 3.5)),
                ('i', ('sora01', None, 'tto708'), (0.0, 1.0)),
                ('i', (None, None, 'tto703'), (0.0, 1.0)),
                ('i', (None, None, 'tto708'), (0.0, 1.0)),
                ('i', (None, None, 'tto703'), (0.0, 1.0)),
                ('i', ('bg01a', None, 'tts016'), (0.0, 1.1)),
                ('i', (None, None, 'tts001'), (0.0, 1.6)),
                ('i', (None, None, 'tts020'), (0.0, 2.3)),
                ]
            SUBS = {
                (2.5, 5.0, 1): "Toshibo doesn't look good.",
                (5.8, 8.5, 1): "He groans and suffers as if in pain.",
                (9.2, 10.5, 1): "What's wrong with him?",
                (11.2, 13.0, 1): "Did he eat something bad?",
                (13.5, 15.8, 1): "He usually eats too much.",
            }

        elif Fnum == 22:
            
            ANI += [
                ('v', 'to0927', 0),
                ('i', (None, 'es_0107', None), (0.5, 3.0)),
                ('i', (None, 'e3_0301', None), (0.5, 3.0)),
                ('i', (None, 'e3_0211', None), (0.5, 3.0)),
                ('i', ('white', None, None), (0.5, 0.0)),
                ]
            SUBS = {
                (1.7, 4.5, 1): "What's wrong with you, Asumi?",
                (5.5, 7.5, 1): "Why don't you tell us anything?",
                (8.8, 12.0, 1): "Do you think we're useless?",
            }

        elif Fnum == 23:
            
            ANI += [
                ('v', 'as1258a', 0),
                ('i', ('sora02', None, None), (0.2, 1.0)),
                ('at', ('raf_23', [], 'ev'), (0.0, 2.0)),
                ('i', (None, 'raf_15', None), (0.2, 2.5)),
                ('i', (None, 'raf_24', None), (0.2, 3.5)),
                ('i', ('white', None, None), (1.0, 0.0)),
                ]
            SUBS = {
                (1.8, 4.5, 0): "Everyone is worried about me.",
                (5.0, 8.0, 0): "But I have to do this alone.",
                (8.8, 10.5, 0): "Sorry guys...{space=162}",
                (10.5, 13.8, 0): "Sorry guys...hey, guys!?",
            }

        elif Fnum == 24:
            
            ANI += [
                ('v', 'hi0096', 0),
                ('i', ('nt2501', None, None), (0.2, 2.0)),
                ('i', ('white', None, None), (0.5, 0.0)),
                ('i', ('nt2502', None, None), (0.2, 2.0)),
                ('i', ('white', None, None), (0.5, 0.0)),
                ('i', ('nt2503', None, None), (0.2, 2.0)),
                ('i', ('white', None, None), (0.5, 0.0)),
                ('i', ('nt2504', None, None), (0.2, 2.5)),
                ]
            SUBS = {
                (1.7, 3.2, 5): "A lot of things have happened.",
                (3.2, 5.0, 5): "I have some sad and hard memories.",
                (6.0, 9.5, 5): "However, I can walk toward the future now.",
                (9.8, 13.2, 5): "Because you guys gave me courage.",
            }



    call anime (ANI, SUBS, CB) from _call_anime

    python:
        SUBS = None

        if Fnum == 1:
            
            ANI = [
                ('v', 'to0910a', 0),
                ('i', ('nt02', None, None), (0.5, 8.2)),
                ]
            SUBS = {
                (0.3, 5.0, 1): 'The next episode of Heart de Roommate: "Transformation"',
                (5.0, 8.4, 1): 'Yusuke, you look good in those clothes. Tee-hee.'
                }

        elif Fnum == 2:
            
            ANI = [
                ('v', 'as1242', 0),
                ('i', ('nt03', None, None), (0.5, 6.0)),
                ]
            SUBS = {
                (0.3, 4.0, 0): 'Next episode of Heart de Roommate: "The Name is Toshibo"',
                (4.0, 6.2, 14): 'Meow, meow, meow.'
                }

        elif Fnum == 3:
            
            ANI = [
                ('v', 'as1244', 0),
                ('i', ('nt04', None, None), (0.5, 7.2)),
                ]
            SUBS = {
                (0.3, 5.1, 0): 'Next episode of Heart de Roommate:\n"Emergency Meeting at the Hot Springs"',
                (5.2, 7.2, 0): 'Haahh, Viva-non, Viva-non.'
                }

        elif Fnum == 4:
            
            ANI = [
                ('v', 'na0369', 0),
                ('i', ('nt05', None, None), (0.5, 9.2)),
                ]
            SUBS = {
                (0.3, 4.6, 3): 'Next episode of Heart de Roommate: "My Savage Sister!"',
                (5.1, 9.2, 3): 'Come on! Throw yourself into my boobs.'
                }

        elif Fnum == 5:
            
            ANI = [
                ('v', 'as1246', 0),
                ('i', ('nt06', None, None), (0.5, 8.2)),
                ]
            SUBS = {
                (0.3, 4.6, 0): 'Next episode of Heart de Roommate: "Code Name: U-SUKE"',
                (5.1, 8.6, 0): "I'll admit you're a man, if you achieve something great."
                }

        elif Fnum == 6:
            
            ANI = [
                ('v', 'yo0364', 0),
                ('i', ('nt07', None, None), (0.5, 10.3)),
                ]
            SUBS = {
                (0.3, 7.5, 4): 'Next episode of Heart de Roommate: "U-SUKE Exposed!',
                (8.0, 11.0, 4): "Stay there, I'll wash your back."
                }

        elif Fnum == 7:
            
            ANI = [
                ('v', 'na0371', 0),
                ('i', ('nt08', None, None), (0.5, 7.2)),
                ]
            SUBS = {
                (0.3, 5.2, 3): 'Next episode of Heart de Roommate: "Clash of the Titans! Asumi vs. Namiki"',
                (5.3, 7.5, 3): "Moe-Moe, I'm coming."
                }

        elif Fnum == 8:
            
            ANI = [
                ('v', 'to0913a', 0),
                ('i', ('nt09', None, None), (0.5, 7.2)),
                ]
            SUBS = {
                (0.3, 5.0, 1): 'Next episode of Heart de Roommate: "A Girl under the Moonlight"',
                (5.0, 7.3, 2): "... Remember whenever you look at the moon."
                }

        elif Fnum == 9:
            
            ANI = [
                ('v', 'yu0042', 0),
                ('i', ('nt10', None, None), (0.5, 10.0)),
                ]
            SUBS = {
                (0.3, 5.5): 'Next episode of Heart de Roommate: "The Baseball Fanatics"',
                (6.8, 9.5): "Well, good luck.{space=92}",
                (9.5, 10.0): "Well, good luck... Ugh."
                }

        elif Fnum == 10:
            
            ANI = [
                ('v', 'yo0365', 0),
                ('i', ('nt11', None, None), (0.5, 10.3)),
                ]
            SUBS = {
                (0.3, 7.3, 4): 'Next episode of Heart de Roommate: "Close Encounter of the Two Sisters"',
                (8.3, 11.0, 4): "... Perhaps you like older women?"
                }

        elif Fnum == 11:
            
            ANI = [
                ('v', 'to0915', 0),
                ('i', ('nt12', None, None), (0.5, 9.2)),
                ]
            SUBS = {
                (0.3, 6.3, 1): 'Next episode of Heart de Roommate: "Shaking Heart: Part 1"',
                (7.5, 10.0, 1): "... Who do you like the most?"
                }

        elif Fnum == 12:
            
            ANI = [
                ('v', 'as1248', 0),
                ('i', ('nt13', None, None), (0.5, 6.0)),
                ]
            SUBS = {
                (0.3, 4.0, 0): 'Next episode of Heart de Roommate: "Shaking Heart: Part 2"',
                (4.6, 6.5, 0): "Be a man!"
                }

        elif Fnum == 13:
            
            ANI = [
                ('v', 'as1250', 0),
                ('i', ('nt14', None, None), (0.5, 7.3)),
                ]
            SUBS = {
                (0.3, 4.8, 0): 'Next episode of Heart de Roommate: "The \'All Girls\' Secret Meeting"',
                (5.5, 6.7, 0): "Something naughty will happen.",
                (6.7, 7.7, 1): "She’s lying"
                }

        elif Fnum == 14:
            
            if F015 == 0:
                ANI = [
                    ('v', 'as1252', 0),
                    ('i', ('nt15', None, None), (0.5, 7.2)),
                    ]
                SUBS = {
                    (0.3, 4.8, F015): 'Next episode of Heart de Roommate: "A New Semester & a Transfer Student"',
                    (5.0, 8.0, F015): "The story is getting more and more interesting!"
                    }
            
            elif F015 == 1:
                ANI = [
                    ('v', 'to0918', 0),
                    ('i', ('nt15', None, None), (0.5, 8.2)),
                    ]
                SUBS = {
                    (0.3, 4.4, F015): 'Next episode of Heart de Roommate: "A New Semester & a Transfer Student"',
                    (5.2, 8.6, F015): "Our stories have just begun."
                    }
            
            else:
                ANI = [
                    ('v', 'ma0477', 0),
                    ('i', ('nt15', None, None), (0.5, 8.2)),
                    ]
                SUBS = {
                    (0.3, 5.0, F015): 'Next episode of Heart de Roommate: "A New Semester & a Transfer Student"',
                    (5.5, 8.5, F015): "Ready for the new semester? Go!"
                    }

        elif Fnum == 15:
            
            ANI = [
                ('v', 'to0920', 0),
                ('i', ('nt16', None, None), (0.5, 6.5)),
                ]
            SUBS = {
                (0.3, 4.0, 1): 'Next episode of Heart de Roommate: "Love Storm"',
                (5.0, 7.0, 1): "Yusuke, you're in danger!"
                }

        elif Fnum == 16:
            
            if F015 == 0:
                ANI = [
                    ('v', 'as1254a', 0),
                    ('i', ('nt17', None, None), (0.5, 7.2)),
                    ]
                SUBS = {
                    (0.3, 4.3, F015): 'Next episode of Heart de Roommate: "One Fine Day-Off"',
                    (5.1, 7.3, F015): "I'm going to cry because I'm a girl!"
                    }
            
            elif F015 == 1:
                ANI = [
                    ('v', 'to0922', 0),
                    ('i', ('nt17', None, None), (0.5, 10.2)),
                    ]
                SUBS = {
                    (0.3, 4.8, F015): 'Next episode of Heart de Roommate: "One Fine Day-Off"',
                    (6.2, 11.0, F015): "Oh, I'm already excited."
                    }
            
            else:
                ANI = [
                    ('v', 'ma0479', 0),
                    ('i', ('nt17', None, None), (0.5, 8.2)),
                    ]
                SUBS = {
                    (0.3, 4.8, F015): 'Next episode of Heart de Roommate: "One Fine Day-Off"',
                    (5.5, 8.0, F015): "Devotion everyday! Devotion!"
                    }

        elif Fnum == 17:
            
            ANI = [
                ('v', 'as1254', 0),
                ('i', ('nt18', None, None), (0.5, 7.2)),
                ]
            SUBS = {
                (0.3, 4.0, 0): 'Next episode of Heart de Roommate: "The Day the Earth Falls"',
                (4.7, 7.5, 0): "We're the ones who will protect world peace!"
                }

        elif Fnum == 18:
            
            if F015 == 0:
                ANI = [
                    ('v', 'as1256', 0),
                    ('i', ('nt19', None, None), (0.5, 6.0)),
                    ]
                SUBS = {
                    (0.3, 4.0, F015): 'Next episode of Heart de Roommate: "Then the Three Meet"',
                    (4.5, 6.3, F015): "You'll find our starting point here!"
                    }
            
            elif F015 == 1:
                ANI = [
                    ('v', 'to0924', 0),
                    ('i', ('nt19', None, None), (0.5, 9.2)),
                    ]
                SUBS = {
                    (0.3, 5.2, F015): 'Next episode of Heart de Roommate: "Then the Three Meet"',
                    (6.2, 10.0, F015): "Memories of the beginning are now..."
                    }
            
            else:
                ANI = [
                    ('v', 'ma0481', 0),
                    ('i', ('nt19', None, None), (0.5, 10.0)),
                    ]
                SUBS = {
                    (0.3, 4.5, F015): 'Next episode of Heart de Roommate: "Then the Three Meet"',
                    (5.0, 9.6, F015): "You'll see the beginning of the legend...{space=156}",
                    (9.6, 10.5, F015): "You'll see the beginning of the legend... Not really."
                    }

        elif Fnum == 19:
            
            ANI = [
                ('v', 'as1258', 0),
                ('i', ('nt20', None, None), (0.5, 8.8)),
                ]
            SUBS = {
                (0.3, 4.0, 0): 'Next episode of Heart de Roommate: "The First Arranged Marriage Meeting"',
                (4.5, 9.5, 0): "He he, don't expect to see the sun tomorrow!"
                }

        elif Fnum == 20:
            
            ANI = [
                ('v', 'ts0079a', 0),
                ('i', ('nt21', None, None), (0.5, 9.2)),
                ]
            SUBS = {
                (0.3, 4.8, 14): 'Next episode of Heart de Roommate: "The Adventures of Toshibo"',
                (5.0, 7.5, 14): "Meow? This is it?",
                (7.5, 9.2, 14): "Meoooow!!",
                }

        elif Fnum == 21:
            
            ANI = [
                ('v', 'to0926', 0),
                ('i', ('nt22', None, None), (0.5, 10.3)),
                ]
            SUBS = {
                (0.3, 3.9, 1): 'Next episode of Heart de Roommate: "The New Life"',
                (5.0, 6.2, 1): "Oh my goodness!",
                (6.2, 10.5, 1): "Is Toshibo a ****** cat?"
                }

        elif Fnum == 22:
            
            ANI = [
                ('v', 'to0928', 0),
                ('i', ('nt23', None, None), (0.5, 11.3)),
                ]
            SUBS = {
                (0.3, 4.8, 1): 'Next episode of Heart de Roommate: "Fading Friendship"',
                (6.3, 11.0, 1): "We're friends...right?"
                }

        elif Fnum == 23:
            
            ANI = [
                ('v', 'as1259', 0),
                ('i', ('nt24', None, None), (0.5, 6.0)),
                ]
            SUBS = {
                (0.3, 4.2, 0): 'Next episode of Heart de Roommate: "Harmony of Minds"',
                (4.5, 6.5, 0): "Our friendship will last forever!"
                }

        elif Fnum == 24:
            
            ANI = [
                ('v', 'hi0097', 0),
                ('i', ('nt25', None, None), (0.5, 7.8)),
                ]
            SUBS = {
                (0.3, 4.2, 5): 'Next episode of Heart de Roommate: "Our Bright Youth"',
                (4.8, 8.2, 5): "A part of youth is over, and another one begins..."
                }

        elif Fnum == 25:
            
            if F015 == 0:
                ANI = [
                    ('v', 'as1260', 0),
                    ('i', ('nt26', None, None), (0.5, 6.5)),
                    ]
            
            elif F015 == 1:
                ANI = [
                    ('v', 'to0929', 0),
                    ('i', ('nt26', None, None), (0.5, 7.2)),
                    ]
            
            else:
                ANI = [
                    ('v', 'ma0481a', 0),
                    ('i', ('nt26', None, None), (0.5, 6.5)),
                    ]
            SUBS = {
                (0.3, 7.2, F015): 'The final episode of Heart de Roommate: "Roommates Forever"',
                }

    call anime (ANI, SUBS) from _call_anime_1

    python:
        del ANI, CB, SUBS

        audio_stop (0.5, 'story')
        audio_stop (0.5, 'decoration')

        bgfx ('black')

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

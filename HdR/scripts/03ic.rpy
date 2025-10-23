

init:
    define ICA = ['',
        'as1274', 'to0942', 'ma0490', 'et0013', 'na0376',
        'as1274', 'yo0368', 'na0376', 'hs0021', 'yu0043',
        'et0011', 'fu0020', ('et0010', 'et0010', 'et0010'), 'et0010', ('as1274', 'as1274', 'ma0484'),
        'to0942', ('as1274', 'to0942', 'ma0490'), None, 'et0014', 'ta0037',
        'ts0080', 'to0942', 'ma0490', 'et0010', 'hi0098a', 
        ]

    define ICB = ['',
        'ic01', 'ic02', 'ic03', 'ic16', 'ic04',
        'ic17', 'ic06', 'ic05', 'ic09', 'ic08',
        'ic18', 'ic10', 'ic19', 'ic20', 'ic21',
        'ic22', ('ic23', 'ic24', 'ic25'), None, 'ic27', 'ic11',
        'ic12', 'ic14', 'ic15', 'ic13', 'ic07',
        ]

label ep_middle:

    show screen anime_overlay ('ep_middle_off')
    python:

        audio_stop (0.0)
        audio_stop (0.0, 'story')
        audio_stop (0.0, 'decoration')

        _sf = ''
        if isinstance(ICA[Fnum], (str, unicode)):
            _sf = ICA[Fnum]
        elif isinstance(ICA[Fnum], (list, tuple)) and (F015 in [0, 1, 2]):
            _sf = ICA[Fnum][F015]

        _pic = ''
        if isinstance(ICB[Fnum], (str, unicode)):
            _pic = ICB[Fnum]
        elif isinstance(ICB[Fnum], (list, tuple)) and (F015 in [0, 1, 2]):
            _pic = ICB[Fnum][F015]

    if Fnum in [7, 9, 11, 13, 16]:
        $ say_hide ()
    else:
        call blackout (True) from _call_blackout_71
    call breakskip from _call_breakskip_4

    python:
        bgfx (_pic, {'master': blinds, 'screens': None})
        wait (1.0)
        empat ('j2')
        vox (_sf, delay=1.5)
        pause (6.0)

label ep_middle_off:

    python:
        audio_stop (1.0, 'story')
        audio_stop (1.0, 'decoration')
        bgfx ('black', {'master': blinds, 'screens': None})
        wait (1.0)
        del _pic, _sf

    hide screen anime_overlay

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

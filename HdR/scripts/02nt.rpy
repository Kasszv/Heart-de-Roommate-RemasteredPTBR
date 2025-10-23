

init:
    define T2A = ['',
        'as1261', 'to0930', 'as1262', 'as1263', 'na0373',
        'as1264', 'yo0366', 'na0374', 'ma0482', 'to0931',
        'na0375', 'to0932', 'as1265', 'as1266', ('as1267', 'to0934', 'ma0484'),
        'to0935', ('as1269', 'to0936', 'ma0485'), 'as1268', ('as1270', 'to0937', 'ma0486'), 'to0938',
        'ma0487', 'as1271', 'to0939', 'as1272', 'hi0098',
        ('as1273', 'to0941', 'ma0489'), '', '', ''
        ]

label ep_start:

    python:
        _pic = 'nt%02d' % Fnum
        _ovl = 't01' if Fnum <= 13 else 't02'
        if 23 <= Fnum <= 27:
            _pic = 't%02d' % Fnum
            _ovl = ''

        _sf = ''
        if isinstance(T2A[Fnum], (str, unicode)):
            _sf = T2A[Fnum]
        elif isinstance(T2A[Fnum], (list, tuple)) and (F015 in [0, 1, 2]):
            _sf = T2A[Fnum][F015]

    if Fnum in [13, 14, 24, 25, 26, 27]:
        $ say_hide ()
    else:
        call blackout (True) from _call_blackout
    call breakskip from _call_breakskip

    python:
        audio_stop (0.0)
        audio_stop (0.0, 'story')
        audio_stop (0.0, 'decoration')

        if Fnum < 23 or Fnum > 27:
            empat ('j1')
        bg (_pic)
        bgfx (_ovl, tag=1, pos=[ALIGN(0.0, 0.0)])
        vox (_sf, delay=1.5)
        if Fnum < 23 or Fnum > 27:
            pause (7.0)
        else:
            pause (5.0)
        del _pic, _ovl, _sf

        audio_stop (0.5, 'story')
        audio_stop (0.5, 'decoration')

    if Fnum not in [25, 27]:
        call blackout () from _call_blackout_1

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

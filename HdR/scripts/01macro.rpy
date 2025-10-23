label breakskip:
    if renpy.is_skipping():
        $ _default_keymap.keymap["toggle_skip"]()
    return

label blackout(cls=False, tm=3.0):
    python:
        audio_stop (tm)
        bgfx ('black', cls=cls)
    return

init -10:

    screen anime_overlay(label_name, subtitles=None):
        zorder 200
        modal True
        default clicked = False
        default showing = 0.0
        key ['mouseup_1', 'mouseup_3', 'K_KP_ENTER', 'K_SPACE', 'K_ESCAPE'] action If (clicked, NullAction(), [SetScreenVariable('clicked', True), Jump (label_name)])
        timer 0.1 repeat True action SetScreenVariable('showing', showing + 0.1)

        if persistent.subtitles and subtitles is not None:

            $ keys = [key for key in subtitles.keys() if key[0] <= showing < key[1]]
            if len(keys) > 0:
                hbox:
                    xalign 0.5
                    yalign 0.99

                    if len(keys[-1]) > 2 and keys[-1][-1] in (0, 1, 2, 3, 4, 5, 14):
                        add ui_face(keys[-1][-1], 1)

                    text subtitles.get(keys[-1], ''):
                        color '#FFF'
                        outlines [(2, '#777', 1, 1), (2, '#000', 0, 0)]
                        text_align 0.5
                        justify True

label anime(items, subtitles=None, chibi=0):

    show screen anime_overlay ('anime_off', subtitles)
    python:

        for kind, item, tm in items:
            
            
            if kind == 'm':
                
                empat (item, delay=tm) 
            
            elif kind == 'v':
                
                vox (item, delay=tm+0.01)
            
            
            
            
            
            
            elif kind == 'at':
                
                if item[2] == 'bg':
                    bg (item[0], None, pos=item[1])
                elif item[2] == 'ev':
                    ev (item[0], None, pos=item[1])
                else:
                    cg (item[0], None, pos=item[1])
            
            elif kind == 'i':
                
                if item[0] is not None:
                    bg (item[0], None)
                if item[1] is not None:
                    cg (item[1], None)
                if item[2] is not None:
                    if len(item) > 3 and item[3] is not None:
                        chars (item[2], item[3], None, chibi=chibi)
                    else:
                        char (item[2], None, chibi=chibi)
            
            if kind in ['i', 'at']:
                
                if tm[0] > 0:
                    _fx ({'master': Dissolve(tm[0]), 'screens': None})
                elif tm[0] < 0:
                    _fx ({'master': blinds, 'screens': None})
                else:
                    _fx ({'master': None, 'screens': None})
                
                wait (abs(tm[0])+tm[1])

label anime_off:
    hide screen anime_overlay

    return


define ETYPE1 = ['effect01', 'effect02']
define ETYPE2 = ['effect03', 'effect02']
define ETYPE3 = ['effect01', 'effect02', 'effect01', 'effect02', 'effect03', 'effect02']
label effect(sound_source=None, graphics=[], sound_loop=False, fx=diss_fast, remove=True):
    if len(graphics) == 0:
        return

    python:
        say_hide (diss_flash)
        if sound_source:
            sfx (sound_source, delay=0.05, loop=sound_loop)
        for img in graphics:
            ev (img, fx)
        if remove:
            ev (fx=fx)

    return

define KENKA1 = ['sde_0401', 'sde_0402']*8
define KENKA2 = ['sde_0403', 'sde_0404']*8
define KENKA3 = ['sde_0405', 'sde_0406']*8
label cgeffect(sound_source=None, graphics=[], sound_loop=False, fx=diss_fast):
    if len(graphics) == 0:
        return

    python:
        if sound_source:
            sfx (sound_source, delay=0.05, loop=sound_loop)
        for img in graphics:
            cg (img, fx)

    return

label triple_slide_from_right(picture=''):
    python:
        cg (picture, diss_flash, pos=[MOVE_HORIZONTAL(tm=0.42, start=1.0, end=0.0)], tag=0)
        wait (0.38)
        cg (picture, None, pos=[MOVE_HORIZONTAL(tm=0.84, start=1.0, end=0.0), SHOW(0.1)], tag=1)
        wait (0.78)
        cg (picture, None, pos=[MOVE_HORIZONTAL(tm=1.68, start=1.0, end=0.0), SHOW(0.1)], tag=2)
        wait (2.0)
    return

label cg_slide(picture='', cls=None, tm=1.0, delay=0.0, kind='h', start=0.0, end=1.0):
    python:
        if cls:
            say_hide (cls)
        if kind == 'h':
            cg (picture, fx=None, pos=[MOVE_HORIZONTAL(tm, delay=delay, start=start, end=end)])
        elif kind == 'v':
            cg (picture, fx=None, pos=[MOVE_VERTICAL(tm, delay=delay, start=start, end=end)])
        else:
            cg (picture, fx=None, pos=[MOVE_HORIZONTAL(tm, delay=delay, start=start, end=end), MOVE_VERTICAL(tm, start=start, end=end)])
        pause (tm + delay) 
        if kind == 'h':
            cg (picture, fx=None, pos=[ALIGN(end, 0.0)])
        elif kind == 'v':
            cg (picture, fx=None, pos=[ALIGN(0.0, end)])
        else:
            cg (picture, fx=None, pos=[ALIGN(end, end)])
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

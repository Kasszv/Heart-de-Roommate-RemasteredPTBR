label credits:

    call blackout (True) from _call_blackout_36
    python:
        if renpy.is_skipping():
            _default_keymap.keymap["toggle_skip"]()

    show screen anime_overlay ('credits_end')
    python:
        bgm (15) 

        bgfx ('sr01', diss_long)
        wait (11) 

        for i in range (2, 9): 
            bgfx ('sr%02d1' % i, diss_long)
            wait (2)
            bgfx ('sr%02d2' % i, diss_long)
            wait (17) 

        bgfx ('sr091', diss_long)
        wait (11)

        bgfx ('sr092', diss_long)
        wait (5)

label credits_end:
    hide screen anime_overlay

    python:
        bgfx ('white', diss_long)
        bgfx ('black', diss_long)
        wait (1)



label game_over:
    call blackout (True, 0.5) from _call_blackout_37
    python:
        if renpy.is_skipping():
            _default_keymap.keymap["toggle_skip"]()
        bgfx ('as_logo')
        vox('et0022')
        wait (3)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

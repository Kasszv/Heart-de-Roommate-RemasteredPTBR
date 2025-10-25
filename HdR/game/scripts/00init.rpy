# Configuração de idioma no init
init -3 python:
    if persistent.lang is None:
        persistent.lang = None  # Inglês como padrão

    # Definir o idioma atual
    config.language = persistent.lang

label splashscreen:
    scene black
    with dissolve

    # SEMPRE mostrar o menu de idioma no início do jogo
    call screen language_choice_screen

    # SEGUNDO SPLASHSCREEN - Logo animado (só depois de escolher idioma)
    $ renpy.movie_cutscene ("video/logo.webm")

    python:
        _skipping = False
        quick_menu = False
        bg ('black', fx=diss_flash)
        bgfx ('bg18a')
        wait (0.5)
        chars ('tas704', 'tma606')
        wait (0.8)
        bgfx ('as_logo')
        vox ('et0022')
        wait (2.5)

    scene black
    with dissolve
    $ wait (1)

    return

# Tela personalizada de escolha de idioma
screen language_choice_screen():
    modal True
    zorder 200
    
    # Fundo com imagem
    add "images/bg/ic13.webp"  # Sua imagem de fundo
    
    # Container central
    frame:
        background None
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        
        vbox:
            spacing 40
            xalign 0.5
            
            # Título
            text "SELECT LANGUAGE":
                size 46
                color "#fff"
                xalign 0.5
                outlines [ (4, "#000", 0, 0) ]
            
            # Botões de idioma
            vbox:
                spacing 25
                xalign 0.5
                
                textbutton "PORTUGUÊS":
                    action [
                        SetVariable("persistent.lang", "portugues"),
                        SetVariable("config.language", "portugues"),
                        Return()
                    ]
                    xalign 0.5
                    xsize 320
                    ysize 70
                    text_size 32
                    text_color "#fff"
                    text_hover_color "#ffff00"
                    background "#000000aa"
                    hover_background "#000000dd"
                
                textbutton "ENGLISH":
                    action [
                        SetVariable("persistent.lang", None),
                        SetVariable("config.language", None),
                        Return()
                    ]
                    xalign 0.5
                    xsize 320
                    ysize 70
                    text_size 32
                    text_color "#fff"
                    text_hover_color "#ffff00"
                    background "#000000aa"
                    hover_background "#000000dd"

# Label para mudar idioma pelo menu principal (opcional)
label language_chooser:
    scene black
    call screen language_choice_screen
    $ renpy.utter_restart()

# Opção para mudar idioma no menu principal (opcional)
init python:
    config.main_menu.insert(3, (u'Language', "language_chooser", "True"))
                    
            
         

init -10:

    default persistent.gallery = set ()
    default persistent.pictures = set ()
    default persistent.episodes = set ()
    default persistent.endings = set ()
    default preferences.voice_sustain = True
    default persistent.hide_top_menu = True
    default preferences.afm_time = 15
    default preferences.text_cps = 0
    default persistent.text_cps = 190
    default persistent.subtitles = True


    define narrator = Character(None, color="#ffffff", what_color='#ffffff')
    define speaker = Character('', color="#ffffff", what_color='#ffffff', what_prefix='"', what_suffix='"', voice_tag='v_others')

    define akane = Character(_("Akane"), kind=speaker)

    define asumi = Character(_("Asumi"), kind=speaker, voice_tag='v_asumi')
    define asumi_namiki = Character(_("Asumi & Namiki"), kind=speaker, voice_tag='v_asumi_namiki')
    define asumi_tomoe = Character(_("Asumi & Tomoe"), kind=speaker, voice_tag='v_asumi_tomoe')

    define blackcat = Character(_("Black Cat"), kind=speaker)
    define boy = Character(_("Boy"), kind=speaker)

    define everyone = Character(_("All"), kind=speaker, voice_tag='v_asumi_tomoe_marumu')

    define girl = Character(_("Girl"), kind=speaker)
    define girl_as = Character(_("Girl"), kind=speaker, voice_tag='v_asumi')
    define girl_na = Character(_("Girl"), kind=speaker, voice_tag='v_namiki')
    define hikaru = Character(_("Hikaru"), kind=speaker, voice_tag='v_hikaru')
    define judge = Character(_("Judge"), kind=speaker)
    define kaoru = Character(_("Kaoru"), kind=speaker)
    define kirimaru = Character(_("Kirimaru"), kind=speaker)
    define kitten1 = Character(_("Kitten 1"), kind=speaker)
    define kitten2 = Character(_("Kitten 2"), kind=speaker)
    define kitten3 = Character(_("Kitten 3"), kind=speaker)
    define kosuke = Character(_("Kosuke"), kind=speaker)
    define leftone = Character(_("Left One"), kind=speaker, voice_tag='v_tomoe')
    define magenta = Character(_("MAGENTA"), kind=speaker, voice_tag='v_marumu')
    define man = Character(_("Man"), kind=speaker)
    define marumu = Character(_("Marumu"), kind=speaker, voice_tag='v_marumu')
    define marutan = Character(_("Marutan"), kind=speaker, voice_tag='v_marumu')
    define midori = Character(_("Midori"), kind=speaker)
    define misaki = Character(_("Misaki"), kind=speaker)
    define moemoe = Character(_("Moe-Moe"), kind=speaker, voice_tag='v_tomoe')
    define namiki = Character(_("Namiki"), kind=speaker, voice_tag='v_namiki')
    define narration = Character(_("Narrator"), kind=speaker)
    define nina = Character(_("Nina"), kind=speaker)
    define others = Character(_("Others"), kind=speaker)

    define red = Character(_("RED"), kind=speaker, voice_tag='v_asumi')
    define rightone = Character(_("Right One"), kind=speaker, voice_tag='v_marumu')
    define servant1 = Character(_("Servant 1"), kind=speaker)
    define servant2 = Character(_("Servant 2"), kind=speaker)
    define shadowleaders = Character(_("Shadow Leaders"), kind=speaker, voice_tag='v_tomoe_marumu')
    define takuto = Character(_("Takuto"), kind=speaker)
    define teacher = Character(_("Teacher"), kind=speaker)
    define tomoe = Character(_("Tomoe"), kind=speaker, voice_tag='v_tomoe')
    define tomoe_marumu = Character(_("Tomoe & Marumu"), kind=speaker, voice_tag='v_tomoe_marumu')
    define tomomi = Character(_("Tomoe's Sister"), kind=speaker)
    define toshibo = Character(_("Toshibo"), kind=speaker)
    define uc = Character(_("Unknown Creature"), kind=speaker)
    define unknown = Character(_("???"), kind=speaker)

    define white = Character(_("WHITE"), kind=speaker, voice_tag='v_tomoe')

    define woman = Character(_("Woman"), kind=speaker)
    define yagami = Character(_("Ms. Yagami"), kind=speaker, voice_tag='v_yagami')
    define yusuke = Character(_("Yusuke"), kind=speaker)
    define yusuke_tomoe = Character(_("Yusuke & Tomoe"), kind=speaker, voice_tag='v_tomoe')


    default Fnum = -1
    default F015 = -1
    default F016 = 0
    default F017 = 0
    default F018 = 0
    default F019 = 0
    default F01A = 0


    define blinds = ImageDissolve(im.Tile("blindstile.png"), 1.0, 8)
    define blinds_long = ImageDissolve(im.Tile("blindstile.png"), 5.0, 8)

    define diss_long = Dissolve (1.0)
    define dissolve = Dissolve (0.6)
    define diss_short = Dissolve (0.3)
    define diss_fast = Dissolve (0.1)
    define diss_flash = Dissolve (0.01)
    define diss_story = Dissolve (1.2)
    define char_dissolve = {'master': diss_short, 'screens': None}

    define TAPE = 0.3

label start:
    $ _skipping = True
    jump episode01

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
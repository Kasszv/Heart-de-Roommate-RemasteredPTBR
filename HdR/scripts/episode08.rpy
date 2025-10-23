label episode08:

    $ Fnum = 8
    $ save_name = "Episode 8: Crash of the Titans! Asumi vs. Namiki"

    $ bgm (12)
    $ bgfx ('bg03b')
    $ char ('tas001')

    voice as0224

    asumi "Vamos fazer uma festa de Okonomiyaki (panqueca japonesa)!"
    yusuke "Hã? Por quê?"
    "A caminho de volta."
    "Tomoe inclina a cabeça com a sugestão da Asumi."
    "Asumi sorri e faz cafuné na cabeça da Marutan enquanto Marutan acena com uma bandeira e concorda."

    $ char ('tas012')

    voice as0225
    asumi "A Sra. Yagami está do nosso lado. Não precisamos nos preocupar com o Yusuke agora!"

    $ char ('tto001')

    voice to0117
    tomoe "Não acho que devamos ser tão otimistas."

    $ char ('tas005')

    voice as0226
    asumi "Você é muito preocupada, Moe-Moe. Não se preocupe. Além disso, o Yusuke está pagando porque pediu desculpas por causar tanta confusão aos colegas."

    $ char ('tto016')

    voice to0118
    tomoe "Eu entendi. Então... eu me pergunto se devo aceitar..."

    $ char ('tma008')

    marumu "...Hum, hum, hum."
    yusuke "...Ohh."
    "Eu realmente não ligo para a Asumin, mas Moe-Moe e Marutan estão felizes."
    "Então é melhor eu ficar contente por enquanto, mesmo que vá gastar toda minha mesada nessa festa..."
    yusuke "Seja homem, aguente firme... snif!"

    $ char ()
    $ music_stop ()
    $ cg ('e3_0102')

    voice as0227
    asumi "OK! O prêmio Asumin de hoje vai para..."
    tomoe "......"
    marumu "......"
    yusuke "......"

    $ cg ('e3_0108')

    voice as0228
    asumi "...Asumin! Yeah!"

    $ empat ('j4')

    "Não consigo deixar de implicar com a vencedora meio estranha."
    yusuke "Por quê? Por quê é isso?"

    $ cg ('e3_0104')
    $ empat ()
    $ bgm (7)

    voice as0229
    asumi "Porque! Ninguém mais merece o prêmio hoje!"
    yusuke "Então ninguém deveria ganhar."

    voice as0230
    asumi "Mas isso seria muito chato! Por isso eu decidi: o prêmio vai para mim hoje. Eu sou a que mais trabalha no grupo, sabia!?"

    voice as0231
    asumi "Além disso, não seria tão estranho se eu ganhasse sempre!"
    yusuke "...Isso é tão errado."

    $ cg ('e3_0102')

    voice as0232
    asumi "Ah, nossa comida chegou! Pessoal, preparem a grelha."

    $ sfx ('SE14')

    "Ela não me escuta mais."

    "Chega o prato favorito dela, o 'Buta Tama (Porco & Ovo)'."
    "Ela instrui todo mundo e começa a cozinhar seu 'Buta Tama'."
    "Não posso deixar de ficar insatisfeito com a atitude dela."
    "...E assim, eu digo a ela."

    $ sfx ()
    $ music_stop ()

    yusuke "Você sempre toma todas as decisões egoisticamente. Não acho isso certo, Asumin."

    voice as0233
    asumi "E daí? Eu sou a líder aqui!"
    yusuke "É mesmo?"

    $ cg ('e3_0103')

    voice as0234
    asumi "Não entende? Quem pode ser líder deste grupo além de mim!?"
    yusuke "...Acho que alguém além de você pode fazer o trabalho."

    $ cg ('e3_0102')

    voice as0235
    asumi "O quê!?"

    $ bgfx ('black')
    call effect ('SE10', ETYPE1) from _call_effect_17

    "O resultado final foi o de sempre."
    "Mas alguns dias depois, minhas dúvidas ressurgem."
    "...de uma forma inesperada."


    call ep_start from _call_ep_start_6

    $ bgm (12)
    $ bgfx ('bg01a')
    $ char ('tna002')

    voice na0057
    namiki "Quanto tempo, pessoal! Como vão?"
    yusuke "Irmã? Namiki?"
    yusuke "O que você está fazendo aqui? Por que está usando nosso uniforme? Com certeza você não está pensando em..."
    "Ela me dá um grande sorriso."

    $ sfx ('SE32')
    $ char ('tna001')

    voice na0059
    namiki "Sim, acertou! Eu acabei de me transferir pra cá!"

    $ sfx ()
    $ char ('tas018')

    voice as0236
    asumi "Ainda não falamos nada!"
    "Totalmente ignorando Asumi, Namiki caminha em direção à Tomoe."

    $ char ('tto011')

    voice to0119
    tomoe "O...olá, Namiki."

    $ char ('tna020')

    voice na0060
    namiki "Senti sua falta, Moe-Moe! Vou ser sua vizinha a partir de agora."

    $ char ('tto001')

    voice to0120
    tomoe "Sério? ...SOCORRO!"

    $ char ('tto037')

    "Eu sabia que a Namiki iria pular nela."
    "Tomoe sai correndo gritando tentando escapar da Namiki."

    $ char ('tma016')

    "Marumu está se divertindo observando."

    $ char ('tas018')

    "Mas não importa como se olhe, Asumi parece bem infeliz."
    "Ela encara a inimiga que entrou em seu território sagrado."

    call blackout from _call_blackout_33
    $ bgfx ('bg01a')
    $ char ('tna001')

    yusuke "...Então, você vai morar ao lado do nosso quarto sozinha."

    voice na0061
    namiki "Sim, foi por coincidência. O quarto estava disponível sem colega!"
    yusuke "Hã, mas o alojamento masculino está cheio..."
    "Eu a invejo."
    "Asumi solta umas palavras duras para a Namiki,"

    $ char ('tas012')

    voice as0237
    asumi "Que pessoa sortuda você é! Por que você não volta para seu QUARTO PRIVADO então!? Hehe!"

    $ char ('tma016')

    voice ma0055
    marumu "...Asumin, você está agindo estranho."

    $ char ('tna001')

    voice na0062
    namiki "Ah, você fala dessas coisas friamente. Você tem rancor de mim por dizer que o Yusuke vestido de menino é mais fofo que você, né?"

    $ char ('tas010')

    voice as0238
    asumi "N...não! Claro que não! Não seja boba!"
    "Ela provavelmente acertou em cheio."
    "Namiki ignora Asumi, que parece pronta para surtir, e cochicha para Tomoe,"

    $ bgm (9)
    $ char ('tna023')

    voice na0063
    namiki "Sozinha em um quarto para três... Sozinha. Esse espaço aberto me deixa solitária, e isso é demais!"

    voice na0064
    namiki "Não acha que isso é triste, Moe-Moe? Não acha?"

    $ char ('tto007')

    voice to0121
    tomoe "Bem, eu acho que seria solitário..."

    $ char ('tna021')

    "Olhando para a Tomoe, que é boa demais, Namiki sorri maliciosamente."
    "Infelizmente, ela é capaz de qualquer coisa se isso significar se divertir."

    $ music_stop ()
    $ char ('tna002')
    $ empat ('j6')

    voice na0065
    namiki "Moe-Moe, por que você..."

    $ char ('tto007')

    voice to0122
    tomoe "Eu... eu não consigo fazer uma coisa dessas!"

    $ char ('tna001')

    voice na0066
    namiki "Ah, por favor, não diga isso! Hã? O que foi, Marutan?"

    $ char ('tma011')

    marumu "......"

    $ char ('tna001')

    voice na0067
    namiki "Você estaria disposta a me ajudar a acabar com esse sentimento de solidão? Agradeço a intenção, mas talvez na próxima vez. Desta vez, eu preciso da Moe-Moe!!!"

    $ empat ()
    $ char ()
    $ bgm (7)

    "O quarto se transforma em um estado caótico, cheio de pânico."
    "Fazem tanto barulho que eu não me surpreenderia se as garotas dos outros quartos, especialmente aquele trio que mora no quarto oposto ao da Namiki, reclamassem de nós."

    $ char ('tas006')

    "Em meio ao caos, Asumi recupera um pouco os sentidos."
    "Após inspirar fundo, ela grita tão alto que faz o quarto tremer."

    $ char ('tas007')

    voice as0239
    asumi "Silêncio! Pessoal, fiquem quietos! Não conseguem ouvir as ordens da sua líder!?"
    yusuke "O quê...?"
    "Ao ouvir Asumi, certa pessoa realmente se cala."
    "Nada menos que a pessoa que começou tudo: Namiki."

    $ music_stop ()
    $ char ('tna001')

    voice na0068
    namiki "Hum... eu tenho uma pergunta."

    $ char ('tas037')

    voice as0240
    asumi "O que foi, Namiki?"

    $ char ('tna001')

    voice na0069
    namiki "Quem é esse 'líder' de que você está falando?"

    $ char ('tas030')

    voice as0241
    asumi "Isso... seria eu, claro!"

    $ char ('tna019')

    voice na0070
    namiki "Você está brincando, né?"
    "Asumi e Namiki se encaram."

    $ bgm (16)

    "O quarto fica quieto, e à medida que a tensão aumenta, uma nova briga está prestes a começar."

    $ bgfx ('black')
    $ bgfx ('bg01a')
    $ char ('tna001')

    voice na0071
    namiki "Eis o que penso: um líder deve ser escolhido corretamente. Só porque ninguém mais quer fazer o trabalho, deixar uma pessoa egoísta e egocêntrica ser líder causa grandes problemas!"

    $ char ('tas036')

    voice as0242
    asumi "Quem foi que chamou alguém de egoísta e egocêntrico!?"
    "Novamente, Namiki ignora Asumi e continua falando com os outros."

    $ char ('tna001')

    voice na0072
    namiki "Um líder é um símbolo para a equipe. Deve ser escolhido adequadamente!"

    $ char ('tas006')

    voice as0243
    asumi "Isso não é necessário. Eu estou cumprindo perfeitamente o papel de líder deste grupo!"

    $ char ('tna007')

    voice na0073
    namiki "Perfeitamente? Perfeitamente... Eu realmente não acho."

    $ char ('tas007')

    voice as0244
    asumi "Como você pode dizer isso! Você acabou de se transferir pra cá! Minhas qualidades só são compreendidas por amigos que cresceram comigo!"

    $ char ('tna004')

    voice na0074
    namiki "Entendo. Se você se sente assim, vamos decidir usando um método apropriado."

    $ bgfx ('sora01')

    "O método sugerido por Namiki... embora antigo, é o mais democrático e ainda é amplamente usado hoje em dia."
    "Vamos decidir o líder com base no voto de todos."
    "Sem saber o que fazer, Tomoe parece apreensiva."
    "Marumu... não sei o que ela está pensando."
    "E eu... estou pensando nisso com bastante seriedade."

    menu:
        " "
        "Eu deveria votar na Asumi.":


            $ bgfx ('bg01a')

            yusuke "Hum. Devo agradecer à Asumi por me permitir morar aqui... De qualquer forma..."

            $ char ('tna022')

            namiki "......"
            yusuke "N... Namiki."
            "Ela me encara sem dizer uma palavra, o que é muito assustador."
            "Claramente, ela está me ameaçando com aquele olhar."
            "Assim que me ouve, ela coloca um sorriso gentil no rosto. Apesar de gentil, o sorriso é aterrorizante."

            $ char ('tna020')

            voice na0077
            namiki "Agora que me transferi pra cá, sou aluna desta escola. Posso ir ao escritório dos professores a qualquer momento, então..."
            yusuke "...E?"

            voice na0078
            namiki "Posso dizer a eles que há uma garota estranha morando no alojamento feminino."
            yusuke "Sua... ardilosa...!"
            "...E assim, cedi às ameaças da Namiki."
            "Eu não tenho escolha... *snif*."

            $ F016 += 1
        "Tenho que votar na Namiki.":


            $ bgfx ('bg01a')

            yusuke "É melhor eu votar na Namiki."

            $ char ('tna020')

            voice na0075
            namiki "Uau! Que ótima ideia, Yusuke!"
            yusuke "Namiki..."
            "Ela coloca um grande sorriso no rosto enquanto faz carinho na minha cabeça."
            "No entanto, vejo em seus olhos... Eles me dizem que se eu não votar nela, estarei encrencado."
            "...E assim, escrevo o nome dela como o de mais uma líder perigosa."

            $ F019 += 1
        "Tomoe poderia ser uma boa líder!":


            $ bgfx ('bg01a')

            yusuke "Hum. Devo agradecer à Asumi por me permitir morar aqui... mas tenho medo da Namiki se eu não votar nela."
            yusuke "Para ficar seguro, por que não voto na Tomoe?"

            $ char ('tna020')

            voice na0075
            namiki "Uau! Que ótima ideia, Yusuke."
            yusuke "Namiki..."

            voice na0076
            namiki "Eu gosto muito da Moe-Moe, MAS neste caso, acho que você deveria votar em mim, ok!?"
            yusuke "Por quê?"

            voice na0077
            namiki "Agora que me transferi pra cá, sou aluna desta escola. Posso ir ao escritório dos professores a qualquer momento, então..."
            yusuke "...E?"

            voice na0078
            namiki "Posso dizer a eles que há uma garota estranha morando no alojamento feminino."
            yusuke "Você... ardilosa...!"
            "...E assim, cedi às ameaças da Namiki."

    $ char ('tna001')

    voice na0079
    namiki "OK, dois votos pra mim, e a líder da era anterior, que luta em vão, tem um voto... DOIS?"
    yusuke "......(Será que foi a Tomoe?)"
    "Namiki de repente se atira em Tomoe, que estava prestes a fugir, e diz,"

    $ char ('tna002')

    voice na0080
    namiki "Ah, pobre Moe-Moe! Aquela mulher má tem algo contra você e te ameaçou para ver as coisas do jeito dela, não é?"

    $ char ('tto007')

    voice to0123
    tomoe "N... não é isso..."
    yusuke "Você é quem está fazendo isso, Namiki... ARGH!"

    $ char ('tna022')
    call effect ('SE43', ETYPE2) from _call_effect_18

    "Namiki desfere um soco com o dorso da mão, e eu caio no chão."
    "Quem fala a verdade sempre corre risco de vida."

    $ char ('tna001')

    voice na0081
    namiki "Se ela está te ameaçando, é só dizer. Eu anularei o voto!"

    $ char ('tto004')

    voice to0124
    tomoe "Na... na verdade, eu não me importo se você se tornar a líder, Namiki, mas mesmo com a Asumi..."

    $ empat ('j6')
    $ char ('tna020')

    voice na0082
    namiki "Ah, Moe-Moe, diga meu nome de novo!"

    $ char ('tto001')

    voice to0125
    tomoe "Hã?"

    $ char ('tna020')

    voice na0083
    namiki "A maneira como você diz meu nome, 'Namiki', tem um som tão agradável."
    "O assunto foi mudado..."

    $ empat ()
    $ bgfx ('black')
    $ bgfx ('bg01a')
    $ char ('tas024')

    voice as0245
    asumi "2-2 agora. Temos mais um voto."
    "Há mais um voto na 'urna provisória', feita de uma caixa de cereais."
    "Asumi lentamente põe a mão na caixa."
    "Ela pega o papel e abre lentamente..."

    voice as0246
    asumi "...'Marutan?'"
    yusuke "Marutan... MARUTAN?"

    $ char ('tma011')

    voice ma0065a
    marumu "......(assente)"
    "Sinto a bandeira que ela segura e seu enfeite de cabelo nos dizendo,"
    "'O líder deste quarto sou eu! Marutan!'"

    $ bgfx ('sora01')

    "A eleição chegou ao fim."
    "O resultado é..."
    "Asumin... Dois votos (com a consideração da Moe-Moe)."
    "Namiki... Dois votos (por me ameaçar)."
    "Marutan... Um voto."
    "O problema não pode ser resolvido assim."
    "Estamos numa situação... Tomoe então, surpreendentemente, nos diz enquanto guarda a caixa,"

    $ bgfx ('bg01a')
    $ char ('tto001')

    voice to0126
    tomoe "Ah, há mais um pedaço de papel na caixa..."

    $ chars ('tas030', 'tna019')

    voice as0247
    asumi_namiki "Huhhh!?"
    "As duas candidatas correm até Tomoe."
    "Tomoe deixa cair a última cédula."
    "Namiki rapidamente a pega e fica em silêncio."

    $ char ('tas006')

    voice as0248
    asumi "O... o quê? Meu nome está no papel, certo!? Me mostra!!!"
    "Asumi pega o papel da Namiki e olha, e então... ela fica tão sem palavras quanto Namiki."

    $ char ('tas024')

    "Há a pegada de um gato no papel."

    $ bgm (6)

    "Tomoe acaricia a cabeça do Toshibo e diz,"

    $ char ('tto016')

    voice to0127
    tomoe "Entendi. Você também queria votar, Toshibo?"

    $ char ('tts002')

    voice ts0020
    toshibo "Miau!"

    voice na0085
    namiki "O gato... votou..."
    "Com apenas uma pegada, não há como saber para quem o Toshibo votou."

    $ bgfx ('sora01')

    "<Resultado da Eleição>"
    "Asumin... Dois votos (com a consideração da Moe-Moe)."
    "Namiki... Dois votos (por me ameaçar)."
    "Marutan... Um voto."
    "Um voto anulado... Um voto."
    "É assim que a eleição termina em falha."
    "Acho que minha vida cheia de acontecimentos continuará..."


    call ep_middle from _call_ep_middle_6

    $ bgm (5)
    $ bgfx ('bg01a')
    $ char ('tna001')

    voice na0086
    namiki "Competição! Sendo assim, vamos fazer uma competição!"

    $ char ('tas006')

    voice as0249
    asumi "Claro! Vamos decidir quem é mais adequado para ser um verdadeiro líder de uma vez por todas!"

    $ char ('tma011')

    voice ma0056
    marumu "...Sim."
    "Marumu levanta a mão torcendo por elas, mas todos a ignoram."
    "Acho que seria divertido se a Marutan se tornasse líder."

    $ bgfx ('black')
    $ music_stop ()

    "Enfim, é assim que Asumi vs. Namiki começa."

    $ bgm (12)
    $ bgfx ('bg01a')

    yusuke "*bocejo* Bom dia... Hã?"

    $ char ('tna102')

    voice na0087
    namiki "Você é uma moleca sonolenta, Yusuke."
    yusuke "Namiki, o que você está fazendo aqui?"

    voice na0088
    namiki "Vim fazer café da manhã para vocês. Um líder deve saber cozinhar."
    yusuke "S... sério? A propósito..."
    "Ela não se importa com a forma como está vestida."
    "Nunca ligou para o que veste na minha frente."
    "Antes de eu mudar de escola, ela dizia 'agora sou uma dama, devo cuidar da minha aparência', mas agora está pior."

    $ char ('tna122')

    voice na0089
    namiki "Do que você está me encarando, Yusuke?"
    yusuke "Eu... ah..."

    $ char ('tna118')

    voice na0090
    namiki "Você não acha que um líder deveria ser sexy como eu, Yusuke?"
    "Ela aperta os seios contra minhas costas."
    "Asumi diz,"

    $ char ('tas110')

    voice as0250
    asumi "O que vocês estão fazendo? Vocês são uns pervertidos!"

    $ sfx ('SE43')

    "Ela então me derruba."
    yusuke "P...por que isso acontece comigo... Argh!"

    $ sfx ()
    $ bgfx ('black')
    $ cg ('e3_0202')
    $ bgm (5)

    voice na0091
    namiki "O que acha, Marutan?"

    $ cg ('e3_0208')

    marumu "......"

    voice as0251
    asumi "Hum... Relutantemente, eu admito, isso não é ruim."
    "Até Asumi admite."
    "Namiki cozinha bem, embora seja desorganizada."
    "Ela é tão boa que muitos restaurantes quiseram contratá-la desde a escola."

    $ bgfx ('bg01a')
    $ char ('tna102')

    voice na0092
    namiki "Ah, onde está a Moe-Moe?"

    voice as0252
    asumi "Namiki, você não pode chamar ela de Moe-Moe!"
    yusuke "Tomoe nunca é uma pessoa matinal. Acho que ela ainda está dormindo."

    $ char ('tna118')

    voice na0093
    namiki "Sério? Vou acordá-la então. Esse também é trabalho de um líder. TOMOEEE!"

    $ char ()

    yusuke "Tenho um mau pressentimento sobre isso."

    $ bgfx ('black')

    "Eu estava certo."

    $ vox ('to0128')

    "Não sei como Namiki acordou Tomoe, mas assim que ela vai ao quarto da Tomoe, ouvimos gritos."

    $ vox (delay=0.3)
    $ bgm (12)
    $ bgfx ('sora01')

    yusuke "Heh, já estou cansado."

    voice to0129
    tomoe "Sim. Seria bom se Namiki e Asumi fossem mais amigas."
    "Tomoe e eu murmuramos enquanto olhamos para o céu azul."
    "Marumu observa suas colegas correndo os 50 metros. Não sei por que ela se interessa tanto."
    yusuke "Hm?"
    "Vejo alguém acenando para nós do prédio da escola."
    "Do segundo andar, ao lado da nossa sala."
    yusuke "Namiki... que vergonha."

    voice to0130
    tomoe "Mas eu acho que ela é engraçada de um jeito bom... Oh?"
    "Tomoe inclina a cabeça e me pergunta,"

    voice to0132
    tomoe "Ela está no mesmo ano que nós?"
    yusuke "Sim, está."
    "Entendi o que ela queria dizer."
    "Nesta escola, alunos do mesmo ano ficam nas salas do mesmo andar."
    "Namiki está acenando para nós da sala ao lado, no mesmo andar."
    "Em conclusão, Namiki (minha 'irmã mais velha') e eu estamos no mesmo ano."
    "Tomoe continua inclinando a cabeça, cheia de curiosidade."

    voice to0133
    tomoe "Por que uma 'irmã mais velha' está no mesmo ano que nós?"
    yusuke "B... bom, é realmente complicado... Ah!"
    "Não falei muito alto porque estou tentando mudar de assunto."
    "É porque Namiki, que estava acenando, desapareceu de vista."
    yusuke "Tenho um pressentimento muito ruim..."
    "Asumi está toda animada para a corrida."
    "Isso é algum tipo de ação de relações públicas para a competição de liderança?"
    "Ela acena para nós e se prepara para correr."
    teacher "Preparar... VÃO!"
    "Isso faz parte da educação física, então não há pistola de largada."
    "No entanto, Asumi parece estar em uma competição atlética séria."
    "Então... vemos alguém aparecer ao lado dela como o vento."

    $ bgm (7)
    $ say_hide ()
    call cgeffect (sound_source='SE13', sound_loop=True, graphics=['sde_0501', 'sde_0502'], fx=diss_long) from _call_cgeffect_1

    voice na0095
    namiki "Um líder também deve correr rápido, certo?"

    voice as0253
    asumi "V... você! Eu não vou perder para você!!!"
    yusuke "Namiki? Você fugiu da aula!?"
    "Elas sumiram num piscar de olhos, deixando uma nuvem de poeira. Tomoe, nossos colegas e eu só podemos ficar em silêncio e assistir à batalha."
    "Marutan se diverte observando."

    $ bgfx ('black')
    $ bgfx ('sora01')
    $ sfx ('SE51')

    "12:23."
    "Intervalo para o almoço na cafeteria."

    $ sfx ()
    $ say_hide ()
    call cgeffect (sound_source=None, graphics=['sde_0601', 'sde_0602']*4, fx=dissolve) from _call_cgeffect_2

    voice na0096
    namiki "Manter bastante pão para os subordinados é uma responsabilidade importante de um líder!"

    call cgeffect (sound_source=None, graphics=['sde_0601', 'sde_0602']*4, fx=dissolve) from _call_cgeffect_3

    voice as0254
    asumi "Eu não vou perder! Vou fazer qualquer tipo de tarefa... Vou fazer! H...ei! Não empurrem!"

    $ bgfx ('black')
    $ bgfx ('sora01')
    $ sfx ('SE51')

    "13:38."
    "Depois do almoço, estamos todos sonolentos. Minha turma e a turma da Namiki foram reunidas."

    $ sfx ()
    $ cg ('sde_02')
    $ unlock_gallery ('g5e9')

    voice na0097
    namiki "Um líder pode dormir a qualquer hora, em qualquer circunstância... ZZZ..."

    voice as0255
    asumi "Sou mestre em tirar cochilos... ZZ... ZZZ..."

    voice yo0092
    yagami "Quando dormem tão abertamente, não consigo deixar de ficar enojada com eles."

    $ bgfx ('black')
    $ bgfx ('sora01')
    $ sfx ('SE51')

    "15:15."
    "Depois da escola, no portão principal."

    $ sfx ()
    call cgeffect (sound_source=None, graphics=['sde_0503', 'sde_0504'], fx=diss_long) from _call_cgeffect_4

    voice na0098
    namiki "Não se torna líder apenas correndo rápido. Também precisa ser bom em provas de resistência!"

    voice as0256
    asumi "Claro. Por que não corremos até o alojamento feminino?"

    $ bgfx ('black')
    $ sfx ('SE13', loop=True)

    "E então o resto de nós volta caminhando para o dormitório..."
    "...enquanto os vemos partir."
    "Finalmente, o dia barulhento e pesado termina."

    $ sfx (delay=0.5)
    $ bgm (3)
    $ bgfx ('bg01c')
    $ char ('tna120')

    voice na0099
    namiki "Hmm... A comida da Moe-Moe é a melhor! Quero comer todos os dias."

    $ char ('tto234')

    voice to0134
    tomoe "M... muito obrigada."

    $ char ('tas106')

    voice as0257
    asumi "Por que você não volta para o seu quarto! Você não é nossa colega de quarto!"

    $ char ('tna118')

    voice na0100
    namiki "Ah, como você é cabeça fechada. Acho que você não nasceu para ser líder."

    $ char ('tas110')

    voice as0258
    asumi "Grr... Essa vadia me irrita!!"
    "Acho que o dia barulhento continua."

    $ bgfx ('black')
    $ bgm (16)
    $ bgfx ('bg01c')
    $ char ('tna104')

    voice na0101
    namiki "Hm, acho que a pontuação de hoje é 80-30."

    $ char ('tas136')

    voice as0259
    asumi "Que pontuação é essa?"

    $ char ('tna102')

    voice na0102
    namiki "Nossos pontos de batalha."
    "Ok..."
    "Asumi não concorda nem um pouco com esses resultados."

    $ char ('tas106')

    voice as0260
    asumi "Como diabos você tirou esses números? Explique direito."

    $ char ('tna102')

    voice na0103
    namiki "He he he. OK, por que você não vem aqui?"
    "Elas começam a brigar por 'a pontuação de hoje'."
    "Parece que esse dia barulhento nunca vai acabar."

    $ char ('tto207')

    voice to0135
    yusuke_tomoe "Ahh..."
    "Tomoe e eu nos olhamos e suspiramos."
    "Marutan escapa do quarto sem que percebamos."

    $ bgfx ('sora08')

    "Incapaz de dormir, estou pensando nas batalhas de hoje."
    "Todas as batalhas que aconteceram hoje... foram realmente necessárias para alguém se tornar líder?"

    call blackout from _call_blackout_34

    "Nos dias seguintes, as incompreensíveis batalhas continuaram."
    "Uma 'competição de acordar cedo', 'competição de beber missô quente' e uma 'competição de karaokê.'"
    "Não sei o que aconteceu com seus resultados."
    "Bem, acho que ninguém mais saberá também."
    "Do meu ponto de vista, acho que Namiki é superior à Asumi. Talvez eu pense assim porque estou sob seu encanto."

    $ bgfx ('sora01')

    "Numa manhã calma e ensolarada..."
    "...Namiki finalmente decide apostar alto."

    $ bgfx ('bg01a')
    $ char ('tna202')

    voice na0104
    namiki "Estou de volta!"

    $ char ('tas107')

    voice as0261
    asumi "EU ESTOU TE DIZENDO! ESTE NÃO É O SEU QUARTO!"

    $ char ('tna202')

    voice na0105
    namiki "Não seja tão cruel! Vim aqui para falar com a Moe-Moe e a Marutan."
    yusuke "......"
    "Nem uma nem outra estão aqui agora."
    "Moe-Moe foi para casa."
    "E Marutan saiu."
    "Elas disseram que voltariam antes do anoitecer."
    "Asumi, desgostosa, diz a Namiki,"

    $ char ('tas143')

    voice as0262
    asumi "Vou dizer a elas para irem ao seu quarto quando voltarem, tudo bem!?"

    $ char ('tna202')

    voice na0106
    namiki "Ok, muito obrigado!"

    $ char ()

    "Namiki sai feliz."
    "Assim que ela vai embora, Asumi fica com uma expressão triste."

    $ bgm (8)

    yusuke "Uh... Asumin."

    $ char ('tas124')

    voice as0263
    asumi "O que?"
    yusuke "Está tudo bem? Deixá-las ir, quero dizer. Não sei o que a Namiki vai dizer a elas."

    voice as0264
    asumi "Está tudo bem. Eu quero lutar contra ela de forma justa."
    yusuke "Asumi..."
    "Pela primeira vez, ela respondeu seriamente."
    "Há algo um pouco diferente nela... Ela não é ela mesma."

    voice as0265
    asumi "Eu só quero que elas sejam honestas. Não quero que tentem ser algo que não são."

    voice as0266
    asumi "É por isso que eu quero que elas decidam por si mesmas, o que acham certo."
    "Ela baixa a cabeça e continua,"

    $ char ('tas143')

    voice as0267
    asumi "Eu acho sua 'irmã' realmente incrível. De muitas maneiras, ela está sempre fazendo pelo menos 20%% melhor que eu."
    yusuke "Eu... entendi... (Isso é realmente algo tão incrível?)"
    "É incomum que Asumi admita e reconheça as habilidades de alguém assim."
    "Como ela está se sentindo pra baixo agora, quero dizer algo a ela."
    "Pode ser qualquer coisa, mas não consigo pensar em nada para animá-la."
    yusuke "Uh... uh, Asumi."

    voice as0268
    asumi "...Mas."
    yusuke "Mas?"

    $ char ('tas106')

    voice as0269
    asumi "Mas eu não vou perder! Eu sei que vou ganhar no final!"
    "Ela de repente se levanta como uma fênix. Ela está pronta para a próxima batalha."
    "Sim, essa é certamente a Asumi que eu conheço."
    "Ela pode ficar deprimida de vez em quando, mas Asumi tem seu jeito de lutar para terminar do seu jeito."
    "Sinto-me de alguma forma mais próximo dela do que antes."

    $ music_stop ()

    menu:
        " "
        "Falar com Namiki.":


            $ bgfx ('black')

            yusuke "OK!"
            "Eu visito o quarto da Namiki com determinação."
            "Há momentos em que até eu preciso me afirmar."

            $ bgm (12)
            $ bgfx ('bg09a')
            $ char ('tna202')

            voice na0107
            namiki "Oi, Yusuke. O que você quer?"
            yusuke "S... sim. Eu tenho algo para te dizer."
            "Quando fico cara a cara com ela, fico com medo."
            "Eu tenho que dizer a ela antes que toda a minha coragem acabe... Sem perder um momento, digo o que preciso dizer."
            yusuke "Eu não sei se vou votar em você na próxima eleição. Eu quero ser honesto comigo mesmo."

            $ char ('tna216')

            namiki "......"
            "(Estou com medo.)"
            "Quando ela grita, ri ou desferi um ataque direto, ela não é tão assustadora quanto agora."
            "Por outro lado, já estou acostumado a isso."
            "Mas não sei o que fazer quando ela fica em silêncio assim como agora."
            "Sinto como se estivesse em cima de um leito de espinhos."
            yusuke "...Ohh, o que eu faço?"

            voice na0108
            namiki "...Hã?"

            $ sfx ('SE44')

            "Novas visitantes chegam na atmosfera desconfortável."
            "(Elas estão na mesma situação que eu.)"

            $ sfx ()
            $ char ('tna202')

            voice na0109
            namiki "Bem-vindas ao meu quarto, Moe-Moe, Marutan!"

            $ char ('tma207')

            marumu "......"

            $ char ('tto201')

            voice to0136
            tomoe "Boa noite, Namiki."

            $ empat ('j6')
            $ char ('tna202')

            voice na0110
            namiki "Oh, a maneira como você diz meu nome tem um som maravilhoso!"
            "Namiki sorri ao ouvir Tomoe dizer seu nome."
            "Preocupado com o que Namiki vai fazer, decido observá-las em silêncio do canto da sala."

            $ empat ()
            $ F016 += 1
        "Pensar um pouco mais.":


            $ bgfx ('black')

            yusuke "Hmm..."
            "Eu tomo minha decisão."
            "...Quem eu vou votar na próxima eleição para líder."
            "Mas estou angustiado em contar isso à Namiki."
            "Já se passaram 15 minutos desde que comecei a me sentir angustiado."
            "Afinal, algo assustador é assustador."
            "Eu tenho um grande medo dela. Ela plantou isso na minha mente quando eu era apenas uma criança."

            $ bgfx ('bg01a')
            $ char ('tto202')

            voice to0279
            tomoe "Olá..."

            $ char ('tma222')

            marumu "......"
            "As duas finalmente voltaram."
            "A voz dela está mais baixa que o normal, obviamente angustiada com algo."
            "Asumi dá a elas a mensagem da Namiki."
            "Elas se olham por um segundo e saem do quarto. Eu as sigo."

            $ bgfx ('black')
            $ bgm (12)
            $ bgfx ('bg09a')
            $ char ('tna202')

            voice na0109
            namiki "Bem-vindas ao meu quarto, Moe-Moe, Marutan!"

            $ char ('tma207')

            marumu "......"

            $ char ('tto201')

            voice to0136
            tomoe "Boa noite, Namiki."

            $ char ('tna202')

            voice na0110
            namiki "Oh, a maneira como você diz meu nome tem um som maravilhoso!"
            "Namiki sorri ao ouvir Tomoe dizer seu nome."
            "Decido observá-las em silêncio do canto da sala."

            $ F019 += 1

    voice na0111
    namiki "Ohh! Quando eu me tornar a líder, Moe-Moe vai dizer meu nome todos os dias. Minha vida será tão maravilhosa."

    $ char ('tto201')

    voice to0137
    tomoe "Hum... Você disse que queria falar conosco?"

    $ char ('tna219')

    voice na0112
    namiki "Ops! Eu escorreguei de novo para o meu mundinho dos sonhos."

    $ char ()

    "Ela pede para elas esperarem e começa a procurar alguns itens em uma bolsa."
    "Assim que ela os encontra, ela os dá às meninas."

    $ char ('tto201')

    voice to0138
    tomoe "Hum... o que são esses?"

    $ char ('tna202')

    voice na0113
    namiki "São presentes meus para vocês! Vocês são tão fofas, precisam viver um pouco!"
    yusuke "Entendi, ela foi à cidade comprar essas coisas hoje."
    "Ela me ameaça, mas dá a elas presentes (subornos)."
    "Quando ela realmente quer algo, ela se torna uma racionalista completa."

    $ char ('tto202')

    tomoe "......"

    $ char ('tma201')

    marumu "......"

    $ music_stop ()
    $ char ('tna216')

    voice na0114
    namiki "Oh, vocês não gostaram deles?"
    "Elas estão apenas olhando para 'os presentes'."
    "Uma faixa de cabelo grande em uma mão, e um broche de cabelo bonito na outra."
    "Parecem coisas que ficariam boas nelas."

    voice na0115
    namiki "Achei que os que vocês têm pareciam um pouco sem graça, então comprei esses."

    $ char ('tto201')

    voice to0139
    tomoe "Hum... Namiki."
    "Depois de parecer estar pensando em algo, Tomoe fala."
    "Mas..."

    $ empat ('j6')
    $ char ('tna202')

    voice na0116
    namiki "Oh... Moe-Moe, seu jeito de dizer meu nome soa maravilhoso, não importa quantas vezes eu ouça."

    $ char ('tto213')

    voice to0140
    tomoe "Escute-me, Namiki!"

    $ empat ()
    $ empat ('SE49')
    $ char ('tna210')

    voice na0117
    namiki "Oh... desculpe, Moe-Moe."
    "O tom de Tomoe fica tão duro que até assusta a Namiki."
    "Surpresa consigo mesma, Tomoe continua falando,"

    $ empat ()
    $ char ('tto202')

    voice to0141
    tomoe "Agradeço a intenção, mas não posso aceitar isso."

    $ char ('tna219')

    voice na0118
    namiki "Por quê?"
    "Namiki olha para Tomoe com surpresa."
    "Tomoe a informa claramente,"

    $ music_stop ()
    $ char ('tto213')

    voice to0142
    tomoe "Eu amo o cachecol que estou usando agora. Também acho que a Marumu gosta de seus próprios acessórios."

    $ char ('tma201')

    voice ma0065a
    marumu "......(assente)"
    "Marumu acena com a cabeça."
    "Tomoe se inclina."

    $ char ('tto204')

    voice to0143
    tomoe "Sinto muito, Namiki."

    $ char ('tma201')

    voice ma0056a
    marumu "......(se inclina)"
    "Depois de levantar a cabeça, Tomoe diz a ela,"

    $ char ('tto202')

    voice to0144
    tomoe "Namiki, também temos algo para te dizer."

    $ char ('tna216')

    voice na0119
    namiki "O que é?"
    "Ela não está animada ao ouvir o nome de Tomoe desta vez."
    "Ela espera pelas próximas palavras de Tomoe."

    $ char ('tto213')

    "Ela não pode estar animada, tendo que olhar para a expressão séria de Tomoe."
    "Assim como eu, Tomoe não parece confortável nesse tipo de atmosfera."
    "Mas ela se esforça e diz,"

    voice to0145
    tomoe "Eu acho que nossa líder é a Asumi."

    $ char ('tma210')

    voice ma0057
    marumu "Estou desistindo da posição de líder."

    $ chars ('tto222', 'tna219')

    voice to0146
    everyone "Huh?"
    "Tomoe começa a chorar. Ela precisou de muita coragem para dizer isso a Namiki, mas..."
    "Marumu perdeu a noção."
    "No entanto, o que ela diz a seguir prova que ela não perdeu."

    $ char ('tma201')

    voice ma0058
    marumu "...A Asumin deveria ser nossa líder."

    $ char ('tto213')

    voice to0147
    tomoe "Eu... eu também acho. Desculpe, Namiki."

    $ char ()

    "Assim que Tomoe diz isso, ela desaba cansada no chão."
    "Ela usou toda a sua energia só para dizer isso."

    $ char ('tna210')

    voice na0121
    namiki "Ah... tudo bem."
    "Namiki responde em uma voz baixa."
    "Mas ela parece satisfeita com isso, de qualquer forma."

    $ bgfx ('black')
    $ bgfx ('bg03b')
    $ char ('tna001')
    $ bgm (12)

    voice na0122
    namiki "Ei, Asumin!"

    $ char ('tas018')

    voice as0270
    asumi "O que?"
    "Depois da escola, a caminho do dormitório."
    "Namiki corre até nós."
    "Ela sorri e diz a Asumi,"

    $ char ('tna002')

    voice na0123
    namiki "Eu desisto."

    $ char ('tas030')

    voice as0271
    asumi "Hã?"
    "Asumi nunca imaginou que Namiki diria isso."
    "Ela abre a boca e congela de surpresa."

    $ char ('tna004')

    voice na0124
    namiki "Na verdade, eu não queria me tornar a líder. Isso dá muito trabalho."

    $ char ('tas043')

    voice as0272
    asumi "Então, por que...?"
    "Namiki sorri maliciosamente."

    $ bgm (10)
    $ char ('tna004')

    voice na0125
    namiki "Eu só queria testar você para descobrir se você era boa o suficiente para ser a líder do meu Yusuke e da Moe-Moe."

    $ char ('tas010')

    voice as0273
    asumi "O que!?"

    $ char ('tna001')

    voice na0126
    namiki "Você ainda não é perfeita, mas acho que você tem o que é necessário para ser uma boa líder. Eu admito isso."
    "Asumi fica irritada com a desistência repentina de Namiki na competição pela liderança."
    "Mas os outros, incluindo eu, olham uns para os outros e riem."
    "Namiki pode ser legal."
    "Mas o que ela diz a seguir me faz arrepender de ter pensado que ela era legal."

    $ bgm (7)

    voice na0127
    namiki "Eu vou te treinar como sua mestre, Asumin!"

    $ char ('tas010')

    voice as0274
    asumi "O que...! Você não pode ser minha mestre!"

    $ char ('tma017')

    voice ma0065a
    marumu "......(assente)"
    "Marumu acena com a cabeça e nos diz,"

    $ char ('tma008')

    voice ma0059
    marumu "Eu já sou a mestre."

    $ char ('tto001')

    voice to0148
    tomoe "Oh... realmente."

    $ chars ('tas006', 'tna019')

    voice as0275
    asumi_namiki "Não concorde, Moe-Moe!"

    $ bgfx ('sora05')

    "A 'declaração de mestre' da Marutan passou despercebida. A discussão entre Asumi e Namiki continua até chegarmos ao dormitório."

    call blackout from _call_blackout_35

    "...No dia seguinte."

    $ sfx ('SE53')

    "Alguém bate violentamente na porta, então eu rapidamente me escondo no armário."

    $ sfx ()

    "Eu fiz a escolha certa."
    "A porta destrancada se abre imediatamente após a batida."

    $ bgm (6)
    $ bgfx ('bg01a')
    $ char ('tyu003')

    voice yu0007
    akane "Ufa, ufa... ufa."

    voice as0276
    asumi "Ei!? Não entre no nosso quarto assim!"

    voice ma0060
    marumu "...Você veio nos desafiar?"

    $ char ('tyu002')

    voice yu0008
    akane "NÃO! Eu vim aqui para reclamar!"

    $ char ('ths002')

    "O rosto da Miss Hisame está totalmente vermelho."

    voice hs0007
    kaoru "A Namiki é sua amiga? Você precisa fazer algo sobre ela!"

    voice as0277
    asumi "Nós a conhecemos... mas o que há de errado?"

    $ char ('tyu002')

    voice yu0009
    akane "Ela entrou inesperadamente no nosso quarto e disse que ia ser nossa líder!"

    $ char ('tfu002')

    voice fu0007
    midori "Ela pegou nossas coisas sem permissão, depois nos fez cozinhar e limpar o quarto! Não aguentamos mais!"
    "As três estão tão bravas, mas minhas colegas de quarto olham umas para as outras e riem."
    yusuke "Não importa onde... Namiki quer ser vista como uma líder."


    call ep_finish from _call_ep_finish_5

    $ renpy.end_replay()
    $ unlock_gallery ('g3e4')
    $ unlock_episode (8)
    jump episode09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

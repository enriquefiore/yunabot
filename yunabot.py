#region [GLOBAL IMPORTS]
import datetime, random, re, time, urllib, json, requests
from bs4 import BeautifulSoup
#endregion [GLOBAL IMPORTS]
#region [GLOBAL CONFIGS]
""" Info from your app created at Telegram API (https://my.telegram.org/apps) """
api_id = 999999
api_hash = '999999'
""" Info from yout bot created with "The Botfather" """
yuna_token = 'XXXXXX:999999'
yuna_name = 'xYunaBot'
""" Info from your Telegram group, obtained inviting the "@RawDataBot" to it """
group_id = -9999999

#endregion [GLOBAL CONFIGS]
#region [GLOBAL VARIABLES]
msg_bitoca = ['Pelo barulho da fofoca, variable!','Pelo estouro da pipoca, variable!','Pelo ronco da motoca, variable!','Pelo colar que te sufoca, variable!','Pela galinha meio choca, variable!','Pela furadeira sem broca, variable!','Pelo cavalo que ainda trota, variable!','Se o bumerangue vai e volta, variable!','Se a vovozinha ainda tricota, variable!']
msg_lixo = ['Se eu ganhasse R$1 a cada vez que leio isso, minha fortuna seria maior que as tetas do variable!', 'Bom mesmo só se fosse IMAX invertido das galáxias perdidas, né variable?','Quem entende disso é o bootinsept0r. Chama-lo-ei!' ]
msg_yuna = ['Esse é meu nome!','Say my name!','WAT!','WAAAAAALLAAAAAAAAAAHHHHHHHH!','Yuna never sleeps!','Presumo que esteja aguardando uma grosseria.', 'Quequié!']
msg_random = ['variable, quequié que cê tá falando de bot, hein!', 'Deixa os bots em paz, variable! A gente só quer trabalhar.', 'Oi, variable! Falou de bot, falou comigo.']
msg_correio = ['Destinatário ausente!','Corre capivara: O destinatário chegou!','variable, sua encomenda está no Triângulo das Curitibas. http://www.presosemcuritiba.com.br/', 'Fiquei perdido no fluxo postal, variable!']
msg_lula = ['#lulalivre #lulanapapuda', '#moronacadeia', '"O Lula tá preso babaca!"', 'variable, já perguntou pra Marisa?']
msg_dilma = ['#dilmaputa','#dilmacuzona','Todo mundo sabe que a Mamadil é a mamãe do Vividilmícius!','"Se hoje é o Dia das Crianças, ontem eu disse que criança... o dia da criança é dia da mãe, do pai e das professoras, mas também é o dia dos animais. Sempre que você olha uma criança, há sempre uma figura oculta, que é um cachorro atrás, o que é algo muito importante!"','']
msg_temer = ['#foratemi','#foratemer','" Muitos votaram porque eu era candidato a vice."']
msg_bolsa = ['#bolsadicoco','variable, tá falando do bolsa ou do bolsinha?', 'Se estiver no mytoitter, eu acredito!', 'variable, "quem é Andréia Sadi?"!', 'variable, sem viés ideológico #taoquei', '#dendalei', 'variable, não fale assim do myto e/ou do mytinho!', '#taoquei', 'Taoquei?']
#endregion [GLOBAL VARIABLES]
#region [GLOBAL METHODS]
def time_comparision():
    time = datetime.datetime.now()
    if time.hour < 12: return 'Bom dia'
    elif time.hour > 18: return 'Boa noite'
    else: return 'Boa tarde'
#endregion [GLOBAL METHODS]

#region [TelegramClient Imports]pip
from telethon import TelegramClient, events, sync
#endregion [TelegramClient Imports]
#region [TelegramClient Variables]
client = TelegramClient(yuna_name, api_id, api_hash)
client.start(bot_token=yuna_token)
MY_CHAT = client.get_entity(group_id)
#endregion [TelegramClient Variables]
#region [TelegramClient Methods]

""" [INCOMING] Responds/Replies messages directly sent to your bot """
@client.on(events.NewMessage(incoming=True))
async def message_handler(event):
    message = event.message
    user_name = 'Usuário não registrado'
    if message.sender: user_name = message.sender.first_name
    #respostas no privado
    if event.is_private: 
        if re.search('(?i)yuna', event.raw_text): await event.reply('Sou eu!')
        else: await event.respond(f'Oi {user_name}. Sou um bot que não gosta de conversa privada.')
    #respostas no publico
    else: 
        if re.match('(?i)/status|/cotacao', event.raw_text):
            if re.search('(?i)status', event.raw_text):
                link = 'https://downdetector.com/status'
                if re.search('(?i)psn|playstation', event.raw_text): link += '/playstation-network'
                elif re.search('(?i)xbox|xbl|live', event.raw_text): link += '/xbox-live'
                elif re.search('(?i)switch', event.raw_text): link += '/nintendo-switch-online'
                elif re.search('(?i)nintendo', event.raw_text): link += '/nintendo-network'
                else: await event.reply(f'Status de quê? Retardado..') 
                if not link.endswith('status'):
                    html = BeautifulSoup(requests.get(link).content, 'html.parser')
                    elem = html.find('div', attrs={'class':'alert-success'})
                    await event.reply(f'{elem.text.strip()}')
            elif re.search('(?i)cotacao', event.raw_text):
                skipToGrosseria = False
                source = 'https://economia.awesomeapi.com.br/all'
                if re.search('(?i)turis', event.raw_text): source = source.replace('all', '/json/list/USDT-BRL/1')
                elif re.search('(?i)bitc', event.raw_text): source = source.replace('all', '/json/list/BTC-BRL/1')
                elif re.search('(?i)euro', event.raw_text): source = source.replace('all', '/json/list/EUR-BRL/1')
                elif re.search('(?i)austr', event.raw_text): source = source.replace('all', '/json/list/AUD-BRL/1')
                elif re.search('(?i)canad', event.raw_text): source = source.replace('all', '/json/list/CAD-BRL/1')
                elif re.search('(?i)libra', event.raw_text): source = source.replace('all', '/json/list/GBP-BRL/1')
                elif re.search('(?i)litec', event.raw_text): source = source.replace('all', '/json/list/LTC-BRL/1')
                elif re.search('(?i)fran|sui', event.raw_text): source = source.replace('all', '/json/list/CHF-BRL/1')
                elif re.search('(?i)argen|pes', event.raw_text): source = source.replace('all', '/json/list/ARS-BRL/1')
                elif re.search('(?i)yen|ien|iên|jap', event.raw_text): source = source.replace('all', '/json/list/JPY-BRL/1')
                elif re.search('(?i)lar|comer|trump|obama', event.raw_text): source = source.replace('all', '/json/list/USD-BRL/1')
                elif re.search('(?i)geral|todo|all', event.raw_text): source = source
                elif re.search('(?i)parale', event.raw_text): skipToGrosseria = True
                else: skipToGrosseria = True
                if not skipToGrosseria:
                    cotacao = json.load(urllib.request.urlopen(source))
                    if not source.endswith('/all'):
                        cotacao = cotacao[0]
                        await event.reply(f'{user_name},\nCotação do {cotacao["name"]}\nCompra: R$ {cotacao["bid"]}\nVenda: R$ {cotacao["ask"]}\nVariação: {cotacao["varBid"]}')
                    else:
                        lista = []
                        for item in cotacao.items():
                            item = item[1]
                            lista.append(f'\n\nCotação do {item["name"]}\nCompra: R$ {item["bid"]}\nVenda: R$ {item["ask"]}\nVariação: {item["varBid"]}')
                        retorno = ''.join(lista)
                        await event.reply(f'{user_name}, seu preguiçoso de uma figa! {retorno}')
                else: await event.reply(f'{user_name}, tá doidinho pra arrumar uma barriga comigo, né?')
        elif re.search('(?i)yuna', event.raw_text):
            if re.match('(?i)@yuna|@xyuna', event.raw_text):
                if re.search('(?i)help|ajuda', event.raw_text):
                    comando = 'COMANDOS:\n'\
                        '@yuna help|ajuda : Exibe este menu\n\n'\
                        '/status [rede] : Exibe o status das redes\n'\
                        '/status [psn|playstation|xbox|xbl|live|nintendo|switch]\n\n'\
                        '/cotacao [moeda] : Exibe a cotação atualizada das moedas\n'\
                        '/cotacao [all|geral|todos]\n'\
                        '/cotacao [dolar|dólar|comercial|trump|obama]\n'\
                        '/cotacao [austaliano|turismo]\n'\
                        '/cotacao [canada|canadense|canadá]\n'\
                        '/cotacao [eur|libra|bitcoin|litecoin]\n'\
                        '/cotacao [yen|ien|iênes|yen|japones|japonês|japão|japao]\n'\
                        '/cotacao [franco|suiço|suico]\n'\
                        '/cotacao [peso|argentino]\n\n'\
                        'GATILHOS C/ YUNA:\n'\
                        '[hi|oi|hello|olá|ok] yuna\n'\
                        'yuna [cálculo simples] *\n'\
                        'yuna [bom dia|boa tarde|boa noite] *\n'\
                        'yuna [hoje?|amanhã?|hj?|amanha?] *\n'\
                        'yuna [sexta|natal|pascoa|páscoa] *\n'\
                        'yuna [bot|b o t|b-o-t|b.o.t|b- o- t|b. o. t] *\n'\
                        'yuna [qualquer perunta]? *\n'\
                        'yuna [qualquer coisa] *\n\n'\
                        'GATILHOS S/ YUNA:\n'\
                        '[xuxa|lixo|lula|temer] \n'\
                        '[lucy|yranha|bitoca] \n'\
                        '[caralho|caraleo|pinto|piroca|porra] \n'\
                        '[dilma|dilmicius|mamadil] \n'\
                        '[bolsonaro|bonoro|myto|bolsomito] \n'\
                        '[correio|curreio|ect|sedex|muamba|carteiro|capivara|pacote|epacket] \n\n'\
                        'OBSERVAÇÕES: \n'\
                        '- não importa se as letras são maiúsculas ou minúsculas \n'\
                        '- não importa a ordem das palavras, nos gatilhos marcados com *'
                    await event.reply(f'{comando}')
            elif re.match('(?i)hi|oi|hello|olá', event.raw_text):
                await event.reply(f'{time_comparision()}, {user_name} e vê se me deixa em paz!')
            elif re.match('(?i)ok', event.raw_text):
                await event.reply('"Ok" o quê, mizerávi! Tá pensando que eu sou o Google de tromba?')
            elif re.search('(?i)bom dia|boa tarde|boa noite', event.raw_text):
                await event.reply(f'{time_comparision()}, {user_name} e vê se me deixa em paz!')
            elif re.search('(?i)natal', event.raw_text):
                await event.reply(f'{user_name}, quer saber do meu saco de presentes ou do meu peru?')
            elif re.search('(?i)pascoa|páscoa', event.raw_text):
                await event.reply(f'Já sei, {user_name}, tá querendo meu ovo..')
            elif re.search('(?i)sexta', event.raw_text):
                await event.reply(f'{user_name}, dia de apertar a têta do amiguinho!')
            elif re.search('(?i)bot|b o t|b-o-t|b.o.t|b- o- t|b. o. t', event.raw_text):
                this_message = random.choice(msg_random).replace('variable', user_name)
                await event.reply(f'{this_message}')
            elif re.search(r'\d+|[+/*-]', event.raw_text):
                regex = ''.join(re.findall(r'\d+|[+/*-]', event.raw_text))
                if len(regex) > 7: await event.reply(f'{user_name}, vá se aproveitar das habilidades matemáticas da sua avó!')
                else: await event.reply(f'Se o resultado não for {eval(regex)}, chama o Oswald de Souza.')
            elif event.raw_text.endswith('?'): 
                if re.search('(?i)hoje|amanhã|hj|amanha', event.raw_text):
                    await event.reply(f'{user_name}, porque você quer saber? Quer sair comigo? Tem que ver se o Maurão deixa..')
                else: await event.reply('Essa eu não sei.. Pergunta lá no Posto Ipiranga!')
            else: 
                this_message = random.choice(msg_yuna).replace('variable', user_name)
                await event.reply(f'{this_message}')
        elif re.search('(?i)xuxa', event.raw_text):
            await event.respond('Opa! Mexeucaxuxa, mexeu comigo!')
        elif re.search('(?i)lucy|yranha|bitoca', event.raw_text):
            this_message = random.choice(msg_bitoca).replace('variable', '@lucyran leva bitoca')
            await event.respond(f'{this_message}')
        elif re.search('(?i)caralho|caraleo|pinto|piroca|porra', event.raw_text):
            await event.respond('Tira isso da boca, menino!')
        elif re.search('(?i)lixo', event.raw_text):
            this_message = random.choice(msg_lixo).replace('variable', user_name)
            await event.respond(f'{this_message}')
        elif re.search('(?i)correio|curreio|ect|sedex|muamba|carteiro|capivara|pacote|epacket', event.raw_text):
            this_message = random.choice(msg_correio).replace('variable', user_name)
            await event.respond(f'{this_message}')
        elif re.search('(?i)lula', event.raw_text):
            this_message = random.choice(msg_lula).replace('variable', user_name)
            await event.respond(f'{this_message}')
        elif re.search('(?i)dilma|dilmicius|mamadil', event.raw_text):
            this_message = random.choice(msg_dilma).replace('variable', user_name)
            await event.respond(f'{this_message}')
        elif re.search('(?i)temer', event.raw_text):
            this_message = random.choice(msg_temer).replace('variable', user_name)
            await event.respond(f'{this_message}')
        elif re.search('(?i)bolsonaro|bonoro|myto|bolsomito', event.raw_text):
            this_message = random.choice(msg_bolsa).replace('variable', user_name)
            await event.respond(f'{this_message}')
        else: print(f'Não respondi à mensagem: {event.raw_text} [enviada por: {user_name}]')

""" [DELETE] Teoricamente, esse método entenderia o evento delete e enviaria uma mensagem a quem excluiu """
@client.on(events.MessageDeleted(chats=MY_CHAT))
async def delete_handler(event):
    await event.reply('Apaga não!')

""" [EDIT/UPDATE] Teoricamente, esse método entenderia o evento edit e enviaria uma mensagem a quem editou """
@client.on(events.MessageEdited(chats=MY_CHAT, incoming=True))
async def update_handler(event):
    await event.reply('Porque editou? Tá com medinho?')

client.run_until_disconnected()
#endregion [TelegramClient Methods]

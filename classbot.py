import telepot

class manicomio:
    def __init__(self, bot, chat_id, msg):
        self.bot = bot
        self.chat_id = chat_id
        self.msg = msg

    def check_command(self, msg):
        log = open('log_commands.txt', 'a')
        links = open('links.txt', 'a')
        adm_id = []
        
        try:
            user = '@' + self.msg['from']['username']
        except:
            user = self.msg['from']['first_name']
        #inicia o bot lindo de morre
        if msg == '/start':
            self.bot.sendMessage(self.chat_id, 'Salve bro, iniciei com sucesso, voce quer ouvir falar um pouco sobre magia negra e Alesteir Crowley?.', reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /start'
        #testa  bot
        elif msg == '/teste':
            self.bot.sendMessage(self.chat_id, 'Say.', reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /test'
        #desfixar as coisas
        elif msg == '/unfix':
            self.bot.unpinChatMessage(self.chat_id)
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /unfix'
        #fixar as coias
        elif msg == '/fix':
            self.bot.pinChatMessage(self.chat_id, self.msg['reply_to_message']['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /fix'
        #banir usuarios:
        elif msg == '/ban':
            try:
                usern = '@' + self.msg['reply_to_message']['from']['username']
            except:
                usern = self.msg['reply_to_message']['from']['first_name']
            self.bot.kickChatMember(self.chat_id, self.msg['reply_to_message']['from']['id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /ban'
            print str(user.encode('utf-8')) + ' has banned ' + str(usern.encode('utf-8'))
        #mensagem de rt do bot
        elif msg == 'rt':
            try:
                reply_user = '@' + self.msg['reply_to_message']['from']['username']
            except:
                reply_user = self.msg['reply_to_message']['from']['first_name']
            self.bot.sendMessage(self.chat_id, user + ' ta puxando saco e sendo gado de  ' + reply_user, reply_to_message_id=self.msg['message_id'])
      

       #lista de comandos do bot

        elif msg == '/comandos@gorpo_bot':
            self.bot.sendMessage(self.chat_id, '[+]Comandos para usuarios[+]\nPara doar com QR code digite - qr\nDigite- site\\nDigite- doar\nDigite- facebook\nDigite- anime\nDigite- netflix\nDigite- painel\n/myid@gorpo_bot -ID do bot\n/id -ID do usuario\n/site -Site da equipe\n/test -Testar plugins ok\n/id -Mostra ID\n[+]Comandos dos admin[+]\n/ban -Bane usuarios\n/fix -Fixa posts\n/unfix -Desfixa posts\n/grupo -Mudar nome do grupo\n/unban -Remove banimento\n/promote -Promove a admin', reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /comandos@gorpo_bot'
        elif msg == 'ajuda':
            self.bot.sendMessage(self.chat_id, '[+]Comandos para usuarios[+]\nPara doar com QR code digite - qr\nDigite- site\\nDigite- doar\nDigite- facebook\nDigite- anime\nDigite- netflix\nDigite- painel\n/myid@gorpo_bot -ID do bot\n/id -ID do usuario\n/site -Site da equipe\n/test -Testar plugins ok\n/id -Mostra ID\n[+]Comandos dos admin[+]\n/ban -Bane usuarios\n/fix -Fixa posts\n/unfix -Desfixa posts\n/grupo -Mudar nome do grupo\n/unban -Remove banimento\n/promote -Promove a admin', reply_to_message_id=self.msg['message_id'])
            
        elif msg == '/admin':
            self.bot.sendMessage(self.chat_id, '[+]Comandos para usuarios[+]\nPara doar com QR code digite - qr\nDigite- site\\nDigite- doar\nDigite- facebook\nDigite- anime\nDigite- netflix\nDigite- painel\n/myid@gorpo_bot -ID do bot\n/id -ID do usuario\n/site -Site da equipe\n/test -Testar plugins ok\n/id -Mostra ID\n[+]Comandos dos admin[+]\n/ban -Bane usuarios\n/fix -Fixa posts\n/unfix -Desfixa posts\n/grupo -Mudar nome do grupo\n/unban -Remove banimento\n/promote -Promove a admin', reply_to_message_id=self.msg['message_id'])
        elif msg == '/help':
            self.bot.sendMessage(self.chat_id, '[+]Comandos para usuarios[+]\nPara doar com QR code digite - qr\nDigite- site\\nDigite- doar\nDigite- facebook\nDigite- anime\nDigite- netflix\nDigite- painel\n/myid@gorpo_bot -ID do bot\n/id -ID do usuario\n/site -Site da equipe\n/test -Testar plugins ok\n/id -Mostra ID\n[+]Comandos dos admin[+]\n/ban -Bane usuarios\n/fix -Fixa posts\n/unfix -Desfixa posts\n/grupo -Mudar nome do grupo\n/unban -Remove banimento\n/promote -Promove a admin', reply_to_message_id=self.msg['message_id'])
        elif msg == 'comandos':
            self.bot.sendMessage(self.chat_id, '[+]Comandos para usuarios[+]\nPara doar com QR code digite - qr\nDigite- site\\nDigite- doar\nDigite- facebook\nDigite- anime\nDigite- netflix\nDigite- painel\n/myid@gorpo_bot -ID do bot\n/id -ID do usuario\n/site -Site da equipe\n/test -Testar plugins ok\n/id -Mostra ID\n[+]Comandos dos admin[+]\n/ban -Bane usuarios\n/fix -Fixa posts\n/unfix -Desfixa posts\n/grupo -Mudar nome do grupo\n/unban -Remove banimento\n/promote -Promove a admin', reply_to_message_id=self.msg['message_id'])
                    
      



            #inicio dos comandos do bot
        elif msg == '/site':
            self.bot.sendMessage(self.chat_id, 'https://tcxsproject.com.br', reply_to_message_id=self.msg['message_id'])
       
        elif msg == '/pin':
            if self.msg['from']['id'] == 749087933:
                self.bot.forwardMessage('@bypassedltda', self.chat_id, self.msg['reply_to_message']['message_id'])
                self.bot.sendMessage(self.chat_id, 'Ok sir.', reply_to_message_id=self.msg['message_id'])
                log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
                print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /forward'
            else:
                self.bot.sendMessage(self.chat_id, 'VAI SE FODER FILHO DA PUTA!!', reply_to_message_id=self.msg['message_id'])
       
       
        #nevia id
        elif msg == '/id':
            self.bot.sendMessage(self.chat_id, self.msg['reply_to_message']['from']['id'], reply_to_message_id=self.msg['message_id'])
        

        elif msg == '/myid@gorpo_bot':
            self.bot.sendMessage(self.chat_id, self.msg['from']['id'], reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /myid@gorpo_bot'
        elif msg == '/unban':
            try:
                fodeu = '@' + self.msg['reply_to_message']['from']['username']
            except:
                fodeu = self.msg['reply_to_message']['from']['first_name']
            self.bot.unbanChatMember(self.chat_id, self.msg['reply_to_message']['from']['id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /unban'
            print str(user.encode('utf-8')) + ' has unbanned ' + str(fodeu.encode('utf-8'))
       
        #promove admins
        elif msg == '/promote':
            try:
                promoted = '@' + self.msg['reply_to_message']['from']['username']
            except:
                promoted = self.msg['reply_to_message']['from']['first_name']
            self.bot.promoteChatMember(self.chat_id, self.msg['reply_to_message']['from']['id'], can_change_info=True, can_post_messages=False, can_edit_messages=False, can_delete_messages=True, can_invite_users=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True)
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /promote'
            print str(user.encode('utf-8')) + ' has promoted ' + str(promoted.encode('utf-8'))
       
         #altera o nome do grupo
        elif self.msg.get('text').startswith('/grupo'):
            mensagem = self.msg.get('text').split()
            mensagem2 = mensagem[1:]
            self.bot.setChatTitle(self.chat_id, ' '.join(mensagem2).encode('utf-8'))
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /grupo'
            print str(user.encode('utf-8')) + ' has changed the name of ' + str(self.chat_id)


             # aqui comeca oque ele responde
        elif msg == 'gorpo':
            self.bot.sendMessage(self.chat_id, 'nao enche o saco dele o filho da puta', reply_to_message_id=self.msg['message_id'])
        elif msg == 'da nada':
            self.bot.sendMessage(self.chat_id, 'da nada nao feio', reply_to_message_id=self.msg['message_id'])
        elif msg == 'toma no cu':
            self.bot.sendMessage(self.chat_id, 'vai toma no cu vc seu bosta do caralho', reply_to_message_id=self.msg['message_id'])
        elif msg == 'cyber':
            self.bot.sendMessage(self.chat_id, 'cyber e um nooob filho da puta cara, vcs deviam banir ele daqui', reply_to_message_id=self.msg['message_id'])
        elif msg == 'gutto':
            self.bot.sendMessage(self.chat_id, 'rip @usergutto', reply_to_message_id=self.msg['message_id'])
        elif msg == 'guto':
            self.bot.sendMessage(self.chat_id, 'rip @usergutto', reply_to_message_id=self.msg['message_id'])
        elif msg == 'guttu':
            self.bot.sendMessage(self.chat_id, 'rip @usergutto', reply_to_message_id=self.msg['message_id'])
        elif msg == 'mahay':
            self.bot.sendMessage(self.chat_id, 'nao cita o nome deste doente filho da puta por favor', reply_to_message_id=self.msg['message_id'])
        elif msg == 'mahayana':
            self.bot.sendMessage(self.chat_id, '@mahayana vai pro inferno este filho da puta', reply_to_message_id=self.msg['message_id'])
        elif msg == 'zmod':
            self.bot.sendMessage(self.chat_id, 'Zmod deveria ser zgod', reply_to_message_id=self.msg['message_id'])
        elif msg == 'ed':
            self.bot.sendMessage(self.chat_id, 'ed filho da puta as vez morre quele pau no cu', reply_to_message_id=self.msg['message_id'])
        elif msg == 'miojo':
            self.bot.sendMessage(self.chat_id, 'Unica user q eu amo e respeito neste grupo', reply_to_message_id=self.msg['message_id'])
        elif msg == 'estives':
            self.bot.sendMessage(self.chat_id, 'nao cita o nome deste filho da puta no grupo por favor', reply_to_message_id=self.msg['message_id'])
        elif msg == 'bom dia':
            self.bot.sendMessage(self.chat_id, 'bom dia teu cu', reply_to_message_id=self.msg['message_id'])
        elif msg == 'boa tarde':
            self.bot.sendMessage(self.chat_id, 'boa tarde o caralho mano, bora cheira uma cocaina', reply_to_message_id=self.msg['message_id'])
        elif msg == 'boa noite':
            self.bot.sendMessage(self.chat_id, 'quando vc for dormir vc vai ter pesadelos com eu estuprando seu cu e empalando vc seu filho da puta', reply_to_message_id=self.msg['message_id'])
        elif msg == 'mit':
            self.bot.sendMessage(self.chat_id, 'quando vcs fala mit eu ja fico doido pra arromba aquele cuzinho maravilhoso nmrl', reply_to_message_id=self.msg['message_id'])
        elif msg == 'feio':
            self.bot.sendMessage(self.chat_id, 'fei do cel nmrl', reply_to_message_id=self.msg['message_id'])
        elif msg == 'tuin':
            self.bot.sendMessage(self.chat_id, 'tuin do caralho fica misturando cocaina com crack e ver cp na deep web de noite', reply_to_message_id=self.msg['message_id'])
        elif msg == '@xurumelo':
            self.bot.sendMessage(self.chat_id, 'PRA QUE MARCAR ESTE FILHO DA PUTA', reply_to_message_id=self.msg['message_id'])
        elif msg == '@Perplex_User':
            self.bot.sendMessage(self.chat_id, 'PRA QUE MARCAR ESTE FILHO DA PUTA', reply_to_message_id=self.msg['message_id'])
        elif msg == 'gorpu':
            self.bot.sendMessage(self.chat_id, 'ele sente tesao quando vcs marcam ele assim', reply_to_message_id=self.msg['message_id'])
        elif msg == 'caralho':
            self.bot.sendMessage(self.chat_id, 'caralho oque feio, para de fala bosta', reply_to_message_id=self.msg['message_id'])
        elif msg == '@fazerlogin':
            self.bot.sendMessage(self.chat_id, 'ja comi o cu desta shemale gordinha de bosta, vadiazinha de merda se acha alguem mas e so mais uma depressiva no telegram esta shema filha da puta', reply_to_message_id=self.msg['message_id'])
        elif msg == '@Perplex_User':
            self.bot.sendMessage(self.chat_id, 'PRA QUE MARCAR ESTE FILHO DA PUTA', reply_to_message_id=self.msg['message_id'])
        elif msg == '@chata_pra_crlh':
            self.bot.sendMessage(self.chat_id, 'MENSAGEM CENSURADA', reply_to_message_id=self.msg['message_id'])
        elif msg == '@usergutto':
            self.bot.sendMessage(self.chat_id, 'Nem adianta marcar que ele mora pra responder nesta bosta, vive jogando xone e ainda apaixonado pela vanessina, guto ta numa merda braba mano deixa ele la nmrl.', reply_to_message_id=self.msg['message_id'])
        elif msg == '@mahayana66':
            self.bot.sendMessage(self.chat_id, 'gordinho mais dodoi do grupo nmrl fei, cara so fala bosta', reply_to_message_id=self.msg['message_id'])
        elif msg == '@gorpo_bot':
            self.bot.sendMessage(self.chat_id, 'Porque voce me acordou das profundezas do inferno seu filho da puta, cara se liga ninguem gosta de vc no grupo, vc e tao retardado que esta marcando bots ja pra conversar de tao vazia que sua vida e seu pau no cu do caralho, agora na boa nao me marca mais e vai pra casa do caralho seu arrombado de merda', reply_to_message_id=self.msg['message_id'])
        elif msg == '@alsnav':
            self.bot.sendMessage(self.chat_id, 'Stives filho da puta pederasta nao libera CP este merda mas vive cheio de ownador de cc na volta dele, amiguinho do jesse pinkman e demais cadders este noia nao dorme nmrl.', reply_to_message_id=self.msg['message_id'])
        elif msg == '@drugsoverd0se':
            self.bot.sendMessage(self.chat_id, 'Cara na boa sua source do coke ate serviu pra algo mas igual vc fez merda em passar seus conhecimentos pro gorpo, agora vamos fazer uma parceria minha com o coke e com vc para nos criar o maior bot ownador de cc e postador de gore do telegram, se estives libera nos poe quela parada proibida nos bots da vida...tmj pau no seu cu vacilao.', reply_to_message_id=self.msg['message_id'])
        elif msg == '@Odeiobot':
            self.bot.sendMessage(self.chat_id, 'Ah ta marcando a bixa loca pode crer que ja vem quelas fotinho de namorado, policial, pai de familia, e cada gato sarado q ate eu fazia uma orgia com estes caras musculosos e galantes, nmrl viadagem e vcs ai fica de frescura.', reply_to_message_id=self.msg['message_id'])
        elif msg == '@cjbugado':
            self.bot.sendMessage(self.chat_id, 'Pra que marcar o cara mais noob do grupo, vc tem demencia ou e retardado igual ele mano, so o pau no cu do cyber pra foder pc neste mundo cara, sai de perto dele q vai da merda nmrl', reply_to_message_id=self.msg['message_id'])
        elif msg == '@MsT3Dz':
            self.bot.sendMessage(self.chat_id, 'Este carinha quando marcam ate eu venho prestar meu respeito, puta baita codder, dev que  ta descendo pau na tcxs, cara tao massa que aperfeicoou os xml e botou a loja em segundo plano, arrumou oque tava bugado este cara ta fazendo a diferenca na cena gamer, nos devemos a tcxs a ele.', reply_to_message_id=self.msg['message_id'])
        elif msg == 'admin':
            self.bot.sendMessage(self.chat_id, 'Nossos admins sao no momento @Odeiobot e @MsT3Dz, voces tambem podem marcar aqui no grupo o @gorpoorko e @usergutto para lhes auxiliar em algo mas nem sempre os mesmos estao online, aconselhamos que visitem nosso forum em procura de erros pois maioria dos mesmos ja encontam-se la e com o tempo serao inseridos neste bot, caso queira entrar para a TCXS Project o valor e de 15 reais mensais e para ter o link com mais descricoes basta digitar site ou donate. Temos a praticidade de pagar nossas doacoes com codigo QR do mercado pago o qual nos tras enorme beneficio para solicitar ele basta digitar qr ou qr code', reply_to_message_id=self.msg['message_id'])
        elif msg == 'gg':
            self.bot.sendMessage(self.chat_id, 'https://www.youtube.com/watch?v=hcMD9hO1vg8', reply_to_message_id=self.msg['message_id'])
        elif msg == 'kkk':
            self.bot.sendMessage(self.chat_id, 'kkkkjjj', reply_to_message_id=self.msg['message_id'])
        elif msg == 'kkkj':
            self.bot.sendMessage(self.chat_id, 'kkkkjjj', reply_to_message_id=self.msg['message_id'])
        elif msg == 'kj':
            self.bot.sendMessage(self.chat_id, 'kkkkjjj', reply_to_message_id=self.msg['message_id'])
        elif msg == 'nmrl':
            self.bot.sendMessage(self.chat_id, 'nmrl o caralho mano, vsf', reply_to_message_id=self.msg['message_id'])    
        elif msg == 'vsf':
            self.bot.sendMessage(self.chat_id, 'vc ta louco mandando eu me foder o seu pau no cu do caralho pra puta que te pariu mano', reply_to_message_id=self.msg['message_id'])
        elif msg == 'filho':
            self.bot.sendMessage(self.chat_id, 'isto, filho, filho da puta mesmo, baita pau no cu', reply_to_message_id=self.msg['message_id'])
        elif msg == 'shemale':
            self.bot.sendMessage(self.chat_id, 'shemale e bom de mais, shemale e vida shemale e poder enfia atras pega na frente e sentir seu pau maior', reply_to_message_id=self.msg['message_id'])
        elif msg == 'dodoi':
            self.bot.sendMessage(self.chat_id, 'dodoi e vc seu demente do caralho, vai te tratar na moral, porra fica e vive ai morrendo se lamentando pro caralho', reply_to_message_id=self.msg['message_id'])
        elif msg == 'namorado':
            self.bot.sendMessage(self.chat_id, 'os namorado do mit sao os mais tarado, safados e gostosos tem de policial a bombeiro, da uns confere pra vcs ver....', reply_to_message_id=self.msg['message_id'])
        elif msg == 'knight':
            self.bot.sendMessage(self.chat_id, 'oque, vcs nao conhecem ainda o knight chan, cario melhor canal do telegram na moral, conferes la ', reply_to_message_id=self.msg['message_id'])
        elif msg == 'cc':
            self.bot.sendMessage(self.chat_id, 'se for falar de cc tem q falar com os melhores da cena, @yJessePinkmanBR e o cara especifico pra isto.', reply_to_message_id=self.msg['message_id'])
        elif msg == 'xcam':
            self.bot.sendMessage(self.chat_id, 'Estives tem um tesao do caralho pelo Xcaminhante eles brigaram por causa de webnramoro por uma e-girl q eles eram gado, isto e tudo q tenho em minha database, ahhh o xcam partilhava cp no telegram tb.', reply_to_message_id=self.msg['message_id'])
        elif msg == 'krl':
            self.bot.sendMessage(self.chat_id, 'krl o caralho escreve direito o seu pau no cu', reply_to_message_id=self.msg['message_id'])
        






        elif msg == 'gay':
            self.bot.sendPhoto(self.chat_id, open('mit.png','rb'), reply_to_message_id=self.msg['message_id'])
        elif msg == 'namorado':
            self.bot.sendPhoto(self.chat_id, open('namorado.jpg','rb'), reply_to_message_id=self.msg['message_id'])
            self.bot.sendPhoto(self.chat_id, open('namorado2.jpg','rb'), reply_to_message_id=self.msg['message_id'])
            self.bot.sendPhoto(self.chat_id, open('namorado3.jpg','rb'), reply_to_message_id=self.msg['message_id'])
            self.bot.sendPhoto(self.chat_id, open('namorado4.jpg','rb'), reply_to_message_id=self.msg['message_id'])
        elif msg == 'airiri':
            self.bot.sendPhoto(self.chat_id, open('airiri.jpg','rb'), reply_to_message_id=self.msg['message_id'])
        

        #comandos para doadores

        elif msg == 'qr':
            self.bot.sendPhoto(self.chat_id, open('qr_15.jpg','rb'), reply_to_message_id=self.msg['message_id'])

        elif msg == 'mercado' :
            self.bot.sendMessage(self.chat_id, 'https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=354396246-315fce8c-d8f9-4aa0-8583-95d678936375', reply_to_message_id=self.msg['message_id'])
        
        elif msg == 'donate':
            self.bot.sendMessage(self.chat_id, 'https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=354396246-315fce8c-d8f9-4aa0-8583-95d678936375', reply_to_message_id=self.msg['message_id'])
        elif msg == 'doar':
            self.bot.sendMessage(self.chat_id, 'https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=354396246-315fce8c-d8f9-4aa0-8583-95d678936375', reply_to_message_id=self.msg['message_id'])
        elif msg == 'facebook':
            self.bot.sendMessage(self.chat_id, 'http://tcxsproject.com.br/facebook', reply_to_message_id=self.msg['message_id'])
        elif msg == 'netflix':
            self.bot.sendMessage(self.chat_id, 'http://tcxsproject.com.br/flix', reply_to_message_id=self.msg['message_id'])
        elif msg == 'painel':
            self.bot.sendMessage(self.chat_id, 'http://tcxsproject.com.br/painel_hacker/', reply_to_message_id=self.msg['message_id'])
        elif msg == 'anime':
            self.bot.sendMessage(self.chat_id, 'http://tcxsproject.com.br/anime', reply_to_message_id=self.msg['message_id']) 
        elif msg == 'anime':
            self.bot.sendMessage(self.chat_id, 'http://tcxsproject.com.br/anime', reply_to_message_id=self.msg['message_id'])                                            
        
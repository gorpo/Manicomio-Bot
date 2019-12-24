# -*- coding: utf-8 -*-

print(r'''

╔╦╗╔═╗═╗ ╦╔═╗  ╔═╗╦═╗╔═╗ ╦╔═╗╔═╗╔╦╗  ╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗  ╔╦╗╔═╗╔═╗╔╦╗
 ║ ║  ╔╩╦╝╚═╗  ╠═╝╠╦╝║ ║ ║║╣ ║   ║   ╠═╣╠═╣║  ╠╩╗║╣ ╠╦╝   ║ ║╣ ╠═╣║║║
 ╩ ╚═╝╩ ╚═╚═╝  ╩  ╩╚═╚═╝╚╝╚═╝╚═╝ ╩   ╩ ╩╩ ╩╚═╝╩ ╩╚═╝╩╚═   ╩ ╚═╝╩ ╩╩ ╩   

                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    






╔╦╗╔═╗═╗ ╦╔═╗  ╔═╗╦═╗╔═╗ ╦╔═╗╔═╗╔╦╗  ╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗  ╔╦╗╔═╗╔═╗╔╦╗
 ║ ║  ╔╩╦╝╚═╗  ╠═╝╠╦╝║ ║ ║║╣ ║   ║   ╠═╣╠═╣║  ╠╩╗║╣ ╠╦╝   ║ ║╣ ╠═╣║║║
 ╩ ╚═╝╩ ╚═╚═╝  ╩  ╩╚═╚═╝╚╝╚═╝╚═╝ ╩   ╩ ╩╩ ╩╚═╝╩ ╩╚═╝╩╚═   ╩ ╚═╝╩ ╩╩ ╩

Manicômio Telegram BOT - @tcxs_bot 

Iniciando a hackeada na galera.


Iniciando o Manicômio Bot TCXS Project...
''')


import telepot
import os
import re
from classbot import manicomio

os.system('clear')

token = '893192395:AAGUm_2rdfwz9Uxc_O7H8WneEzup3XSfNYU'
bot = telepot.Bot(token)

def handle(msg):
    uid = msg['from']['id']
    firstname = msg['from']['first_name']
    chat_id = msg['chat']['id']
    chat_type = msg['chat']['type']
    msgid = msg['message_id']
    user_message = msg.get('text')
    try:
        user = '@' + msg['from']['username']
    except:
        user = firstname
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'document':
        pdfile = open('pdfile.txt', 'a')
        pdfile_read = open('pdfile.txt', 'r')
        pdfile_readed = pdfile_read.read()
        if msg['document']['mime_type'] == 'application/pdf':
            if msg['document']['file_name'] in pdfile_readed:
                bot.sendMessage(chat_id, 'Exists.', reply_to_message_id=msgid)
            else:
                bot.sendMessage(chat_id, 'Uploading....', reply_to_message_id=msgid)
                pdfile.write(msg['document']['file_name'])
                bot.sendMessage('@yourchannel', 'File name: ' + msg['document']['file_name'])
                bot.sendDocument('@yourchannel', msg['document']['file_id'])
                print 'Document sended!'
    elif msg.get('new_chat_member'):
        bot.sendMessage(chat_id, 'Bem-vindo a TCXS Project!  Nossos jogos são apenas para doadores, e a doacao no valor de 15 mensais, para realizar sua doacao acesse nosso site tcxsproject.com.br e logo no comecinho do site tera os botoes de doação. Usamos o sistema de pagamento do Mercado Pago, que por sinal caso queira o link basta digitar "mercado pago" que eu te dou o link ta!', reply_to_message_id=msgid)
        print 'novo usuario entrou em um de seus grupos'
    elif msg.get('text'):
        manicomio_object = manicomio(bot, chat_id, msg)
        texto = msg['text'].split()[0]
        manicomio_object.check_command(texto)

bot.message_loop(handle)
print '*Estamos ONLINE com o BOT Manicômio!'
  
while 1:
    pass

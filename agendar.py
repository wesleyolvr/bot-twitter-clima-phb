from calendar import weekday
import schedule
import time
import requests
from client_twitter import api
import random


url_phb = 'https://api.hgbrasil.com/weather?woeid=455975&format=json'


def DrinkWater():
    frases = ['vai beber água vai! quem avisa amigo é viu 💦🚰',
              'ja bebeu agua? não? pois vaitimbora beber agua então abestado! 💦🚰',
              'Beba água, ja bastam as pedras no caminho, não queira ter nos ✨ rins ✨ ',
              'Você não é um cacto, beba água! 💦🚰',
              'Hidrate-se para :\n-Ter uma pele jovem\n-Ajudar o metabolismo\n-Regular o intestino\n-Eliminar toxinas\n-Emagrecer',
              'Por favor, não se esqueça de beber agua, te amo ❤️',
              'Quando você quer algo e não sabe o quê, beba água. é sempre água. 💦',
              'nera tu que disse que ia ser fitness esses dias? pois vai pelo menos beber água! 💦',
              'BEBA AGUA, pois se você não cuida do seu corpo, onde vocẽ vai viver? 💦🚰',
              "Você é 70% água, então vamos manter o seu 'eu' hidratado e feliz! 💦🚰",
              "Água é a poção mágica dos atletas... ou pelo menos é o que ouvi dizer! 💦🚰",
              "Água: o elixir da vida, e também uma ótima desculpa para pausas no trabalho! 💦🚰",
              "Quer ter um cérebro brilhante? Beba água e deixe seu pensamento fluir como um rio! 💦🚰",
              "Água, o combustível que mantém seu corpo funcionando sem pedir aumento! 💦🚰",
              "Beber água é como um banho interno - só que mais refrescante e sem a necessidade de sabonete! 💦🚰",
              "Se a vida te der limões, adicione água e faça uma limonada. Ou beba água pura mesmo, porque é mais fácil! 💦🚰",
              "Água é como dinheiro: quanto mais você tem, mais segura a onda! 💦🚰",
              "Complete a frase: Água é vida, porque _________. #HidrataçãoSaudável 💦🚰",
              "Qual é a sua dica criativa para beber mais água durante o dia? Compartilhe nos comentários! 💧 #DicasDeHidratação 💦🚰",
              "Se você fosse uma garrafa d'água, qual seria a sua marca e por quê? Responda abaixo! 💦 #MarcaHidratada 💦🚰",
              "Vamos brincar de jogo da palavra! Escreva uma palavra que rime com 'água' nos comentários. Eu começo: Sede! 😄 #RimaDaÁgua 💦🚰",
              "Sabia que a água tem superpoderes? Conte-nos um benefício surpreendente da hidratação nos comentários! 💪💧 #SuperpoderesDaÁgua 💦🚰"]
    text = random.choice(frases)
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        text = random.choice(frases)
        api.update_status(status=text)
        print(e)
        pass

def SayGoodFriday():
    frases_friday = ['"Sexta-feira. Dia de espalhar gentilezas. Dia de falar, sentir, fazer e sorrir. De beber, flertar, olhar e gargalhar. Dia meu. Dia nosso." - Livia Araújo',
                     '"Todo dia é dia de ser Feliz,\nMas hoje você tem um motivo a mais....\nÉ sexta-feira. Feliz sexta-feira!!!" - Rosangela Zorio',
                     '"O ânimo misteriosamente põe fim na canseira quando enfim chega a sexta-feira". - Leandro Cesaroni',
                     '"Sexta-feira! Um dos dias que muitos de nós gostamos, pois é como estar na véspera de uma recompensa." - Edu Lazaro',
                     '"Tenho paixão pelo Sábado, mas meu grande amor é a sexta-feira. - Freitas Branco"']
    text = random.choice(frases_friday)
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass


def sayGoodMorning():
    text = 'Bom dia seus lindos! 🌞\nsó os educados respondem. 😊'
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass


def sayGoodNight():
    text = 'Boa noite negada! 🌚 \nsó os educados respondem. 😊'
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass

def sayPrevisaoParnaiba():
    print('Previsão para o dia seguinte')
    response = requests.get(url_phb)
    day_today = response.json()['results']['forecast'][0]
    data_previsao = day_today['date']
    dia_previsao = day_today['weekday']
    max = day_today['max']
    min = day_today['min']
    text = f'Previsão para {dia_previsao}, {data_previsao}:\n🌡️ Max: {max}°C\n🥶 Min: {min}°C'
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass
    

def saytimeParnaiba():
    response = requests.get(url_phb)
    city = response.json()['results']['city'].replace(',',' -')
    data = response.json()['results']['date']
    velocidade_vento = response.json()['results']['wind_speedy']
    nascer_sol = response.json()['results']['sunrise']
    por_sol = response.json()['results']['sunset']
    graus = response.json()['results']['temp']
    horario = response.json()['results']['time']
    descricao = response.json()['results']['description']
    day_today = response.json()['results']['forecast'][0]
    max = day_today['max']
    min = day_today['min']
    
    # text = f'Clima em {city} em {data}\n🕐 Ultima consulta: {horario}\n🌡️ Temperatura: {graus}°C com {descricao}\n🌬️ Velocidade do vento: {velocidade_vento}.\n🌅 Nascer do Sol: {nascer_sol}\n🌇 Por do Sol: {por_sol}'
    text = f'Clima em {city} em {data}\n🌡️ Max: {max}°C\n🥶 Min: {min}°C\n☁️ T️emperatura: {graus}°C , {descricao}\n🌬️ Velocidade do vento: {velocidade_vento}.\n🌅 Nascer do Sol: {nascer_sol}\n🌇 Por do Sol: {por_sol}\n🕐 Ultima consulta: {horario}'
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass


schedule.every().friday.at("09:00").do(SayGoodFriday)
schedule.every().day.at("08:00").do(sayGoodMorning)
schedule.every().day.at("22:00").do(sayGoodNight)
schedule.every(2).hours.at(":10").do(DrinkWater)
schedule.every(2).hours.at(":40").do(saytimeParnaiba)

try:    
    while True:
        schedule.run_pending()
        time.sleep(2)
except Exception as e:
    print(e)
    pass
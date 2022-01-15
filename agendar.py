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
              'Hidrate-se para :\n-Ter uma pele jovem\n-Ajudar o metabolismo\n-Regular o intestino\n-Eliminar toxinas\n-Emagrecer'
              'Por favor, não se esqueça de beber agua, te amo ❤️',
              'Quando você quer algo e não sabe o quê, beba água. é sempre água. 💦',
              'nera tu que disse que ia ser fitness esses dias? pois vai pelo menos beber água! 💦',
              'BEBA AGUA, pois se você não cuida do seu corpo, onde vocẽ vai viver? 💦🚰']
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
    response = requests.get(url_phb)
    data_previsao = response.json()['results']['forecast'][1]['date']
    dia_previsao = response.json()['results']['forecast'][1]['weekday']
    max = response.json()['results']['forecast'][1]['max']
    min = response.json()['results']['forecast'][1]['min']
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
    
    # text = f'Clima em {city} em {data}\n🕐 Ultima consulta: {horario}\n🌡️ Temperatura: {graus}°C com {descricao}\n🌬️ Velocidade do vento: {velocidade_vento}.\n🌅 Nascer do Sol: {nascer_sol}\n🌇 Por do Sol: {por_sol}'
    text = f'Clima em {city} em {data}\n🕐 Ultima consulta: {horario}\n🌡️ T️emperatura: {graus}°C , {descricao}\n🌬️ Velocidade do vento: {velocidade_vento}.\n🌅 Nascer do Sol: {nascer_sol}\n🌇 Por do Sol: {por_sol}'
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass


schedule.every().friday.at("09:00").do(SayGoodFriday)
schedule.every().day.at("08:00").do(sayGoodMorning)
schedule.every().day.at("14:44").do(sayPrevisaoParnaiba)
schedule.every().day.at("22:00").do(sayGoodNight)
schedule.every(2).hours.at(":10").do(DrinkWater)
schedule.every().hour.at(":40").do(saytimeParnaiba)

try:    
    while True:
        schedule.run_pending()
        time.sleep(2)
except Exception as e:
    print(e)
    pass
import requests

link = 'http://icanhazip.com/';
my_IP = requests.get(link) #запроc мой IP
print("Мой IP - ", my_IP.text)

link = 'https://random.dog/woof.json'; #случайная картинка животного
response = requests.get(link)
if response.status_code==200:
  print(response.text) #получили ответ и вывели что пришло
  data = response.json() #перевели ответ в json
  print(data['url']) #вывели ссылку на картинку
  link = data['url']; #запрос к картинке
  response = requests.get(link)
  if response.status_code==200:
    with open("picthure.jpg",'wb') as imgfile:
     imgfile.write(response.content)#записали байтики


import os
import requests

message = 'Essa é uma mensagem!'

response = requests.get(
    url ='https://api.textmebot.com/addphone.php?apikey=1WyqTtZoCJzV',
    params = {
        'recipient':os.getenv('1WyqTtZoCJzV'),
        'text':message,
        'apikey':os.getenv('API_KEY'),
    }
)
if response.status_code == 200:
    print('Mensagem enviada com sucesso!')

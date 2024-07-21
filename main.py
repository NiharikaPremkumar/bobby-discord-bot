from typing import Final
import os
from dotenv  import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#tokenloading
load_dotenv()
TOKEN:Final[str]= os.getenv('DISCORD_TOKEN')
#bot setup(intents/permissions)
intents:Intents=Intents.default()
intents.message_content= True #NOQA
client: Client=Client(intents=intents)

#message  function
async def send_message(message: Message, user_message:str)-> None:
    if not user_message:
        print('(Meassage empty;intents were not enabled)')
        return
    if is_private := user_message[0] =='?': #indicated privacy
        user_message=user_message[1:] #exclude ?
    try:
        response: str=get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)#send to author or channel if message is private
    except Exception as e:
        print(e)
# handling startup 
@client.event
async def on_ready()-> None:
    print(f'{client.user} is now running!')
#handling incoming messages
@client.event
async def on_message(message: Message)->None:
    if message.author ==client.user:
        return
    username: str=str(message.author)
    user_message: str=message.content
    channel:str=str(message.channel)
    print(f'[{channel}] {username} : "{user_message}" ')
    await send_message(message, user_message)
#MAIN entry point
def main()-> None:
    client.run(token=TOKEN)


if __name__=='__main__':
    main()

    
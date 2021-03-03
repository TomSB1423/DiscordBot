from commands.base_command  import BaseCommand
from utils                  import get_emoji
import discord

class Love(BaseCommand):

    def __init__(self):
        description = ":cat: 4 U"
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            param = str(params[0])
        except ValueError:
            await client.send_message(message.channel, "Please, provide valid numbers")
            return
        
        if '<@!793966532036263986>' in param or '<@!457585333350039563>' in param:
            await message.channel.send('Bow down to me')
            await message.channel.send('http://gph.is/1eQCRJQ')
        else:    
            await message.channel.send("You're a Polish willy" + param)
            await message.channel.send('Shup up Freestone')
            await message.channel.send('http://gph.is/2oJ04H0')
import discord
import os
from dotenv import load_dotenv
import httpx
load_dotenv()

class ZetaClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user: return

        #await message.channel.send(self.generate(message.content))

        if message.content == "join_vc":
            await message.author.voice.channel.connect()

        if message.content == "play_music":
            self.play_music()

    def play_music(self):
        if self.voice_clients != None:
            source = discord.FFmpegPCMAudio(r"C:\Users\lumi192\zeta\src\music.mp3")
            self.voice_clients[0].play(source)
        else:
            print("not in vc!")

    def generate(input):
        response = httpx.post(
            url="https://api.groq.com/openai/v1/chat/completions", #endpoint, remember that the server expects specific data
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {os.getenv("GROQ_API_KEY")}"
            },
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [{ "role": "user", "content": input}]
            }
        )

        data = response.json()
        return data["choices"][0]["message"]["content"]



intents = discord.Intents.default()
intents.message_content = True
client = ZetaClient(intents=intents)
client.run(os.getenv("BOT_TOKEN"))

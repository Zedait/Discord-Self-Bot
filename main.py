import discord

OWNER_ID = KENDİ DİSCORD İDNİZ

class MyClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.oto_cevap = True
        self.sunucu_cevap = False

    async def on_ready(self):
        print(f"Giriş yapıldı: {self.user}")

    async def on_message(self, message):
        if message.author.id == self.user.id and message.author.id != OWNER_ID:
            return

        content = message.content.lower()

        if message.author.id == OWNER_ID:
            if "!otocevap aç" in content:
                self.oto_cevap = True
                await message.channel.send("✅ Otomatik cevap **açıldı**.")
                return
            elif "!otocevap kapat" in content:
                self.oto_cevap = False
                await message.channel.send("❌ Otomatik cevap **kapatıldı**.")
                return
            elif "!sunucucevap aç" in content:
                self.sunucu_cevap = True
                await message.channel.send("✅ Sunucu cevapları **açıldı**.")
                return
            elif "!sunucucevap kapat" in content:
                self.sunucu_cevap = False
                await message.channel.send("❌ Sunucu cevapları **kapatıldı**.")
                return

        if message.guild and not self.sunucu_cevap:
            return

        if self.user in message.mentions and self.oto_cevap:
            await message.channel.send("🟡 **Müsait değil!**\nBirazdan geri dönüş yapacak.")

client = MyClient()
client.run("KENDİ HESAP TOKENİNİZİ GİRİN")

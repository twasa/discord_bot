from services.discord import api as discord_api

discord_bot = discord_api.BotApp()

if __name__ == '__main__':
    discord_bot.run()

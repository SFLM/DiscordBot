from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Interaction, app_commands, Object
from responses import get_response

# Load our token from the .env file
load_dotenv()
TOKEN: Final = os.getenv("DISCORD_TOKEN")

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
tree: app_commands.CommandTree = app_commands.CommandTree(client)
guild_id = 235049617354391563


# Listen for messages/interactions
@tree.command(
    name = "no_args",
    description="My application command",
    guild = Object(id=guild_id)
)
async def no_args(interaction: Interaction) -> None:
    try:
        await interaction.response.send_message("Hi there!")
    except Exception as e:
        print(e)

@tree.command(
    name = "with_args",
    description="My application command",
    guild = Object(id=guild_id)
)
async def with_args(interaction: Interaction, user_input: str) -> None:
    try:
        response: str = get_response(user_input)
        await interaction.response.send_message(response)
    except Exception as e:
        print(e)

# Handling startup for bot
@client.event
async def on_ready() -> None:
    await tree.sync(guild=Object(id=guild_id))
    print(f"{client.user} is now running!!!!")

# Main entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()
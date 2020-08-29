import discord
from discord.ext import commands
from datetime import datetime
from pypresence import Presence
import time
import random

client_id = '749319383276585032'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

#print(RPC.update(state="Hello hello", details="Hello hello, I am details"))  # Set the presence

# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)

details = "Waiting for death."
state = "A status"
startTimestamp = timestamp
endTimestamp = 1599248160
largeImageKey = "faustdread"
largeImageText = "Dread"

while True:  # The presence will stay on as long as the program is running
    RPC.update(details=details, state=state, start=startTimestamp, end=endTimestamp, large_image=largeImageKey, large_text=largeImageText) #Set the presence, picking a random quote
    time.sleep(60)
import discord.message
import discord
from ..helpers import config

# flowchart
# 1 check current action
# 2 process location
# 3 process authority of command 
# 4 process action
PROCESSING_CMD = None
AWAITING_CMD_LIST = []
SAMPLE_CMD = {'cmd_msg': 123, 'cmd_reply': 321}

def update_cmd_list(message = discord.message):
    if message != None:
        reply = message.reply('initializing process')
        new_cmd = {'cmd_msg': message.id, 'cmd_reply': reply.id}
        AWAITING_CMD_LIST.append(new_cmd)
    
    process_command(AWAITING_CMD_LIST[0].cmd_msg)
    return
def process_command(message = discord.message):
    update_cmd_list(message)
        
    if message.guild:  # If the message is from a guild (server)
        return f"Guild: {message.guild.name}"
    else:  # If the message is a private/direct message
        return f"Private message from: {message.author.name}"

def process_guild_command(message = discord.message):
    
    return

def process_pm_command(message = discord.message):
    return
def delete_messsage(message_id):

def sudo_add_user():
    # 1 send a message to prompt reaction
    # 2 check if user_id in employee list bypass if id == bypass
    # 3 prompt schedule service 
    return

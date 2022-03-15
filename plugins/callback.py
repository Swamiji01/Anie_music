from driver.core import me_bot, me_user
from driver.queues import QUEUE
from driver.decorators import check_blacklist
from program.utils.inline import menu_markup, stream_markup

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""Hi [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})\n
~ I'm {me.bot.first_name} and I will help u play music and stream videos in your group Voice chat!

Click On the **Command** Button to know all my Commands!

⁉️For Beginners Click Guide Button!
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("メAdd me to a Groupメ", url=f"https://t.me/{me_bot.username}?startgroup=true")
                ],[
                    InlineKeyboardButton("❓Guide", callback_data="user_guide")
                ],[
                    InlineKeyboardButton("Commands🎶", callback_data="command_list"),
                    InlineKeyboardButton("My Owner🍣", url=f"https://t.me/{OWNER_USERNAME}")
                ],[
                    InlineKeyboardButton("👥 Support Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                    InlineKeyboardButton("☑️ Support Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton("Source Code", url="https://github.com/godfatherakkii/anie_music")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""Guide To use bot!!!

メ /play - Use this with song title or yt link or audio file to play song.

メ /vplay - Use this with song title or yt link or video file to play Video.

メ /vstream - Use this with give the YouTube live stream video link.
⁉️ Confused? Contact us in [Support Group](https://t.me/{GROUP_SUPPORT}).""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◀️ Go Back", callback_data="user_guide")]]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""**How to use this Bot ?**, read the Guide given below !

1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{me_user.username} to your group or type /userbotjoin to invite bot assistant, The userbot will joined by itself when you type `/play (song name)` or `/vplay (song name)`.
4.) Turn On the video chat first before start to play video/music.

`Done! You are ready to rock!`

🍣 Make sure that the voice chat is already on otherwise music assistant might not join your group.

🍁 For Any Queries Join Support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("» Quick use Guide «", callback_data="quick_use")
                ],[
                    InlineKeyboardButton("◀️ Go Back", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""🍣 **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» Check out the menu below to read the module information & see the list of available Commands !

All commands can be used with (`! / .`) handler""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("メ Admins Commands", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("メ Users Commands", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("メ Sudo Commands", callback_data="sudo_command"),
                    InlineKeyboardButton("メ Owner Commands", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("◀️ Go Back", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""🍣 Command list for all user.

メ /play (song name/youtube link) - play the music from youtube
メ /stream (youtube live link) - play yt live stream music
メ /vplay (video name/youtube link) - play the video from youtube
メ /vstream (youtube live link) - play yt live stream video
メ /playlist - view the queue list of songs and current playing song
メ /lyric (query) - search for song lyrics based on the name of the song
メ /video (query) - download video from youtube
メ /song (query) - download song from youtube
メ /search (query) - search for the youtube video link
メ /ping - show the bot ping status
メ /uptime - show the bot uptime status
メ /anie - show the bot alive info (in Group only)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◀️ Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""🍣 Command list for group admin.

メ /pause - pause the current track being played
メ /resume - play the previously paused track
メ /skip - goes to the next track
メ /stop - stop playback of the track and clears the queue
メ /vmute - mute the streamer userbot on group call
メ /vunmute - unmute the streamer userbot on group call
メ /adjustvolume `1-200` - adjust the volume of music (userbot must be admin)
メ /reload - reload bot and refresh the admin data
メ /userbotjoin - invite the userbot to join group
メ /userbotleave - order userbot to leave from group
メ /startvc - start/restart the group call
メ /stopvc - stop/discard the group call""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◀️ Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    if user_id not in SUDO_USERS:
        await query.answer("⚡ You don't have permissions to click this button\n\n» This button is for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""🍣 Command list for sudo user.

メ /stats - get the bot current statistic
メ /calls - show you the list of all active group call in database
メ /block (`chat_id`) - use this to blacklist any group from using your bot
メ /unblock (`chat_id`) - use this to whitelist any group from using your bot
メ /blocklist - show you the list of all blacklisted chat
メ /speedtest - run the bot server speedtest
メ /sysinfo - show the system information
メ /logs - generate the current bot logs
メ /eval - run an code
メ /sh - run an code""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◀️ Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    if user_id not in OWNER_ID:
        await query.answer("⚡ You don't have permissions to click this button\n\n» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""🍣 Command list for bot owner.

メ /update - update your bot to latest version
メ /restart - restart your bot server
メ /leaveall - order userbot to leave from all group
メ /leavebot (`chat id`) - order bot to leave from the group you specify
メ /broadcast (`message`) - send a broadcast message to all groups in bot database
メ /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◀️ Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("**⚡Admin with manage video chat permission can tap this button !**", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("**❌ nothing is currently Playing!**", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("**⚡Admin with manage video chat permission can tap this button !**", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("**⚡Admin with manage video chat permission can tap this button !**", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()

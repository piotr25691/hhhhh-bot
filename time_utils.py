import datetime
import uptime

"""Adds functionality for anything related to time."""


def get_bot_uptime(start_time):
    now = datetime.datetime.utcnow()
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = f"`{days}` days, `{hours}` hours, `{minutes}` minutes, and `{seconds}` seconds."
    else:
        time_format = f"`{hours}` hours, `{minutes}` minutes, and `{seconds}` seconds."
    return time_format


def get_sys_uptime():
    hours, remainder = divmod(int(uptime.uptime()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = f"`{days}` days, `{hours}` hours, `{minutes}` minutes, and `{seconds}` seconds."
    else:
        time_format = f"`{hours}` hours, `{minutes}` minutes, and `{seconds}` seconds."
    return time_format

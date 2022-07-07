import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("BQC3nVUR8ds57hrQUmcjJji3iJjLse9tZQwsTKsehk1_0KPVo_qVfd8v92lu4Ybx1x5yT2FUTlkdhQRA8WlXn1FOPGJa1-RIMz7bceFSnDgvBMDiC4i-S_q3qyD64kSpv1oLePL50E3Mp8CasOwh623AOP0YqOKAOEEz1rtrg21UW64dFWRgJcY1JH9eswBda2_aGI2AYlcyanXQw2s3bOpd9OQYnugzK5W7F_hlqJRvHWvKqWqS5OG1mEMOKIqHvyM99QYbpNNVjRqjH0drbyOwrMXBEehjO2kFZ-zESW82Fs1KhxvP062a4D1Uz7ETpcSkmReY24U-jevE1jfCaTMwX0S6dQA", "BQC3nVUR8ds57hrQUmcjJji3iJjLse9tZQwsTKsehk1_0KPVo_qVfd8v92lu4Ybx1x5yT2FUTlkdhQRA8WlXn1FOPGJa1-RIMz7bceFSnDgvBMDiC4i-S_q3qyD64kSpv1oLePL50E3Mp8CasOwh623AOP0YqOKAOEEz1rtrg21UW64dFWRgJcY1JH9eswBda2_aGI2AYlcyanXQw2s3bOpd9OQYnugzK5W7F_hlqJRvHWvKqWqS5OG1mEMOKIqHvyM99QYbpNNVjRqjH0drbyOwrMXBEehjO2kFZ-zESW82Fs1KhxvP062a4D1Uz7ETpcSkmReY24U-jevE1jfCaTMwX0S6dQA")
BOT_TOKEN = getenv("5424124234:AAFW4YrS8cowJNPBw26ScOMugL3Y2cui5t0")
BOT_NAME = getenv("VCsMusicBot")
UPDATES_CHANNEL = getenv("-1001633387358", "tgbotproject")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/b8f543959432c991f0537.jpg")
admins = {}
API_ID = int(getenv("API_ID", "16267784"))
API_HASH = getenv("b29707434744713a3dad070bda43d856")
BOT_USERNAME = getenv("asnik_music_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VCsMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "zauteschat")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "SKQFAI-IMSCOW-LZSWKM-LIDTSS-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# Discord BOT

## reference
- https://discordpy.readthedocs.io/en/stable/api.html#

## pre-request
1. login Discord and go to develop page https://discord.com/developers/applications
2. New Application and set a name
3. Bot > Add Bot and set Username
4. Bot permissions
5. check permissions that your BOT needed (https://discord.com/developers/docs/topics/permissions)

## dependency
```
beautifulsoup4 4.9.3 Screen-scraping library
└── soupsieve >1.2
discord.py 1.7.3 A Python wrapper for the Discord API
└── aiohttp >=3.6.0,<3.8.0
    ├── async-timeout >=3.0,<4.0
    ├── attrs >=17.3.0
    ├── chardet >=2.0,<5.0
    ├── multidict >=4.5,<7.0
    ├── typing-extensions >=3.6.5
    └── yarl >=1.0,<2.0
        ├── idna >=2.0
        └── multidict >=4.0 (circular dependency aborted here)
opencc-python-reimplemented 0.1.6 OpenCC made with Python
python-dotenv 0.18.0 Read key-value pairs from a .env file and set them as environment variables
requests 2.26.0 Python HTTP for Humans.
├── certifi >=2017.4.17
├── charset-normalizer >=2.0.0,<2.1.0
├── idna >=2.5,<4
└── urllib3 >=1.21.1,<1.27
```

## run discord BOT
```shell
python main.py
```

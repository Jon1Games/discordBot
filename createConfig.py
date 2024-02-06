import yaml

configInfo = {
        'WelcomeMessage': {
            'ChannelID': None,
            'Title': "Welcome",
            'Description': "hello {user}",
            'Color': {
                'Info': "This works with RGB colors (dont change this)",
                'Red': 0,
                'Green': 255,
                'Blue': 0
            }
        },
        'TemporaryVoice': {
            'ChannelID' : None,
            'CreateChannelName': "{user}´s Channel"
        }
    }


async def createConf(guildID):
    file = open("config/" + str(guildID) + '.yml', 'a')
    file.close()
    with open("config/" + str(guildID) + ".yml", 'w') as yamlfile:
        yaml.dump(configInfo, yamlfile, sort_keys=True, default_flow_style=None)

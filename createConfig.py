import yaml

configInfo = {
        'WelcomeMessage': {
            'Enabled': False,
            'ChannelID': None,
            'Title': "Welcome",
            'Description': "hello {user}",
            'Color': {
                'Info': "This works with RGB colors",
                'Red': 0,
                'Green': 255,
                'Blue': 0
            }
        },
        'TemporaryVoice': {
            'Enabled': False,
            'ChannelID': None,
            'CreateChannelName': "{user}´s Channel"
        },
        'AutoRole': {
            'Enabled': False
        }
    }


async def createConf(guildID):
    file = open("config/" + str(guildID) + '.yml', 'a')
    file.close()
    with open("config/" + str(guildID) + ".yml", 'w') as yamlfile:
        yaml.dump(configInfo, yamlfile, sort_keys=True)

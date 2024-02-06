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
    print("10")
    file = open("config/" + str(guildID) + '.yml', 'a')
    print("11")
    file.close()
    print("12")
    with open("config/" + str(guildID) + ".yml", 'w') as yamlfile:
        print("13")
        yaml.dump(configInfo, yamlfile, sort_keys=True, default_flow_style=None)
        print("14")

import configparser
config = configparser.ConfigParser()

config['database']={
    'host':'locahost',
    'port':'3000',
    'user':'dave'
}

config['api']={
    'key': '0fbad929579d1a873ea7fb94d55dbf7d794d32f9'
}

with open('settings.ini','w') as configfile:
    config.write(configfile) 

config.read('./settings.ini')
# db_host=config.get('database','host')
db_host=config['database']['host']
db_api=config['api']['key']
db_port=config.getint('database','port')

print(f"The database host is {db_host}")
print(f"The database api is {db_api}")
print(f"The database port(int) is {db_port}")
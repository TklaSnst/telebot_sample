
async def get_env_data():
    with open(".env", "r+") as file:
        env_data = {}
        lines = file.readlines()
        for line in lines:
            env_data[line.split('=')[0]] = line.split('=')[1][:-1]
    return env_data

import configparser
c = configparser.ConfigParser()
c.read(r"C:\Users\ssbai\PycharmProjects\pythonProject\conf\case_conf.conf")
print(c.get("mode", "name"))

import base64
import my_log
logging = my_log.MyLog()


class EnDecryption:

    def __init__(self, encryption_str=None, decryption_str=None, encryption_code="utf_8", decryption_code="utf_8"):
        self.encryption_str = encryption_str
        self.decryption_str = decryption_str
        self.encryption_code = encryption_code
        self.decryption_code = decryption_code

    def enbease64(self):
        logging.info("编码前的数据是：{}".format(self.encryption_str))
        self.encryption_str = str(base64.b64encode(str(self.encryption_str).encode(self.encryption_code)), self.decryption_code)
        logging.info("编码后的数据是：{}".format(self.encryption_str))
        return self.encryption_str

    def debease64(self):
        logging.info("解码前的数据是：{}".format(self.decryption_str))
        try:
            self.decryption_str = str(base64.b64decode(self.decryption_str), self.encryption_code)
        except Exception as e:
            logging.info("解码的数据'{}'格式错误".format(self.decryption_str))
        else:
            logging.info("解码后的数据是：{}".format(self.decryption_str))
            return self.decryption_str


if __name__ == '__main__':
    print(EnDecryption("ssbai").enbease64())
    print(EnDecryption(decryption_str="c3NqqiYWk=1dsknsdj").debease64())
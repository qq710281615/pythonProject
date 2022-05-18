import yaml


class YamlDo:

    def __init__(self, filename, cont=None, encoding="utf-8"):
        """
        操作yaml文件
        :param filename: 文件名
        :param encoding: 文件编码
        :param cont: 要写入的文件内容
        """
        self.filename = filename
        self.encoding = encoding
        self.cont = cont

    def read_yaml(self):
        """
        读取yaml文件内容
        :return: 返回yaml文件内容
        """
        with open(self.filename, "r", encoding=self.encoding) as f:
            data = yaml.load(f.read(), Loader=yaml.FullLoader)
        return data

    def write_yaml(self):
        """
        写入yaml文件
        :return:
        """
        # 先判断是否是字典，字典就是单组数据
        print("------开始写入数据-----")
        if isinstance(self.cont, dict):
            try:
                with open(self.filename, "w", encoding=self.encoding) as f:
                    yaml.dump(stream=f, data=self.cont, allow_unicode=True)
            except Exception as E:
                print(E)
            else:
                print("------单组数据写入成功------")
        # 列表就是多组数据，通过遍历列表写入
        elif isinstance(self.cont, list):
            # 清空文件
            with open(self.filename, "w", encoding=self.encoding) as f_q:
                f_q.truncate()
            # 写入
            try:
                with open(self.filename, "a", encoding=self.encoding) as f:
                    for i in self.cont:
                        if isinstance(i, dict):
                            yaml.dump(stream=f, data=i, allow_unicode=True)
            except Exception as e:
                print(e)
            else:
                print("------多组数据写入成功-----")
        else:
            print("要输入的内容格式错误")


if __name__ == '__main__':
    # print(YamlDo("../test_yaml.yml").read_yaml())
    YamlDo("../test_yaml.yml", [{"a": "b"}, {"c": "d"}, {"q1": [{"w": "wo"}]}, {"q": {"q": [1, 2]}}]).write_yaml()
    print(YamlDo("../test_yaml.yml").read_yaml())


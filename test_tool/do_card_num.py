# 生成银行卡号
import random


class CreateCardNum:

    def __init__(self):
        # 多个银行卡bin
        self.card_bin_list = ["621785",  "622525"]
        # 银行卡号
        self.card_num_list = []
        # 银行卡号最后一位
        self.check_last()

    def no_last(self):
        # 生成银行卡号中间9位数的 列表
        list_str = [random.randint(0, 9) for _ in range(12)]
        # 将列表转为字符串
        str_null = ""
        for s in list_str:
            str_null = str_null + str(s)
        # 循环
        for j in self.card_bin_list:
            self.card_num_list.append(j + str_null)

    def check_last(self):
        """计算银行卡号最后一位数"""
        #   生成中间位数
        self.no_last()

        for m in range(len(self.card_num_list)):
            c = self.card_num_list[m] + "X"
            sum_o = []
            sum_j = []
            # 偶数位 乘2 后 值转乘列表
            for ii in c[-2::-2]:
                for j in str(int(ii) * 2):
                    sum_o.append(j)
            # 奇数位值转乘列表
            for _ in c[-3::-2]:
                sum_j.append(_)
            # 所的位数 合成一个列表
            so_ = [int(ls) for ls in sum_j + sum_o]
            # 计算最后一位(校验码)
            d = 10 - (sum(so_) % 10)
            # print(d)
            x_true = d if d != 10 else 0
            # 替换
            self.card_num_list[m] = c.replace("X", str(x_true))
        return self.card_num_list


if __name__ == '__main__':
    # 生成20个银行卡号
    data = []
    for i in range(10):
        data.extend(CreateCardNum().card_num_list)
    print(str(data))

          
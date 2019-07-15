import allure
import yaml


@allure.step(title='正在进行读取yaml数据操作')
def read_yaml(filename):
    with open('./data/{}.yaml'.format(filename), 'r')as f:
        # 去除警告方法
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    """以下为验证login_data的参数化数据"""
    # data_list = []
    # for data in result.values():
    #     data_list.append(tuple(data.values()))
    # print(data_list)
    """以下为验证address_data的参数化数据"""
    result = read_yaml('address_data')
    data_list=[tuple(data.values()) for data in result.values()]
    print(data_list)
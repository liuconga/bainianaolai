import allure
import yaml

@allure.step(title='正在进行读取yaml数据操作')
def read_yaml():
    with open('./data/login_data.yaml', 'r')as f:
        #去除警告方法
        return yaml.load(f,Loader=yaml.FullLoader)


if __name__ == '__main__':
    result=read_yaml()
    data_list = []
    for data in result.values():
        data_list.append(tuple(data.values()))
    print(data_list)

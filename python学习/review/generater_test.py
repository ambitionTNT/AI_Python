# python learing
# author:TNT
#设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
import random

def generate_code(code_len = 4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    #所有的字符
    all_char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #字符长度
    last_pos = len(all_char)-1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_char[index]
    return code

if __name__ == '__main__':
    print(generate_code())
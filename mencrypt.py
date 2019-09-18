#coding = utf-8
import base64
import sys
import argparse
import os


def base_code(targetString, funcName):
    try:
        targetFunc = getattr(base64, funcName)
        if targetFunc is None:
            print('decode type error')
            return
        return targetFunc(targetString)
    except Exception as identifier:
        print(identifier)


def get_options():
    parser = argparse.ArgumentParser(
        description="base16,base32,base64,base85加密、解密")
    parser.add_argument("data", help="被处理数据")
    parser.add_argument("-O",
                        choices=['b16encode', 'b16decode', 'b32encode', 'b32decode',
                                 'b64encode', 'b64decode', 'b85encode', 'b85decode'],
                        default="b64decode",
                        help="对输入数据的操作")
    parser.add_argument('-o', help="输出文件名")
    parser.add_argument('-f', action="store_true", help="是否将输入解释为文件名")
    parser.add_argument('-e', default='utf8', help="字符串编码(默认utf8)")
    return parser.parse_args()


def process_data(args):
    targetData = args.data
    if args.f:
        try:
            if not os.path.exists(targetData) or not os.path.isfile(targetData):
                print("文件不存在")
                return
            fp = open(targetData, 'rb')
            targetData = fp.read()
            fp.close()
        except Exception as identifier:
            print(identifier)
    else:
        targetData = bytes(targetData, args.e)

    ret = base_code(targetData, args.O)
    if args.o is not None:
        try:
            fp = open(args.o, 'wb')
            fp.write(ret)
            fp.close()
        except Exception as identifier:
            print(identifier)
    else:
        print(ret)


if __name__ == "__main__":
    args = get_options()
    process_data(args)

# mencrypt
加密解密命令行工具

usage: mencrypt.py [-h]
                   [-O {b16encode,
                        b16decode,
                        b32encode,
                        b32decode,
                        b64encode,
                        b64decode,
                        b85encode,
                        b85decode,
                        a85encode,
                        a85decode}]
                   [-o O] [-f] [-e E]
                   data

base16,base32,base64,base85加密、解密

positional arguments:
  data                  被处理数据

optional arguments:
  -h, --help            show this help message and exit
  -O                    {b16encode,
                        b16decode,
                        b32encode,
                        b32decode,
                        b64encode,
                        b64decode,
                        b85encode,
                        b85decode,
                        a85encode,
                        a85decode}
                        对输入数据的操作
  -o O                  输出文件名
  -f                    是否将输入解释为文件名
  -e E                  字符串编码(默认utf8)

test:
1 python3 mencrypt.py -f ./test/beauty.jpg -O b64encode -o ./test/beauty.txt
2 python3 mencrypt.py -f ./test/ascimg.txt -o ./test/ascimg.jpg
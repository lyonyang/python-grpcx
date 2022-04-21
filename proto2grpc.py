# coding=UTF-8
"""
Created on '2022/4/21'

@author: 'lyon'

$ python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. helloworld.proto

--python_out=. : 编译生成处理 protobuf 相关的代码的路径, 这里生成到当前目录
--grpc_python_out=. : 编译生成处理 grpc 相关的代码的路径, 这里生成到当前目录
-I. helloworld.proto : proto 文件的路径, 这里的 proto 文件在当前目录

"""
import os
import sys

SERVICE_PATH = os.path.realpath(os.path.dirname(__file__))

from grpc_tools import protoc

GRPC_PATH = 'app/grpc'
PROTO_PATH = 'app/proto'

if __name__ == '__main__':
    for proto in os.listdir(os.path.join(SERVICE_PATH, PROTO_PATH)):
        if proto.endswith('.proto'):
            proto_include = protoc.pkg_resources.resource_filename('grpc_tools', '_proto')
            protoc.main(
                ['-',
                 '--python_out=%s' % GRPC_PATH,
                 '--grpc_python_out=%s' % GRPC_PATH,
                 '-I%s' % PROTO_PATH, proto] + ['-I{}'.format(proto_include)])

    sys.exit()

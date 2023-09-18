# -*- coding: utf-8 -*-

# import hashlib
# import os
# import random
#
#
# def openfile():
#     global file_list
#     file_list = os.listdir(path)
#     print(file_list)
#
# def jionfile(file_name):
#     global file_path
#     file_path = os.path.join(path, file_name)
#     return file_path
#
# def get_file_md5():
#     global file_path  # 引用全局变量 file_path
#     hash_object = hashlib.md5()
#     try:
#         with open(file_path, 'rb') as f:
#             for chunk in iter(lambda: f.read(4096), b''):
#                 hash_object.update(chunk)
#     except PermissionError:
#         return None
#     file_hash = hash_object.hexdigest()
#     return file_hash
#
# path = r"C:\Users\21016.LAPTOP-KGP1GRG0\Desktop"
# openfile()
#
# hash_dict = {}
#
# for file_name in file_list:
#     file_path = jionfile(file_name)
#     hash_value = get_file_md5()
#     if hash_value:
#         print(f"文件哈希值（默认为 MD5）：{hash_value}")
#         if hash_value in hash_dict:
#             hash_dict[hash_value].append(file_path)
#         else:
#             hash_dict[hash_value] = [file_path]
#     else:
#         print("权限不足，跳过计算文件的哈希值")
#
# samehash = {}
#
# for hash_value, file_paths in hash_dict.items():
#     if len(file_paths) > 1:
#         print(f"哈希值相同的文件是:")
#         for file_path in file_paths:
#             print(file_path)
#         print(f"哈希值是:{hash_value}")
#         samehash[hash_value] = file_paths
#
# print(samehash)
#
# # file_delect = random.choices(samehash)
# # os.remove(file_delect)
# # print(f"删除文件：{file_delect}")
#
# if samehash:
#     hash_value = random.choice(list(samehash.keys()))
#     file_paths = samehash[hash_value]
#     file_to_delete = random.choice(file_paths)
#     os.remove(file_to_delete)
#     print(f"删除文件：{file_to_delete}")
# else:
#     print("没有找到具有相同哈希值的文件")

import hashlib
import os
import random


def openfile():
    global file_list
    file_list = list(os.walk(path))
    print(file_list)


def jionfile(file_name):
    global file_path
    file_path = os.path.join(file_name[0], file_name[2][0])
    return file_path


def get_file_md5():
    global file_path
    hash_object = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_object.update(chunk)
    except PermissionError:
        return None
    file_hash = hash_object.hexdigest()
    return file_hash


path = input("请输入路径:"r"")#r"C:\Users\21016.LAPTOP-KGP1GRG0\Desktop\1"
openfile()

hash_dict = {}

for dirpath, dirnames, filenames in file_list:
    for file_name in filenames:
        file_path = jionfile((dirpath, dirnames, [file_name]))
        hash_value = get_file_md5()
        if hash_value:
            print(f"文件哈希值（默认为 MD5）：{hash_value}")
            if hash_value in hash_dict:
                hash_dict[hash_value].append(file_path)
            else:
                hash_dict[hash_value] = [file_path]
        else:
            print("权限不足，跳过计算文件的哈希值")

samehash = {}

for hash_value, file_paths in hash_dict.items():
    if len(file_paths) > 1:
        print(f"哈希值相同的文件是:")
        for file_path in file_paths:
            print(file_path)
        print(f"哈希值是:{hash_value}")
        samehash[hash_value] = file_paths

# if samehash:
#     for hash_value, file_paths in samehash.items():
#         for file_path in file_paths:
#             file_to_delete = random.choice(file_paths)
#             os.remove(file_to_delete)
#             print(f"删除文件：{file_path}")
if samehash:
    for hash_value, file_paths in samehash.items():
        file_to_keep = file_paths[0]
        for file_path in file_paths[1:]:
            os.remove(file_path)
            print(f"删除文件: {file_path}")
            print(f"保留文件: {file_to_keep}")
else:
    print("没有找到具有相同哈希值的文件")

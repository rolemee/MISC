# for a in range(100000, 200000):

import zipfile
#
# def extractFile(zipFile, password):


def main():
  zipFile = zipfile.ZipFile('1.zip')
  PwdLists = open('2.txt')  #读入所有密码
  for line in PwdLists.readlines():  #挨个挨个的写入密码
    password = line.strip('\n')
    try:

      zipFile.extractall(pwd=bytes(password, "utf8"))
      print("破解成功" + password)  # 破解成功
      break
    except:
      print("密码错误"+line)
      pass  # 失败，就跳过

if __name__ == '__main__':
  main()

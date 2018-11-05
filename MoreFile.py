# author by LYS 2017/5/24
# for Deep Learning course
'''
1. read the whole files under a certain folder
2. chose 10000 files randomly
3. copy them to another folder and save
'''
import os, random, shutil


def copyFile(fileDir,tarDir):
    # 1
    pathDir = os.listdir(fileDir)

    # 2
    sample = random.sample(pathDir, 300)
    print (sample)

    # 3
    for name in sample:
        shutil.copyfile(fileDir + name, tarDir + name)


if __name__ == '__main__':
    for i in range(1, 10):
        fileDir = "C:\Sunaoxue\IT_Project/NSM/tuzhuang/ALL/" + str(i) +"/"
        tarDir = "C:\Sunaoxue\IT_Project/NSM/tuzhuang/Ver/" + str(i)+ "/"

        copyFile(fileDir,tarDir)
        i = i + 1

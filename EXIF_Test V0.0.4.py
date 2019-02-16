# -*- coding: utf-8 -*-
import os
import exiftool
import logging
import pdb
logging.basicConfig(level=logging.DEBUG)

#获取当前的绝对路径
def GetTheCurrentPath():
	TheCurrentPath = os.path.abspath('.')
	#logging.debug('当前路径为：%s' %TheCurrentPath)
    #傻屌函数，学好了再优化吧，脑子不行。
def SplitSuffix(a , b):
	return os.path.splitext(a)[1]== b
#获取当前绝对路径下的后缀为（）的名称
def GetAllSuffixThisPath():
	TheListOfsuffix = [x for x in os.listdir('.') if os.path.isfile(x) and (SplitSuffix(x , '.jpg') or SplitSuffix(x , '.DNG') or SplitSuffix(x , '.jpeg')) ]
	#logging.debug('当前目录后缀为文件名称：%s' %(TheListOfsuffix))
	#print(TheListOfsuffix)
	return TheListOfsuffix


#获取当前文件夹中，所有jpg和dng格式照片的gps信息,以及RTKFlag
def GetTheRTKflag():
	with exiftool.ExifTool() as et:
		RTKflag = et.get_tag_batch("xmp:RtkFlag",TheListOfsuffix)
	return RTKflag

def GetTheGPSLatitude():
	with exiftool.ExifTool() as et:
		GPSLatitude = et.get_tag_batch("GPS:GPSLatitude",TheListOfsuffix)
	return GPSLatitude

def GetTheGPSLongitude():
	with exiftool.ExifTool() as et:
		GPSLongitude = et.get_tag_batch("GPS:GPSLongitude",TheListOfsuffix)
	return GPSLongitude

def PrintListGpsInfo():
	for f in range(0,len(TheListOfsuffix)):		
		PrintGPSInfo = print(TheListOfsuffix[f],"[","%.8s"% GPSLatitude[f],"%.8s"% GPSLongitude[f],"]",RTKflag[f])

def CalculateRTKFlag():	
	RTKflag_number = 0
	for x in RTKflag:
		if x == 1:
			RTKflag_number = RTKflag_number + 1
	RTKflag_percent = (RTKflag_number / Photo_number) * 100
	print("共检查%.1f张照片" % Photo_number) 
	print("RtkFlag的百分比为%.2f" % RTKflag_percent)




if __name__ == '__main__':
	TheListOfsuffix = GetAllSuffixThisPath()
	RTKflag = GetTheRTKflag()
	GPSLatitude = GetTheGPSLatitude()
	GPSLongitude = GetTheGPSLongitude()
	PrintListGpsInfo()
	Photo_number = len(TheListOfsuffix)
	CalculateRTKFlag()























"""
#以下内容是V0.9.3版本的旧查看exif工具
# -*- coding: utf-8 -*-
import os
import exiftool
rootdir = r"D:\Python\EXIF查看RTKflag\test"   #想要查的照片放置在这个文件夹中。


'''想只需要把照片放到其中一个文件夹中，但是没有成功，后续再做尝试。'''
#exiftool.executable = 'D:/Python/EXIF查看RTKflag/exiftool'
#exiftool.ExifTool(executable_="D:/Python/EXIF查看RTKflag/exiftool")
list = os.listdir(rootdir)  #列出文件夹下所有的目录与文件
list.remove('exiftool.exe')   #在list中去除文件中'exiftool.exe', 'exiftool.py', 'EXIF_Test V0.9.3.py', '__pycache__'，以免这几个文件被查RTKFlag
list.remove('exiftool.py')    #代码有些恶心，以后学习多了再改。
list.remove('EXIF_Test V0.9.3.py')
list.remove('__pycache__')
list.remove('UI test1.py')

files = list
#print(list)   #调试用，查看文件名称是否获取准确


with exiftool.ExifTool() as et:
    RTKflag = et.get_tag_batch("xmp:RtkFlag",files)
with exiftool.ExifTool() as et:
    GPSLatitude = et.get_tag_batch("GPS:GPSLatitude",files)
with exiftool.ExifTool() as et:
    GPSLongitude = et.get_tag_batch("GPS:GPSLongitude",files)

for x in range(0,len(list)):
	#print(x)
	ycy = print(list[x],"[","%.8f"% GPSLatitude[x],"%.8f"% GPSLongitude[x],"]",RTKflag[x])
	#循环把名字list和经纬度list，一个一个print出来。
	#2018.12.29 加入RTKflag的打印



photo_number = len(RTKflag)
RTKflag_number = 0
for x in RTKflag:
	if x == 1:
		RTKflag_number = RTKflag_number + 1
	#return RTKflag_number
RTKflag_percent = (RTKflag_number / photo_number) * 100
#print(ycy)
print("共检查%.1f张照片" % photo_number) 
print("RtkFlag的百分比为%.2f" % RTKflag_percent)

"""

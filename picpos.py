import os
from PIL import Image
from PIL.ExifTags import TAGS
# 获取 JPEG 的 exif
def get_exif_data(fname):
    """Get embedded EXIF data from image file."""
    ret = {}
    try:
        img = Image.open(fname)
        if hasattr( img, '_getexif' ):
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
    except IOError:
        print ('IOERROR ' + fname)
    return ret


# 通过 JPEG 文件名获取 经纬度和高度 
## pfilename 有文件的完整路径


def getgpsinfo(pfilename):
    exif = get_exif_data(pfilename)
    try:
        gpsinfo = exif['GPSInfo']
        #维度
        latitude = gpsinfo[2][0][0]+gpsinfo[2][1][0]/60+gpsinfo[2][2][0]/gpsinfo[2][2][1]/3600
        #经度
        longitude = gpsinfo[4][0][0]+gpsinfo[4][1][0]/60+gpsinfo[4][2][0]/gpsinfo[4][2][1]/3600
        #高度
        altitude = gpsinfo[6][0]/gpsinfo[6][1]
    except:
        print("Error 没有GPS信息")
    return [latitude,longitude,altitude]

  

 
##返回指定目录下面的所有JPEG文件的列表
def JPEGlist(path):
    file_list=[]
    for file in os.listdir(path):
        if os.path.splitext(file)[-1] == ".JPG":
            file_list.append(file)
          
    return file_list
        
def getpos(path,outname,h1):
    """把pos数据写入 outname 文件.

    path 为路径
    h1 为高度偏移，可以为负数
    """
    outfile = open(os.path.join(path,outname), "w") 
    jpeglist = JPEGlist(path)
    for f1 in jpeglist:
        myfilename = os.path.join(path,f1)
        gps_info = getgpsinfo(myfilename)
        print("%s,%.7f,%.7f,%.2f" % (f1,gps_info[0],gps_info[1],gps_info[2]+h1),file=outfile)
    outfile.close()
    

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html
# export LD_LIBRARY_PATH=/home/ebapp/instantclient_21_3
#vim /etc/profile
# LD_LIBRARY_PATH=/home/ebapp/instantclient_21_3/:$LD_LIBRARY_PATH ，NLS_LANG=SIMPLIFIED CHINESE_CHINA.ZHS16GBK ,并添加到 ~/.bash_profile

#编写时间:2021/10/27 11:38
#作者:Zhangebapp
#说明:通过数据库进行文件夹创建,并复制相应的文件到刚创建的文件夹中,最后tar包.
#脚本执行周期 1次/月

######################1.获取系统时间函数##########################
def mytime(nowTime):
    import time
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return nowTime
def mytime2(nowTime):
    import time
    nowTime = time.strftime('%Y-%m-%d', time.localtime())
    return nowTime
############################2.输出日志###########################
def copyFileLog(logcontext):
    import time
    startTime = time.time()
    endTime = time.time()
    logfile=open('/jzjgbs/copyfile.log','a')
    logfile.write('\n'+logcontext)
    logfile.close()
###################3.链接数据库函数###################

def con_database(sql, result):
    import cx_Oracle as cx
    con = cx.connect('xtcrm', '1QaZ#eDc', '10.69.103.22:1521/jzdb')
    # con = cx.connect('xtcrm', 'abs', '10.69.101.170:1521/fmltdb')
    cursor = con.cursor()  # 创建游标
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchall()  # 获取一条数据
    cursor.close()  # 关闭游标
    con.close()  # 关闭数据库连接
    return result

####################4.创建文件夹函数###################
def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + '创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+"目录已存在")
        return False

####################5.复制文件夹函数#########################
# srcfile 需要复制、移动的文件
# dstpath 目的地址

# member = ['a','b','c','1','2',3]
# member1 = ['one','two','three']
# member.extend(member1)
# print(member)
# a='/home/ebapp/test/'
# b='/home/ebapp/test2/'
# c=['*.txt','*.pdf']
# copyFiles(a,b,c)

def copyFiles(startfolder,endfolder,fileType):
    filetypes=[]
    def mycopyfile(srcfile,dstpath):
        import os
        import shutil
        import time
        startTime = time.time()
        # srcfile = r'/home/ebapp/test/a.txt'
        # dstpath = r'/home/ebapp/test2/'
        if not os.path.isfile(srcfile):
            print("%s not exist!" % (srcfile))
        else:
            fpath, fname = os.path.split(srcfile)             # 分离文件名和路径
            if not os.path.exists(dstpath):
                os.makedirs(dstpath)                       # 创建路径
            shutil.copy(srcfile, dstpath + fname)    # 复制文件
            logcontext= "copy %s -> %s" % (srcfile, dstpath + fname)
            print(logcontext)
            copyFileLog(logcontext+'    '+mytime(nowTime=0))
        endTime = time.time()

    #要复制文件夹目录,所有文件
    src_dir = startfolder #'/home/ebapp/test/'
    dst_dir = endfolder #'/home/ebapp/test2/'                                    # 目的路径记得加斜杠
    # # glob获得路径下所有文件，可根据需要修改

    import glob
    fileType.extend(filetypes)
    newfilePath1=[]
    for i in range(len(fileType)):
        a=fileType[i]
        newfilePath = glob.glob(src_dir+a)
        newfilePath1.extend(newfilePath)
    # print(newfilePath1)

    for srcfile in newfilePath1:
        mycopyfile(srcfile, dst_dir)

##########################6.批量文件重命名########################
def renameFile(rename_filepath):
    import os
    # 列出当前目录(E:\Python\Code)下所有的文件
    files = os.listdir(rename_filepath)
    # 分离文件名字和后缀
    for filename in files:
        portion = os.path.splitext(filename)
        print(portion)
        # 根据后缀来修改
        # if portion[1] == ".pdf":
        #     newname = portion[0]+".htqzsm"
        #     # 切换文件路径
        #     os.chdir(rename_filepath)
        #     os.rename(filename, newname)
        newname = portion[0]+".pdf"
        os.chdir(rename_filepath)
        os.rename(filename, newname)

##########################7.函数调用##############################
import os 
import time
nowTime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime())

os.system("source /etc/profile")    #刷新linux系统环境变量
os.system("mv /jzjgbs/f财富管理总部.tar.xz /jzjgbs/f财富管理总部.tar.xz"+"_"+nowTime)

# 读取数据库
sql_fileFolderName = "SELECT FILEFODERNAME FROM (SELECT DISTINCT W.NOTE,TRIM(UPPER(TRIM(F.XMID_TA) || '-' || TRIM(W.NOTE))) FILEFODERNAME,M.CPMC FROM TFP_CPDM M , TXTDM W, TFP_XTJH F, THTXX Q   WHERE Q.HTQSRQ <= '20210930'   AND Q.HTZT =1  AND Q.CPID = M.ID   AND W.FLMC = '项目系列'AND W.IBM = M.XMXL AND F.ID = M.XTJH   AND M.XMXL IS NOT NULL AND W.NOTE IN ('光盈人生臻享','光盈人生鼎承','光耀世家·坤厚','光耀德合','融享人生','光盈人生')) WHERE NOTE IN ('光盈人生臻享','光盈人生鼎承','光耀世家·坤厚','光耀德合','融享人生')  OR (NOTE = '光盈人生' AND REGEXP_SUBSTR(CPMC, '[0-9]+') > 1000 )"
fileFolderName = con_database(sql_fileFolderName, result=0)
# 获取数组长度
y = len(fileFolderName)
times='2021-09-30'
end_filename='信托合同'
# 循环给变量复制,并获取数据库列名作为文件夹名称
for i in range(y):
    listFileFolderName = fileFolderName[i]

    # print(listFileFolderName)
    # 定义要创建的目录名称
    mkpath = r"/jzjgbs/f财富管理总部/"+times+'-信托业务'+'/'+'21-信信业务'+'/'+listFileFolderName[0]
    print(mkpath)
    logcontext=mkpath
    # 调用创建文件夹函数
    mkdir(mkpath)
    copyFileLog(logcontext+'    '+mytime(nowTime=0))

            ########################7.1复制主合同##########################
    #创建文件夹后,同时复制主合同文件
    sql_fileName = " SELECT id||'.HTQZSM'  FROM (SELECT *  FROM (SELECT DISTINCT W.NOTE,  TRIM(UPPER(TRIM(F.XMID_TA) || '-' ||  TRIM(W.NOTE))) FILEFODERNAME,  M.CPMC,  M.ID CPID,  Q.ID FROM TFP_CPDM M, TXTDM W, TFP_XTJH F, THTXX Q   WHERE Q.HTQSRQ <= '20210930'   AND Q.HTZT =1   AND Q.CPID = M.ID   AND W.FLMC = '项目系列'   AND W.IBM = M.XMXL   AND F.ID = M.XTJH   AND M.XMXL IS NOT NULL   AND W.NOTE IN ('光盈人生臻享', '光盈人生鼎承', '光耀世家·坤厚', '光耀德合', '融享人生', '光盈人生'))   WHERE NOTE IN ('光盈人生臻享',  '光盈人生鼎承',  '光耀世家·坤厚',  '光耀德合',  '融享人生') OR (NOTE = '光盈人生' AND REGEXP_SUBSTR(CPMC, '[0-9]+') > 1000)) WHERE FILEFODERNAME = "+"'"+listFileFolderName[0]+"'"
    # print(sql_fileName)
    fileName = con_database(sql_fileName, result=0)
    q=len(fileName)
    g=[]
    for j in range(q):
        listFileName = fileName[j]
        # 要把文件拷贝到的路径
        filepath = listFileName[0]
        g.append(filepath)
    print(g)
    e='/ApexSoft/tomcat_jzxt/data/app/THTXX/'#源文件目录
    f=mkpath+'/3-信托合同/'#目标文件夹
    print(f)
    copyFiles(e,f,g)
    mkdir(f)
    renameFile(f)


            ########################7.2复制明细合同##########################
    sql_fileName_mx=" SELECT mxid||'.DCHT'   FROM (SELECT *  FROM (SELECT DISTINCT W.NOTE, TRIM(UPPER(TRIM(F.XMID_TA) || '-' ||  TRIM(W.NOTE))) FILEFODERNAME, M.CPMC, M.ID CPID, Q.ID, h.id mxid   FROM TFP_CPDM M,  TXTDM  W,  TFP_XTJH F,  THTXX  Q,  TTZMX  H WHERE Q.HTQSRQ <= '20210930'  AND Q.HTZT =1  AND H.HKZT=2  and q.cpid=h.cpid  AND Q.CPID = M.ID  AND W.FLMC = '项目系列'  AND W.IBM = M.XMXL  AND F.ID = M.XTJH  AND M.XMXL IS NOT NULL  AND W.NOTE IN ('光盈人生臻享',  '光盈人生鼎承',  '光耀世家·坤厚',  '光耀德合',  '融享人生',  '光盈人生'))  WHERE NOTE IN ('光盈人生臻享',  '光盈人生鼎承',  '光耀世家·坤厚',  '光耀德合',  '融享人生') OR (NOTE = '光盈人生' AND  REGEXP_SUBSTR(CPMC, '[0-9]+') > 1000)) WHERE FILEFODERNAME = "+"'"+listFileFolderName[0]+"'"
    fileName_mx = con_database(sql_fileName_mx, result=0)
    p=len(fileName_mx)
    t=[]
    for j in range(p):
        listFileName_mx = fileName_mx[j]
        # 要把文件拷贝到的路径
        filepath_mx = listFileName_mx[0]
        t.append(filepath_mx)
    print(t)
    eu='/ApexSoft/tomcat_jzxt/data/app/TTZMX/'
    fy=mkpath+'/2-关联交易协议/'
    print(fy)
    mkdir(fy)
    copyFiles(eu,fy,t)
    renameFile(fy)

            ########################7.3复制财产权交易结构图#####################                                                                                                             #####
    ##查出目的文件夹
    sql_fileName_jgt=" SELECT mxid||'.DCHT'   FROM (SELECT *  FROM (SELECT DISTINCT W.NOTE, TRIM(UPPER(TRIM(F.XMID_TA) || '-' ||  TRIM(W.NOTE)))  FILEFODERNAME, M.CPMC, M.ID CPID, Q.ID, h.id mxid   FROM TFP_CPDM M,  TXTDM  W,  TFP_XTJH F,  THTXX  Q,  TTZMX  H WHERE Q.HTQSRQ <= '20210930'   and( h.ywly=2)   AND Q.HTZT =1  AND H.HKZT=2  and q.cpid=h.cpid  AND Q.CPID = M.ID  AND W.FLMC = '项目系列'  AND W.IBM = M.XMXL  AND F.ID = M.XTJH     AND M.XMXL IS NOT NULL  AND W.NOTE IN ('光盈人生臻享',  '光盈人生鼎承',  '光耀世家·坤厚',  '光耀德合',  '融享人生',  '光盈人生'))     WHERE NOTE IN ('光盈人生臻享',  '光盈人生鼎承',  '光耀世家·坤厚',  '光耀德合',  '融享人生') OR (NOTE = '光盈人生'  AND  REGEXP_SUBSTR(CPMC, '[0-9]+') > 1000)) WHERE FILEFODERNAME = "+"'"+listFileFolderName[0]+"'"
    fileName_jgt = con_database(sql_fileName_jgt, result=0)
    if len(fileName_jgt)!=0:
        print(fileName_jgt)
        zhuanrang='/home/ebapp/jiaoyijiegoutu/'#源文件夹
        mubiao=mkpath+'/1-穿透的交易架构图/'
        huf=['*转让*.*']
        copyFiles(zhuanrang,mubiao,huf)
    else:
        print(fileName_jgt)
        zhuanrang='/home/ebapp/jiaoyijiegoutu/'#源文件夹
        mubiao=mkpath+'/1-穿透的交易架构图/'
        huf=['*资金*.*']
        copyFiles(zhuanrang,mubiao,huf)

    #         ########################7.4复制关联交易涉及的有关审批文件##########################
    # sql_fileName_mx=" SELECT mxid||'.DCHT'   FROM (SELECT *  FROM (SELECT DISTINCT W.NOTE, TRIM(UPPER(TRIM(F.XMID_TA) || '-' ||  TRIM(W.NOTE))) FILEFODERNAME, M.CPMC, M.ID CPID, Q.ID, h.id mxid   FROM TFP_CPDM M,  TXTDM  W,  TFP_XTJH F,  THTXX  Q,  TTZMX  H WHERE Q.HTQSRQ <= '20210930'  AND Q.HTZT =1  AND H.HKZT=2  and q.cpid=h.cpid  AND Q.CPID = M.ID  AND W.FLMC = '项目系列'  AND W.IBM = M.XMXL  AND F.ID = M.XTJH  AND M.XMXL IS NOT NULL  AND W.NOTE IN ('光盈人生臻享',  '光盈人生鼎承',  '光耀世家·坤厚',  '光耀德合',  '融享人生',  '光盈人生'))  WHERE NOTE IN ('光盈人生臻享',  '光盈人生鼎承',  '光耀世家·坤厚',  '光耀德合',  '融享人生') OR (NOTE = '光盈人生' AND  REGEXP_SUBSTR(CPMC, '[0-9]+') > 1000)) WHERE FILEFODERNAME = "+"'"+listFileFolderName[0]+"'"
    # fileName_mx = con_database(sql_fileName_mx, result=0)
    # p=len(fileName_mx)
    # t=[]
    # for j in range(p):
    #     listFileName_mx = fileName_mx[j]
    #     # 要把文件拷贝到的路径
    #     filepath_mx = listFileName_mx[0]
    #     t.append(filepath_mx)
    # print(t)
    # eu='/ApexSoft/tomcat_jzxt/data/app/TTZMX/'
    # fy=mkpath+'/6-关联交易涉及的有关审批文件/'
    # print(fy)
    # mkdir(fy)
    # copyFiles(eu,fy,t)
    # renameFile(fy)

##########################################endfor.压缩整理的文件夹#########################
os.system("tar -Jvcf f财富管理总部.tar.xz  /jzjgbs/f财富管理总部/")
os.system("rm -rf /jzjgbs/f财富管理总部/")

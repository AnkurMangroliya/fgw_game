list = ["ankur","mangroliya","minali","vidisha","nirup"]
dic={"school":"pps","school1":"ppscvs","college":"gecr"}
def ank(normal,*ankurt,**ankf):
    print(normal)
    for item in ankurt:
        print(item)
    for key, value in ankf.items():
        print(key,value)
normal="this is python"
ank(normal,*list,**dic)

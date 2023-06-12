import atexit
from pyVmomi import vim, vmodl
from pyVim.connect import SmartConnectNoSSL, Disconnect

def run(host,user,pwd,port):
    try:
        si = SmartConnectNoSSL(host=host, user=user, pwd=pwd, port=port)
        atexit.register(Disconnect, si)
        content = si.RetrieveContent()
        print "Hellow World!"
    except vmodl.MethodFault as error:
        print "Caught vmodl fault : " + error.msg
        return False, error.msg
    return True, "ok"

if __name__ == "__main__":
    host = "vcenter.host"
    user = "administrator@vpshere.local"
    pwd = "password"
    port = 443

    print run(host,user,pwd,port)
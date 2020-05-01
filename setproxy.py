
import subprocess
import os
result=subprocess.check_output("wsl -- ifconfig eth0",universal_newlines=True)
IP=result.splitlines()[1].split(" netmask")[0].split("inet ")[1]

cmd="netsh interface portproxy add v4tov4 listenport=#SPORT# connectport=#DPORT# connectaddress=#DIP#"
os.system(cmd.replace("#SPORT#","445").replace("#DPORT#","445").replace("#DIP#",IP))
#os.system(cmd.replace("#PORT#","138").replace("#IP#",IP))
#os.system(cmd.replace("#PORT#","139").replace("#IP#",IP))
#os.system(cmd.replace("#PORT#","445").replace("#IP#",IP))
#os.system("wsl -- service smbd restart")
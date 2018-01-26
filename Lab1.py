"""
Question:
Pick one IP from each region, find network latency from via the below code snippet
(ping 3 times), and finally sort the average latency by region.
http://ec2-reachability.amazonaws.com/
Expected Output for all 15 regions:
1. us-west-1 [50.18.56.1] - 100ms (Smallest average latency)
2. xx-xxxx-x [xx.xx.xx.xx] - 200ms
3. xx-xxxx-x [xx.xx.xx.xx] - 300ms
...
15. xx-xxxx-x [xx.xx.xx.xx] - 1000ms (Largest average latency)
"""
from __future__ import print_function
import subprocess
import subprocess
from operator import itemgetter

ip = ["23.23.255.255","13.52.0.2,34.240.0.253","34.208.63.251","18.196.0.253","35.176.0.252","52.47.32.127","52.61.0.254","13.112.63.251","13.58.0.253","35.182.0.251","18.231.0.252","13.124.63.251","13.228.0.251","13.54.63.252","13.126.0.252","52.80.5.207","52.83.214.0"]
regions = ["us-east-1","us-west-1","eu-west-1","us-west-2","eu-central-1","eu-west-2","eu-west-3","us-gov-west-1","ap-northeast-1","us-east-2","ca-central-1","sa-east-1","ap-northeast-2","ap-southeast-1","ap-southeast-2","ap-south-1","cn-north-1","cn-northwest-1"]
latency = []
AWSregion = ["US EAST","US WEST","EU","Oregon","Frankfurt","London","Paris","GovCloud","Tokyo","Ohio","CANADA","SOUTH AMERICA","Seoul","Singapore","Sydney","Mumbai","CHINA","Ningxia"]
i = 0
for host in ip:
    ping = subprocess.Popen(
       ["ping", "-c", "3", host],
       stdout = subprocess.PIPE,
       stderr = subprocess.PIPE
    )
    out, error = ping.communicate()
    output = str(out).split("min/avg/max/stddev = ")
    if len(output) > 1:
        latency.append((float(output[1].split("/")[1]), host, regions[i], AWSregion[i]))
    else:
        latency.append((None, host, regions[i], AWSregion[i]))
    i+=1

latency.sort(key=itemgetter(0))

for results in latency:
    print(results[2] + "\t\t\t"+ results[3] + "\t\t"+ results[1] + "\t\t\t\t" + str(results[0]))
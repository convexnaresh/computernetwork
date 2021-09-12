
#Disclaimer: This program code is written or adapted or imported from different sources for education purpose only. 
#Usage of this code for any 
#other purpose beyond education is not permitted. 
#The author pays due credit to the source or original author(s), without explicitly taking their names.

import dns
import dns.resolver




result = dns.resolver.resolve('google.com', 'A')
for cnameval in result:
    print ("ip addr:", cnameval.to_text())

print("\n")

result = dns.resolver.resolve('mail.google.com', 'CNAME')
for cnameval in result:
    print ("cname target address:", cnameval.target)

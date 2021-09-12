#!./env/bin/python



#Disclaimer: This program code is written or adapted or imported from different sources for education purpose only. 
#Usage of this code for any 
#other purpose beyond education is not permitted. 
#The author pays due credit to the source or original author(s), without explicitly taking their names.
#https://www.tutorialspoint.com/python_network_programming/python_dns_look_up.htm
#sudo pip install dnspython

#Or download the source install it via:

#sudo python setup.py install

#Your code would be something like this:

from dns import resolver

res = resolver.Resolver()
res.nameservers = ['8.8.8.8']

answers = res.query('stackexchange.com')

for rdata in answers:
    print (rdata.address)


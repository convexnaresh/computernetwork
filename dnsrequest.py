import dns
import dns.resolver




result = dns.resolver.resolve('google.com', 'A')
for cnameval in result:
    print ("ip addr:", cnameval.to_text())

print("\n")

result = dns.resolver.resolve('mail.google.com', 'CNAME')
for cnameval in result:
    print ("cname target address:", cnameval.target)

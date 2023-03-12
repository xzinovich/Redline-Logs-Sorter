import re

logfile = open('access.log', 'r')
logtext = logfile.read()

ipregex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
match = re.findall(ipregex, logtext, re.MULTILINE)

ip_dict = {}
for ip in match:
    ip_parts = ip.split('.')
    country_code = ip_parts[0]
    if country_code not in ip_dict:
        ip_dict[country_code] = []
    ip_dict[country_code].append(ip)

for country_code, ip_list in ip_dict.items():
    filename = country_code + '.log'
    with open(filename, 'w') as f:
        f.write('\n'.join(ip_list))

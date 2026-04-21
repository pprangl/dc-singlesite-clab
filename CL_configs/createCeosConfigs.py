import yaml

data = dict()
serialnumber = 'HBG251009'
systemmacaddr = 'b8:a1:b8:ce:85:'

with open('../topology.clab.yml', 'r') as input:
    data = yaml.load(input, Loader=yaml.SafeLoader)

for item, value in data['topology']['nodes'].items():
    if 'arista' in value['group']:
        print(item)
        mac = str(hex(int(value['mgmt-ipv4'].split('.')[3]))).replace('0x', '')
        
        data = "SERIALNUMBER=" + serialnumber + mac.rjust(2, '0').upper() + "\n" + "SYSTEMMACADDR=" + systemmacaddr + mac.rjust(2, '0')
        with open(str(item) + "_ceos_config", "w") as f:
            f.writelines(data)
            f.close()
import re

in_data = []
out_data = []
my_file = open("access.log")

in_data = my_file.readlines()
my_file.close()

for count, x in enumerate(in_data):
    if x.find("BotPoke") < 0:
        out_data.append(x)

out_file = open("parsed_access.log","w")
out_file.writelines(out_data)
out_file.close()

log_entries = len(out_data)

print("Number of remaining log entries:", log_entries)


ip_finder = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}")
ip_address_set = set()
for x in out_data:
    result = re.match(ip_finder, x)
    if result:
        ip_address_set.add(result[0])

print("Remaining unique ip addresses:", ip_address_set)
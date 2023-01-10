#MODEL DRIVEN PROGRAMMABILITY
from ncclient import manager

nexus = manager.connect(
    host='sandbox-iosxe-latest-1.cisco.com',
    username='developer',
    password='C1sco12345',
    allow_agent=False,
    look_for_keys=False,
    hostkey_verify=False,
    unknown_host_cb=True)

for capability in nexus.server_capabilities:
    print(capability)
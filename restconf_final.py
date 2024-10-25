import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.181-184
api_url = "https://10.0.15.183/restconf"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {"Accept": "application/yang-data+json","Content-Type": "application/yang-data+json"}
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "loopback65070141",
            "description": "created loopback by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.30.141.1",
                        "netmask": "255.255.255.255"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    } # Add 

    resp = requests.put(
        api_url + "/data/ietf-interfaces:interfaces/interface=loopback65070141", 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070141 is created successfully"
    else:
        print("Cannot create: Interface loopback 65070141")


def delete():
    resp = requests.delete(
        api_url + "/data/ietf-interfaces:interfaces/interface=loopback65070141", 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070141 is deleted successfully"
    else:
        print("Cannot delete: Interface loopback 65070141")


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "loopback65070141",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
        } # Add
    }

    resp = requests.patch(
        api_url + "/data/ietf-interfaces:interfaces/interface=loopback65070141", 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070141 is enabled successfully"
    else:
        print("Cannot enable: Interface loopback 65070141")


def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "loopback65070141",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False,
        } # Add
    }

    resp = requests.patch(
        api_url + "/data/ietf-interfaces:interfaces/interface=loopback65070141", 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070141 is disable successfully"
    else:
        print("Cannot enable: Interface loopback 65070141")


def status():
    api_url_status = "https://10.0.15.183/restconf/data/ietf-interfaces:interfaces-state/interface=loopback65070141"

    resp = requests.get(
        api_url_status, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = response_json["ietf-interfaces:interface"]["admin-status"]
        oper_status = response_json["ietf-interfaces:interface"]["oper-status"]
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback 65070141 is enabled"
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface loopback 65070141 is disable"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "Not Found 65070141 JA"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))

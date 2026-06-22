<h1 align="center">
  <img src="https://github.com/daemoncibsec/mcpExec/blob/main/mcpexec-logo.png" alt="crtfindr" width="1000px">
  <br>
</h1>

mcpExec is a tool that takes advantage of the CVE-2026-23744 to gather a reverse shell using the URL of the vulnerable MCPJam Inspector installation.

## Installation

```bash
git clone https://github.com/daemoncibsec/mcpExec.git
pip install rich
pip install argparse
pip install requests
cd mcpExec
chmod +x mcpExec.py
```

## Usage/Examples

```bash
./mcpExec.py http://localhost:6274
```

## Authors

- [@daemoncibsec](https://www.github.com/daemoncibsec)

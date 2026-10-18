import json

# This reads a list of IPs from the log files.

# Set to the log file to read
# This should match what this variable is using in the Caddyfile.
# You can view the logs for the IPs that have hit this Caddy instance.

# import subdomain-log download.example.com
logfile = "../logs/download.example.com.log"
# This disables displaying the IPs if they are duplicates.
unique = True

seen = set()
with open(logfile, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        # nested keys safe-get
        client_ip = None
        req = obj.get("request") if isinstance(obj, dict) else None
        if isinstance(req, dict):
            client_ip = req.get("client_ip")
        if client_ip:
            if unique:
                if client_ip not in seen:
                    print(client_ip)
                    seen.add(client_ip)
            else:
                print(client_ip)
import subprocess

# Fonction pour exécuter une commande en utilisant subprocess
def run_command(command):
    subprocess.run(command, shell=True, check=true)

# Désactiver toutes les connexions entrantes
run_command("netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound")

# Autoriser les connexions sortantes
run_command("netsh advfirewall set allprofiles firewallpolicy allowoutbound")

# Autoriser le trafic HTTP entrant
run_command("netsh advfirewall firewall add rule name=\"HTTP (TCP-In)\" protocol=TCP localport=80 action=allow dir=in")

# Autoriser le trafic HTTPS entrant
run_command("netsh advfirewall firewall add rule name=\"HTTPS (TCP-In)\" protocol=TCP localport=443 action=allow dir=in")

# Autoriser le trafic DNS entrant
run_command("netsh advfirewall firewall add rule name=\"DNS (UDP-In)\" protocol=UDP localport=53 action=allow dir=in")

# Autoriser le trafic FTP entrant
run_command("netsh advfirewall firewall add rule name=\"FTP (TCP-In)\" protocol=TCP localport=21 action=allow dir=in")

# Autoriser le trafic RDP entrant
run_command("netsh advfirewall firewall add rule name=\"RDP (TCP-In)\" protocol=TCP localport=3389 action=allow dir=in")

# Autoriser le trafic ICMP entrant (ping)
run_command("netsh advfirewall firewall add rule name=\"ICMPv4-In\" protocol=icmpv4:any,any action=allow dir=in")

print("Les règles du pare-feu ont été configurées avec succès.")


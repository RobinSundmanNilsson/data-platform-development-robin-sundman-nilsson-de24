# 3. Extract data from logs

# In data engineering, log files and log messages are very common. 
# Sometimes you need to parse them to find valuable information, 
# for example for debugging reasons.

# Read in network.log and extract source IP, destination IP, protocol and data size.

# Expected output:

# Source: 10.0.0.1 | Destination: 10.0.0.2 | Protocol: TCP | Bytes: 1024
# Source: 10.0.0.2 | Destination: 10.0.0.3 | Protocol: UDP | Bytes: 2048
# Source: 10.0.0.3 | Destination: 10.0.0.1 | Protocol: TCP | Bytes: 512

# Data Transfer Summary:
# TCP: 1536 bytes
# UDP: 2048 bytes

# Hint: you could probably find some complex regexp pattern, 
# but a more strategic approach is to check the formatting and make a strategy based on that.

def extract_log_data(log_filename):
    # En ordbok för att summera byte-data per protokoll
    protocol_summary = {
        "TCP": 0,
        "UDP": 0
    }

    # Öppna loggfilen och läsa rad för rad
    with open(log_filename, 'r') as file:
        for line in file:
            # Dela upp raden i olika delar baserat på '|' symbolen, bortse från tidsstämpeln
            parts = line.split('|')

            # Vi går direkt till käll-IP, destinations-IP, protokoll och bytes efter tidsstämpeln
            try:
                source_ip = parts[1].split(':')[1].strip()
                destination_ip = parts[2].split(':')[1].strip()
                protocol = parts[3].split(':')[1].strip()
                bytes = int(parts[4].split(':')[1].strip())
            except IndexError:
                print(f"Felaktig radformat: {line.strip()}")
                continue
            except ValueError:
                print(f"Felaktig datastorlek på rad: {line.strip()}")
                continue

            # Skriv ut informationen i önskat format
            print("-"*75)
            print(f"Source: {source_ip} | Destination: {destination_ip} | Protocol: {protocol} | Bytes: {bytes}")
            
            # Summera datastorlek per protokoll
            if protocol in protocol_summary:
                protocol_summary[protocol] += bytes

    # Skriv ut sammanfattningen
    print("\nData Transfer Summary:")
    for protocol, total_bytes in protocol_summary.items():
        print(f"{protocol}: {total_bytes} bytes")
        print("-"*75)

# Uppdaterad filväg för att läsa från 'data' mappen i 'exercises'
extract_log_data('/Users/kidquatro/Documents/STI-DE24/Data Platform Development/data-platform-development-robin-sundman-nilsson-de24/exercises/data/network.log')
def analyze_trace_file(filename):
    sent_packets = 0
    received_packets = 0
    lost_packets = 0
    total_delay = 0.0
    pkt_size = 0  
    time = 0.0  
    with open(filename, 'r') as f:
        for line in f:
            tokens = line.split()
            event_type = tokens[0]
            
            if event_type in ['+', 'r']:
                time = float(tokens[1])  
                pkt_size = int(tokens[5]) 
            from_node = tokens[2]
            to_node = tokens[3]

            if event_type == "+":
                sent_packets += 1
            elif event_type == "r":
                received_packets += 1
                total_delay += time
                
    lost_packets = sent_packets - received_packets

    packet_loss_rate = (lost_packets / sent_packets) * 100 if sent_packets > 0 else 0
    throughput = (received_packets * pkt_size * 8) / time if time > 0 else 0  # in bits/sec
    average_delay = total_delay / received_packets if received_packets > 0 else 0  # in seconds

    print(f"=== Analysis for {filename} ===")
    print(f"Packet Loss Rate: {packet_loss_rate}%")
    print(f"Throughput: {throughput} bits/sec")
    print(f"Average End-to-End Delay: {average_delay} seconds")

analyze_trace_file("vegas.tr")

# Analyze the tahoe.tr file
analyze_trace_file("reno.tr")

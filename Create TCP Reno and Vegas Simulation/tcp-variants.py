def analyze_trace_file(filename):
    sent_packets = 0
    received_packets = 0
    lost_packets = 0
    total_delay = 0.0
    pkt_size = 0  # Initialize to default value
    time = 0.0  # Initialize to default value
    
    with open(filename, 'r') as f:
        for line in f:
            tokens = line.split()
            event_type = tokens[0]
            
            # Update time and pkt_size only if the event_type is either "+" or "r"
            if event_type in ['+', 'r']:
                time = float(tokens[1])  # Update time for each line
                pkt_size = int(tokens[5])  # Update pkt_size for each line

            from_node = tokens[2]
            to_node = tokens[3]

            if event_type == "+":
                sent_packets += 1
            elif event_type == "r":
                received_packets += 1
                total_delay += time
                
    lost_packets = sent_packets - received_packets

    # Metrics
    packet_loss_rate = (lost_packets / sent_packets) * 100 if sent_packets > 0 else 0
    throughput = (received_packets * pkt_size * 8) / time if time > 0 else 0  # in bits/sec
    average_delay = total_delay / received_packets if received_packets > 0 else 0  # in seconds

    print(f"=== Analysis for {filename} ===")
    print(f"Packet Loss Rate: {packet_loss_rate}%")
    print(f"Throughput: {throughput} bits/sec")
    print(f"Average End-to-End Delay: {average_delay} seconds")

# Analyze the vegas.tr file
analyze_trace_file("vegas.tr")

# Analyze the tahoe.tr file
analyze_trace_file("reno.tr")

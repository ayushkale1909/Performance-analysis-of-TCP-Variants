def analyze_trace_file(filename):
    sent_packets = 0
    received_packets = 0
    lost_packets = 0
    total_delay = 0.0

    with open(filename, 'r') as f:
        for line in f:
            tokens = line.split()
            event_type = tokens[0]
            time = float(tokens[1])
            pkt_type = tokens[4]
            pkt_size = int(tokens[5])
            from_node = tokens[2]
            to_node = tokens[3]

            # Count sent, received, and lost packets
            if event_type == "+":
                sent_packets += 1
            elif event_type == "r":
                received_packets += 1
                total_delay += time  # This is a simplification; normally you'd match the sent and received packets
            
            # You may also add other conditions to filter by packet type, nodes, etc.
    lost_packets = sent_packets - received_packets

    # Calculate metrics
    packet_loss_rate = (lost_packets / sent_packets) * 100 if sent_packets > 0 else 0
    throughput = (received_packets * pkt_size * 8) / time  # in bits/sec
    average_delay = total_delay / received_packets if received_packets > 0 else 0  # in seconds

    print(f"Packet Loss Rate: {packet_loss_rate}%")
    print(f"Throughput: {throughput} bits/sec")
    print(f"Average End-to-End Delay: {average_delay} seconds")

# Usage
analyze_trace_file("tcp-example2.tr")

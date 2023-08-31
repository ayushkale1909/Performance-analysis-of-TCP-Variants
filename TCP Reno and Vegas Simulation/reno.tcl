# Create a new simulator object
set ns [new Simulator]
set tracefile [open "reno.tr" w]
$ns trace-all $tracefile

# Create nodes
set n0 [$ns node]
set n1 [$ns node]

# Create a TCP agent and attach it to node n0
set tcp [new Agent/TCP/Reno]
$ns attach-agent $n0 $tcp

# Create a TCP sink and attach it to node n1
set sink [new Agent/TCPSink]
$ns attach-agent $n1 $sink

# Connect the TCP agent to the sink
$ns connect $tcp $sink

# Create a FTP application over TCP
set ftp [new Application/FTP]
$ftp attach-agent $tcp

# Set up link with a bandwidth of 1Mb and a delay of 10ms
$ns duplex-link $n0 $n1 1Mb 10ms DropTail

# Schedule events
$ns at 1.0 "$ftp start"
$ns at 5.0 "$ftp stop"

# Run simulation
$ns at 5.5 "finish"
proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    puts "Simulation complete. Trace file is sample.tr"
    exit 0
}
$ns run

# Initialize 
set ns [new Simulator]

# Create trace file
set tracefile [open "tcp-example2.tr" w]
$ns trace-all $tracefile

set n0 [$ns node]
set n1 [$ns node]
$ns duplex-link $n0 $n1 1Mb 10ms DropTail

set tcp [new Agent/TCP]
$tcp set class_ 2
$ns attach-agent $n0 $tcp

# TCP sink attached to node n1
set sink [new Agent/TCPSink]
$ns attach-agent $n1 $sink

$ns connect $tcp $sink

# FTP application over TCP
set ftp [new Application/FTP]
$ftp attach-agent $tcp

# FTP application Start and Stop Times 
$ns at 1.0 "$ftp start"
$ns at 5.0 "$ftp stop"

proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    puts "Simulation Completed."
    exit 0
}

$ns at 5.5 "finish"

# Run 
$ns run

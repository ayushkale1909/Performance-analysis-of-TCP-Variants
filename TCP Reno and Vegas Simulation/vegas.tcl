set ns [new Simulator]
set tracefile [open "vegas.tr" w]
$ns trace-all $tracefile

set n0 [$ns node]
set n1 [$ns node]

set tcp [new Agent/TCP/Vegas]
$ns attach-agent $n0 $tcp

set sink [new Agent/TCPSink]
$ns attach-agent $n1 $sink

$ns connect $tcp $sink

set ftp [new Application/FTP]
$ftp attach-agent $tcp

$ns duplex-link $n0 $n1 1Mb 10ms DropTail

$ns at 1.0 "$ftp start"
$ns at 5.0 "$ftp stop"


$ns at 5.5 "finish"
proc finish {} {
    global ns tracefile
    $ns flush-trace
    close $tracefile
    puts "Simulation complete. Trace file is vegas.tr"
    exit 0
}
$ns run

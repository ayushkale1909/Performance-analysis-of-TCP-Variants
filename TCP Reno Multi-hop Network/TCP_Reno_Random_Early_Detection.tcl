set ns [new Simulator]
set tracefile [open "wired_multihop_red.tr" w]
set namfile [open "wired_multihop_red.nam" w]

$ns trace-all $tracefile
$ns namtrace-all $namfile

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]

$ns duplex-link $n0 $n1 1Mb 10ms RED
$ns duplex-link $n1 $n2 1Mb 10ms RED
$ns duplex-link $n2 $n3 1Mb 10ms RED
$ns duplex-link $n3 $n4 1Mb 10ms RED

set tcp0 [new Agent/TCP/Reno]
set sink0 [new Agent/TCPSink]
$ns attach-agent $n0 $tcp0
$ns attach-agent $n1 $sink0
$ns connect $tcp0 $sink0

set tcp1 [new Agent/TCP/Reno]
set sink1 [new Agent/TCPSink]
$ns attach-agent $n1 $tcp1
$ns attach-agent $n2 $sink1
$ns connect $tcp1 $sink1

set tcp2 [new Agent/TCP/Reno]
set sink2 [new Agent/TCPSink]
$ns attach-agent $n2 $tcp2
$ns attach-agent $n3 $sink2
$ns connect $tcp2 $sink2

set tcp3 [new Agent/TCP/Reno]
set sink3 [new Agent/TCPSink]
$ns attach-agent $n3 $tcp3
$ns attach-agent $n4 $sink3
$ns connect $tcp3 $sink3

set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0
$ns at 0.5 "$ftp0 start"

set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ns at 0.5 "$ftp1 start"

set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2
$ns at 0.5 "$ftp2 start"

set ftp3 [new Application/FTP]
$ftp3 attach-agent $tcp3
$ns at 0.5 "$ftp3 start"

$ns at 20.0 "stop"
$ns at 20.1 "puts \"NS Exit\"; $ns halt"

proc stop {} {
    global ns tracefile namfile
    $ns flush-trace
    close $tracefile
    close $namfile
}

$ns run

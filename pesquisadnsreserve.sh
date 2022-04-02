for ip in $(seq 1 255);do host $1.$ip;done | grep -v "NXDOMAIN"

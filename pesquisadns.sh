#!/bin/bash
for palavra in $(cat /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt);do host $palavra.$1;done | grep -v "NXDOMAIN" 

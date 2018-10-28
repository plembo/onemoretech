#!/bin/bash
# Script: my-pi-temp.sh
# Purpose: Display the ARM CPU temperature of Raspberry Pi Zero 
# Author: Vivek Gite <www.cyberciti.biz> under GPL v2.x+
# -------------------------------------------------------
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo "CPU => $((cpu/1000))'C"


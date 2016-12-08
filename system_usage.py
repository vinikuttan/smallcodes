# !/usr/bin/python

## import statements
import os
import psutil

def return_os_type():
    """os type"""
    os_type = os.uname()[0]

    if os_type == "nt":
        return "Windows"
    return os_type


def cpu_usage():
    """return cpu usage"""
    # interval param should have least value which informs
    # system to fetch cpu usage from last interval period
    return psutil.cpu_percent(interval=0.1)


def print_sys_mem_info(obj):
    """
    print system memory informations
    """
    for mem_field in obj._fields:
        value = getattr(obj, mem_field)
        if mem_field != 'percent':
            value = str(value/1024/1024)+ " MB"

        print "%-10s %s"%(mem_field, value)

if __name__=="__main__":
    print "OS TYPE \n------"
    print return_os_type()

    print "\nCPU USAGE \n-----"
    print cpu_usage()

    print "\nMEMORY \n--------"
    print_sys_mem_info(psutil.virtual_memory())

    print "\nSWAP \n----------"
    print_sys_mem_info(psutil.swap_memory())

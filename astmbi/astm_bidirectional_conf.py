#!/usr/bin/python3
astm_log_filename='/var/log/vitros_read.log'
file2mysql_log_filename='/var/log/vitros_write.log'
#if you wish to be specific
#host_address='12.207.3.240'
#host_address='11.207.1.1'
#if you wish general declaration
host_address='127.0.0.1'
host_port='8081'
select_timeout=1
alarm_time=10
#trailing slash is must to reconstruct path
inbox_data='/mnt/c/Users/betti/Projects/astmbi/inbox'
inbox_arch='/mnt/c/Users/betti/Projects/astmbi/inbox/arch'
outbox_data='/mnt/c/Users/betti/Projects/astmbi'
outbox_arch='/mnt/c/Users/betti/Projects/astmbi/outbox/arch'
equipment='VITROS3600'

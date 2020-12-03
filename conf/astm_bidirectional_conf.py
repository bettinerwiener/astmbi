#!/usr/bin/python3
astm_log_filename='/var/log/astmbi_read.log'
file2mysql_log_filename='/var/log/astmbi_write.log'
#if you wish to be specific
#host_address='12.207.3.240'
#host_address='11.207.1.1'
#if you wish general declaration
host_address=''
host_port='2577'
select_timeout=1
alarm_time=10
#trailing slash is must to reconstruct path
inbox_data='/root/astmbi.inbox.data/'
inbox_arch='/root/astmbi.inbox.arch/'
outbox_data='/root/astmbi.outbox.data/'
outbox_arch='/root/astmbi.outbox.arch/'
equipment='ANY_EQUIPMENT'

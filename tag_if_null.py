from __future__ import print_function
import logging
import json
import ipaddress
import boto3

def name_me(event, context):
  ec2 = boto3.client('ec2')
  boto_response = ec2.describe_instances()
  for reservation in boto_response['Reservations']:
    for instance in reservation['Instances']:
#       Excludes terminated instances from the list.
        if instance['State']['Name'] != 'terminated':
          if 'PrivateIpAddress' in instance.keys():
#           Finds if the ip is in the CIDR
            if ipaddress.ip_address(unicode(instance['PrivateIpAddress'])) in ipaddress.ip_network(unicode('10.10.0.0/24')):
               if 'Tags' in instance.keys():
#                  Finds the value of the tag.               
                 if instance['Tags'][0]['Value'] == "":
#                    Applies the tagname.
                    ec2.create_tags(Resources=[(instance['InstanceId'])], Tags=[{'Key': 'Name', 'Value': 'NGAP'}])
                 else:
                   print (instance['InstanceId'])
               else:
                   print ("Key called 'Tags' not present")
#           Finds if the ip is in the CIDR
            elif ipaddress.ip_address(unicode(instance['PrivateIpAddress'])) in ipaddress.ip_network(unicode('10.10.1.0/24')):
               if 'Tags' in instance.keys():
#                  Finds the value of the tag.
                   if instance['Tags'][0]['Value'] == '':
#                    Applies the tagname.
                     ec2.create_tags(Resources=[(instance['InstanceId'])], Tags=[{'Key': 'Name', 'Value': 'NGAP'}])
                   else:
                     print (instance['InstanceId'])
               else:
                 print ('Not Null')
          else:
             print('Not Ngap')

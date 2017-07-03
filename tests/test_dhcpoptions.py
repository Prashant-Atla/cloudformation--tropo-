#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.dhoption = {'Type': 'AWS::EC2::DHCPOptions',
                         'Properties': {'Tags': [{'Value': 'ApiDev',
                                                  'Key': 'Environment'},
                                                 {'Value': 'ApiDev-Dev-DhcpOptions',
                                                  'Key': 'Name'},
                                                 {'Value': 'Foo industries',
                                                  'Key': 'Owner'},
                                                 {'Value': 'ServiceVPC',
                                                  'Key': 'Service'},
                                                 {'Value': 'Dev',
                                                  'Key': 'VPC'}],
                                        'DomainNameServers': ['AmazonProvidedDNS'],
                                        'DomainName': {"Fn::Join": ["",
                                                                    [{'Ref': "AWS::Region"},
                                                                     ".compute.internal"]]}}}

    def test_create_Dhcp_options(self):
        print(self.cloudformation.vpc.dhcp_options.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.dhcp_options.to_dict(),
            self.dhoption)


if __name__ == '__main__':
    unittest.main()

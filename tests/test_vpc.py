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

        self.vpc1 = {'Type': 'AWS::EC2::VPC',
                     'Properties': {'InstanceTenancy': "default",
                                    'EnableDnsSupport': "true",
                                    'CidrBlock': "10.0.0.0/16",
                                    'EnableDnsHostnames': "true",
                                    'Tags': [{'Value': 'ApiDev',
                                              'Key': 'Environment'},
                                             {'Value': 'ApiDev-Dev-ServiceVPC',
                                              'Key': 'Name'},
                                             {'Value': 'Foo industries',
                                              'Key': 'Owner'},
                                             {'Value': 'ServiceVPC',
                                              'Key': 'Service'},
                                             {'Value': 'Dev',
                                              'Key': 'VPC'}]}}

    def test_create_vpc1(self):
        print(self.cloudformation.vpc.vpc.to_dict())
        self.assertDictEqual(self.cloudformation.vpc.vpc.to_dict(), self.vpc1)


if __name__ == '__main__':
    unittest.main()

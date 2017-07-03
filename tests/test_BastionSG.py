#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.securityGroup = {
            'Type': 'AWS::EC2::SecurityGroup', 'Properties': {
                'VpcId': {
                    'Ref': 'VPC'}, 'Tags': [
                    {
                        'Value': 'ApiDev', 'Key': 'Environment'}, {
                        'Value': 'ApiDev-Dev-VPC-Bastion-SG', 'Key': 'Name'}, {
                            'Value': 'Foo industries', 'Key': 'Owner'}, {
                                'Value': 'ServiceVPC', 'Key': 'Service'}, {
                                    'Value': 'Dev', 'Key': 'VPC'}], 'GroupDescription': 'Used for source/dest rules'}}

    def test_create_bsg(self):
        print(self.cloudformation.vpc.Bsg.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.Bsg.to_dict(),
            self.securityGroup)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.vpcacl = {
            'Type': 'AWS::EC2::NetworkAcl', 'Properties': {
                'VpcId': {
                    'Ref': 'VPC'}, 'Tags': [
                    {
                        'Value': 'ApiDev', 'Key': 'Environment'}, {
                        'Value': 'ApiDev-Dev-NetworkAcl', 'Key': 'Name'}, {
                            'Value': 'Foo industries', 'Key': 'Owner'}, {
                                'Value': 'ServiceVPC', 'Key': 'Service'}, {
                                    'Value': 'Dev', 'Key': 'VPC'}]}}

    def test_create_network_Acl(self):
        print(self.cloudformation.vpc.vpcnetworkacl.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.vpcnetworkacl.to_dict(),
            self.vpcacl)


if __name__ == '__main__':
    unittest.main()

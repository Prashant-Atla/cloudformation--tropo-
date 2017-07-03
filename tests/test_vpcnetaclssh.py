#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.vpcnwaclssh = {
            'Type': 'AWS::EC2::NetworkAclEntry',
            'Properties': {
                'NetworkAclId': {
                    'Ref': 'VpcNetworkAcl'},
                "RuleNumber": 10000,
                "Protocol": "6",
                "PortRange": {
                    "To": "22",
                    "From": "22"},
                "Egress": "false",
                "RuleAction": "allow",
                "CidrBlock": "127.0.0.1/32"}}

    def test_create_vpcnetworkaclssh(self):
        print(self.cloudformation.vpc.vpcnetworkaclssh.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.vpcnetworkaclssh.to_dict(),
            self.vpcnwaclssh)


if __name__ == '__main__':
    unittest.main()

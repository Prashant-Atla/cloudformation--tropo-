#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.vpcnetworkaclinboundrulepublic_80 = {
            'Type': 'AWS::EC2::NetworkAclEntry',
            'Properties': {
                'NetworkAclId': {
                    'Ref': 'VpcNetworkAcl'},
                "RuleNumber": 20000,
                "Protocol": "6",
                "PortRange": {
                    "To": "80",
                    "From": "80"},
                "Egress": "false",
                "RuleAction": "allow",
                "CidrBlock": "0.0.0.0/0"}}

    def test_create_vpcnetworkaclinboundrulepublic_80(self):
        print(self.cloudformation.vpc.vpcnetworkaclinboundpublic80.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.vpcnetworkaclinboundpublic80.to_dict(),
            self.vpcnetworkaclinboundrulepublic_80)


if __name__ == '__main__':
    unittest.main()

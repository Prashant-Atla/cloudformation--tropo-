#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.vpcnetworkinboundpubl443 = {
            'Type': 'AWS::EC2::NetworkAclEntry',
            'Properties': {
                'NetworkAclId': {
                    'Ref': 'VpcNetworkAcl'},
                'RuleNumber': 20001,
                'Protocol': '6',
                'PortRange': {
                    "To": "443",
                    "From": "443"},
                "Egress": "false",
                "RuleAction": "allow",
                "CidrBlock": "0.0.0.0/0"}}

    def test_create_vpcnetworkaclinboundrulepublic443(self):
        print(self.cloudformation.vpc.vpcnetworkaclinboundrulepublic443.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.vpcnetworkaclinboundrulepublic443.to_dict(),
            self.vpcnetworkinboundpubl443)


if __name__ == '__main__':
    unittest.main()

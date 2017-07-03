#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.netvpcoutr = {
            'Type': 'AWS::EC2::NetworkAclEntry',
            'Properties': {
                'NetworkAclId': {
                    'Ref': 'VpcNetworkAcl'},
                'RuleNumber': 30000,
                'Protocol': "-1",
                'Egress': "true",
                'RuleAction': "allow",
                'CidrBlock': "0.0.0.0/0"}}

    def test_create_bsg(self):
        print(self.cloudformation.vpc.vpcnetworkaclboundrule.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.vpcnetworkaclboundrule.to_dict(),
            self.netvpcoutr)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.dhoptionass = {
            'Type': 'AWS::EC2::VPCDHCPOptionsAssociation', 'Properties': {
                'VpcId': {
                    'Ref': 'VPC'}, 'DhcpOptionsId': {
                    "Ref": "DhcpOptions"}}}

    def test_create_Dhcp_options_ass(self):
        print(self.cloudformation.vpc.vpcdhcpoass.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.vpcdhcpoass.to_dict(),
            self.dhoptionass)


if __name__ == '__main__':
    unittest.main()

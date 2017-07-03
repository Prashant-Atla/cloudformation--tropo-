#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.vpcGatewayattached = {
            'Type': 'AWS::EC2::VPCGatewayAttachment', 'Properties': {
                'VpcId': {
                    'Ref': 'VPC'}, 'InternetGatewayId': {
                    "Ref": 'InternetGateway'}}}

    def test_gateway_attachment(self):
        print(self.cloudformation.vpc.gateway_attachment.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.gateway_attachment.to_dict(),
            self.vpcGatewayattached)


if __name__ == '__main__':
    unittest.main()

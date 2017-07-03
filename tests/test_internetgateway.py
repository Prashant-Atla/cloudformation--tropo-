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

        self.internet_Gateway = {
            'Type': 'AWS::EC2::InternetGateway', 'Properties': {
                'Tags': [
                    {
                        'Value': 'ApiDev', 'Key': 'Environment'}, {
                        'Value': 'ApiDev-Dev-InternetGateway', 'Key': 'Name'}, {
                        'Value': 'Foo industries', 'Key': 'Owner'}, {
                            'Value': 'ServiceVPC', 'Key': 'Service'}, {
                                'Value': 'Dev', 'Key': 'VPC'}]}}

    def test_create_internet_gateway(self):
        print(self.cloudformation.vpc.internet_gateway.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.internet_gateway.to_dict(),
            self.internet_Gateway)


if __name__ == '__main__':
    unittest.main()

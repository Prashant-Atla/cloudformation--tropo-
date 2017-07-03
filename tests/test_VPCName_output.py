#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.vpcnamen = {"Value": {"Ref": "AWS::StackName"}}

    def test_vpcname_output(self):
        print(self.cloudformation.vpc.vpcname.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.vpcname.to_dict(),
            self.vpcnamen)


if __name__ == '__main__':
    unittest.main()

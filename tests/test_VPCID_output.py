#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.vpcidn = {"Value": {"Ref": "VPC"}}

    def test_vpcid_output(self):
        print(self.cloudformation.vpc.vpcid.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.vpcid.to_dict(),
            self.vpcidn)


if __name__ == '__main__':
    unittest.main()

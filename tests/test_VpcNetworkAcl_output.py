#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.vpcnetaclo = {"Value": {"Ref": "VpcNetworkAcl"}}

    def test_vpcnnetworkacl_output(self):
        print(self.cloudformation.vpc.vpcnnetworkacl_out.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.vpcnnetworkacl_out.to_dict(),
            self.vpcnetaclo)


if __name__ == '__main__':
    unittest.main()

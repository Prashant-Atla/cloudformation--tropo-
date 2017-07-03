#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.basg = {"Value": {"Ref": "BastionSG"}}

    def test_bsg_output(self):
        print(self.cloudformation.vpc.bsg_out.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.bsg_out.to_dict(),
            self.basg)


if __name__ == '__main__':
    unittest.main()

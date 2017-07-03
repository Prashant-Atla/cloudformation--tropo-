#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.natemTopic = {
            'Type': 'AWS::SNS::Topic', 'Properties': {
                'TopicName': 'ApiDev-Dev-NatEmergencyTopic'}}

    def test_create_Nat_Emergency_Topic(self):
        print(self.cloudformation.vpc.natemergencytop.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.natemergencytop.to_dict(),
            self.natemTopic)


if __name__ == '__main__':
    unittest.main()

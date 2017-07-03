#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)

        self.cloudalarmwatchtopic = {
            'Type': 'AWS::SNS::Topic', 'Properties': {
                'TopicName': 'ApiDev-Dev-CloudWatchAlarms'}}

    def test_create_bsg(self):
        print(self.cloudformation.vpc.cloudwatchalarmtopic.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.cloudwatchalarmtopic.to_dict(),
            self.cloudalarmwatchtopic)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python

import unittest
import template_creator
import yaml


class TestVpcMethods(unittest.TestCase):

    def setUp(self):
        with open('template_config.yaml', 'r') as f:
            self.config = yaml.load(f.read())
        self.cloudformation = template_creator.Cloudformation(self.config)
        self.cloudwatchalarmtopic = {'Value': {"Ref": "CloudWatchAlarmTopic"}}

    def test_create_vcloudwatchalarmtopic(self):
        print(self.cloudformation.vpc.cloudwatchalarmtopic_output.to_dict())
        self.assertDictEqual(
            self.cloudformation.vpc.cloudwatchalarmtopic_output.to_dict(),
            self.cloudwatchalarmtopic)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python

"""
Usage:
  template_creator.py generate [--config-file <config_file>] [--output-file <OUTPUT_FILE>]...
  template_creator.py (-h | --help)
  template_creator.py --version
python template_creator.py generate --config-file template_config.yaml

Options:
  -h --help                     Show this screen.
  --version                     Show version.
  --config-file <CONFIG_FILE>   Input for config data for the generated CF template. Defaults to template_config.yaml
  --output-file <OUTPUT_FILE>   Destination for the generated CF template. Defaults to workspace.cfn file
"""
import json
from docopt import docopt
import yaml

from troposphere import Template
from vpc import VPCCreator


class Cloudformation:
    # Class creates CloudFormation template for VPC service

    def __init__(self, config_dictionary):
        self.globals = config_dictionary.get('globals', {})
        self.template_args = config_dictionary.get('template', {})

        self.template = Template()
        self.template.description = self.globals.get('description', '')
        self.template.metadata = self.globals.get('metadata', '')
        self.vpc = VPCCreator(config_dictionary)

        for resource in self.vpc.resources:
            self.template.add_resource(resource)

        for output in self.vpc.outputs:
            self.template.add_output(output)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='CFLab 0.1')

    config_file = arguments.get('--config-file') or 'template_config.yaml'
    output_file = arguments.get('--output-file') or 'workspace.cfn'

    print '\nParsing the yaml config file from %s' % config_file
    with open(config_file, 'r') as f:
        config = yaml.load(f.read())

    print '\nGenerating required template'
    cloudformation = Cloudformation(config)

    print '\ncreating template to %s\n' % output_file
    with open(output_file, 'w') as text_file:
        json.dump(json.loads(cloudformation.template.to_json()),
                  text_file, indent=2, separators=(',', ': '))

    if arguments.get('--debug'):
        print cloudformation.template.to_json()

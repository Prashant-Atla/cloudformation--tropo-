#!/usr/bin/python

from troposphere import Ref, Output, Join, Tags
import troposphere.ec2 as ec2
import troposphere.sns as sns


class VPCCreator:
    def __init__(self, template_args):
        self.resources = []
        self.outputs = []

        self.ref_stack_id = Ref('AWS::StackId')
        self.ref_region = Ref('AWS::Region')
        self.ref_stack_name = Ref('AWS::StackName')

        if 'vpc' in template_args['template']:
            self.create_vpc1(template_args['template']['vpc'])
        if 'Bastionsg' in template_args['template']:
            self.create_bsg(template_args['template']['Bastionsg'])
        if 'Internetgateway' in template_args['template']:
            self.create_internet_gateway(
                template_args['template']['Internetgateway'])
        if 'DhcpOptions' in template_args['template']:
            self.create_dhcp_options(template_args['template']['DhcpOptions'])
        if 'Cloudwatchalarmtopic' in template_args['template']:
            self.create_cloud_watch_alarm_topic(
                template_args['template']['Cloudwatchalarmtopic'])
        if 'NatEmergencyTopic' in template_args['template']:
            self.create_nat_emergency_topic(
                template_args['template']['NatEmergencyTopic'])
        if 'vpcNetworkAcl' in template_args['template']:
            self.create_network_acl(template_args['template']['vpcNetworkAcl'])
        self.create_dhcp_options_assocition()

    def create_bsg(self, bsg_arg):
        self.Bsg = self.add_resource(ec2.SecurityGroup(
            "BastionSG",
            GroupDescription="Used for source/dest rules",
            Tags=Tags(
                Environment=bsg_arg['Environment'],
                Name=bsg_arg['Name'],
                Owner=bsg_arg['Owner'],
                Service=bsg_arg['Service'],
                VPC=bsg_arg['VPC'],
            ),
            VpcId=Ref(self.vpc),
        ))
        self.bsg_out = self.add_output(Output(
            'BastionSG',
            Value=Ref(self.Bsg)
        ))

    def create_vpc1(self, vpc_arg):

        self.vpc = self.add_resource(
            ec2.VPC(
                "VPC",
                CidrBlock=vpc_arg['CidrBlock'],
                EnableDnsHostnames=vpc_arg['EnableDnsHostnames'],
                EnableDnsSupport=vpc_arg['EnableDnsSupport'],
                InstanceTenancy=vpc_arg['InstanceTenancy'],
                Tags=Tags(
                    Environment=vpc_arg['Tags']["Environment"],
                    Name=vpc_arg['Tags']['Name'],
                    Owner=vpc_arg['Tags']["Owner"],
                    Service=vpc_arg['Tags']["Service"],
                    VPC=vpc_arg['Tags']['VPC'],
                ),
            ))

    def create_internet_gateway(self, inga_arg):

        self.internet_gateway = self.add_resource(ec2.InternetGateway(
            'InternetGateway',
            Tags=Tags(
                Environment=inga_arg['Tags']['Environment'],
                Owner=inga_arg['Tags']['Owner'],
                Service=inga_arg['Tags']['Service'],
                VPC=inga_arg['Tags']['VPC'],
                Name=inga_arg['Tags']['Name'])))

        self.gateway_attachment = self.add_resource(
            ec2.VPCGatewayAttachment(
                'VpcGatewayAttachment',
                InternetGatewayId=Ref(self.internet_gateway),
                VpcId=Ref(self.vpc)))
        self.internetgateway_output = self.add_output(Output(
            'InternetGateway',
            Value=Ref(self.internet_gateway)
        ))

    def create_dhcp_options(self, dhcp_arg):
        self.dhcp_options = self.add_resource(
            ec2.DHCPOptions(
                'DhcpOptions',
                DomainName=Join("", (self.ref_region, ".compute.internal")),
                DomainNameServers=[
                    "AmazonProvidedDNS"
                ],
                Tags=Tags(
                    Environment=dhcp_arg['Tags']['Environment'],
                    Owner=dhcp_arg['Tags']['Owner'],
                    Service=dhcp_arg['Tags']['Service'],
                    VPC=dhcp_arg['Tags']['VPC'],
                    Name=dhcp_arg['Tags']['Name'])))

    def create_cloud_watch_alarm_topic(self, cwat_arg):

        self.cloudwatchalarmtopic = self.add_resource(
            sns.Topic(
                "CloudWatchAlarmTopic",
                TopicName=cwat_arg['TopicName']
            ))
        self.cloudwatchalarmtopic_output = self.add_output(Output(
            'CloudWatchAlarmTopic',
            Value=Ref(self.cloudwatchalarmtopic)
        ))

    def create_dhcp_options_assocition(self):
        self.vpcdhcpoass = self.add_resource(ec2.VPCDHCPOptionsAssociation(
            "VpcDhcpOptionsAssociation",
            DhcpOptionsId=Ref(self.dhcp_options),
            VpcId=Ref(self.vpc),
        ))

    def create_nat_emergency_topic(self, naet_arg):

        self.natemergencytop = self.add_resource(sns.Topic(
            "NatEmergencyTopic",
            TopicName=naet_arg['TopicName'],
        ))
        self.natemergencytopArn_output = self.add_output(Output(
            'NatEmergencyTopicARN',
            Value=Ref(self.natemergencytop)
        ))

    def create_network_acl(self, acl_arg):

        self.vpcnetworkacl = self.add_resource(ec2.NetworkAcl(
            "VpcNetworkAcl",
            Tags=Tags(
                Environment=acl_arg['Tags']['Environment'],
                Owner=acl_arg['Tags']['Owner'],
                Service=acl_arg['Tags']['Service'],
                VPC=acl_arg['Tags']['VPC'],
                Name=acl_arg['Tags']['Name'],
            ),
            VpcId=Ref(self.vpc)
        ))

        self.vpcnetworkaclinboundpublic80 = self.add_resource(
            ec2.NetworkAclEntry(
                "VpcNetworkAclInboundRulePublic80",
                CidrBlock=acl_arg['VpcNetworkaclinboundpublic80']['CidrBlock'],
                Egress=acl_arg['VpcNetworkaclinboundpublic80']['Egress'],
                NetworkAclId=Ref(
                    self.vpcnetworkacl),
                PortRange=ec2.PortRange(
                    To=acl_arg['VpcNetworkaclinboundpublic80']['To_port'],
                    From=acl_arg['VpcNetworkaclinboundpublic80']['From_port']),
                Protocol=acl_arg['VpcNetworkaclinboundpublic80']['Protocol'],
                RuleAction=acl_arg['VpcNetworkaclinboundpublic80']['RuleAction'],
                RuleNumber=acl_arg['VpcNetworkaclinboundpublic80']['RuleNumber']))

        self.vpcnetworkaclinboundrulepublic443 = self.add_resource(
            ec2.NetworkAclEntry(
                "VpcNetworkAclInboundRulePublic443",
                CidrBlock=acl_arg['VpcNetworkaclinboundpublic443']['CidrBlock'],
                Egress=acl_arg['VpcNetworkaclinboundpublic443']['Egress'],
                NetworkAclId=Ref(
                    self.vpcnetworkacl),
                PortRange=ec2.PortRange(
                    To=acl_arg['VpcNetworkaclinboundpublic443']['To_port'],
                    From=acl_arg['VpcNetworkaclinboundpublic443']['From_port']),
                Protocol=acl_arg['VpcNetworkaclinboundpublic443']['Protocol'],
                RuleAction=acl_arg['VpcNetworkaclinboundpublic443']['RuleAction'],
                RuleNumber=acl_arg['VpcNetworkaclinboundpublic443']['RuleNumber']))

        self.vpcnetworkaclboundrule = self.add_resource(
            ec2.NetworkAclEntry(
                "VpcNetworkAclOutboundRule",
                CidrBlock=acl_arg['VpcNetworkacloutboundrule']['CidrBlock'],
                Egress=acl_arg['VpcNetworkacloutboundrule']['Egress'],
                NetworkAclId=Ref(self.vpcnetworkacl),
                Protocol=acl_arg['VpcNetworkacloutboundrule']['Protocol'],
                RuleAction=acl_arg['VpcNetworkacloutboundrule']['RuleAction'],
                RuleNumber=acl_arg['VpcNetworkacloutboundrule']['RuleNumber']
            ))

        self.vpcnetworkaclssh = self.add_resource(
            ec2.NetworkAclEntry(
                "VpcNetworkAclSsh",
                CidrBlock=acl_arg['VpcNetworkaclssh']['CidrBlock'],
                Egress=acl_arg['VpcNetworkaclssh']['Egress'],
                NetworkAclId=Ref(
                    self.vpcnetworkacl),
                PortRange=ec2.PortRange(
                    To=acl_arg['VpcNetworkaclssh']['To_port'],
                    From=acl_arg['VpcNetworkaclssh']['From_port']),
                Protocol=acl_arg['VpcNetworkaclssh']['Protocol'],
                RuleAction=acl_arg['VpcNetworkaclssh']['RuleAction'],
                RuleNumber=acl_arg['VpcNetworkaclssh']['RuleNumber']))
        self.vpcid = self.add_output(Output("VPCID",
                                            Value=Ref(self.vpc)))

        self.vpcnnetworkacl_out = self.add_output(Output(
            "VpcNetworkAcl",
            Value=Ref(self.vpcnetworkacl)))

        self.vpcname = self.add_output(Output(
            "VPCName",
            Value=Ref('AWS::StackName')))

    def add_resource(self, resource):

        # Method helper for adding resources to the resource list
        # resource [object] troposphere resource object
        self.resources.append(resource)
        return resource

    def add_output(self, output):

        # Method helper for adding output to the output list
        # output [object] troposphere output object

        self.outputs.append(output)
        return output

#####################################################################################################################
	Read me
#####################################################################################################################
- Pre-requisits 
  Please permissions for the file
	-command `chmod -R 777 viaplay task`

- Requirements

	1. docopt
	2. boto
	3. trophosphere
	4. PyYAML
- The above dependencies are required for the script to create a coudformation template.
 	
	The below command can be used for installation of all the required dependencies. 
	The dependencies required for the script to run as specifiedin the file "requirements.txt".

	---command

		pip install -r requirements.txt

- Generation of the required template
	
	To generate a template simply run the command 

	python template_creator.py generate --config-file template_config.yaml

	 - This will produce the template file "worksample.cfn" which can be used for deploying the cloudformation stack.

 	 - If more instances are requied The required instances can be simply be added in the "vpc.py" 
   	   and configuration can be mentioned in the yaml file.
 
 	 - In the present template the configuration values are fetched from the Yaml file "template_config.yaml".

#######################################################################################################################

 Make use of the Makefile (OPtional)
	
  - To create a output file just type make to automatically install all the requirements and to execute the script



###################################################################################################################### 

********************** UNIT Test ********************************

  Some of the test cases are provided for the script for validation

	The tests can be ran by usnig command. All the test files are included in the directory tests
	
	python setup.py test 

 The script is written in python version 2.7

	The scripts are in the pep8 format 

*******author**********
  Prashant Atla





















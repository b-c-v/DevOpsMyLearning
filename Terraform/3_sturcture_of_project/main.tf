# AWS create infrastructure: VPC + subnet + internet gateway + route table + security group + EC2 + KeyPairs + install Docker & nginx

provider "aws" {
  region = "eu-central-1"
}

resource "aws_vpc" "bcv_vpc" {
  cidr_block = var.main_vpc_cidr_block
  tags = {
    Name = "${var.main_env_prefix}-vpc"
  }
}

module "name_module_myapp_subnet" {                     #connect module
  source                   = "./modules/subnet"         #path to directory with module
  module_vpc_id            = aws_vpc.bcv_vpc.id
  module_subnet_cidr_block = var.main_subnet_cidr_block #values are definied in .tfvars file ==> set as values in .tf in root ==> values are passed to child module as arguments ==> via variables.tf in child module
  module_avail_zone        = var.main_avail_zone        # module_variable (./subnet/variables.tf) =  (./.tf) = value (./terraform.tfvars)
  module_env_prefix        = var.main_env_prefix
  }


module "name_module_myapp_webserver" {
  source = "./modules/webserver"
  ws_vpc_id = aws_vpc.bcv_vpc.id
  ws_my_ip = var.main_my_ip
  ws_env_prefix = var.main_env_prefix
  ws_webserver_image_name = var.main_image_name
  ws_my_publick_key_location = var.main_my_publick_key_location
  ws_instance_type = var.main_instance_type
  ws_subnet_id = module.name_module_myapp_subnet.name_output_subnet.id #call value from output of another module
  ws_avail_zone = var.main_avail_zone

}






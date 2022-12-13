# AWS create subnet in existing (default) VPC


provider "aws" {
    region = "eu-central-1"
    access_key = "xxx"
    secret_key = "xxx"
}

data "aws_vpc" "name_existing_vpc"{                 # take data about default VPC
    default = true                                  # Boolean constraint on whether the desired VPC is the default VPC for the region.
}
resource "aws_subnet" "name_aws_subnet2" {          # create subnet inside VPC which depends on another created recurs
    vpc_id = data.aws_vpc.name_existing_vpc.id      # take ID from existing data
    cidr_block ="172.31.48.0/20"                    # create IP range of subnet (IPv4 CIDR)
    #availability_zone = "eu-central-1a"
    tags = {
        Name = "name_aws_subnet2"                   # add Name of this resource  
    }
}
# AWS create new VPC and subnet


provider "aws" {
    region = "eu-central-1"
    access_key = "xxx"
    secret_key = "xxx"
}

resource "aws_vpc" "name_aws_vpc"{
    cidr_block = "10.0.0.0/16"                  # create VPC with IP range(IPv4 CIDR)
}

resource "aws_subnet" "name_aws_subnet"{        # create subnet inside VPC which depends on another created recurs
    vpc_id = aws_vpc.name_aws_vpc.id            # we don't know ID of aws_vpc - made link to it
    cidr_block ="10.0.1.0/24"                   # create IP range of subnet (IPv4 CIDR)
    availability_zone = "eu-central-1c"
}
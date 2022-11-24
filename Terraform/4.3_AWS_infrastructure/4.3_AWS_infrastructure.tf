# AWS create infrastructure: VPC + subnet + internet gateway + route table + security group + EC2 + KeyPairs + install Docker & nginx

variable "vpc_cidr_block" {}
variable "subnet_cidr_block" {}
variable "avail_zone" {}
variable "env_prefix" {}
variable "my_ip" {}
variable "instance_type" {}
variable "my_publick_key_location" {}


provider "aws" {
  region = "eu-central-1"
}

resource "aws_vpc" "bcv_vpc" { #create VPC
  cidr_block = var.vpc_cidr_block
  tags = {
    Name = "${var.env_prefix}-vpc"
  }
}

resource "aws_subnet" "bcv_subnet_1" { #create Subnet inside VPS 
  vpc_id            = aws_vpc.bcv_vpc.id
  cidr_block        = var.subnet_cidr_block
  availability_zone = var.avail_zone
  tags = {
    Name = "${var.env_prefix}-subnet1"
  }
}

resource "aws_internet_gateway" "bcv_igw" { #create Gateway
  vpc_id = aws_vpc.bcv_vpc.id
  tags = {
    Name = "${var.env_prefix}-igw"
  }
}

resource "aws_route_table" "bcv_route_table" { #add to rout table possibility to connect internet
  vpc_id = aws_vpc.bcv_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.bcv_igw.id
  }
  tags = {
    Name = "${var.env_prefix}-route_table"
  }
}

resource "aws_route_table_association" "bcv_subnet_route" { #create an association between a route table and a subnet
  subnet_id      = aws_subnet.bcv_subnet_1.id
  route_table_id = aws_route_table.bcv_route_table.id
}

resource "aws_security_group" "bcv_sg" { #open ports in VPC
  name        = "Allow HTTP and SSH"
  description = "Allow HTTP (8080) and SSH(22) in VPC"
  vpc_id      = aws_vpc.bcv_vpc.id

  ingress { #rule for incoming SSH traffic                    
    description = "SSH to VPC"
    from_port   = 22 #if need open range of ports 0-1986: from_port=0 to_port=1986
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.my_ip] #who is allowed to access resource
  }

  ingress { #rule for incoming HTTP traffic                    
    description = "HTTP to VPC"
    from_port   = 8080 #open port 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] #all can allow resource by HTTP
  }

  egress {          #rule for outgoing traffic 
    from_port   = 0 #open all ports
    to_port     = 0
    protocol    = "-1"          #open all protocols
    cidr_blocks = ["0.0.0.0/0"] #open all IP
  }

  tags = {
    Name = "${var.env_prefix}-ports"
  }
}

data "aws_ami" "latest_amazon_linux_image" { #find the latest version of Amazon Linux 
  most_recent = true
  owners      = ["amazon"]
  filter { #here can be more than one filter
    name   = "name"
    values = ["amzn2-ami-kernel-*-x86_64-gp2"] #regular expression to find image by name
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

}

output "aws_ami_id" {                               #check in output number of aws_ami_id
  value = data.aws_ami.latest_amazon_linux_image.id #if here delete .id in output will be more wide information
}

resource "aws_key_pair" "ssh-key" {              #SSH connect to ec2 with using public and private key of host. Can connect with host credentials "ssh ec2-user@ip" and not necessary download (EC2==>Network & Security==>Key Pairs)
  key_name   = "${var.env_prefix}-key"           #name of automatically creating key in AWS (EC2==>Network & Security==>Key Pairs)
  public_key = file(var.my_publick_key_location) #path to key id_rsa.pub of host
}

resource "aws_instance" "bcv_server" {
  ami           = data.aws_ami.latest_amazon_linux_image.id #from result of work data block assign the ami number of OS image
  instance_type = var.instance_type

  subnet_id              = aws_subnet.bcv_subnet_1.id #add instance to subnet
  vpc_security_group_ids = [aws_security_group.bcv_sg.id]
  availability_zone      = var.avail_zone

  associate_public_ip_address = true #enable public IP on instance
  #key_name = "terraform" #deprecated in AWS (EC2==>Network & Security==>Key Pairs) created the key with this name and put this key to ~/.ssh/ directory
  key_name = aws_key_pair.ssh-key.key_name #call value from separate resource aws_key_pair
  

  user_data = file("docker_nginx.sh")  #from file docker_nginx.sh run script for install docker and run container nginx
  


  tags = {
    Name = "${var.env_prefix}-bcv_server"
  }
}



output "ec2_public_ip" { #print in output public IP of ec2 instance for SSH connection
  value = aws_instance.bcv_server.public_ip
}


#create two EC2 instances and save public and private IPs to ansible-host file

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  count = 2

  ami           = "ami-0aa7d40eeae50c9a9"
  instance_type = "t2.micro"

  tags = {
    Name = "terraform-example-instance-${count.index}"
  }
}

output "instance_ips" {
  value = [for instance in aws_instance.example : instance.private_ip]
}

output "instance_public_ips" {
  value = [for instance in aws_instance.example : instance.public_ip]
}

locals {
  host_ips    = [for instance in aws_instance.example : instance.private_ip]
  host_public = [for instance in aws_instance.example : instance.public_ip]
}

locals {
  private_ips = "${join("\n", local.host_ips)}\n"
  public_ips  = "${join("\n", local.host_public)}\n"
}

resource "local_file" "ansible_hosts" {
  content  = <<EOF
  [web]
  ${local.private_ips}
  [web:vars]
  ansible_user=ubuntu
  ansible_ssh_private_key_file=~/.ssh/id_rsa

  [public]
  ${local.public_ips}
  [public:vars]
  ansible_user=ubuntu
  ansible_ssh_private_key_file=~/.ssh/id_rsa
  EOF
  filename = "ansible-hosts"
}

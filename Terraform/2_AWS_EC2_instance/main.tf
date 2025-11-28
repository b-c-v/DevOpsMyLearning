# Sequence of resources and dependencies in Terraform for a public EC2 instance:
# 1. Create VPC (logical network boundary in AWS)
# 2. Create Public Subnet in the VPC. Define a CIDR block within the VPC. This subnet becomes "public" once it’s associated with a route table that routes to an Internet Gateway (IGW).
# 3. Create Internet Gateway (IGW) and attach it to the VPC (enables outbound internet access).
# 4. Create Route Table + Default Route to IGW (allows traffic to flow to the internet).
# 5. Associate the Route Table with the Public Subnet (so instances in that subnet can use the IGW).
# 6. Create Security Group (virtual firewall for the EC2 instance).
# 7. Allow inbound traffic on port 80 (HTTP) from anywhere.
# 8. Allow inbound traffic on port 443 (HTTPS) from anywhere.
# 9. Create EC2 Instance inside the public subnet, attach Security Group, and allocate a public IP.

# 1. Create VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = merge(local.common_tags, {
    Name = "ec2-terraform"
  })
}

# 2. Create Public Subnet in the VPC. Define CIDR block within VPC. Mark it as a public subnet by associating it with a route table that points to the IGW.
resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.0.0/24"

  tags = merge(local.common_tags, {
    Name = "ec2-terraform"
  })
}

# Create Internet Gateway (IGW) and associate it with the VPC
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = merge(local.common_tags, {
    Name = "ec2-terraform"
  })
}

# 4. Create Route Table with a default route to the IGW
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = merge(local.common_tags, {
    Name = "06-resources-main"
  })
}

# 5. Associate the route table with the subnet.
resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

# 6. Create Security Group
resource "aws_security_group" "public_http_traffic" {
  description = "Security group allowing traffic on ports 443 and 80"
  name        = "public-http-traffic"
  vpc_id      = aws_vpc.main.id

  tags = merge(local.common_tags, {
    Name = "ec2-terraform-sg"
  })
}

# 7. Allow inbound traffic on port 80 (HTTP) from anywhere
resource "aws_vpc_security_group_ingress_rule" "http" {
  security_group_id = aws_security_group.public_http_traffic.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 80
  to_port           = 80
  ip_protocol       = "tcp"
}

# 8. Allow inbound traffic on port 443 (HTTPS) from anywhere
resource "aws_vpc_security_group_ingress_rule" "https" {
  security_group_id = aws_security_group.public_http_traffic.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 443
  to_port           = 443
  ip_protocol       = "tcp"
}

# 9. Create EC2 Instance
resource "aws_instance" "web" {
  ami                         = "ami-0dfee6e7eb44d480b"
  associate_public_ip_address = true
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.public.id
  vpc_security_group_ids      = [aws_security_group.public_http_traffic.id]
  root_block_device {
    delete_on_termination = true
    volume_size           = 10
    volume_type           = "gp3"
  }

  tags = merge(local.common_tags, {
    Name = "ec2-terraform"
  })

  lifecycle {
    create_before_destroy = true
  }
}

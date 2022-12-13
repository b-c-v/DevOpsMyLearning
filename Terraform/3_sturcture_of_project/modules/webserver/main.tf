resource "aws_security_group" "bcv_sg" {
  name        = "Allow HTTP and SSH"
  description = "Allow HTTP (8080) and SSH(22) in VPC"
  vpc_id      = var.ws_vpc_id

  ingress {
    description = "SSH to VPC"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.ws_my_ip]
  }

  ingress {
    description = "HTTP to VPC"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.ws_env_prefix}-ports"
  }
}

data "aws_ami" "latest_amazon_linux_image" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = [var.ws_webserver_image_name]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

}

resource "aws_key_pair" "ssh-key" {
  key_name   = "${var.ws_env_prefix}-key"
  public_key = file(var.ws_my_publick_key_location)
}

resource "aws_instance" "bcv_server" {
  ami           = data.aws_ami.latest_amazon_linux_image.id
  instance_type = var.ws_instance_type

  subnet_id              =  var.ws_subnet_id
  vpc_security_group_ids = [aws_security_group.bcv_sg.id]
  availability_zone      = var.ws_avail_zone

  associate_public_ip_address = true
  key_name                    = aws_key_pair.ssh-key.key_name


  user_data = file("./modules/webserver/docker_nginx.sh")


  tags = {
    Name = "${var.ws_env_prefix}-bcv_server"
  }
}
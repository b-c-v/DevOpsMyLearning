resource "aws_subnet" "module_bcv_subnet_1" {
  vpc_id            = var.module_vpc_id
  cidr_block        = var.module_subnet_cidr_block
  availability_zone = var.module_avail_zone
  tags = {
    Name = "${var.module_env_prefix}-subnet1"
  }
}

resource "aws_internet_gateway" "bcv_igw" {
  vpc_id = var.module_vpc_id
  tags = {
    Name = "${var.module_env_prefix}-igw"
  }
}

resource "aws_route_table" "bcv_route_table" {
  vpc_id = var.module_vpc_id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.bcv_igw.id
  }
  tags = {
    Name = "${var.module_env_prefix}-route_table"
  }
}

resource "aws_route_table_association" "bcv_subnet_route" {
  subnet_id      = aws_subnet.module_bcv_subnet_1.id
  route_table_id = aws_route_table.bcv_route_table.id
}
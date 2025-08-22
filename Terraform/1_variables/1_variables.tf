# AWS create new VPC and subnet

# ***Defining Variables***
# Declare a variable in any "*.tf" file (commonly variables.tf). Block "variable <variable_name> {}" declares the variable's name, type, and an optional description or default value. 
# You can have multiple variables defined in a single file or spread across several "*.tf" files in your configuration.

# ***Assigning Values to Variables***
# You can assign values to your defined variables in several ways. The "*.tfvars" file is recommended one for managing static values.

# ***Using Variables in Resources***
# Once a variable is defined and has a value assigned, you can reference it in any resource block or other parts of your Terraform configuration using the syntax "var.<variable_name>"

provider "aws" {
  region = "eu-central-1"
}

variable "name_variable_vpc_cidr_block" { # create variable
  description = "vpc cidr block variable"
  default     = "10.0.0.0/16" # will use if value of variable don't assign in file terraform.tfvars
  type        = string        # specifies what value types are accepted

}

resource "aws_vpc" "name_aws_vpc" {
  cidr_block = var.name_variable_vpc_cidr_block # call variable
  tags = {
    Name = "test_delete"
  }
}

variable "name_variable_subnet_cidr_block" { # create variable
  description = "subnet cidr block array variable"
  type        = list(string) # array of type string

}

variable "zone_name_subnet" {
  description = "availabilyty zone&name array of object" # create variable array of object type string 
  type = list(object({
    zone = string
    name = string
  }))
}

resource "aws_subnet" "name_aws_subnet" {
  vpc_id            = aws_vpc.name_aws_vpc.id
  cidr_block        = var.name_variable_subnet_cidr_block[1] # list(string) call second element of array values type string                     
  availability_zone = var.zone_name_subnet[1].zone           # list(object) call second element from array
  tags = {
    Name = var.zone_name_subnet[2].name # list(object) call third element from array                  
  }
}


# Provider configuration for Vultr
provider "vultr" {
  api_key = var.vultr_api_key
}

# Input variables for the deployment
variable "vultr_api_key" {
  description = "API key for Vultr"
  type        = string
}

variable "vm_name" {
  description = "Name of the VM to be created"
  type        = string
  default     = "my-vm"
}

variable "region" {
  description = "Region in which the VM will be created"
  type        = string
  default     = "nrt"
}

variable "plan" {
  description = "Vultr plan ID for the VM"
  type        = string
  default     = "vc2-1c-1gb"
}

variable "os_id" {
  description = "Vultr OS ID for the VM"
  type        = string
  default     = "387"
}

# Create a Vultr VM
resource "vultr_server" "my_vm" {
  name     = var.vm_name
  region   = var.region
  plan     = var.plan
  os_id    = var.os_id
  hostname = "${var.vm_name}.example.com"
}


variable "resourcename" {
  default = "identity-aks-rg"
}

variable "clustername" {
  default = "identity-aks"
}

variable "location" {
  type    = string
  default = "westeurope"
}

variable "prefix" {
  type    = string
  default = "dev-identity"
}

variable "ssh-key" {
  type    = string
  default = "~/.ssh/tf-aks.pub"
}

#variable "size" {
#  default = "Standard_D2_V2"
#}

#variable "agentnode" {
#  default = "2"
#}

variable "subscription_id" {
}
variable "client_id" {
}
variable "client_secret" {
}
variable "tenant_id" {
}

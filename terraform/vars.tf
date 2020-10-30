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
  default = "e90bd4d0-3b50-4a27-a7e8-bc88cf5f5398"
}
variable "client_id" {
  default = "0c56ff6c-269a-4f8c-afcb-c9cc8ec96501"
}
variable "client_secret" {
  default = "phyM5Xf7v~7p93.O1~TcpLNlwkHvJS~Z17"
}
variable "tenant_id" {
  default = "1bef4fb2-f9cc-478e-ac6f-da7d49fcad00"
}

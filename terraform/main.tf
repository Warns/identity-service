provider "azurerm" {
  version         = "=2.20.0"
  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  tenant_id       = var.tenant_id

  features {}
}

terraform {
  backend "azurerm" {
    resource_group_name  = "tstate-rg"
    storage_account_name = "tstateidentity15466"
    container_name       = "tstate"
    key                  = "terraform.tfstate"
  }
}

# create resource group
resource "azurerm_resource_group" "dev-identity-k8s" {
  name     = var.resourcename
  location = var.location
  tags = {
    env    = "identity-aks-rg"
    source = "sociallme"
  }
}


# resource "azurerm_resource_group" "tstate" {
#   name = "tstateidentityrg"
#   location = var.location
#   tags = {
#     env = "tstate-rg"
#     source = "sociallme"
#   }
# }

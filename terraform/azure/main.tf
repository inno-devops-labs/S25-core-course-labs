terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "0ff37950-3e06-4453-aab7-a3633926c961"
}

resource "azurerm_resource_group" "example_group" {
  name     = "Devops_iu"
  location = "eastus"
  tags     = {}
}

resource "azurerm_virtual_network" "vnet" {
  name                = "vnet-devops"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.example_group.location
  resource_group_name = azurerm_resource_group.example_group.name
}

resource "azurerm_subnet" "subnet" {
  name                 = "subnet-devops"
  resource_group_name  = azurerm_resource_group.example_group.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_public_ip" "public_ip" {
  name                = "vps-public-ip"
  location            = azurerm_resource_group.example_group.location
  resource_group_name = azurerm_resource_group.example_group.name
  allocation_method   = "Dynamic"
}

resource "azurerm_network_interface" "nic" {
  name                = "vps-nic"
  location            = azurerm_resource_group.example_group.location
  resource_group_name = azurerm_resource_group.example_group.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.public_ip.id
  }
}

resource "azurerm_linux_virtual_machine" "vps" {
  name                = "devops-vps"
  resource_group_name = azurerm_resource_group.example_group.name
  location            = azurerm_resource_group.example_group.location
  size                = "Standard_B1s"
  admin_username      = "adminuser"
  network_interface_ids = [
    azurerm_network_interface.nic.id,
  ]

  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/id_rsa_personal.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
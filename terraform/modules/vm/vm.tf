resource "azurerm_network_interface" "test" {
  name                = "${var.application_type}-${var.resource_type}-ni"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip}"
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  name                = "${var.application_type}-${var.resource_type}-vm"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS2_v2"
  admin_username      = "${var.admin_username}"
  admin_password      = "${var.admin_password}"
  disable_password_authentication = false
  network_interface_ids = [azurerm_network_interface.test.id]
  admin_ssh_key {
    username   = "${var.admin_username}"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC74btQ3kM63g75kMX81E5Xm+eFT62/29I7EM0A9SP5P19d7BmJvyKxkRsRd1t51wz3Ma+ZU7VY+X44akd0AUVlcidvl8y84ofwpe1OCDV2B9dpAggs8dy6BBtigEfJH1hKfBRoKKwP0DdennM0P2Bz0xvGeeIiCfwLuVHv5bvsx7W+NcRXvO6mbMOKsjaSjCjrK8zQ0CEpivvsjH3uskRF4O7qY8ZK4uHjeen/XRU4hN8QiYHgHJKLl+OuBOVUdlaAzgZs3RNIi6HA2dPTiV0m19AZe5YRYcsEw4a2JMqVJ5piyd1Cy19uDY01pTPVSbwMJ7nqO6saAKTWaIbPnnn6sgiEikWcihLOivhUjn7IBRPAXPcfsw9GSmuUH4Os4RKKzZtPm+aS1H0k3RcFC+o0W/WM+H288g/gpKU104vembPdV2oAYNzt2kD3e3psPg8hTaF9ABFgucjTqnOeW4zvNtzCK9OLwdsbOxtN7XdgX0EPc8sxxisC+GdAUG9Gb9s= devopsagent@ThontnLinuxVM"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}

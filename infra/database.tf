module "postgresql" {
  source = "./modules/postgresql"

  name = var.dctfsi_postgres_name

  postgres_user     = var.dctfsi_postgres_user
  postgres_password = var.dctfsi_postgres_password
  postgres_database = var.dctfsi_postgres_database

  k8s_namespace = "default"
  k8s_image = "postgres:14-alpine"

  azure_disk_type = var.dctfsi_postgres_azure_disk_type
  azure_disk_size = var.dctfsi_postgres_azure_disk_size

  azure_resource_group_name     = "MC_${azurerm_resource_group.challs.name}_${azurerm_kubernetes_cluster.k8s.name}_${azurerm_resource_group.challs.location}"
  azure_resource_group_location = azurerm_resource_group.challs.location
}

module "postgresql-international" {
  source = "./modules/postgresql"

  name = var.dctf_postgres_name

  postgres_user     = var.dctf_postgres_user
  postgres_password = var.dctf_postgres_password
  postgres_database = var.dctf_postgres_database

  k8s_namespace = "default"
  k8s_image = "postgres:14-alpine"

  azure_disk_type = var.dctf_postgres_azure_disk_type
  azure_disk_size = var.dctf_postgres_azure_disk_size

  azure_resource_group_name     = "MC_${azurerm_resource_group.challs.name}_${azurerm_kubernetes_cluster.k8s.name}_${azurerm_resource_group.challs.location}"
  azure_resource_group_location = azurerm_resource_group.challs.location
}

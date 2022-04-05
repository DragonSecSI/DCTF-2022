resource "kubernetes_persistent_volume_claim" "psql" {
  metadata {
    name = "psql-${var.name}-pvc"
    namespace = var.k8s_namespace
  }
  spec {
    access_modes = ["ReadWriteOnce"]
    resources {
      requests = {
        storage = "${var.azure_disk_size}Gi"
      }
    }
    volume_name = "${kubernetes_persistent_volume.psql.metadata.0.name}"
  }
}

resource "kubernetes_persistent_volume" "psql" {
  metadata {
    name = "psql-${var.name}-pv"
  }
  spec {
    capacity = {
      storage = "${var.azure_disk_size}Gi"
    }
    access_modes = ["ReadWriteOnce"]
    persistent_volume_source {
      azure_disk {
        caching_mode  = "None"
        data_disk_uri = azurerm_managed_disk.storage.id
        disk_name     = "psql-${var.name}-disk"
        kind          = "Managed"
      }
    }
    storage_class_name = "default"
  }
}

resource "azurerm_managed_disk" "storage" {
  name                 = "psql-${var.name}-disk"
  location             = var.azure_resource_group_location
  resource_group_name  = var.azure_resource_group_name
  storage_account_type = var.azure_disk_type
  create_option        = "Empty"
  disk_size_gb         = var.azure_disk_size
}

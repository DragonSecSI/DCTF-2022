output "service_name" {
  value = kubernetes_service.service.metadata.0.name
}

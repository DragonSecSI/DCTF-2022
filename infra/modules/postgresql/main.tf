resource "kubernetes_service" "service" {
  metadata {
    name = "psql-${var.name}-service"
    namespace = var.k8s_namespace
  }
  spec {
    selector = {
      app = kubernetes_deployment.deployment.spec.0.template.0.metadata.0.labels.app
    }

    port {
      port        = 5432
      target_port = 5432
    }

    type = "ClusterIP"
  }
}

resource "kubernetes_deployment" "deployment" {
  metadata {
    name = "psql-${var.name}-deployment"
    namespace = var.k8s_namespace
    labels = {
      app = "psql-${var.name}"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "psql-${var.name}"
      }
    }

    template {
      metadata {
        labels = {
          app = "psql-${var.name}"
        }
      }

      spec {
        container {
          image = "${var.k8s_image}"
          name  = "psql-${var.name}"

          env {
            name  = "POSTGRES_USER"
            value = var.postgres_user
          }
          env {
            name  = "POSTGRES_PASSWORD"
            value = var.postgres_password
          }
          env {
            name  = "POSTGRES_DB"
            value = var.postgres_database
          }

          resources {
            limits = {
              cpu    = "2"
              memory = "4Gi"
            }
            requests = {
              cpu    = "1.5"
              memory = "3Gi"
            }
          }

          volume_mount {
            name = "storage"
            mount_path = "/var/lib/postgresql/data"
            sub_path = "pgdata"
          }
        }

        volume {
          name = "storage"
          persistent_volume_claim {
            claim_name = kubernetes_persistent_volume_claim.psql.metadata.0.name
          }
        }
      }
    }
  }
}

resource "kubernetes_network_policy" "app" {
  metadata {
    name      = "web-${var.name}-network-policy"
    namespace = var.k8s_namespace
  }

  spec {
    pod_selector {
      match_labels = {
        app = "${var.name}"
      }
    }

    egress {
      to {
        pod_selector {
          match_labels = {
            app = "${var.name}-mongo"
          }
        }
      }
      ports {
        port     = 27017
        protocol = "TCP"
      }
    }

    policy_types = ["Egress"]
  }
}

resource "kubernetes_network_policy" "mongo" {
  metadata {
    name      = "web-${var.name}-mongo-network-policy"
    namespace = var.k8s_namespace
  }

  spec {
    pod_selector {
      match_labels = {
        app = "${var.name}-mongo"
      }
    }

    egress {
      to {
        ip_block {
          cidr = "0.0.0.0/0"
          except = [
            "0.0.0.0/8",
            "10.0.0.0/8",
            "100.64.0.0/10",
            "127.0.0.0/8",
            "169.254.0.0/16",
            "172.16.0.0/12",
            "192.0.0.0/24",
            "192.0.2.0/24",
            "192.168.0.0/16",
            "198.18.0.0/15",
            "198.51.100.0/24",
            "203.0.113.0/24",
            "224.0.0.0/3",
          ]
        }
      }
    }

    policy_types = ["Egress"]
  }
}

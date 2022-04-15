data "google_client_config" "provider" {}

resource "google_service_account" "dctf" {
  account_id   = "dctf-sa"
  display_name = "dctf-sa"
}

resource "google_container_cluster" "dctf" {
  name     = "dctf"
  location = "europe-west3-a"

  remove_default_node_pool = true
  initial_node_count = 1
}

resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "default-pool"
  location   = "europe-west3-a"
  cluster    = google_container_cluster.dctf.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "e2-highcpu-8"

    service_account = google_service_account.dctf.email
    oauth_scopes    = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}

resource "google_compute_address" "dctf_challs_pwn" {
  name   = "dctf-challs-pwn-ip-address"
  region = "europe-west3"
}

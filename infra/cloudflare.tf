data "cloudflare_zone" "dragonsec" {
  name = "dragonsec.si"
}

data "cloudflare_zone" "dctf" {
  name = "dctf.si"
}

resource "cloudflare_record" "pwn" {
  zone_id = data.cloudflare_zone.dctf.id
  name    = "pwn"
  proxied = false
  value   = azurerm_public_ip.challs_pwn.ip_address
  type    = "A"
  ttl     = 1
}

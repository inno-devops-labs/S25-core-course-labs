resource "github_membership" "all" {
  for_each = {
    for member in csvdecode(file("members.csv")) :
    member.username => member
  }

  username = each.value.username
  role     = each.value.role
}
provider "aws" {
  region     = "us-east-2"
  access_key = "_"
  secret_key = "-"

}
resource "aws_iam_role" "Engineering" {
    name  = "engineering"
  assume_role_policy = "${file("admin.json")}"
}
resource "aws_iam_role" "Finance" {
    name  = "finance"
  assume_role_policy = "${file("admin.json")}"
}
resource "aws_iam_policy_attachment" "Engineering-attach" {
  name       = "engineering-attachment"
  roles      = ["${aws_iam_role.Engineering.name}"]
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}
resource "aws_iam_policy_attachment" "Finance-attach" {
  name       = "finance-attachment"
  roles      = ["${aws_iam_role.Finance.name}"]
  policy_arn = "arn:aws:iam::aws:policy/job-function/Billing"
}

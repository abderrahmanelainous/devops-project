output "master_public_ip" {
  description = "Public IP of the K3s master node"
  value       = aws_instance.master.public_ip
}

output "worker_public_ip" {
  description = "Public IP of the K3s worker node"
  value       = aws_instance.worker.public_ip
}

output "master_private_ip" {
  description = "Private IP of the K3s master node"
  value       = aws_instance.master.private_ip
}

output "worker_private_ip" {
  description = "Private IP of the K3s worker node"
  value       = aws_instance.worker.private_ip
}

output "ssh_master" {
  description = "SSH command to connect to master"
  value       = "ssh -i ~/.ssh/devops-project-key.pem ubuntu@${aws_instance.master.public_ip}"
}

output "ssh_worker" {
  description = "SSH command to connect to worker"
  value       = "ssh -i ~/.ssh/devops-project-key.pem ubuntu@${aws_instance.worker.public_ip}"
}

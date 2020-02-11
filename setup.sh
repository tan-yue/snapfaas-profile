#!/bin/bash

# start dockerd
sudo groupadd docker
sudo service docker start
sudo usermod -aG docker $USER

# add cpu cgroup firecracker
sudo mount -o remount,ro -t cgroup /sys/fs/cgroup
sudo mkdir /sys/fs/cgroup/cpu/firecracker

# TritonsRCSC-Software-Pack

**Note**
* When switching branch, don't forget to clean the target or build folders
### Install Guide
```bash
# Start at an empty directory ...

# Install all dependencies
sudo apt update
sudo apt install git build-essential cmake pkg-config qt5-default libqt5opengl5-dev libgl1-mesa-dev libglu1-mesa-dev libprotobuf-dev protobuf-compiler libode-dev libboost-all-dev maven openjdk-14-jdk libarmadillo-dev clang 

# Git clone
git clone https://github.com/RoboCup-SSL/grSim.git
git clone https://github.com/IEEE-UCSD-RoboCupSSL/TritonsRCSC-Software-Pack.git

# Setup
cd TritonsRCSC-Software-Pack
make install

# Compile All
make

# Run All
make run

# # GrSim setup
# cd grSim
# mkdir build
# cd build 
# cmake -DCMAKE_INSTALL_PREFIX=/usr/local ..
# make

# # TRC setup
# cd ../../TritonsRCSC-Software-Pack/TritonBot
# mkdir build
# cd build 
# cmake ..
# make clean
# make proto
# cmake ..
# make -j

# cd ../../TritonSoccerAI
# mvn clean package

# cd ../Virtual-Firmware-grSim
# make 

# cd ../../ 

# Everything is finished
# sudo ./grSim/bin/grSim
# python TritonsRCSC-Software-Pack/run.py
```

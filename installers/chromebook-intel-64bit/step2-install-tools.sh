cd $HOME
sudo apt install -y thonny
wget -O vscode.deb 'https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64'
sudo apt install -y ./vscode.deb
rm vscode.deb
wget -O arduino-ide.tar.xz 'https://downloads.arduino.cc/arduino-1.8.19-linux64.tar.xz'
tar -xf arduino-ide.tar.xz
cd arduino-1.8.19
sudo ./install.sh
cd $HOME
rm arduino-ide.tar.xz
wget -O miniforge3-installer.sh 'https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh'
bash ./miniforge3-installer.sh
rm miniforge3-installer.sh

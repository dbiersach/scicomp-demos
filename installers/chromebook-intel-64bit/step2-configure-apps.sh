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
wget -O miniconda3-installer.sh 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh'
bash ./miniconda3-installer.sh
rm miniconda3-installer.sh

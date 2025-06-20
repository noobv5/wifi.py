#!/bin/bash

echo "🔧 Installing all requirements..."
pkg update -y && pkg upgrade -y
pkg install git -y
pkg install python -y
pkg install figlet -y
pip install --upgrade pip

echo "✅ Installation complete!"
echo "📥 Cloning DDOS tool by SHOJIB WIFI..."

git clone https://github.com/noobv5/wifi.py.git


echo "🚀 Running DDOS Attack Tool..."
python ddos.py

#!/bin/bash

blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'

clear
ulang = "y"
[ $ulang = "y" ] ;


    echo
    toilet -f big -F gay By 4!Xz
    echo
    echo
    echo $purple "[ 1 ] spam call"
    echo $yellow "[ 2 ] Dark FB"
    echo $white "[ 3 ) Virus"
    echo $cyan "[ 4 ] Coming Soon.."
    echo $blue "[ 5 ] Dlm perbaikan"
    echo $red "{ 0 } exit"
    echo $green
read -p "Silahkan Pilih Menu :" pilih ;
if [ $pilih = "1" ] ;
then

      echo "installing Spam Call"
      cd $HOME
      apt updte && aot upgrade -y
      apt install php -y
      apt install git
      git clone https://github.com/BangDanz/mascall
      cd mascall
      bash call.sh
      echo "installing succes"
      sleep 1

elif [ $pilih = "2" ] ;
then
      echo "installing Dark FB "
      cd $HOME
      apt update && apt upgrade -y
      apt install php -y
      apt install git
      git clone https://github.com/TheMagizz/DarkPremium
      cd DarkPremium
      python2 DarkFB.py
      echo "installing succes...!"
      sleep 2
elif [ $pilih = "3" ] ;
then
      echo "installing VIRUS"
      cd $HOME
      apt uodate && aot uograde -y
      apt install php -y
      apt install git
      git clone https://github.com/Gameye98/vbug
      cd vbug
      python2 vbug.py
      echo "installing sucess...!"
      sleep 2

elif [ $pilih = "4" ];
then
      echo
      cd $HIME
      apt update && apt upgrade -y
      apt install php -y
      apt install git
      git clone https://github.com/



elif [ $pilih = "0" ] ;
then
      echo "Terima kasih, BYE²..."
      sleep 1
      exit
      
      else
      echo "EROR BOSS : Anda memasukkan input yg salah"
      sleep 1
      echo $ulang
fi
exit

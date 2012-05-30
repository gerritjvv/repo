for u in gvanvuuren aali imontesinos amorales pyesuraj; do

 mkdir -p /home/$u
 cp /root/.bash_profile /home/$u/
 cp /root/.bashrc /home/$u/
 chown -R $u /home/$u

done

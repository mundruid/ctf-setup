import os
import pexpect

os.system("hostname > file.txt")

temp_file = open("file.txt", "r")

name = ""

for line in temp_file:
	name = line[:line.index(".")]

print(name)
temp_file.close()
os.system("sudo rm file.txt")

if "pivot" in name:
	os.system("sudo useradd pivot")
	child = pexpect.spawn("sudo passwd pivot")
	child.expect("Enter new UNIX password: ")
	child.sendline("...")
	child.expect("Retype new UNIX password: ")
	child.sendline("...")
	os.system("sudo mkdir /home/pivot")
	os.system("sudo mkdir /home/pivot/Desktop")
	os.system("sudo mkdir /home/pivot/Downloads")
	os.system("sudo mkdir /home/pivot/Documents")
	os.system("sudo touch /home/pivot/Desktop/password.txt")
	os.system("sudo echo \"Alice's password: password\" >> /home/pivot/Desktop/password.txt")
	os.system("sudo chown -R pivot /home/pivot")
	os.system("sudo chgrp -R pivot /home/pivot")
elif "alice" in name or "bob" in name or "carol" in name or "david" in name:
	if "alice" in name:
		os.system("sudo useradd alice")
		child = pexpect.spawn("sudo passwd alice")
		child.expect("Enter new UNIX password: ")
		child.sendline("password")
		child.expect("Retype new UNIX password: ")
		child.sendline("password")
		os.system("sudo mkdir /home/alice")
		os.system("sudo mkdir /home/alice/Desktop")
		os.system("sudo mkdir /home/alice/Downloads")
		os.system("sudo mkdir /home/alice/Documents")
		os.system("sudo mkdir /home/alice/Documents/mySecret")	
		os.system("sudo mkdir /home/alice/Music")
		os.system("sudo mkdir /home/alice/Pictures")
		os.system("sudo mkdir /home/alice/Videos")
		os.system("sudo touch /home/alice/Documents/mySecret/password.txt")
		os.system("sudo echo \"Yggv bgt xafvafy lzak hskkogjv sfv xaymjafy gml ozsl wfujqhlagf al mkwv... lzw fwpl gfw ogf'l tw kg wskq, lzgmyz. \" >> /home/alice/Documents/mySecret/password.txt")
		os.system("sudo echo \"Tgt'k Hskkogjv: hdslafme\" >> /home/alice/Documents/mySecret/password.txt")
		os.system("sudo chown -R alice /home/alice")
		os.system("sudo chgrp -R alice /home/alice")
		
		os.system("sudo iptables -A INPUT -s 10.10.1.1 -j ACCEPT")
		os.system("sudo iptables -A INPUT -s 10.10.1.2 -j ACCEPT")
	elif "bob" in name:
		os.system("sudo useradd bob")
		child = pexpect.spawn("sudo passwd bob")
		child.expect("Enter new UNIX password: ")
		child.sendline("platinum")
		child.expect("Retype new UNIX password: ")
		child.sendline("platinum")
		os.system("sudo mkdir /home/bob")
		os.system("sudo mkdir /home/bob/Desktop")
		os.system("sudo touch /home/bob/Desktop/my_shopping_list.txt")
		os.system("sudo touch /home/bob/Desktop/dog_name_ideas.txt")
		os.system("sudo touch /home/bob/Desktop/home_calendar.txt")
		os.system("sudo touch /home/bob/Desktop/work_calendar.txt")
		os.system("sudo touch /home/bob/Desktop/family_birthdays.txt")
		os.system("sudo touch /home/bob/Desktop/daily_schedule.txt")
		os.system("sudo mkdir /home/bob/Downloads")
		os.system("sudo mkdir /home/bob/Downloads/not_a_malicious_file.py")
		os.system("sudo mkdir /home/bob/Downloads/mirai_botnet.c")
		os.system("sudo mkdir /home/bob/Downloads/cute_puppy.png")
		os.system("sudo mkdir /home/bob/Downloads/not_a_pirated_movie.mv")
		os.system("sudo mkdir /home/bob/Documents")
		os.system("sudo touch /home/bob/Documents/government_secrets.txt")
		os.system("sudo touch /home/bob/Documents/lab_results1.txt")
		os.system("sudo touch /home/bob/Documents/lab_results2.txt")
		os.system("sudo touch /home/bob/Documents/weekly_memo22.txt")
		os.system("sudo touch /home/bob/Documents/resume.txt")
		os.system("sudo mkdir /home/bob/Music")
		os.system("sudo mkdir /home/bob/Music/best_of_classical_music.wav")
		os.system("sudo mkdir /home/bob/Music/all_journey_songs.wav")
		os.system("sudo mkdir /home/bob/Music/smooth_jaz.mp3")
		os.system("sudo touch /home/bob/Music/.password.txt")
		os.system("sudo mkdir /home/bob/Pictures")
		os.system("sudo touch /home/bob/Pictures/empire_state_building_picture.png")
		os.system("sudo touch /home/bob/Pictures/vacation1.png")
		os.system("sudo touch /home/bob/Pictures/vacation2.png")
		os.system("sudo touch /home/bob/Pictures/vacation3.png")
		os.system("sudo touch /home/bob/Pictures/family_photo.png")
		os.system("sudo touch /home/bob/Pictures/venice.png")
		os.system("sudo touch /home/bob/Pictures/background.png")
		os.system("sudo touch /home/bob/Pictures/screen_saver.png")
		os.system("sudo mkdir /home/bob/Videos")
		os.system("sudo mkdir /home/bob/Videos/christmas_party.mov")
		os.system("sudo mkdir /home/bob/Videos/solar_eclipse.mov")
		os.system("sudo mkdir /home/bob/Videos/parade.mov")
		os.system("sudo mkdir /home/bob/Videos/graduation.mov")
		os.system("sudo mkdir /home/bob/Videos/grand_canyon.mov")
		os.system("sudo echo \"Nice job finding the hidden file - here is Carol's password, but it is encrypted...\" >> /home/bob/Music/.password.txt")
		os.system("sudo echo \"Carol's Password: 8601f6e1028a8e8a966f6c33fcd9aec4\" >> /home/bob/Music/.password.txt")
		os.system("sudo chown -R bob /home/bob")
		os.system("sudo chgrp -R bob /home/bob")

		os.system("sudo iptables -A INPUT -s 10.10.2.1 -j ACCEPT")
		os.system("sudo iptables -A INPUT -s 10.10.2.2 -j ACCEPT")
		os.system("sudo iptables -A INPUT -s 10.10.3.1 -j ACCEPT")
		os.system("sudo iptables -A INPUT -s 10.10.3.2 -j ACCEPT")
	elif "carol" in name:
		os.system("sudo useradd carol")
		child = pexpect.spawn("sudo passwd carol")
		child.expect("Enter new UNIX password: ")
		child.sendline("maxwell")
		child.expect("Retype new UNIX password: ")
		child.sendline("maxwell")
		os.system("sudo mkdir /home/carol")
		os.system("sudo mkdir /home/carol/Desktop")
		os.system("sudo touch /home/carol/Desktop/password0.txt")
		os.system("sudo touch /home/carol/Desktop/password1.txt")
		os.system("sudo touch /home/carol/Desktop/password2.txt")
		os.system("sudo touch /home/carol/Desktop/password3.txt")
		os.system("sudo touch /home/carol/Desktop/password4.txt")
		os.system("sudo touch /home/carol/Desktop/password5.txt")
		os.system("sudo touch /home/carol/Desktop/password6.txt")
		os.system("sudo touch /home/carol/Desktop/password7.txt")
		os.system("sudo touch /home/carol/Desktop/password8.txt")
		os.system("sudo mkdir /home/carol/Downloads")
		os.system("sudo touch /home/carol/Downloads/password0.txt")
		os.system("sudo touch /home/carol/Downloads/password1.txt")
		os.system("sudo touch /home/carol/Downloads/password2.txt")
		os.system("sudo touch /home/carol/Downloads/password3.txt")
		os.system("sudo touch /home/carol/Downloads/password4.txt")
		os.system("sudo touch /home/carol/Downloads/password5.txt")
		os.system("sudo touch /home/carol/Downloads/password6.txt")
		os.system("sudo touch /home/carol/Downloads/password7.txt")
		os.system("sudo touch /home/carol/Downloads/password8.txt")
		os.system("sudo touch /home/carol/Downloads/password9.txt")
		os.system("sudo touch /home/carol/Downloads/password10.txt")
		os.system("sudo touch /home/carol/Downloads/password11.txt")
		os.system("sudo touch /home/carol/Downloads/password12.txt")
		os.system("sudo mkdir /home/carol/Documents")
		os.system("sudo touch /home/carol/Documents/password0.txt")
		os.system("sudo touch /home/carol/Documents/password1.txt")
		os.system("sudo touch /home/carol/Documents/password2.txt")
		os.system("sudo touch /home/carol/Documents/password3.txt")
		os.system("sudo touch /home/carol/Documents/password4.txt")
		os.system("sudo touch /home/carol/Documents/password5.txt")
		os.system("sudo mkdir /home/carol/Music")
		os.system("sudo touch /home/carol/Music/password0.txt")
		os.system("sudo touch /home/carol/Music/password1.txt")
		os.system("sudo mkdir /home/carol/Pictures")
		os.system("sudo touch /home/carol/Pictures/password0.txt")
		os.system("sudo touch /home/carol/Pictures/password1.txt")
		os.system("sudo touch /home/carol/Pictures/password2.txt")
		os.system("sudo mkdir /home/carol/Videos")
		os.system("sudo touch /home/carol/Videos/password0.txt")
		os.system("sudo touch /home/carol/Videos/password1.txt")
		os.system("sudo echo \"You found the final password, but it is encrypted again!\" >> /home/carol/Documents/password3.txt")
		os.system("sudo echo \"David's Password: 44cd8a200a396ce2748ff9e657fc96e6fbe46f1e2c4972511047ce7b03faf0f3c3a1742b6b3a532bfa330f56e7c004f00b2b2c00fbecf8aa0b018057c8206abb\" >> /home/carol/Documents/password3.txt")
		os.system("sudo chown -R carol /home/carol")
		os.system("sudo chgrp -R carol /home/carol")
		
		os.system("sudo iptables -A INPUT -s 10.10.3.1 -j ACCEPT")
		os.system("sudo iptables -A INPUT -s 10.10.3.2 -j ACCEPT")
		os.system("sudo iptables -A INPUT -s 10.10.4.1 -j ACCEPT")
		os.system("sudo iptables -A INPUT -s 10.10.4.2 -j ACCEPT")
	elif "david" in name:
		os.system("sudo useradd david")
		child = pexpect.spawn("sudo passwd david")
		child.expect("Enter new UNIX password: ")
		child.sendline("#xena202#")
		child.expect("Retype new UNIX password: ")
		child.sendline("#xena202#")
		os.system("sudo mkdir /home/david")
		os.system("sudo touch /home/david/congratulations.txt")
		os.system("sudo echo \"If you got here, CONGRATS! That's the end!\" >> /home/david/congratulations.txt")
		os.system("sudo chown -R david /home/david")
		os.system("sudo chgrp -R david /home/david")
		
		os.system("sudo iptables -A INPUT -s 10.10.4.1 -j ACCEPT")
		os.system("sudo iptables -A INPUT -s 10.10.4.2 -j ACCEPT")
		
	ssh_config_file = open("/etc/ssh/sshd_config", "r")
	new_ssh_config_file = open("/etc/ssh/sshd_config_2", "w")

	count = 1

	ports = [
	]

	for line in ssh_config_file:
		if count == 55:
			new_ssh_config_file.write("PasswordAuthentication yes")
		else:
			new_ssh_config_file.write(line)

		if "Port" in line:
			ports.append(line[line.index(" ") + 1:-1])
		count += 1

	ssh_config_file.close()
	new_ssh_config_file.close()

	os.system("sudo mv /etc/ssh/sshd_config_2 /etc/ssh/sshd_config")
	os.system("sudo service ssh restart")

	for port in ports:
		os.system("sudo iptables -A INPUT -p tcp --dport " + port + " -j DROP")

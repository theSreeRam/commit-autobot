import git
import os 


print("This script will invert the binary in the file and push changes to the repo")
print("Author: Sreeram Panigrahi")

path = "./gitpythondemo"
isRepoPresent = os.path.isdir(path)

print("Is repository already present? : " , isRepoPresent)


if(isRepoPresent):
	print("Repository already exists")
	repo = git.Repo(path)
	o = repo.remotes.origin
	o.pull()
	print("Pulled the latest changes")

	# opening file to invert binary
	f = open("./gitpythondemo/inversion.txt", "r+")
	bit = f.readline()
	print(bit)
	if(bit=="0"):
		print("The bit is 0, inverting it to 1")
		f.seek(0,0)
		f.write("1")

	else:
		print("The bit is 1, inverting it to 0")
		f.seek(0,0)
		f.write("0")
	repo.git.add(all=True)
	repo.git.commit('-m', 'inverting commit')
	repo.git.push()

	print("Pushed the changes to the remote")
else:
	print("Repository doesn't exist, cloning it")
	remoteurl="git@github.com:theSreeRam/commit-autobot.git"
	localfolder="./gitpythondemo"

	myrepo = git.Repo.clone_from(remoteurl, localfolder)
	myrepo.git.checkout("main")

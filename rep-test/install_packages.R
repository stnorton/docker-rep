#installs R packages

#read in R packages
args <- commandArgs(trailingOnly=TRUE)
print(args)

req_file <- args[1]
print(req_file)

packs <- scan(req_file, what = 'character', sep = ',')
print(packs)

for(i in 1:length(packs)){
	    install.packages(packs[i])
}

quit(save = 'no')

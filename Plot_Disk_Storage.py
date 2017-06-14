##!/usr/bin/python3.5
#!/Applications/anaconda3/anaconda/bin/python3.6
import csv, os, re
"""
Read section:
Load archival data
Load all newer data
"""
# path = "/var/www/html/_admin/Disk_Storage/" # ubuntu dev
path = "/Users/juehara/opt/Disk_Storage_Plot/Disk_Storage/" # mac dev
archive_file = "archive/archived_Disk_Storage-1.csv"
transpose_file = "archive/diskstorage-transpose-1.csv"

date_array = []
tv_array = []
movies_array = []
anime_array = []
special_array = []
user_array = []
plex_array = []
music_array = []
backups_array = []
media_array = []
danish_array = []
eclair_array = []
granola_array = []
mochi_array = []
mousse_array = []
# Archive Data
with open(path+transpose_file) as archive_csv:
    read = csv.reader(archive_csv, delimiter=',')
    for row in read:
        if row:
            date = row[0]
            tv = row[1]
            movies = row[2]
            anime = row[3]
            special = row[4]
            user = row[5]
            plex = row[6]
            music = row[7]
            backups = row[8]
            media = row[9]
            danish = row[10]
            eclair = row[11]
            granola = row[12]
            mochi = row[13]
            mousse = row[14]
            date_array.append(date)
            tv_array.append(tv)
            movies_array.append(movies)
            anime_array.append(anime)
            special_array.append(special)
            user_array.append(user)
            plex_array.append(plex)
            music_array.append(music)
            backups_array.append(backups)
            media_array.append(media)
            danish_array.append(danish)
            eclair_array.append(eclair)
            granola_array.append(granola)
            mochi_array.append(mochi)
            mousse_array.append(mousse)

del date_array[0], tv_array[0], movies_array[0], anime_array[0]
del special_array[0], user_array[0], plex_array[0], music_array[0]
del backups_array[0], media_array[0], danish_array[0], eclair_array[0]
del granola_array[0], mochi_array[0], mousse_array[0]

# New Data
regex_date = r"201\d-\d\d-\d\d"
regex_value = r"\d+"
newpath = path + "new/"

for path, subdirs, files in os.walk(newpath):
    for name in sorted(files, key=lambda name: os.path.getmtime(os.path.join(newpath, name))):
        datafile = open(newpath + name, "r")
        match = re.search(regex_date,name)
        date_array.append(match.group(0))
        for line in datafile:
            if "Anime Total" in line:
                match = re.search(regex_value, line)
                anime_array.append(match.group(0))
            elif "TV Shows Total" in line:
                match = re.search(regex_value, line)
                tv_array.append(match.group(0))
            elif "Movies Total" in line:
                match = re.search(regex_value, line)
                movies_array.append(match.group(0))
            elif "Specials Total" in line:
                match = re.search(regex_value, line)
                special_array.append(match.group(0))
            elif "Users Total" in line:
                match = re.search(regex_value, line)
                user_array.append(match.group(0))
            elif "Plex Database Total" in line:
                match = re.search(regex_value, line)
                plex_array.append(match.group(0))
            elif "Music Total" in line:
                match = re.search(regex_value, line)
                music_array.append(match.group(0))
            elif "Backups Total" in line:
                match = re.search(regex_value, line)
                backups_array.append(match.group(0))
            elif "/media/ " in line:
                match = re.search(regex_value, line)
                media_array.append(match.group(0))
            elif "/media/DANISH " in line:
                match = re.search(regex_value, line)
                danish_array.append(match.group(0))
            elif "/media/ECLAIR " in line:
                match = re.search(regex_value, line)
                eclair_array.append(match.group(0))
            elif "/media/GRANOLA " in line:
                match = re.search(regex_value, line)
                granola_array.append(match.group(0))
            elif "/media/MOCHI " in line:
                match = re.search(regex_value, line)
                mochi_array.append(match.group(0))
            elif "/media/MOUSSE " in line:
                match = re.search(regex_value, line)
                mousse_array.append(match.group(0))

        # read = csv.reader(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        # for row in read:
        #     print (row)
        #     if row:
        #         tv = row[1]
        #         movies = row[2]
        #         anime = row[3]
        #         special = row[4]
        #         user = row[5]
        #         plex = row[6]
        #         music = row[7]
        #         backups = row[8]
        #         media = row[9]
        #         danish = row[10]
        #         eclair = row[11]
        #         granola = row[12]
        #         mochi = row[13]
        #         mousse = row[14]
        #         tv_array.append(tv)
        #         movies_array.append(movies)
        #         anime_array.append(anime)
        #         special_array.append(special)
        #         user_array.append(user)
        #         plex_array.append(plex)
        #         music_array.append(music)
        #         backups_array.append(backups)
        #         media_array.append(media)
        #         danish_array.append(danish)
        #         eclair_array.append(eclair)
        #         granola_array.append(granola)
        #         mochi_array.append(mochi)
        #         mousse_array.append(mousse)

print (date_array)
print (tv_array)
print (movies_array)
print (anime_array)
print (special_array)
print (user_array)
print (plex_array)
print (music_array)
print (backups_array)
print (media_array)
print (danish_array)
print (eclair_array)
print (granola_array)
print (mochi_array)
print (mousse_array)

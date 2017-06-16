#!/usr/bin/python3.5
import csv, time, subprocess, re
date = time.strftime("%Y-%m-%d")
path = "/var/www/html/_admin/Disk_Storage/new/"
file = ("Disk_storage-{0}.csv" .format(date))

tv_shows_loc = ["/media/DANISH/Media/TV\ Shows"]
tv_shows_val = [""]
movies_loc = ["/media/ECLAIR/Movies"]
movies_val = [""]
anime_loc = ["/media/MOCHI/Anime", "/media/ECLAIR/Anime"]
anime_val = [""]
specials_loc = ["/media/DANISH/Media/Special\ Libraries"]
specials_val = [""]
user_loc = ["/home/clara", "/media/MOUSSE/home"]
user_val = [""]
plex_loc = ["/var/lib/plexmediaserver"]
plex_val = [""]
music_loc = ["/media/DANISH/Media/Music"]
music_val = [""]
backup_loc = ["/media/GRANOLA/Backups-Muffin"]
backup_val = [""]
media_loc = ["/media "]
media_val = [""]
danish_loc = ["/media/DANISH "]
danish_val = [""]
# donut_loc = ["/media/DONUT "]
# donut_val = [""]
eclair_loc = ["/media/ECLAIR "]
eclair_val = [""]
granola_loc = ["/media/GRANOLA "]
granola_val = [""]
mochi_loc = ["/media/MOCHI "]
mochi_val = [""]
mousse_loc = ["/media/MOUSSE "]
mousse_val = [""]
# master_loc = [tv_shows_loc, movies_loc, anime_loc, specials_loc, user_loc,
#     plex_loc, music_loc, backup_loc, media_loc, danish_loc, donut_loc,
#     eclair_loc, granola_loc, mochi_loc, mousse_loc]

command_mac = "du -shm "
command_linux = "du -shBM "
command = command_linux

def fillarray(array_loc, array_val):
    regex = r"^\d+"
    for items in array_loc:
        b_output = subprocess.check_output(command + items, shell=True)
        output = b_output.decode("utf-8")
        match = re.match(regex, output)
        array_val.append(int(match.group(0)))
    del array_val[0]
    print (array_val)
    print (array_loc)

def writearray(write, array_loc, array_val, name, multi=True):
    i = 0
    for items in array_loc:
        write.writerow([array_val[i], array_loc[i]])
        i += 1
    if multi == True:
        write.writerow([sum(array_val), '{0} Total' .format(name)])

"""
Writing section
"""
fillarray(tv_shows_loc,tv_shows_val)
fillarray(movies_loc,movies_val)
fillarray(anime_loc,anime_val)
fillarray(specials_loc,specials_val)
fillarray(user_loc,user_val)
fillarray(plex_loc,plex_val)
fillarray(music_loc,music_val)
fillarray(backup_loc,backup_val)
fillarray(media_loc,media_val)
fillarray(danish_loc,danish_val)
#fillarray(donut_loc,donut_val)
fillarray(eclair_loc,eclair_val)
fillarray(granola_loc,granola_val)
fillarray(mochi_loc,mochi_val)
fillarray(mousse_loc,mousse_val)

with open(path+file, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writearray(writer, anime_loc, anime_val, "Anime")
        writearray(writer, tv_shows_loc,tv_shows_val, "TV Shows")
        writearray(writer, movies_loc,movies_val, "Movies")
        writearray(writer, specials_loc,specials_val, "Specials")
        writearray(writer, user_loc,user_val, "Users")
        writearray(writer, plex_loc,plex_val, "Plex Database")
        writearray(writer, music_loc,music_val, "Music")
        writearray(writer, backup_loc,backup_val, "Backups")
        writearray(writer, media_loc,media_val, "Storage", False)
        writearray(writer, danish_loc,danish_val, "DANISH", False)
        # writearray(writer, donut_loc,donut_val, "DONUT", False)
        writearray(writer, eclair_loc,eclair_val, "ECLAIR", False)
        writearray(writer, granola_loc,granola_val, "GRANOLA", False)
        writearray(writer, mochi_loc,mochi_val, "MOCHI", False)
        writearray(writer, mousse_loc,mousse_val, "MOUSSE", False)

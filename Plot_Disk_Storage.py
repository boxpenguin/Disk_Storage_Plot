#!/Applications/anaconda3/anaconda/bin/python3.6
"""!/usr/bin/python3.5"""

import csv, os, re, plotly
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go
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
            elif "/media " in line:
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
# Plotting to plotly
plotly.tools.set_credentials_file(username='jordan.uehara', api_key='Ukl8ZY0ZiKH6njDW0hAc')
#plotly.tools.set_credentials_file(username='jordan.uehara1', api_key='jo67DJSssv81gozJQOwG')

plotly.tools.set_config_file(world_readable=True, sharing='public')

trace1 = go.Scatter(
    x = date_array,
    y = tv_array,
    name = "TV Shows",
    line = dict(
        color = ('rgb(22,22,22)'),
        width = 2,
        dash = 'line')
)
trace2 = go.Scatter(
    x = date_array,
    y = movies_array,
    name = "Movies",
    line = dict(
        color = ('rgb(22,22,22)'),
        width = 2,
        dash = 'line')
)
trace3 = go.Scatter(
    x = date_array,
    y = anime_array,
    name = "Anime",
    line = dict(
        color = ('rgb(22,22,22)'),
        width = 2,
        dash = 'line')
)
trace4 = go.Scatter(
    x = date_array,
    y = special_array,
    name = "Specials",
    line = dict(
        color = ('rgb(22,22,22)'),
        width = 2,
        dash = 'line')
)
trace5 = go.Scatter(
    x = date_array,
    y = user_array,
    name = "Home dirs",
    line = dict(
        color = ('rgb(22,22,22)'),
        width = 2,
        dash = 'line')
)
trace6 = go.Scatter(
    x = date_array,
    y = plex_array,
    name = "Plex",
    line = dict(
        color = ('rgb(22,22,22)'),
        width = 2,
        dash = 'line')
)
trace7 = go.Scatter(
    x = date_array,
    y = music_array,
    name = "Music",
    line = dict(
        color = ('rgb(22,22,22)'),
        width = 2,
        dash = 'line')
)
trace8 = go.Scatter(
    x = date_array,
    y = backups_array,
    name = "Backup",
    line = dict(
        color = ('rgb(22,22,22)'),
        width = 2,
        dash = 'line')
)
trace9 = go.Scatter(
    x = date_array,
    y = media_array,
    name = "Total Storage",
    line = dict(
        color = ('rgb(22,96,167)'),
        width = 2,
        dash = 'line')
)
trace10 = go.Scatter(
    x = date_array,
    y = danish_array,
    name = "DANISH Storage",
    line = dict(
        color = ('rgb(22,96,167)'),
        width = 2,
        dash = 'line')
)
trace11 = go.Scatter(
    x = date_array,
    y = eclair_array,
    name = "ECLAIR Storage",
    line = dict(
        color = ('rgb(22,96,167)'),
        width = 2,
        dash = 'line')
)
trace12 = go.Scatter(
    x = date_array,
    y = granola_array,
    name = "GRANOLA Storage",
    line = dict(
        color = ('rgb(22,96,167)'),
        width = 2,
        dash = 'line')
)
trace13 = go.Scatter(
    x = date_array,
    y = mochi_array,
    name = "MOCHI Storage",
    line = dict(
        color = ('rgb(22,96,167)'),
        width = 2,
        dash = 'line')
)
trace14 = go.Scatter(
    x = date_array,
    y = mousse_array,
    name = "MOUSSE Storage",
    line = dict(
        color = ('rgb(22,96,167)'),
        width = 2,
        dash = 'line')
)

libraries = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8] #, trace9, trace10, trace11, trace12, trace13, trace14 ]
drives = [trace9, trace10, trace11, trace12, trace13, trace14]
layout = dict(title = "Storage",
    xaxis = dict(title = "Week"),
    yaxis = dict(title = "GB")
    )
print ("Plotting Complete")
fig = dict(data=libraries, layout=layout)
fig1 = dict(data=drives, layout=layout)

plot_url = py.plot(fig, filename="Libraries", auto_open=False)
plot_url1 = py.plot(fig1, filename="Drives", auto_open=False)
print ("Sent to plotly")

# print ("date_array: " + date_array[-1])
# print ("tv_array: " + tv_array[-1])
# print ("movies_array: " + movies_array[-1])
# print ("anime_array: " + anime_array[-1])
# print ("special_array: " + special_array[-1])
# print ("user_array: " + user_array[-1])
# print ("plex_array: " + plex_array[-1])
# print ("music_array: " + music_array[-1])
# print ("backups_array: " + backups_array[-1])
# print ("media_array: " + media_array[-1])
# print ("danish_array: " + danish_array[-1])
# print ("eclair_array: " + eclair_array[-1])
# print ("granola_array: " + granola_array[-1])
# print ("mochi_array: " + mochi_array[-1])
# print ("mousse_array: " + mousse_array[-1])

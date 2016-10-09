import urllib2, json, time, urllib, sqlite3
from send import message

READ_API_KEY1="I1R400XJYV6X1R32"
READ_API_KEY2="TYLL76XQAAJF70DD"
CHANNEL_ID1=168773
CHANNEL_ID2=168777

time.sleep(2)
conn1 = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
          % (CHANNEL_ID1,READ_API_KEY1))

response = conn1.read()
print "http status code=%s" % (conn1.getcode())
data=json.loads(response)
lat = data['field1']
time.sleep(2)
conn2 = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
          % (CHANNEL_ID2,READ_API_KEY2))

response = conn2.read()
print "http status code=%s" % (conn2.getcode())
data=json.loads(response)
lon = data['field1']

print lat, lon

with sqlite3.connect("lock.db") as connection:
    cur = connection.cursor()
    cur1 = cur.execute("select latitude from accidents")
    dat_db1 = [row[0] for row in cur1.fetchall()]

    cur1 = cur.execute("select hospitals2 from accidents")
    dat_db2 = [row[0] for row in cur1.fetchall()]

    print(type(lat))
    print(type(dat_db1[-1]))

    i = 0
    for x in dat_db1:
        if float(lat) == float(x):
            with sqlite3.connect("lock.db") as connection:
                cur = connection.cursor()
                values = (i+6, str(str(lat) + " " + str(lon)), str(dat_db2[i]), str(dat_db2[i]), float(x), float(548),)
                cur1 = cur.execute("insert into accidents values(?, ?, ?, ?, ?, ?)",values)
                dat_db1 = [row[0] for row in cur1.fetchall()]
                print dat_db1         
        i += 1

message(7264849909, str[dat_db2[i-1]])
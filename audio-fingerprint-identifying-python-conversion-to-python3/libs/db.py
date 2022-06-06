import sys

class Database(object):
  TABLE_SONGS = None
  TABLE_FINGERPRINTS = None

  def __init__(self, a):
    self.a = a

  def connect(self): pass
  def insert(self, table, params): pass

  def get_song_by_filehash(self, filehash):
    return self.findOne(self.TABLE_SONGS, {
      "filehash": filehash
    })

  def get_song_by_id(self, id):
    return self.findOne(self.TABLE_SONGS, {
      "id": id
    })

  def add_song(self, filename, filehash):
    song = self.get_song_by_filehash(filehash)
    if not song:
      c = self.conn.cursor()
      print(c)
      print(filename)
      print(filehash)
      c.execute(f'''INSERT INTO songs(ID,name,filehash) VALUES('11','patito.mp3','0541CACA54B5E94BF11E0BB0279B78573D39212F')''')
      self.conn.commit()
      '''song_id = self.insert(self.TABLE_SONGS, {
        "name": filename,
        "filehash": filehash
      })'''
      song_id = 12
    else:
      song_id = song[0]
    return song_id

  def get_song_hashes_count(self, song_id):
    pass

  def store_fingerprints(self, values):
    self.insertMany(self.TABLE_FINGERPRINTS,
      ['song_fk', 'hash', 'offset'], values
    )

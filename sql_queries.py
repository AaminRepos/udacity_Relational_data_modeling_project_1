# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES



songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id int PRIMARY KEY NOT NULL,
                                song_id varchar NOT NULL,
                                user_id int NOT NULL,
                                artist_id varchar NOT NULL,
                                session_id int,
                                location varchar,
                                start_time int NOT NULL,
                                user_agent varchar,
                                level varchar); """)


user_table_create = (""" CREATE TABLE IF NOT EXISTS users(
                            user_id int PRIMARY KEY NOT NULL ,
                            Level varchar, 
                            first_name text,
                            last_name text, 
                            gender varchar); 
                            """)

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs(
                            song_id varchar PRIMARY KEY NOT NULL, 
                            artist_id varchar,
                            year int,
                            title text NOT NULL, 
                            duration float NOT NULL); 
                            """)

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists(
                              artist_id varchar
                              PRIMARY KEY NOT NULL, 
                              name text NOT NULL, 
                              latitude float, 
                              longitude float, 
                              location varchar); 
                              """)

time_table_create = (""" CREATE TABLE IF NOT EXISTS time(
                            start_time timestamp PRIMARY KEY NOT NULL, 
                            hour int,
                            day int,
                            month int,
                            year int); 
                            """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(
                            songplay_id, 
                            song_id, 
                            user_id,
                            artist_id, 
                            session_id, 
                            location, 
                            start_time,
                            user_agent, 
                            level)\
                             
                             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                             ON CONFLICT DO NOTHING;
                             """)

user_table_insert = ("""INSERT INTO users( user_id, 
                        level,
                        first_name,
                        last_name,
                        gender)\
                            
                        VALUES(%s,%s,%s,%s,%s)
                        ON CONFLICT (user_id) DO UPDATE
                            set level = EXcLUDED.level ;""")

song_table_insert = ("""INSERT INTO songs(
                        song_id, 
                        artist_id, 
                        year, 
                        title,
                        duration)\
                         
                        VALUES(%s,%s,%s,%s,%s)
                        ON CONFLICT DO NOTHING;""")

artist_table_insert = ("""INSERT INTO artists(
                          artist_id, 
                          name,
                          latitude,
                          longitude,
                          location)\
                          
                          VALUES(%s,%s,%s,%s,%s)
                          ON CONFLICT DO NOTHING;""")


time_table_insert = ("""INSERT INTO time(
                        start_time, 
                        hour, 
                        day, 
                        month, 
                        year)\

                        VALUES(%s,%s,%s,%s,%s)
                        ON CONFLICT DO NOTHING;""")

# FIND SONGS

song_select = ("""SELECT songs.song_id, artists.artist_id
                    FROM songs JOIN artists 
                    ON songs.artist_id = artists.artist_id 
                    WHERE ( 
                    artists.name = %s 
                    AND songs.title = %s 
                    AND songs.duration =%s);
                    """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
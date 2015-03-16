import class_music_info

u2=class_music_info.Music_Collection("U2", "Rock", "Achtung Baby")
ultra_violet=class_music_info.Favorite_Songs("Ultra Violet", "U2", "Rock", "Achtung Baby",
                                             "https://www.youtube.com/watch?v=q6iO_HpT4F4")
the_fly=class_music_info.Favorite_Songs("The Fly", "U2", "Rock", "Achtung Baby",
                                        "https://www.youtube.com/watch?v=5Y1YFH9A3Bw")

florence_and_the_machine=class_music_info.Music_Collection("Florence and the Machine", "Alternative",
                                                           "Ceremonials")
leave_my_body=class_music_info.Favorite_Songs("Leave My Body", "Florence and the Machine",
                                              "Alternative", "Ceremonials",
                                              "https://www.youtube.com/watch?v=AjWJ3W30NVg")
bedroom_hymns=class_music_info.Favorite_Songs("Bedroom Hymns","Florence and the Machine",
                                              "Alternative", "Ceremonials",
                                              "https://www.youtube.com/watch?v=A-vrYeVGGZ0")


the_fly.show_info()
the_fly.play_song()
leave_my_body.show_info()
leave_my_body.play_song()


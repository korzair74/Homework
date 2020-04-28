/*
Create a new Mongo Database, load 6 “documents” into a Mongo Collection all at once, show how to delete the 3rd, and 5th documents that you added. You should only have 4 documents left.
Write down each step for me to review, "To create a new DB, I did this: etc"
*/

// initiate mongo with command in command prompt or shell.

$ mongo 

// I then then created my db and confirmed available by using:
> use homeworkDb
> db 

// created a collection and an array of items to insert:

>
const guild_data = 
[
  {
    char_name: 'Brûce',
    char_class: 'Monk',
    level: 120
  },
  {
    char_name: 'Nystana',
    char_class: 'Priest',
    level: 90
  },
  {
    char_name: 'Buddacup',
    char_class: 'Druid',
    level: 10
  },
  {
    char_name: 'Taynte',
    char_class: 'Warlock',
    level: 100
  },
  {
    char_name: 'Grimmly',
    char_class: 'Warrior',
    level: 21
  },
  {
    char_name: 'Skoi',
    char_class: 'Hunter',
    level: 110
  }
]

db.Guild.insert(guild_data)

// remove the 3rd and 5th item:

db.Guild.remove( { level: { $lte: 22 } } )
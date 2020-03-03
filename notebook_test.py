from notebook import Note, Notebook


n1 = Note("hello first")
n2 = Note("hello again")
print("ID of n1 : " + str(n1.id))
print("List of the attributes and methods of object n1.id : " +
      str(dir(n1.id)))
print("Check if type of object n1.id is list : " +
      str(isinstance(n1.id, list)))
print("Check if type of object n1.id is integer : " +
      str(isinstance(n1.id, int)))
print("ID of n2: " + str(n2.id))
print("List of the attributes and methods of object n2.id : " +
      str(dir(n2.id)))
print("Check if type of object n2.id is list : " +
      str(isinstance(n2.id, list)))
print("Check if type of object n2.id is integer : " +
      str(isinstance(n2.id, int)))
print("This note n1 matches the filter text : " +
      str(n1.match('hello')))
print("This note n2 matches the filter text : " +
      str(n2.match('second')))
n = Notebook()
print("List of the attributes and methods of object n : " +
      str(dir(n)))
print("Class of n : " + str(type(n)))
n.new_note("hello world")
print("Class of n.new_note('hello world') : " +
      str(type(n.new_note("hello world"))))
n.new_note("hello again")
print("List of all objects of notes : " + str(n.notes))
print("List of the attributes and methods of object n.notes : " +
      str(dir(n.notes)))
print("ID of n.notes[0] : " + str(n.notes[0].id))
print("ID of n.notes[1] : " + str(n.notes[1].id))
print("Print first note in memory :  " + n.notes[0].memo)
print("Check if type of object n.notes[0].memo is list : " +
      str(isinstance(n.notes[0].memo, list)))
print("Check if type of object n.notes[0].memo is string : " +
      str(isinstance(n.notes[0].memo, str)))
print("List of the attributes and methods of object n.notes[0].memo : " +
      str(dir(n.notes[0].memo)))
print("Note objects that match the given filter 'hello' : " +
      str(n.search("hello")))
print("Note objects that match the given filter 'world' : " +
      str(n.search("world")))
print("List of the attributes and methods of object n.note : " +
      str(dir(n.notes)))
print("Check if type of object n.notes is integer : " +
      str(isinstance(n.notes, int)))
print("Check if type of object n.notes is list : " +
      str(isinstance(n.notes, list)))

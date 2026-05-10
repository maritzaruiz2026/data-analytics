movie_list = ['The Nightmare Before Christmas', 'Brave', 'Inside Out', 'Coco', 'Zootopia', 'A.I. Artificial Intelligence', 'The Incredibles', 'The Incredibles 2']

print(f'The list movie_list includes my top {len(movie_list)} favorite movies')
print(movie_list)

print(sorted(movie_list))
print(movie_list)   
# The sorted() function returns a new list that is sorted, but does not change the original list. It even sorts after "The" for The Incredibles and The Incredibles 2 (and has The Nightmare Before Christmas last).

movie_list.sort()
print(movie_list) 
#This sorts the list the same as sorted() as far as I can tell

movie_list.append('The Lion King')
print(movie_list)
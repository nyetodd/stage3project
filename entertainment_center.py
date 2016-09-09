import media
import fresh_tomatoes

def main():
	''' main method - prompts the methods that generate the movie content and then load the webpage'''
	movies = generate_movies()
	create_movie_page(movies)	

def generate_movies():
	''' Creates insances of the movie class to display on the page. Returns these movies as a list.'''

	the_ladykillers = media.Movie("The Ladykillers", 97,
							"Five diverse oddball criminal types planning a bank robbery rent rooms on a cul-de-sac from an octogenarian widow under the pretext that they are classical musicians.", "Alec Guinness, Katie Johnson, Herbert Lom, Peter Sellers, Danny Green, Cecil Parker", "William Rose", "Alexander Mackendrick" ,
							"http://torontofilmsociety.org/files/2013/10/277306-the_lady_killers-poster.jpg",
							"https://www.youtube.com/tv#/watch?v=hwTBKuRzYd4", "8 December 1955 (UK)")

	easy_a = media.Movie("Easy A", 92,
						"After a little white lie about losing her virginity gets out, a clean cut high school girl sees her life paralleling Hester Prynne's in 'The Scarlet Letter,' which she is currently studying in school - until she decides to use the rumor mill to advance her social and financial standing.",
						"Emma Stone, Stanley Tucci, Patricia Clarkson, Thomas Haden Church", "Bert V. Royal", "Will Gluck",
						"http://www.impawards.com/2010/posters/easy_a.jpg", 
						"https://www.youtube.com/tv#/watch?v=sE-hZ8OQzAU", 
						"September 17, 2010 (United States)")

	empire_strikes_back = media.Movie("Empire Strikes Back", 124,
						"The adventure continues in this 'Star Wars' sequel. Luke Skywalker , Han Solo , Princess Leia and Chewbacca face attack by the Imperial forces and its AT-AT walkers on the ice planet Hoth. While Han and Leia escape in the Millennium Falcon, Luke travels to Dagobah in search of Yoda. Only with the Jedi master's help will Luke survive when the dark side of the Force beckons him into the ultimate duel with Darth Vader.",
						" Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew and Frank Oz.",
						"Leigh Brackett, Lawrence Kasdan", 
						"Irvin Kershner",
						"http://posterwire.com/wp-content/uploads/empire_strikes_back_style_a.jpg", 
						"https://www.youtube.com/tv#/watch?v=mz_YWNhKOkM",
						"21 May 1980 (United States)")

	in_the_loop = media.Movie("In The Loop", 105,
						"Satirical black comedy directed by Armando Iannucci as a spin-off from the BBC Television series The Thick of It. The film satirizes Anglo-American politics in the 21st century and the Invasion of Iraq",
						"Peter Capaldi, Tom Hollander, Gina McKee, Chris Addison, David Rasche, and James Gandolfini",
						"	Jesse Armstrong, Simon Blackwell, Armando Iannucci, Tony Roche", 
						"Armando Iannucci",
						"http://www.impawards.com/2009/posters/in_the_loop_ver5.jpg", 
						"https://www.youtube.com/tv#/watch?v=dQrqMkCuHqA", 
						"17 April 2009 (UK)")


	hedwig = media.Movie("Hedwig and the Angry Inch", 92,
						"""After a botched sex-change operation, East German glam rocker Hansel becomes Hedwig and travels across the United States with a stage show, following her ex-boyfriend (and former band mate) and telling her life story. Hedwig's offbeat show slays audiences -- but in diners not clubs.""",
						"John Cameron Mitchell, Miriam Shor, Stephen Trask, Andrea Martin and Michael Pitt", 
						"John Cameron Mitchell, Stephen Trask", 
						"John Cameron Mitchell",
						"http://www.impawards.com/2001/posters/hedwig_and_the_angry_inch.jpg", 
						"https://www.youtube.com/tv#/watch?v=4p9mPhGo1j0", 
						"20 July 2001")

	rocky_horror = media.Movie("The Rocky Horror Picture Show", 100,
						"In this cult classic, sweethearts Brad and Janet, stuck with a flat tire during a storm, discover the eerie mansion of Dr. Frank-N-Furter, a transvestite scientist. As their innocence is lost, Brad and Janet meet a houseful of wild characters, including a rocking biker and a creepy butler. Through elaborate dances and rock songs, Frank-N-Furter unveils his latest creation: a muscular man named 'Rocky.'",
							"Tim Curry, Susan Sarandon, Barry Bostwick and Richard O'Brien", 
							"Richard O'Brien, Jim Sharman", 
							"Jim Sharman",
						"http://vignette4.wikia.nocookie.net/rockyhorror/images/f/f0/The_rocky_horror_picture_show_poster.jpg/revision/latest?cb=20130914000612", 
						"https://www.youtube.com/tv#/watch?v=dEBQ3haBi3c", 
						"14 August 1975")

	movies = [easy_a, the_ladykillers,empire_strikes_back, rocky_horror, hedwig, in_the_loop]
	return movies


def create_movie_page(movies):
	''' takes list of movie instances and uses them to generate and open the movie webpage'''
	fresh_tomatoes.open_movies_page(movies)

main()


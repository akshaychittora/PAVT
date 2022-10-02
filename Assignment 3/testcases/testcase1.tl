left 90
pendown
:move = 20
forward :move
repeat 5 [

	forward 4

	repeat 4 [
		forward :move
		left 45
	]
	:move = :move +5

]
forward 3
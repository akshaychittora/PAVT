penup
if :x > 10 [
	right 90
	if :y > 20 [
		forward 80
	]
	else [
		backward 70 ]	
]
else[
	left 90
	if :y > 20 [
		forward 80 ]
	else [
		backward 70 ]
]

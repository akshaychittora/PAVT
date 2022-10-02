penup
:x = 50
:t = :y + :x + :x
:x = :x - 10
if :t <= 50[
	:y = :t + 10
	if :y < 50[
	forward 40
	]
]
else[
	:y = :t - 20
	if :y < 50 [
	forward 20
	]
]
forward 40